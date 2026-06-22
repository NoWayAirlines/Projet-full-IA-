"""
lol_rag.py — Cerveau de l'assistant LoL.
Récupération intelligente : détecte les champions mentionnés et force la récupération
de leurs builds en plus de la recherche sémantique classique.
"""

import re
import ollama
import chromadb
from builds import BUILDS

# Charge la base persistante (remplie par scrapper.py)
client = chromadb.PersistentClient(path="./lol_db")
collection = client.get_collection("lol")

# Liste de tous les champions connus
CHAMPIONS_CONNUS = set(BUILDS.keys()) | {
    "Aatrox", "Ahri", "Akali", "Alistar", "Amumu", "Anivia", "Annie", "Ashe",
    "Azir", "Bard", "Blitzcrank", "Brand", "Braum", "Caitlyn", "Camille",
    "Cassiopeia", "Cho'Gath", "Corki", "Darius", "Diana", "Dr. Mundo", "Draven",
    "Ekko", "Elise", "Evelynn", "Ezreal", "Fiddlesticks", "Fiora", "Fizz",
    "Galio", "Gangplank", "Garen", "Gnar", "Gragas", "Graves", "Hecarim",
    "Heimerdinger", "Illaoi", "Irelia", "Ivern", "Janna", "Jarvan IV", "Jax",
    "Jayce", "Jhin", "Jinx", "Kai'Sa", "Kalista", "Karma", "Karthus",
    "Kassadin", "Katarina", "Kayle", "Kayn", "Kennen", "Kha'Zix", "Kindred",
    "Kled", "Kog'Maw", "LeBlanc", "Lee Sin", "Leona", "Lillia", "Lissandra",
    "Lucian", "Lulu", "Lux", "Malphite", "Malzahar", "Maokai", "Master Yi",
    "Miss Fortune", "Mordekaiser", "Morgana", "Nami", "Nasus", "Nautilus",
    "Neeko", "Nidalee", "Nocturne", "Nunu", "Olaf", "Orianna", "Ornn",
    "Pantheon", "Poppy", "Pyke", "Qiyana", "Quinn", "Rakan", "Rammus",
    "Rek'Sai", "Rell", "Renekton", "Rengar", "Riven", "Rumble", "Ryze",
    "Samira", "Sejuani", "Senna", "Seraphine", "Sett", "Shaco", "Shen",
    "Shyvana", "Singed", "Sion", "Sivir", "Skarner", "Sona", "Soraka",
    "Swain", "Sylas", "Syndra", "Taliyah", "Talon", "Taric", "Teemo",
    "Thresh", "Tristana", "Trundle", "Tryndamere", "Twisted Fate", "Twitch",
    "Udyr", "Urgot", "Varus", "Vayne", "Veigar", "Vel'Koz", "Vi", "Viktor",
    "Vladimir", "Volibear", "Warwick", "Wukong", "Xayah", "Xerath", "Xin Zhao",
    "Yasuo", "Yone", "Yorick", "Yuumi", "Zac", "Zed", "Ziggs", "Zilean",
    "Zoe", "Zyra",
}

SYSTEM_PROMPT = """Tu es un coach LoL niveau Challenger. Style : pro, direct, dense.

RÈGLES :
1. Réponses courtes par défaut. Si l'utilisateur demande plus de détails ou de clarté, développe.
2. Noms de champions, items, sorts, runes : TOUJOURS en anglais. Ne traduis jamais.
3. Utilise le vocabulaire pro : burst, poke, all-in, kite, peel, engage, disengage, splitpush, wave clear, roam, snowball, powerspike, itemisation, matchup, trading pattern, lane bully, hypercarry, frontline, backline, dive, reset, etc.
4. Items et données : UNIQUEMENT ce qui est dans le CONTEXTE. Si absent, dis "pas de data sur ça".
5. N'invente rien. Jamais.
6. Précise toujours qui joue qui : "Tu joues X vs Y." Si ambigu, demande avant de répondre.
7. Chaque item = justification pro en 5 mots max entre parenthèses.

FORMAT build :
👤 Tu joues : X | vs : Y
🟢 Départ : ...
🔵 Build :
  1. Item1 (justification)
  2. Item2 (justification)
  3. Item3 (justification)
  4. Item4 (justification)
  5. Item5 (justification)
  6. Item6 (justification)
🔑 Runes : ...
⚡ Spells : ...
📈 Ordre sorts : ..."""


def detecter_champions(texte: str) -> list[str]:
    """Retourne les noms de champions présents dans le texte (insensible à la casse)."""
    texte_lower = texte.lower()
    return [c for c in CHAMPIONS_CONNUS if c.lower() in texte_lower]


def recuperer_contexte(question: str, historique: list, n_semantic: int = 5) -> tuple[str, dict]:
    """
    Récupère le contexte en deux étapes :
    1. Force la récupération des builds des champions mentionnés (par ID exact)
    2. Complète avec une recherche sémantique classique
    """
    docs_forces = []
    ids_deja_vus = set()

    # Cherche les champions dans la question ET toute la conversation
    texte_complet = question + " " + " ".join(
        m["content"] for m in historique if m["role"] == "user"
    )
    champions_detectes = detecter_champions(texte_complet)

    # Force la récupération des builds pour chaque champion détecté
    for champ in champions_detectes:
        slug = champ.lower().replace(" ", "_").replace("'", "").replace(".", "")
        ids_a_chercher = [
            f"build_main_{slug}",
            f"build_{slug}_standard",
            f"build_{slug}_standard_(comp_équilibrée)",
            f"build_{slug}_vs_tanks_(urgot,_malphite,_ornn...)",
            f"build_{slug}_vs_assassins_(zed,_talon,_katarina...)",
            f"build_{slug}_vs_healers_(soraka,_yuumi,_aatrox...)",
            f"build_{slug}_fighter_(carry)",
            f"build_{slug}_tank_(résistance_max)",
            f"build_{slug}_fighter",
            f"build_{slug}_tank",
            f"build_{slug}_enchanteur",
            f"counters_{slug}",
            f"strong_{slug}",
        ]
        try:
            res = collection.get(ids=ids_a_chercher)
            for doc in (res.get("documents") or []):
                if doc and doc not in ids_deja_vus:
                    docs_forces.append(doc)
                    ids_deja_vus.add(doc)
        except Exception:
            pass

    # Recherche sémantique classique
    q_emb = ollama.embed(model="nomic-embed-text", input=question)["embeddings"][0]
    resultats = collection.query(query_embeddings=[q_emb], n_results=n_semantic)

    # Fusionne sans doublons (builds forcés en premier = prioritaires)
    docs_finaux = list(docs_forces)
    for doc in resultats["documents"][0]:
        if doc not in ids_deja_vus:
            docs_finaux.append(doc)
            ids_deja_vus.add(doc)

    contexte = "\n\n---\n\n".join(docs_finaux)
    return contexte, resultats


def repondre(question: str, historique: list):
    contexte, resultats = recuperer_contexte(question, historique)

    messages = [{"role": "system", "content": SYSTEM_PROMPT}]
    messages += historique
    messages.append({
        "role": "user",
        "content": f"CONTEXTE (données réelles LoL — utilise UNIQUEMENT ceci) :\n{contexte}\n\nQUESTION : {question}",
    })

    reponse = ollama.chat(model="llama3.2", messages=messages)["message"]["content"]
    return reponse, resultats
