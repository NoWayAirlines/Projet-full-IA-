"""
scrapper.py — Lance UNE SEULE FOIS pour remplir la base de données LoL.
Sources :
  0. builds.py                  — builds détaillés avec chemins d'items complets (PRIORITAIRE)
  1. Data Dragon (Riot officiel) — stats, sorts, items
  2. U.GG                       — tier, win rate, counters
  3. LoL Wiki (MediaWiki API)   — mécaniques, interactions, glossaire
  4. Patch notes Riot           — derniers changements

Durée estimée : 20-40 min (dépend de ta connexion et ton CPU pour les embeddings)
"""

import re
import time
import requests
import ollama
import chromadb
from builds import builds_to_chunks

# ─── CONFIG ────────────────────────────────────────────────────────────────────
DB_PATH      = "./lol_db"
EMBED_MODEL  = "nomic-embed-text"
DELAY_UGG    = 1.5   # secondes entre chaque requête u.gg (évite le ban)
DELAY_WIKI   = 0.5

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0.0.0 Safari/537.36"
    )
}

def clean(text: str) -> str:
    text = re.sub(r"<[^>]+>", " ", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()

# ─── CHROMADB ─────────────────────────────────────────────────────────────────
print("Initialisation de la base ChromaDB...")
client = chromadb.PersistentClient(path=DB_PATH)
try:
    client.delete_collection("lol")
except Exception:
    pass
collection = client.create_collection("lol")

chunks: list[str] = []
ids:    list[str] = []

def add(id_: str, texte: str):
    if texte.strip():
        chunks.append(texte.strip())
        ids.append(id_)

# ══════════════════════════════════════════════════════════════════════════════
# 0. BUILDS DÉTAILLÉS (prioritaires — injected en premier)
# ══════════════════════════════════════════════════════════════════════════════
print("\n[0/4] Builds détaillés (builds.py)...")
for id_, texte in builds_to_chunks():
    add(id_, texte)
print(f"   {len(chunks)} chunks de builds injectes OK")

# ══════════════════════════════════════════════════════════════════════════════
# 1. DATA DRAGON — stats + sorts + items
# ══════════════════════════════════════════════════════════════════════════════
print("\n[1/4] Data Dragon...")
version = requests.get("https://ddragon.leagueoflegends.com/api/versions.json").json()[0]
print(f"   Version : {version}")

champ_summary = requests.get(
    f"https://ddragon.leagueoflegends.com/cdn/{version}/data/en_US/champion.json"
).json()["data"]

for name, c in champ_summary.items():
    add(f"dd_champ_{name}", (
        f"Champion: {c['name']} — {c['title']}\n"
        f"Rôles: {', '.join(c['tags'])}\n"
        f"Description: {clean(c['blurb'])}\n"
        f"Stats de base → HP: {c['stats']['hp']}, Armure: {c['stats']['armor']}, "
        f"Attaque: {c['stats']['attackdamage']}, Vitesse: {c['stats']['movespeed']}\n"
    ))

print(f"   {len(champ_summary)} champions (résumé) OK")
print(f"   Telechargement des sorts ({len(champ_summary)} appels)...")

for i, (name, c) in enumerate(champ_summary.items()):
    try:
        detail = requests.get(
            f"https://ddragon.leagueoflegends.com/cdn/{version}/data/en_US/champion/{name}.json"
        ).json()["data"][name]

        sorts = "\n".join(
            f"  - {s['name']}: {clean(s['description'])[:250]}"
            for s in detail["spells"]
        )
        passif = detail["passive"]
        ally   = " ".join(detail.get("allytips", []))
        enemy  = " ".join(detail.get("enemytips", []))

        add(f"dd_spells_{name}", (
            f"Sorts de {detail['name']} :\n"
            f"  Passif — {passif['name']}: {clean(passif['description'])[:200]}\n"
            f"{sorts}\n"
            + (f"Tips alliés : {ally}\n" if ally else "")
            + (f"Tips ennemis : {enemy}\n" if enemy else "")
        ))

        if (i + 1) % 30 == 0:
            print(f"   {i+1}/{len(champ_summary)} sorts traites...")
    except Exception as e:
        print(f"   Erreur sorts {name}: {e}")

items_data = requests.get(
    f"https://ddragon.leagueoflegends.com/cdn/{version}/data/en_US/item.json"
).json()["data"]

item_count = 0
for item_id, item in items_data.items():
    if not item.get("name"):
        continue
    gold = item.get("gold", {})
    if gold.get("total", 0) < 1000:
        continue
    add(f"dd_item_{item_id}", (
        f"Item: {item['name']} (cout: {gold.get('total','?')} or)\n"
        f"Tags: {', '.join(item.get('tags', []))}\n"
        f"Description: {clean(item.get('plaintext', ''))}\n"
    ))
    item_count += 1

print(f"   {item_count} items OK")

# ══════════════════════════════════════════════════════════════════════════════
# 2. U.GG — tier, win rate, counters, skill order
# ══════════════════════════════════════════════════════════════════════════════
print(f"\n[2/4] U.GG (tier, win rate, counters)...")
print(f"   {len(champ_summary)} champions a scraper — delai {DELAY_UGG}s entre chaque.")

def scrape_ugg(champ_display: str) -> str:
    slug = champ_display.lower().replace(" ", "-").replace("'", "").replace(".", "")
    url = f"https://u.gg/lol/champions/{slug}/build"
    try:
        r = requests.get(url, headers=HEADERS, timeout=12)
        if r.status_code != 200:
            return ""
        text = r.text
        lines = []

        wr_m = re.search(r'"win_rate"\s*:\s*([\d.]+)', text)
        if wr_m:
            lines.append(f"Win Rate : {float(wr_m.group(1)):.1f}%")

        pr_m = re.search(r'"pick_rate"\s*:\s*([\d.]+)', text)
        if pr_m:
            lines.append(f"Pick Rate : {float(pr_m.group(1)):.1f}%")

        br_m = re.search(r'"ban_rate"\s*:\s*([\d.]+)', text)
        if br_m:
            lines.append(f"Ban Rate : {float(br_m.group(1)):.1f}%")

        rank_m = re.search(r'"overall_ranking"\s*:\s*(\d+)', text)
        total_m = re.search(r'"total_champion_count"\s*:\s*(\d+)', text)
        if rank_m and total_m:
            lines.append(f"Rang dans le méta : {rank_m.group(1)}/{total_m.group(1)}")

        return "\n".join(lines)
    except Exception:
        return ""

ugg_ok = 0
for i, (name, c) in enumerate(champ_summary.items()):
    data = scrape_ugg(c["name"])
    if data:
        add(f"ugg_{name}", f"Statistiques U.GG pour {c['name']} :\n{data}\n")
        ugg_ok += 1
    time.sleep(DELAY_UGG)
    if (i + 1) % 20 == 0:
        print(f"   {i+1}/{len(champ_summary)} champions U.GG traites ({ugg_ok} avec donnees)...")

print(f"   U.GG termine : {ugg_ok}/{len(champ_summary)} champions avec donnees OK")

# ══════════════════════════════════════════════════════════════════════════════
# 3. LOL WIKI (MediaWiki API) — mécaniques, glossaire, gameplay
# ══════════════════════════════════════════════════════════════════════════════
print("\n[3/4] LoL Wiki (MediaWiki API)...")

WIKI_API = "https://leagueoflegends.fandom.com/api.php"

WIKI_PAGES = [
    "Glossary of League of Legends",
    "Game modes",
    "Minion (League of Legends)",
    "Turret",
    "Jungle (League of Legends)",
    "Baron Nashor",
    "Dragon",
    "Rift Herald",
    "Vision",
    "Gold",
    "Experience (League of Legends)",
    "Wave management",
    "Champion",
    "Item (League of Legends)",
    "Rune (League of Legends, 2017)",
    "Summoner spell",
    "Crowd control",
    "Damage",
    "Healing",
    "Shielding",
    "Teamfight",
    "Lane",
    "Rotation",
    "Map (League of Legends)",
]

wiki_ok = 0
for page in WIKI_PAGES:
    try:
        r = requests.get(WIKI_API, params={
            "action": "query",
            "titles": page,
            "prop": "extracts",
            "exintro": True,
            "explaintext": True,
            "format": "json",
        }, headers=HEADERS, timeout=10)
        pages_data = r.json().get("query", {}).get("pages", {})
        for p in pages_data.values():
            extract = p.get("extract", "")
            if extract and len(extract) > 100:
                add(f"wiki_{page.replace(' ', '_')[:40]}", f"Wiki — {page} :\n{extract[:2000]}\n")
                wiki_ok += 1
        time.sleep(DELAY_WIKI)
    except Exception as e:
        print(f"   Erreur wiki '{page}': {e}")

print(f"   Wiki : {wiki_ok}/{len(WIKI_PAGES)} pages recuperees OK")

# ══════════════════════════════════════════════════════════════════════════════
# 4. PATCH NOTES (Riot officiel)
# ══════════════════════════════════════════════════════════════════════════════
print("\n[4/4] Patch notes Riot...")

PATCH_URLS = [
    ("26.12", "https://www.leagueoflegends.com/en-us/news/game-updates/patch-26-12-notes/"),
    ("26.11", "https://www.leagueoflegends.com/en-us/news/game-updates/patch-26-11-notes/"),
    ("26.10", "https://www.leagueoflegends.com/en-us/news/game-updates/patch-26-10-notes/"),
]

for pid, url in PATCH_URLS:
    try:
        r = requests.get(url, headers=HEADERS, timeout=15)
        if r.status_code != 200:
            print(f"   Patch {pid} introuvable (status {r.status_code})")
            continue
        raw = re.sub(r"<script[^>]*>.*?</script>", "", r.text, flags=re.DOTALL)
        raw = re.sub(r"<style[^>]*>.*?</style>", "", raw, flags=re.DOTALL)
        text = clean(raw)
        # Garde une portion lisible
        add(f"patch_{pid}", f"Patch notes {pid} :\n{text[500:4000]}\n")
        print(f"   Patch {pid} OK")
    except Exception as e:
        print(f"   Erreur patch {pid}: {e}")

# ══════════════════════════════════════════════════════════════════════════════
# 5. CONTEXTE MÉTA & STRATÉGIE
# ══════════════════════════════════════════════════════════════════════════════
meta_chunks = [
    ("meta_macro",
     "Macro LoL — Priorite objectifs :\n"
     "1. Dragon (ame apres 4 stacks = avantage massif). "
     "2. Baron Nashor (buff 3 min, renforce les minions). "
     "3. Rift Herald (detruit les tours). "
     "4. Tourelles (pression de carte, or). "
     "5. Inhibiteurs (super minions). "
     "Regle d'or : ne pas mourir pour rien. Jouer autour des objectifs, pas des kills."),

    ("meta_roles",
     "Roles et responsabilites :\n"
     "Top : duels, split push, tanks ou fighters.\n"
     "Jungle : gank, objectifs, vision, tempo.\n"
     "Mid : roam, pression centrale, mages/assassins.\n"
     "ADC : DPS constant en late game, se positionner loin en teamfight.\n"
     "Support : engage, peel, vision, proteger l'ADC."),

    ("meta_wave",
     "Wave management :\n"
     "Freeze : garder la vague sous sa tour pour affamer l'ennemi.\n"
     "Slow push : laisser grossir la vague -> pression + dive possible.\n"
     "Fast push : push rapide -> roam ou objectif.\n"
     "Crash : envoyer une grosse vague sur la tour avant de roam."),

    ("meta_vision",
     "Vision (wards) :\n"
     "Toujours avoir des wards actives. Les placer avant 5 min en riviere.\n"
     "Control ward : a poser sur l'objectif (dragon/baron) avant le combat.\n"
     "Sweeper (Trinket rouge) : nettoyer les wards ennemies avant d'engager."),

    ("meta_ranked",
     "Conseils ranked :\n"
     "1. Jouer 2-3 champions max, les maitriser a fond.\n"
     "2. Analyser ses propres erreurs (replay).\n"
     "3. Regarder la minimap toutes les 5 secondes.\n"
     "4. Ping avant d'agir.\n"
     "5. Ne jamais tilt. Mute si necessaire.\n"
     "6. Savoir qui gagne le late/early et jouer en consequence."),

    ("meta_teamfight",
     "Teamfight :\n"
     "Assassin : attendre que le front engage, puis tuer le carry ennemi.\n"
     "Tank/Engage : initier quand l'ennemi est mal positionne.\n"
     "ADC : rester a portee max, tirer en continu, NE PAS S'AVANCER.\n"
     "Mage : zone de controle, AoE sur un max d'ennemis.\n"
     "Support : coller son ADC ou peel le carry allie."),

    ("meta_early",
     "Early game (0-14 min) :\n"
     "Focus sur le farm (CS). 6 CS = 1 kill en or.\n"
     "Jungle : clear camps + gank les lanes en faiblesse.\n"
     "Mid : roam top ou bot apres avoir push la vague.\n"
     "Bot lane : dominer la lane pour prendre le dragon facilement."),

    ("meta_mid",
     "Mid game (14-25 min) :\n"
     "Grouper autour des objectifs (dragon, herald).\n"
     "Ne pas split push seul sans vision.\n"
     "Pousser l'avantage apres un baron ou une ame de dragon."),

    ("meta_late",
     "Late game (25+ min) :\n"
     "Jouer ensemble, ne pas se faire attraper seul.\n"
     "Baron + Elder Dragon = win condition.\n"
     "Eviter les trades inutiles, attendre le bon moment pour engager."),
]

for id_, texte in meta_chunks:
    add(id_, texte)

# ══════════════════════════════════════════════════════════════════════════════
# EMBEDDING & INSERTION
# ══════════════════════════════════════════════════════════════════════════════
print(f"\nEmbedding de {len(chunks)} chunks dans ChromaDB...")
print("(Environ 1s par chunk)")

errors = 0
for i, (texte, id_) in enumerate(zip(chunks, ids)):
    try:
        emb = ollama.embed(model=EMBED_MODEL, input=texte)["embeddings"][0]
        collection.add(ids=[id_], documents=[texte], embeddings=[emb])
    except Exception as e:
        print(f"   Erreur embedding {id_}: {e}")
        errors += 1
    if (i + 1) % 100 == 0:
        print(f"   {i+1}/{len(chunks)} chunks indexes...")

print(f"\n Base LoL prete ! {len(chunks) - errors} chunks indexes ({errors} erreurs).")
print("Lance maintenant : streamlit run app.py")