"""
builds.py — Builds détaillés avec chemins d'items complets + ajustements selon l'ennemi.
Source : u.gg / lolalytics (patch 2025).
"""

BUILDS = {

    # ══════════════════════════════════════════════════════════════════════════
    # ADC
    # ══════════════════════════════════════════════════════════════════════════

    "Jinx": {
        "role": "ADC (Bot Lane)",
        "playstyle": (
            "Hypercarry late game. Très faible early, dévastatrice à partir du 2e-3e item. "
            "Ne prends pas de risques avant d'avoir Kraken Slayer + Hurricane. "
            "Ton ult (Super Mega Death Rocket!) est global : surveille la minimap."
        ),
        "summoner_spells": "Flash + Heal",
        "runes": {
            "primary_keystone": "Lethal Tempo (Precision)",
            "precision": "Presence of Mind | Legend: Bloodline | Cut Down",
            "secondary_tree": "Domination",
            "secondary": "Eyeball Collection | Treasure Hunter",
        },
        "skill_order": "Monter R dès que possible. Puis Q > W > E.",
        "starting_items": "Doran's Blade + Health Potion",

        "build_paths": {
            "standard (comp équilibrée)": {
                "ordre": ["Kraken Slayer", "Runaan's Hurricane", "Infinity Edge", "Phantom Dancer", "Lord Dominik's Regards", "Bloodthirster"],
                "chemins": {
                    "Kraken Slayer (3200g)": "Long Sword (350g) → Pickaxe (875g) → Kraken Slayer",
                    "Runaan's Hurricane (2600g)": "Zeal (1050g) → Runaan's Hurricane",
                    "Infinity Edge (3400g)": "BF Sword (1300g) → Pickaxe (875g) → Cloak of Agility (600g) → Infinity Edge",
                    "Phantom Dancer (2600g)": "Zeal (1050g) → Phantom Dancer",
                    "Lord Dominik's Regards (3000g)": "Last Whisper (1450g) → Lord Dominik's Regards",
                    "Bloodthirster (3400g)": "BF Sword (1300g) → Bloodthirster",
                },
                "premier_retour": "Accroche Long Sword (350g). Si 875g → Pickaxe. Si 1600g → Pickaxe + Dagger.",
            },
            "vs tanks (Urgot, Malphite, Ornn...)": {
                "ordre": ["Kraken Slayer", "Runaan's Hurricane", "Infinity Edge", "Lord Dominik's Regards", "Mortal Reminder", "Phantom Dancer"],
                "chemins": {
                    "Kraken Slayer (3200g)": "Long Sword → Pickaxe → Kraken Slayer",
                    "Runaan's Hurricane (2600g)": "Zeal → Runaan's Hurricane",
                    "Infinity Edge (3400g)": "BF Sword → Pickaxe → Cloak of Agility → Infinity Edge",
                    "Lord Dominik's Regards (3000g)": "Last Whisper (1450g) → Lord Dominik's",
                    "Mortal Reminder (2500g)": "Last Whisper (1450g) → Mortal Reminder (si beaucoup de heal ennemi)",
                    "Phantom Dancer (2600g)": "Zeal → Phantom Dancer",
                },
                "note": "Kraken Slayer fait des vrais dégâts aux tanks. Lord Dominik's Regards ignore la moitié de l'armure adverse.",
            },
            "vs assassins (Zed, Talon, Katarina...)": {
                "ordre": ["Galeforce", "Kraken Slayer", "Infinity Edge", "Phantom Dancer", "Guardian Angel", "Bloodthirster"],
                "chemins": {
                    "Galeforce (3400g)": "Caulfield's Warhammer (1100g) → BF Sword (1300g) → Galeforce",
                    "Kraken Slayer (3200g)": "Long Sword → Pickaxe → Kraken Slayer",
                    "Infinity Edge (3400g)": "BF Sword → Pickaxe → Cloak → Infinity Edge",
                    "Phantom Dancer (2600g)": "Zeal → Phantom Dancer",
                    "Guardian Angel (3200g)": "Cloth Armor (300g) → Pickaxe (875g) → Guardian Angel",
                },
                "note": "Galeforce te donne un dash pour fuir les assassins. Guardian Angel pour la résurrection.",
            },
            "vs healers (Soraka, Yuumi, Aatrox...)": {
                "ordre": ["Kraken Slayer", "Runaan's Hurricane", "Infinity Edge", "Mortal Reminder", "Lord Dominik's Regards", "Phantom Dancer"],
                "chemins": {
                    "Mortal Reminder (2500g)": "Last Whisper (1450g) → Mortal Reminder — applique Grievous Wounds (-40% heal)",
                },
                "note": "Prends Mortal Reminder avant Lord Dominik's si l'ennemi a beaucoup de heal.",
            },
        },

        "matchup_jinx_vs_urgot": (
            "Urgot est un juggernaut tanky avec armor naturel et Purge (W) qui mitraille. "
            "Jinx est en désavantage en lane early — évite les trades courts. "
            "BUILD recommandé vs Urgot : Kraken Slayer → Runaan's Hurricane → Infinity Edge → Lord Dominik's Regards → Mortal Reminder → Phantom Dancer. "
            "Kraken Slayer perce les tanks, Runaan permet de hitter plusieurs cibles avec ses passifs, "
            "Lord Dominik's ignore l'armure d'Urgot. "
            "En teamfight : reste à distance max avec Fishbones (rockets Q). "
            "Utilise Flame Chompers! (E) pour stopper le dash/engage d'Urgot."
        ),

        "tips": [
            "Utilise Pow-Pow (attaque rapide, Q vers minigun) pour farmer en lane.",
            "Fishbones (rockets, Q vers lance-roquettes) pour le poke et les teamfights AoE.",
            "Flame Chompers! (E) : pose-les sous toi pour empêcher les dives.",
            "Ton passif Excited! : un kill ou assist te donne AS + MS — enchaîne les kills.",
            "Ton ult est global. Lance-le sur des ennemis bas HP repérés sur la minimap.",
        ],
    },

    "Caitlyn": {
        "role": "ADC (Bot Lane)",
        "playstyle": "Sniper, domination early, poke, contrôle de zone.",
        "summoner_spells": "Flash + Heal",
        "runes": {
            "primary_keystone": "Lethal Tempo ou Fleet Footwork (Precision)",
            "precision": "Presence of Mind | Legend: Bloodline | Cut Down",
            "secondary_tree": "Inspiration",
            "secondary": "Magical Footwear | Biscuit Delivery",
        },
        "skill_order": "R > Q > E > W",
        "starting_items": "Doran's Blade + Health Potion",
        "build_paths": {
            "standard": {
                "ordre": ["Galeforce", "Kraken Slayer", "Infinity Edge", "Phantom Dancer", "Lord Dominik's Regards", "Mortal Reminder"],
                "chemins": {
                    "Galeforce (3400g)": "Caulfield's Warhammer (1100g) → BF Sword → Galeforce",
                    "Kraken Slayer (3200g)": "Long Sword → Pickaxe → Kraken Slayer",
                    "Infinity Edge (3400g)": "BF Sword → Pickaxe → Cloak → Infinity Edge",
                },
            },
        },
        "tips": [
            "Yordle Snap Trap (W) : pose les pièges sur les buissons et autour des objectifs.",
            "Headshot (passif) : tous les 6 coups, ton auto fait x2 dégâts.",
            "En teamfight, vise toujours les ennemis piégés par ton E ou tes W.",
        ],
    },

    "Jhin": {
        "role": "ADC (Bot Lane)",
        "playstyle": "4 balles, burst, assassin-ADC. Forte la 4e balle.",
        "summoner_spells": "Flash + Heal",
        "runes": {
            "primary_keystone": "Fleet Footwork (Precision)",
            "precision": "Presence of Mind | Legend: Bloodline | Cut Down",
            "secondary_tree": "Sorcery",
            "secondary": "Absolute Focus | Gathering Storm",
        },
        "skill_order": "R > Q > W > E",
        "starting_items": "Doran's Blade + Health Potion",
        "build_paths": {
            "standard": {
                "ordre": ["Galeforce", "The Collector", "Infinity Edge", "Mortal Reminder", "Lord Dominik's Regards", "Bloodthirster"],
                "chemins": {
                    "Galeforce (3400g)": "Caulfield's Warhammer → BF Sword → Galeforce",
                    "The Collector (3000g)": "Serrated Dirk (1100g) → Pickaxe → The Collector — exécute sous 5% HP",
                    "Infinity Edge (3400g)": "BF Sword → Pickaxe → Cloak → Infinity Edge",
                },
            },
        },
        "tips": [
            "La 4e balle scale sur ton AD total — plus tu as d'AD, plus elle fait de dégâts.",
            "Ne gaspille pas ta 4e balle sur un minion. Reload = vulnérabilité.",
            "Deadly Flourish (W) : root l'ennemi s'il a été touché par un allié.",
        ],
    },

    # ══════════════════════════════════════════════════════════════════════════
    # TOP
    # ══════════════════════════════════════════════════════════════════════════

    "Malphite": {
        "role": "Top Lane / Support",
        "playstyle": "Tank CC, engage AoE one-shot avec R, frontline inaccessible. Powerspike fort au R lvl 6.",
        "summoner_spells": "Flash + Teleport (ou Ignite si lane agressive)",
        "runes": {
            "primary_keystone": "Arcane Comet (Sorcery) — poke en lane | ou Grasp of the Undying (Resolve) — sustain",
            "sorcery": "Manaflow Band | Transcendence | Scorch (poke) ou Gathering Storm (scaling)",
            "secondary_tree": "Resolve",
            "secondary": "Bone Plating | Overgrowth",
        },
        "skill_order": "R > E > W > Q",
        "starting_items": "Doran's Ring + Health Potion x2 (AP) ou Doran's Shield + Health Potion (tank)",
        "build_paths": {
            "full tank (engage teamfight)": {
                "ordre": ["Sunfire Aegis", "Thornmail", "Warmog's Armor", "Force of Nature", "Randuin's Omen", "Abyssal Mask"],
                "chemins": {
                    "Sunfire Aegis (3200g)": "Bami's Cinder (1000g) → Chain Vest (800g) → Sunfire Aegis",
                    "Thornmail (2700g)": "Chain Vest → Bami's Cinder → Thornmail — Grievous Wounds si heal ennemi",
                    "Warmog's Armor (3000g)": "Giant's Belt (900g) → Warmog's — regen passive si +1100 HP",
                    "Force of Nature (2900g)": "Negatron Cloak (900g) → Force of Nature — si AP lourde",
                    "Randuin's Omen (2700g)": "Warden's Mail (1000g) → Giant's Belt → Randuin's — réduit les crits ennemis",
                    "Abyssal Mask (2300g)": "Spectre's Cowl → Abyssal Mask — booste AP alliés proches",
                },
                "premier_retour": "Rush Bami's Cinder (1000g) pour le sustain et les dégâts passifs.",
            },
            "AP (one-shot assassin)": {
                "ordre": ["Rod of Ages", "Shadowflame", "Rabadon's Deathcap", "Zhonya's Hourglass", "Void Staff", "Ionian Boots of Lucidity"],
                "chemins": {
                    "Rod of Ages (2600g)": "Catalyst of Aeons (1100g) → Rod of Ages — scale sur 10 min",
                    "Shadowflame (3000g)": "Needlessly Large Rod (1250g) → Shadowflame — perce les boucliers",
                    "Rabadon's Deathcap (3800g)": "Needlessly Large Rod → Rabadon's — +40% AP total",
                    "Zhonya's Hourglass (2900g)": "Seeker's Armguard (1300g) → Zhonya's — stase après le R",
                    "Void Staff (2800g)": "Blighting Jewel → Void Staff — perce la MR",
                },
                "note": "Build AP = one-shot garanti au R si ennemi squishy. Risqué mais dévastateur.",
            },
            "vs Jayce (lane poke)": {
                "ordre": ["Rod of Ages", "Sunfire Aegis", "Warmog's Armor", "Thornmail", "Force of Nature", "Randuin's Omen"],
                "note": (
                    "Jayce est un lane bully à distance qui te poke en forme canon. "
                    "Rush Rod of Ages pour le sustain. Reste derrière tes minions pour éviter le poke. "
                    "Wait lvl 6 : ton R (Unstoppable Force) est un engage AoE instantané — Jayce ne peut pas l'esquiver. "
                    "Flash + R = kill assuré si Jayce est mal positionné."
                ),
            },
        },
        "counters": "Jayce, Kennen, Vayne Top (kite). Évite les ranged bully.",
        "strong_vs": "Yasuo, Tryndamere, Zed Top, Pantheon. Tous les melees sans dash.",
        "tips": [
            "Unstoppable Force (R) : engage AoE instantané, inévitable. Combo avec Flash pour surprendre.",
            "Ground Slam (E) : réduit l'AS des ennemis proches — parfait contre ADC et fighters AA-based.",
            "Thunderclap (W) : passif bouclier permanent. Actif = prochain AA + éclaboussures.",
            "En teamfight : R sur le maximum d'ennemis, priorité sur les carries ennemis.",
        ],
    },

    "Jayce": {
        "role": "Top Lane / Mid Lane",
        "playstyle": "Lane bully ranged, poke dominant, switch marteau/canon. Forte early, tombe en late.",
        "summoner_spells": "Flash + Teleport",
        "runes": {
            "primary_keystone": "Conqueror (Precision) — trades longs | ou Arcane Comet (Sorcery) — poke",
            "precision": "Triumph | Legend: Alacrity | Last Stand",
            "secondary_tree": "Sorcery",
            "secondary": "Manaflow Band | Transcendence",
        },
        "skill_order": "R > Q > W > E",
        "starting_items": "Long Sword + Health Potion x3 (agressif) ou Doran's Shield (safe)",
        "build_paths": {
            "standard (fighter)": {
                "ordre": ["Trinity Force", "The Collector", "Serylda's Grudge", "Edge of Night", "Lord Dominik's Regards", "Guardian Angel"],
                "chemins": {
                    "Trinity Force (3333g)": "Phage (1100g) → Sheen (700g) → Stinger (1100g) → Trinity Force — powerspike massif",
                    "The Collector (3000g)": "Serrated Dirk (1100g) → Pickaxe → The Collector — exécute sous 5% HP",
                    "Serylda's Grudge (3200g)": "Caulfield's Warhammer → Pickaxe → Serylda's — slow permanent sur Q",
                    "Edge of Night (2900g)": "Serrated Dirk → Long Sword → Edge of Night — spell shield anti-engage",
                    "Lord Dominik's Regards (3000g)": "Last Whisper → Lord Dominik's — si tanks",
                    "Guardian Angel (3200g)": "Cloth Armor → Pickaxe → Guardian Angel — résurrection",
                },
                "premier_retour": "Rush Phage (1100g). Si 1300g → Sheen.",
            },
            "vs tanks": {
                "ordre": ["Trinity Force", "Void Staff", "Serylda's Grudge", "Lord Dominik's Regards", "Edge of Night", "Guardian Angel"],
                "note": "Ajoute Void Staff pour percer la MR si les tanks stackent de la résistance magique.",
            },
        },
        "counters": "Malphite (R inévitable), Camille, Irelia (post-6).",
        "strong_vs": "Garen, Malphite early (poke), Nasus, champions sans dash.",
        "tips": [
            "Forme Canon : poke à distance avec Q (Shock Blast) amplifié par W (Hyper Charge).",
            "Forme Marteau : engage, all-in, trades courts avec E (Thundering Blow) pour repousser.",
            "Switch forme intelligemment : poke en canon → all-in en marteau si ennemi low.",
            "Jayce tombe en late game — snowball ou impacter avant 25 min.",
        ],
    },
    # ══════════════════════════════════════════════════════════════════════════

    "Urgot": {
        "role": "Top Lane",
        "playstyle": "Juggernaut tanky-fighter. Domine la lane early/mid. Exécution au R.",
        "summoner_spells": "Flash + Ignite (agressif) ou Flash + Teleport (macro)",
        "runes": {
            "primary_keystone": "Conqueror (Precision)",
            "precision": "Triumph | Legend: Tenacity | Last Stand",
            "secondary_tree": "Resolve",
            "secondary": "Bone Plating | Overgrowth",
        },
        "skill_order": "R > E > Q > W",
        "starting_items": "Doran's Shield + Health Potion (Longsword si agressif)",
        "build_paths": {
            "fighter (carry)": {
                "ordre": ["Trinity Force", "Sterak's Gage", "Death's Dance", "Thornmail", "Force of Nature", "Guardian Angel"],
                "chemins": {
                    "Trinity Force (3333g)": "Phage (1100g) → Sheen (700g) → Stinger (1100g) → Trinity Force",
                    "Sterak's Gage (3100g)": "Kindlegem (800g) → Giant's Belt (900g) → Sterak's Gage",
                    "Death's Dance (3300g)": "Caulfield's Warhammer (1100g) → Chain Vest (800g) → Death's Dance",
                    "Thornmail (2700g)": "Chain Vest (800g) → Bami's Cinder (1000g) → Thornmail — si heal ennemi",
                    "Force of Nature (2900g)": "Negatron Cloak (900g) → Force of Nature — si beaucoup d'AP ennemi",
                },
                "premier_retour": "Rush Phage (1100g) si possible, sinon Long Sword.",
            },
            "tank (résistance max)": {
                "ordre": ["Heartsteel", "Sunfire Aegis", "Warmog's Armor", "Thornmail", "Force of Nature", "Randuin's Omen"],
                "chemins": {
                    "Heartsteel (2800g)": "Crystalline Bracer (800g) → Giant's Belt (900g) → Heartsteel",
                    "Sunfire Aegis (3200g)": "Bami's Cinder (1000g) → Chain Vest (800g) → Sunfire Aegis",
                    "Warmog's Armor (3000g)": "Giant's Belt (900g) → Warmog's",
                },
            },
            "vs healing (Mundo, Soraka...)": {
                "ordre": ["Trinity Force", "Sterak's Gage", "Thornmail", "Death's Dance", "Force of Nature", "Guardian Angel"],
                "note": "Rush Thornmail en 3e si beaucoup de heal ennemi. Grievous Wounds (-40% heal).",
            },
        },
        "counters": "Trundle, Fiora, Vayne (Top). Évite ces matchups si possible.",
        "strong_vs": "Garen, Malphite, Sett, Cho'Gath.",
        "tips": [
            "Purge (W) : mitraille pendant 4s, slow, root si ennemi proche. Utilise en échange court.",
            "Disdain (E) : dash + CC sur un ennemi derrière toi. Parfait pour interrompre les fuyards.",
            "Fear Beyond Death (R) : exécute les ennemis sous ~25% HP. Réactivable pour les tirer.",
            "Ta force vient de l'échange Purge (W) + Corrosive Charge (Q). Engage, Q, W, E si nécessaire.",
        ],
    },

    "Darius": {
        "role": "Top Lane",
        "playstyle": "Juggernaut, saignement (Hemorrhage), snowball, exécution Noxian Guillotine (R).",
        "summoner_spells": "Flash + Ghost (pour rattraper) ou Flash + Ignite",
        "runes": {
            "primary_keystone": "Conqueror (Precision)",
            "precision": "Triumph | Legend: Tenacity | Last Stand",
            "secondary_tree": "Resolve",
            "secondary": "Bone Plating | Overgrowth",
        },
        "skill_order": "R > Q > W > E",
        "starting_items": "Doran's Shield + Health Potion",
        "build_paths": {
            "standard": {
                "ordre": ["Trinity Force", "Sterak's Gage", "Death's Dance", "Hullbreaker", "Thornmail", "Warmog's Armor"],
                "chemins": {
                    "Trinity Force (3333g)": "Phage → Sheen → Stinger → Trinity Force",
                    "Sterak's Gage (3100g)": "Kindlegem → Giant's Belt → Sterak's Gage",
                    "Death's Dance (3300g)": "Caulfield's Warhammer → Chain Vest → Death's Dance",
                    "Hullbreaker (3000g)": "Longsword → Pickaxe → Hullbreaker — pour split push",
                },
            },
        },
        "tips": [
            "Ton Q Decimate heal si tu touches le bord extérieur. Toujours viser avec le bord.",
            "5 stacks de Hemorrhage = passif Noxian Might (+bonus AD énorme).",
            "Ghost > Flash pour kiter les fuyards et rester en range pour le R.",
        ],
    },

    "Garen": {
        "role": "Top Lane",
        "playstyle": "Tank-fighter simple, silence Q, spin E, exécution R. Bon pour apprendre le top.",
        "summoner_spells": "Flash + Teleport",
        "runes": {
            "primary_keystone": "Conqueror (Precision)",
            "precision": "Triumph | Legend: Tenacity | Last Stand",
            "secondary_tree": "Resolve",
            "secondary": "Bone Plating | Revitalize",
        },
        "skill_order": "R > Q > E > W",
        "starting_items": "Doran's Shield + Health Potion",
        "build_paths": {
            "standard": {
                "ordre": ["Trinity Force", "Sterak's Gage", "Warmog's Armor", "Thornmail", "Force of Nature", "Dead Man's Plate"],
                "chemins": {
                    "Trinity Force (3333g)": "Phage → Sheen → Stinger → Trinity Force",
                    "Sterak's Gage (3100g)": "Kindlegem → Giant's Belt → Sterak's Gage",
                    "Warmog's Armor (3000g)": "Giant's Belt → Warmog's — active la regen passive",
                },
            },
        },
    },

    # ══════════════════════════════════════════════════════════════════════════
    # MID
    # ══════════════════════════════════════════════════════════════════════════

    "Ahri": {
        "role": "Mid Lane",
        "playstyle": "Assassin-mage mobile, pick, roam. Fort au milieu de partie.",
        "summoner_spells": "Flash + Ignite",
        "runes": {
            "primary_keystone": "Electrocute (Domination)",
            "domination": "Taste of Blood | Eyeball Collection | Treasure Hunter",
            "secondary_tree": "Sorcery",
            "secondary": "Manaflow Band | Transcendence",
        },
        "skill_order": "R > Q > E > W",
        "starting_items": "Doran's Ring + Health Potion x2",
        "build_paths": {
            "standard": {
                "ordre": ["Luden's Tempest", "Shadowflame", "Rabadon's Deathcap", "Zhonya's Hourglass", "Void Staff"],
                "chemins": {
                    "Luden's Tempest (3200g)": "Lost Chapter (1300g) → Amplifying Tome → Luden's Tempest",
                    "Shadowflame (3000g)": "Amplifying Tome → Needlessly Large Rod (1250g) → Shadowflame",
                    "Rabadon's Deathcap (3800g)": "Needlessly Large Rod → Rabadon's — +40% AP",
                    "Zhonya's Hourglass (2900g)": "Seeker's Armguard (1300g) → Zhonya's — si beaucoup d'AD",
                    "Void Staff (2800g)": "Blighting Jewel (1250g) → Void Staff — si ennemis résistants magie",
                },
                "premier_retour": "Rush Lost Chapter (1300g) pour la mana et le CDR.",
            },
            "vs tanks": {
                "ordre": ["Luden's Tempest", "Shadowflame", "Void Staff", "Rabadon's Deathcap", "Zhonya's Hourglass"],
                "note": "Prends Void Staff en 3e si les ennemis stackent de la résistance magique.",
            },
        },
        "tips": [
            "Orb of Deception (Q) : touche à l'aller ET au retour. Vise pour maximiser.",
            "Charm (E) : immobilise et amplifie tes dégâts. Engage toujours avec E → Q → W.",
            "Spirit Rush (R) : 3 dash en 10s. Utilise pour engage, pourchasser ou fuir.",
        ],
    },

    "Zed": {
        "role": "Mid Lane / Top",
        "playstyle": "Assassin, burst one-shot, split push. Snowball violent.",
        "summoner_spells": "Flash + Ignite",
        "runes": {
            "primary_keystone": "Electrocute (Domination)",
            "domination": "Taste of Blood | Eyeball Collection | Treasure Hunter",
            "secondary_tree": "Inspiration",
            "secondary": "Magical Footwear | Future's Market",
        },
        "skill_order": "R > Q > W > E",
        "starting_items": "Long Sword + Health Potion x3",
        "build_paths": {
            "standard": {
                "ordre": ["The Collector", "Youmuu's Ghostblade", "Edge of Night", "Serpent's Fang", "Lord Dominik's Regards", "Serylda's Grudge"],
                "chemins": {
                    "The Collector (3000g)": "Serrated Dirk (1100g) → Pickaxe → The Collector — exécute sous 5%",
                    "Youmuu's Ghostblade (3000g)": "Serrated Dirk → Caulfield's Warhammer (1100g) → Youmuu's",
                    "Edge of Night (2900g)": "Serrated Dirk → Long Sword → Edge of Night — bouclier anti-sort",
                    "Serpent's Fang (2600g)": "Serrated Dirk → Long Sword → Serpent's Fang — si boucliers ennemis",
                    "Lord Dominik's Regards (3000g)": "Last Whisper → Lord Dominik's — si tanks",
                    "Serylda's Grudge (3200g)": "Caulfield's Warhammer → Pickaxe → Serylda's — slow permanent",
                },
                "premier_retour": "Rush Serrated Dirk (1100g) pour le lethality.",
            },
        },
        "tips": [
            "Combo de base : W (shadow) → E (slow) → Q (shurikens) → R (ult) → reposition → Q + E → récupère W.",
            "Living Shadow (W) : échange avec ta shadow pour repositionner. Utilise pour fuir aussi.",
            "Death Mark (R) : ta marque explose après 3s. Assure le kill avant.",
        ],
    },

    "Lux": {
        "role": "Mid Lane / Support",
        "playstyle": "Mage burst longue portée, poke, snipe.",
        "summoner_spells": "Flash + Ignite (mid) | Flash + Exhaust (support)",
        "runes": {
            "primary_keystone": "Arcane Comet (Sorcery)",
            "sorcery": "Manaflow Band | Transcendence | Scorch",
            "secondary_tree": "Precision",
            "secondary": "Presence of Mind | Cut Down",
        },
        "skill_order": "R > E > Q > W",
        "starting_items": "Doran's Ring + Health Potion x2",
        "build_paths": {
            "standard": {
                "ordre": ["Luden's Tempest", "Shadowflame", "Rabadon's Deathcap", "Void Staff", "Zhonya's Hourglass"],
                "chemins": {
                    "Luden's Tempest (3200g)": "Lost Chapter → Amplifying Tome → Luden's",
                    "Shadowflame (3000g)": "Needlessly Large Rod → Shadowflame",
                    "Rabadon's Deathcap (3800g)": "Needlessly Large Rod → Rabadon's",
                    "Void Staff (2800g)": "Blighting Jewel → Void Staff",
                    "Zhonya's Hourglass (2900g)": "Seeker's Armguard → Zhonya's",
                },
            },
        },
        "tips": [
            "Light Binding (Q) : snare sur 2 cibles. Toujours Q avant R pour garantir le touch.",
            "Finales Funkeln (R) : très faible CD si tu touches. Utilise souvent.",
            "Passif Illumination : marque les ennemis, ton prochain auto double les dégâts.",
        ],
    },

    "Yasuo": {
        "role": "Mid Lane / Top",
        "playstyle": "Fighter carry, bouclier passif, critkeur, hypercarry.",
        "summoner_spells": "Flash + Ignite",
        "runes": {
            "primary_keystone": "Lethal Tempo (Precision)",
            "precision": "Triumph | Legend: Alacrity | Last Stand",
            "secondary_tree": "Resolve",
            "secondary": "Bone Plating | Overgrowth",
        },
        "skill_order": "R > Q > E > W",
        "starting_items": "Doran's Blade + Health Potion",
        "build_paths": {
            "standard": {
                "ordre": ["Immortal Shieldbow", "Infinity Edge", "Kraken Slayer", "Phantom Dancer", "Death's Dance", "Guardian Angel"],
                "chemins": {
                    "Immortal Shieldbow (3400g)": "Caulfield's Warhammer → Pickaxe → Cloak → Immortal Shieldbow",
                    "Infinity Edge (3400g)": "BF Sword → Pickaxe → Cloak → Infinity Edge — ne prends QUE si tu as 60%+ crit",
                    "Kraken Slayer (3200g)": "Long Sword → Pickaxe → Kraken Slayer — si tanks",
                    "Phantom Dancer (2600g)": "Zeal → Phantom Dancer",
                    "Death's Dance (3300g)": "Caulfield's Warhammer → Chain Vest → Death's Dance",
                    "Guardian Angel (3200g)": "Cloth Armor → Pickaxe → Guardian Angel",
                },
                "note": "N'achète Infinity Edge QUE quand tu as déjà 60% de crit (= Shieldbow + Phantom Dancer).",
            },
        },
    },

    # ══════════════════════════════════════════════════════════════════════════
    # JUNGLE
    # ══════════════════════════════════════════════════════════════════════════

    "Lee Sin": {
        "role": "Jungle",
        "playstyle": "Very strong early, invade, gank, carry early-mid. Tombe off en late.",
        "summoner_spells": "Flash + Smite",
        "runes": {
            "primary_keystone": "Conqueror (Precision)",
            "precision": "Triumph | Legend: Tenacity | Last Stand",
            "secondary_tree": "Resolve",
            "secondary": "Bone Plating | Overgrowth",
        },
        "skill_order": "R > Q > W > E",
        "starting_items": "Mosstomper Seedling (jungle item) + Health Potion",
        "build_paths": {
            "fighter": {
                "ordre": ["The Collector", "Youmuu's Ghostblade", "Death's Dance", "Sterak's Gage", "Serylda's Grudge", "Guardian Angel"],
                "chemins": {
                    "The Collector (3000g)": "Serrated Dirk → Pickaxe → The Collector",
                    "Youmuu's Ghostblade (3000g)": "Serrated Dirk → Caulfield's Warhammer → Youmuu's",
                    "Death's Dance (3300g)": "Caulfield's → Chain Vest → Death's Dance",
                },
            },
        },
    },

    "Vi": {
        "role": "Jungle",
        "playstyle": "Engage, dive sur le carry ennemi, tank-fighter.",
        "summoner_spells": "Flash + Smite",
        "runes": {
            "primary_keystone": "Conqueror (Precision)",
            "precision": "Triumph | Legend: Tenacity | Last Stand",
            "secondary_tree": "Resolve",
            "secondary": "Bone Plating | Unflinching",
        },
        "skill_order": "R > Q > E > W",
        "starting_items": "Gustwalker Hatchling (jungle item) + Health Potion",
        "build_paths": {
            "standard": {
                "ordre": ["Trinity Force", "Sterak's Gage", "Death's Dance", "Thornmail", "Force of Nature", "Guardian Angel"],
                "chemins": {
                    "Trinity Force (3333g)": "Phage → Sheen → Stinger → Trinity Force",
                    "Sterak's Gage (3100g)": "Kindlegem → Giant's Belt → Sterak's",
                    "Death's Dance (3300g)": "Caulfield's → Chain Vest → Death's Dance",
                },
            },
        },
    },

    "Amumu": {
        "role": "Jungle / Support",
        "playstyle": "Tank CC, engage AoE, teamfight dominant. Simple à jouer.",
        "summoner_spells": "Flash + Smite (jungle) | Flash + Exhaust (support)",
        "runes": {
            "primary_keystone": "Aftershock (Resolve)",
            "resolve": "Font of Life | Bone Plating | Overgrowth",
            "secondary_tree": "Sorcery",
            "secondary": "Manaflow Band | Transcendence",
        },
        "skill_order": "R > W > Q > E",
        "starting_items": "Gustwalker Hatchling (jungle) + Health Potion",
        "build_paths": {
            "tank": {
                "ordre": ["Sunfire Aegis", "Abyssal Mask", "Force of Nature", "Thornmail", "Warmog's Armor"],
                "chemins": {
                    "Sunfire Aegis (3200g)": "Bami's Cinder (1000g) → Chain Vest → Sunfire Aegis",
                    "Abyssal Mask (2300g)": "Spectre's Cowl → Abyssal Mask — boost AP alliés proches",
                    "Force of Nature (2900g)": "Negatron Cloak → Force of Nature",
                    "Thornmail (2700g)": "Chain Vest → Bami's Cinder → Thornmail",
                    "Warmog's Armor (3000g)": "Giant's Belt → Warmog's",
                },
            },
        },
    },

    # ══════════════════════════════════════════════════════════════════════════
    # SUPPORT
    # ══════════════════════════════════════════════════════════════════════════

    "Thresh": {
        "role": "Support",
        "playstyle": "Engage/peel, hook (Q), lanterne (W), versatile.",
        "summoner_spells": "Flash + Ignite (agressif) | Flash + Exhaust (peel)",
        "runes": {
            "primary_keystone": "Aftershock (Resolve)",
            "resolve": "Font of Life | Bone Plating | Overgrowth",
            "secondary_tree": "Inspiration",
            "secondary": "Biscuit Delivery | Cosmic Insight",
        },
        "skill_order": "R > W > E > Q",
        "starting_items": "Spellthief's Edge + Health Potion x2",
        "build_paths": {
            "standard": {
                "ordre": ["Locket of the Iron Solari", "Zeke's Convergence", "Knight's Vow", "Redemption", "Mikael's Blessing"],
                "chemins": {
                    "Locket of the Iron Solari (2500g)": "Kindlegem → Crystalline Bracer → Locket",
                    "Zeke's Convergence (2400g)": "Kindlegem → Null-Magic Mantle → Zeke's",
                    "Knight's Vow (2300g)": "Kindlegem → Giant's Belt → Knight's Vow",
                    "Redemption (2300g)": "Kindlegem → Crystalline Bracer → Redemption",
                },
            },
        },
        "tips": [
            "Death Sentence (Q) : hook. Réactive immédiatement pour te propulser vers l'ennemi.",
            "Dark Passage (W) : lanterne pour te placer et sauver un allié. Toujours avoir une lanterne dispo.",
            "Thresh est un champion skill-cap — la qualité de ton Q détermine tout.",
        ],
    },

    "Lulu": {
        "role": "Support",
        "playstyle": "Enchanteur, boucliers, peel. Protège le hypercarry allié.",
        "summoner_spells": "Flash + Exhaust",
        "runes": {
            "primary_keystone": "Summon Aery (Sorcery)",
            "sorcery": "Manaflow Band | Transcendence | Scorch",
            "secondary_tree": "Resolve",
            "secondary": "Font of Life | Revitalize",
        },
        "skill_order": "R > E > Q > W",
        "starting_items": "Spellthief's Edge + Health Potion x2",
        "build_paths": {
            "enchanteur": {
                "ordre": ["Moonstone Renewer", "Staff of Flowing Water", "Ardent Censer", "Redemption", "Mikael's Blessing"],
                "chemins": {
                    "Moonstone Renewer (2500g)": "Kindlegem → Amplifying Tome → Moonstone",
                    "Staff of Flowing Water (2300g)": "Forbidden Idol → Amplifying Tome → Staff",
                    "Ardent Censer (2300g)": "Forbidden Idol → Amplifying Tome → Ardent Censer",
                    "Redemption (2300g)": "Kindlegem → Crystalline Bracer → Redemption",
                },
            },
        },
    },

    # ══════════════════════════════════════════════════════════════════════════
    # ADC SUPPLÉMENTAIRES
    # ══════════════════════════════════════════════════════════════════════════

    "Ezreal": {
        "role": "ADC (Bot Lane)",
        "playstyle": "Poke ADC, kite, safe laner. Powerspike lent mais fort en late.",
        "summoner_spells": "Flash + Heal",
        "runes": {
            "primary_keystone": "Conqueror (Precision)",
            "precision": "Presence of Mind | Legend: Bloodline | Cut Down",
            "secondary_tree": "Sorcery",
            "secondary": "Manaflow Band | Transcendence",
        },
        "skill_order": "R > Q > W > E",
        "starting_items": "Doran's Blade + Health Potion",
        "build_paths": {
            "standard": {
                "ordre": ["Trinity Force", "Manamune", "Serylda's Grudge", "Rabadon's Deathcap", "Shadowflame", "Ionian Boots of Lucidity"],
                "chemins": {
                    "Trinity Force (3333g)": "Phage → Sheen → Stinger → Trinity Force — powerspike Q poke",
                    "Manamune (2900g)": "Tear of the Goddess (400g) — rush dès le départ → Manamune — scaling mana",
                    "Serylda's Grudge (3200g)": "Caulfield's → Pickaxe → Serylda's — slow sur Q",
                },
                "premier_retour": "Rush Tear of the Goddess (400g) immédiatement + Long Sword.",
            },
        },
        "tips": [
            "Mystic Shot (Q) : reset tous tes cooldowns si tu touche. Spam Q en permanence.",
            "Arcane Shift (E) : ton dash, garde-le pour esquiver les CC ou fuir.",
            "Joue safe early, scale sur 3 items. Ne prends pas de risques inutiles.",
        ],
    },

    "Ashe": {
        "role": "ADC (Bot Lane)",
        "playstyle": "Utility ADC, kite, CC global, vision avec W.",
        "summoner_spells": "Flash + Heal",
        "runes": {
            "primary_keystone": "Lethal Tempo (Precision)",
            "precision": "Presence of Mind | Legend: Bloodline | Cut Down",
            "secondary_tree": "Sorcery",
            "secondary": "Manaflow Band | Gathering Storm",
        },
        "skill_order": "R > W > Q > E",
        "starting_items": "Doran's Blade + Health Potion",
        "build_paths": {
            "standard": {
                "ordre": ["Kraken Slayer", "Runaan's Hurricane", "Infinity Edge", "Lord Dominik's Regards", "Mortal Reminder", "Bloodthirster"],
                "chemins": {
                    "Kraken Slayer (3200g)": "Long Sword → Pickaxe → Kraken Slayer",
                    "Runaan's Hurricane (2600g)": "Zeal → Runaan's — AoE slow avec passif Ashe",
                    "Infinity Edge (3400g)": "BF Sword → Pickaxe → Cloak → IE",
                },
            },
        },
        "tips": [
            "Volley (W) : spam en lane pour le poke et la vision des buissons.",
            "Enchanted Crystal Arrow (R) : CC global. Utilise cross-map pour sauver un allié ou initier.",
            "Ton passif slow permanent = kite naturel. Reste à distance et attaque en reculant.",
        ],
    },

    "Draven": {
        "role": "ADC (Bot Lane)",
        "playstyle": "Lane bully hyper agressif, snowball, one of the highest early damage ADC.",
        "summoner_spells": "Flash + Ignite",
        "runes": {
            "primary_keystone": "Lethal Tempo (Precision)",
            "precision": "Presence of Mind | Legend: Bloodline | Cut Down",
            "secondary_tree": "Domination",
            "secondary": "Taste of Blood | Treasure Hunter",
        },
        "skill_order": "R > Q > W > E",
        "starting_items": "Doran's Blade + Health Potion",
        "build_paths": {
            "standard": {
                "ordre": ["Kraken Slayer", "Infinity Edge", "Lord Dominik's Regards", "Phantom Dancer", "Bloodthirster", "Mortal Reminder"],
                "chemins": {
                    "Kraken Slayer (3200g)": "Long Sword → Pickaxe → Kraken Slayer",
                    "Infinity Edge (3400g)": "BF Sword → Pickaxe → Cloak → IE",
                },
            },
        },
        "tips": [
            "Spinning Axes (Q) : attrape tes haches pour les relancer. Mouvement constant pour les récupérer.",
            "Snowball violent — si tu n'es pas fed avant 15 min, tu perds ton avantage.",
            "Ignore les stacks League of Draven si tu risques de mourir pour les récupérer.",
        ],
    },

    "Samira": {
        "role": "ADC (Bot Lane)",
        "playstyle": "Assassin-ADC, all-in, style combo, R dévastateur en melee range.",
        "summoner_spells": "Flash + Ignite",
        "runes": {
            "primary_keystone": "Conqueror (Precision)",
            "precision": "Triumph | Legend: Bloodline | Last Stand",
            "secondary_tree": "Domination",
            "secondary": "Taste of Blood | Treasure Hunter",
        },
        "skill_order": "R > Q > E > W",
        "starting_items": "Doran's Blade + Health Potion",
        "build_paths": {
            "standard": {
                "ordre": ["Immortal Shieldbow", "Kraken Slayer", "Infinity Edge", "Phantom Dancer", "Lord Dominik's Regards", "Bloodthirster"],
                "chemins": {
                    "Immortal Shieldbow (3400g)": "Caulfield's → Pickaxe → Cloak → Shieldbow — survie en melee",
                    "Kraken Slayer (3200g)": "Long Sword → Pickaxe → Kraken Slayer",
                    "Infinity Edge (3400g)": "BF Sword → Pickaxe → Cloak → IE — attend 60% crit",
                },
            },
        },
        "tips": [
            "Buildup style grade S (passif) avant de lancer Inferno Trigger (R).",
            "Wild Rush (E) : dash sur un ennemi ou allié, réinitialise sur kill.",
            "Joue agressivement, engage avec support, R dans le tas.",
        ],
    },

    "Tristana": {
        "role": "ADC (Bot Lane)",
        "playstyle": "Hypercarry late, portée augmente avec les niveaux, reset sur kill.",
        "summoner_spells": "Flash + Heal",
        "runes": {
            "primary_keystone": "Lethal Tempo (Precision)",
            "precision": "Presence of Mind | Legend: Bloodline | Cut Down",
            "secondary_tree": "Domination",
            "secondary": "Taste of Blood | Treasure Hunter",
        },
        "skill_order": "R > E > Q > W",
        "starting_items": "Doran's Blade + Health Potion",
        "build_paths": {
            "standard": {
                "ordre": ["Kraken Slayer", "Runaan's Hurricane", "Infinity Edge", "Phantom Dancer", "Lord Dominik's Regards", "Bloodthirster"],
                "chemins": {
                    "Kraken Slayer (3200g)": "Long Sword → Pickaxe → Kraken Slayer",
                    "Runaan's Hurricane (2600g)": "Zeal → Runaan's",
                    "Infinity Edge (3400g)": "BF Sword → Pickaxe → Cloak → IE",
                },
            },
        },
        "tips": [
            "Rapid Fire (Q) : AS massif pendant 7s. Toujours actif avant un trade.",
            "Rocket Jump (W) : jump sur ennemi (engage) ou en arrière (fuite). Reset sur kill/assist.",
            "Buster Shot (R) : repousse l'ennemi, stacks les bombes sur tour pour la demolish.",
        ],
    },

    # ══════════════════════════════════════════════════════════════════════════
    # MID SUPPLÉMENTAIRES
    # ══════════════════════════════════════════════════════════════════════════

    "Akali": {
        "role": "Mid Lane / Top",
        "playstyle": "Assassin mobile, sustain en zone, burst très fort post-6.",
        "summoner_spells": "Flash + Ignite",
        "runes": {
            "primary_keystone": "Electrocute (Domination)",
            "domination": "Taste of Blood | Eyeball Collection | Treasure Hunter",
            "secondary_tree": "Sorcery",
            "secondary": "Celerity | Waterwalking",
        },
        "skill_order": "R > Q > E > W",
        "starting_items": "Doran's Shield + Health Potion (top) | Long Sword + potions (mid)",
        "build_paths": {
            "standard": {
                "ordre": ["Hextech Rocketbelt", "Shadowflame", "Rabadon's Deathcap", "Zhonya's Hourglass", "Void Staff", "Sorcerer's Shoes"],
                "chemins": {
                    "Hextech Rocketbelt (3200g)": "Hextech Alternator (1050g) → Hextech Rocketbelt — dash + burst",
                    "Shadowflame (3000g)": "Needlessly Large Rod → Shadowflame",
                    "Rabadon's Deathcap (3800g)": "Needlessly Large Rod → Rabadon's",
                    "Zhonya's Hourglass (2900g)": "Seeker's Armguard → Zhonya's — stase anti-assassin",
                    "Void Staff (2800g)": "Blighting Jewel → Void Staff",
                },
                "premier_retour": "Rush Hextech Alternator (1050g).",
            },
        },
        "tips": [
            "Shroud (W) : zone invisible, utilise pour reset trades ou fuir.",
            "Combo : Q → E → Q (mark) → R1 → auto → R2 pour le burst complet.",
            "Powerspike fort au R lvl 6 — cherche le kill dès que tu l'as.",
        ],
    },

    "Viktor": {
        "role": "Mid Lane",
        "playstyle": "Mage scaling, zone control, upgrades progressifs, fort en late teamfight.",
        "summoner_spells": "Flash + Ignite",
        "runes": {
            "primary_keystone": "Arcane Comet (Sorcery)",
            "sorcery": "Manaflow Band | Transcendence | Scorch",
            "secondary_tree": "Precision",
            "secondary": "Presence of Mind | Cut Down",
        },
        "skill_order": "R > E > Q > W",
        "starting_items": "Doran's Ring + Health Potion x2",
        "build_paths": {
            "standard": {
                "ordre": ["Luden's Tempest", "Shadowflame", "Rabadon's Deathcap", "Void Staff", "Zhonya's Hourglass", "Sorcerer's Shoes"],
                "chemins": {
                    "Luden's Tempest (3200g)": "Lost Chapter → Amplifying Tome → Luden's",
                    "Shadowflame (3000g)": "Needlessly Large Rod → Shadowflame",
                    "Rabadon's Deathcap (3800g)": "Needlessly Large Rod → Rabadon's",
                    "Void Staff (2800g)": "Blighting Jewel → Void Staff — si MR ennemi",
                },
            },
        },
        "tips": [
            "Rush les upgrades de Viktor : Q → W → E dans l'ordre de priorité.",
            "Death Ray (E) : zone de dégâts + explosion après. Colle-le sur les groupes ennemis.",
            "Chaos Storm (R) : suit les ennemis, repositionne-le sur le carry adverse.",
        ],
    },

    "Katarina": {
        "role": "Mid Lane",
        "playstyle": "Assassin reset, snowball violent, AoE sur groupes, haut skill cap.",
        "summoner_spells": "Flash + Ignite",
        "runes": {
            "primary_keystone": "Conqueror (Precision)",
            "precision": "Triumph | Legend: Tenacity | Last Stand",
            "secondary_tree": "Domination",
            "secondary": "Sudden Impact | Treasure Hunter",
        },
        "skill_order": "R > Q > E > W",
        "starting_items": "Long Sword + Health Potion x3",
        "build_paths": {
            "standard": {
                "ordre": ["Hextech Rocketbelt", "Shadowflame", "Rabadon's Deathcap", "Zhonya's Hourglass", "Void Staff", "Sorcerer's Shoes"],
                "chemins": {
                    "Hextech Rocketbelt (3200g)": "Hextech Alternator → Rocketbelt — dash + burst",
                    "Shadowflame (3000g)": "Needlessly Large Rod → Shadowflame",
                    "Rabadon's Deathcap (3800g)": "Needlessly Large Rod → Rabadon's",
                    "Zhonya's Hourglass (2900g)": "Seeker's Armguard → Zhonya's — stase pendant R",
                },
            },
        },
        "tips": [
            "Passif : chaque kill/assist reset Shunpo (E). Enchaîne les resets en teamfight.",
            "Daggers sur le sol = dégâts bonus si tu les ramasses ou Shunpo dessus.",
            "Contre les CC : Zhonya's pendant R pour éviter le one-shot.",
        ],
    },

    "Kassadin": {
        "role": "Mid Lane",
        "playstyle": "Late game hyper carry, très faible early, invincible à partir du lvl 11-16.",
        "summoner_spells": "Flash + Ignite (ou Teleport pour safer)",
        "runes": {
            "primary_keystone": "Fleet Footwork (Precision)",
            "precision": "Presence of Mind | Legend: Tenacity | Last Stand",
            "secondary_tree": "Sorcery",
            "secondary": "Manaflow Band | Transcendence",
        },
        "skill_order": "R > Q > E > W",
        "starting_items": "Doran's Shield + Health Potion (safe) ou Doran's Ring",
        "build_paths": {
            "standard": {
                "ordre": ["Rod of Ages", "Seraph's Embrace", "Rabadon's Deathcap", "Zhonya's Hourglass", "Void Staff", "Sorcerer's Shoes"],
                "chemins": {
                    "Rod of Ages (2600g)": "Catalyst of Aeons (1100g) → Rod of Ages — rush, scale sur 10 min",
                    "Seraph's Embrace (2600g)": "Tear of the Goddess (400g) — rush aussi → Seraph's — mana infini",
                    "Rabadon's Deathcap (3800g)": "Needlessly Large Rod → Rabadon's",
                    "Zhonya's Hourglass (2900g)": "Seeker's Armguard → Zhonya's",
                    "Void Staff (2800g)": "Blighting Jewel → Void Staff",
                },
                "note": "Survive early (Fleet Footwork), scale lvl 11-16. Ne cherche pas à gagner avant.",
            },
        },
        "tips": [
            "Riftwalk (R) : cd très court, dash + dégâts. Spam en teamfight.",
            "Void Stone (P) : réduit les dégâts magiques de 15%. Bon vs mages.",
            "Joue ultra safe jusqu'au lvl 6. Rush Rod of Ages + Tear en priorité.",
        ],
    },

    "Ekko": {
        "role": "Mid Lane / Jungle",
        "playstyle": "Assassin-mage, mobilité, reset avec R, snowball solide.",
        "summoner_spells": "Flash + Ignite",
        "runes": {
            "primary_keystone": "Electrocute (Domination)",
            "domination": "Taste of Blood | Eyeball Collection | Treasure Hunter",
            "secondary_tree": "Sorcery",
            "secondary": "Manaflow Band | Transcendence",
        },
        "skill_order": "R > Q > W > E",
        "starting_items": "Doran's Ring + Health Potion x2",
        "build_paths": {
            "standard": {
                "ordre": ["Hextech Rocketbelt", "Lich Bane", "Shadowflame", "Rabadon's Deathcap", "Zhonya's Hourglass", "Sorcerer's Shoes"],
                "chemins": {
                    "Hextech Rocketbelt (3200g)": "Hextech Alternator → Rocketbelt",
                    "Lich Bane (3000g)": "Sheen (700g) → Amplifying Tome → Lich Bane — empowered AA après sort",
                    "Shadowflame (3000g)": "Needlessly Large Rod → Shadowflame",
                    "Rabadon's Deathcap (3800g)": "Needlessly Large Rod → Rabadon's",
                },
            },
        },
        "tips": [
            "Chronobreak (R) : revient en arrière, heal, burst. Utilise si tu es en danger ou pour finir.",
            "Timewinder (Q) : retour du boomerang = stun si 3 stacks passif sur ennemi.",
            "Parallel Convergence (W) : bouclier + stun si ennemi dedans. Engage dessus avec E.",
        ],
    },

    # ══════════════════════════════════════════════════════════════════════════
    # TOP SUPPLÉMENTAIRES
    # ══════════════════════════════════════════════════════════════════════════

    "Aatrox": {
        "role": "Top Lane / Mid Lane",
        "playstyle": "Juggernaut sustain, revivre passif, poke avec Q, dominant en prolonged trades.",
        "summoner_spells": "Flash + Ignite (ou Teleport)",
        "runes": {
            "primary_keystone": "Conqueror (Precision)",
            "precision": "Triumph | Legend: Tenacity | Last Stand",
            "secondary_tree": "Resolve",
            "secondary": "Bone Plating | Overgrowth",
        },
        "skill_order": "R > Q > W > E",
        "starting_items": "Doran's Shield + Health Potion",
        "build_paths": {
            "standard": {
                "ordre": ["Trinity Force", "Sterak's Gage", "Death's Dance", "Thornmail", "Force of Nature", "Guardian Angel"],
                "chemins": {
                    "Trinity Force (3333g)": "Phage → Sheen → Stinger → Trinity Force",
                    "Sterak's Gage (3100g)": "Kindlegem → Giant's Belt → Sterak's",
                    "Death's Dance (3300g)": "Caulfield's → Chain Vest → Death's Dance — heal sur dégâts",
                    "Thornmail (2700g)": "Chain Vest → Bami's Cinder → Thornmail — si beaucoup de heal ennemi",
                },
            },
        },
        "tips": [
            "Vise les bords extérieurs de Darkin Blade (Q) pour le maximum de dégâts.",
            "World Ender (R) : revive passif + heal massif. Active avant d'engager une fight.",
            "Infernal Chains (W) : slow + pull si ennemi reste dedans. Utilise pour Q ou E combo.",
        ],
    },

    "Fiora": {
        "role": "Top Lane",
        "playstyle": "Duelist 1v1 imbattable, splitpush, execute les tanks via Vitals.",
        "summoner_spells": "Flash + Ignite (ou Teleport)",
        "runes": {
            "primary_keystone": "Conqueror (Precision)",
            "precision": "Triumph | Legend: Alacrity | Last Stand",
            "secondary_tree": "Resolve",
            "secondary": "Bone Plating | Overgrowth",
        },
        "skill_order": "R > Q > W > E",
        "starting_items": "Doran's Blade + Health Potion",
        "build_paths": {
            "standard": {
                "ordre": ["Trinity Force", "Ravenous Hydra", "Death's Dance", "Guardian Angel", "Sterak's Gage", "Wit's End"],
                "chemins": {
                    "Trinity Force (3333g)": "Phage → Sheen → Stinger → Trinity Force",
                    "Ravenous Hydra (3300g)": "Tiamat (1325g) → Pickaxe → Ravenous Hydra — sustain + waveclear",
                    "Death's Dance (3300g)": "Caulfield's → Chain Vest → Death's Dance",
                    "Guardian Angel (3200g)": "Cloth Armor → Pickaxe → Guardian Angel",
                },
            },
        },
        "tips": [
            "Vitals (passif) : toucher les 4 Vitals avec Grand Challenge (R) = heal massif zonal.",
            "Riposte (W) : parry un CC — crucial contre les all-in. Pratique le timing.",
            "Lunge (Q) : 2 charges, reset sur hit de Vital. Combo Q → touche Vital → Q de retour.",
        ],
    },

    "Camille": {
        "role": "Top Lane / Jungle",
        "playstyle": "Duelist mobile, lock-down R, splitpush dangereux.",
        "summoner_spells": "Flash + Teleport (ou Ignite)",
        "runes": {
            "primary_keystone": "Conqueror (Precision)",
            "precision": "Triumph | Legend: Alacrity | Last Stand",
            "secondary_tree": "Resolve",
            "secondary": "Bone Plating | Overgrowth",
        },
        "skill_order": "R > Q > W > E",
        "starting_items": "Doran's Shield + Health Potion",
        "build_paths": {
            "standard": {
                "ordre": ["Trinity Force", "Sterak's Gage", "Death's Dance", "Guardian Angel", "Thornmail", "Force of Nature"],
                "chemins": {
                    "Trinity Force (3333g)": "Phage → Sheen → Stinger → Trinity Force — powerspike majeur",
                    "Sterak's Gage (3100g)": "Kindlegem → Giant's Belt → Sterak's",
                    "Death's Dance (3300g)": "Caulfield's → Chain Vest → Death's Dance",
                },
            },
        },
        "tips": [
            "Hookshot (E) : wall-hook + dash sur ennemi. Engage ou fuite.",
            "Hextech Ultimatum (R) : emprisonne un ennemi 1v1. Utilise sur le carry isolé.",
            "Precision Protocol (Q) : empowered AA avec slow. Double Q si tu attends 1.5s.",
        ],
    },

    "Irelia": {
        "role": "Top Lane / Mid Lane",
        "playstyle": "Duelist reset sur minions, fort post-4-5 stacks passif.",
        "summoner_spells": "Flash + Teleport (ou Ignite)",
        "runes": {
            "primary_keystone": "Conqueror (Precision)",
            "precision": "Triumph | Legend: Alacrity | Last Stand",
            "secondary_tree": "Resolve",
            "secondary": "Bone Plating | Overgrowth",
        },
        "skill_order": "R > Q > E > W",
        "starting_items": "Doran's Shield + Health Potion",
        "build_paths": {
            "standard": {
                "ordre": ["Trinity Force", "Sterak's Gage", "Death's Dance", "Guardian Angel", "Wit's End", "Thornmail"],
                "chemins": {
                    "Trinity Force (3333g)": "Phage → Sheen → Stinger → Trinity Force",
                    "Sterak's Gage (3100g)": "Kindlegem → Giant's Belt → Sterak's",
                    "Death's Dance (3300g)": "Caulfield's → Chain Vest → Death's Dance",
                    "Wit's End (2900g)": "Negatron Cloak → Recurve Bow → Wit's End — si beaucoup d'AP",
                },
            },
        },
        "tips": [
            "Bladesurge (Q) : reset sur kill de minion/champion. Manage tes minions pour entrer en range.",
            "Stack ton passif (Ionian Fervor) à 5 avant d'engager le carry adverse.",
            "Flawless Duet (E) : CC AoE entre 2 lames. Place les 2 lames de chaque côté de l'ennemi.",
        ],
    },

    "Mordekaiser": {
        "role": "Top Lane / Mid Lane",
        "playstyle": "Tank-mage, 1v1 en Death Realm, résistant, AoE dégâts.",
        "summoner_spells": "Flash + Ignite (ou Teleport)",
        "runes": {
            "primary_keystone": "Conqueror (Precision)",
            "precision": "Triumph | Legend: Tenacity | Last Stand",
            "secondary_tree": "Resolve",
            "secondary": "Bone Plating | Overgrowth",
        },
        "skill_order": "R > Q > W > E",
        "starting_items": "Doran's Shield + Health Potion",
        "build_paths": {
            "standard": {
                "ordre": ["Riftmaker", "Rylai's Crystal Scepter", "Demonic Embrace", "Shadowflame", "Void Staff", "Sorcerer's Shoes"],
                "chemins": {
                    "Riftmaker (3200g)": "Hextech Alternator → Kindlegem → Riftmaker — true damage passif",
                    "Rylai's Crystal Scepter (2600g)": "Hextech Alternator → Giant's Belt → Rylai's — slow permanent",
                    "Demonic Embrace (3000g)": "Blighting Jewel → Giant's Belt → Demonic — burn + survie",
                    "Shadowflame (3000g)": "Needlessly Large Rod → Shadowflame",
                    "Void Staff (2800g)": "Blighting Jewel → Void Staff",
                },
            },
        },
        "tips": [
            "Realm of Death (R) : emmène l'ennemi en 1v1. Tu voles ses stats — engage sur le carry.",
            "En Death Realm, focus stats volées. Si tu peux pas kill, au moins fais-le perdre du temps.",
            "Indestructible (W) : absorbe dégâts en bouclier. Actif APRÈS avoir pris des dégâts.",
        ],
    },

    "Nasus": {
        "role": "Top Lane",
        "playstyle": "Scaling hyper carry, farm les stacks, invincible en late game.",
        "summoner_spells": "Flash + Teleport",
        "runes": {
            "primary_keystone": "Conqueror (Precision)",
            "precision": "Triumph | Legend: Tenacity | Last Stand",
            "secondary_tree": "Resolve",
            "secondary": "Bone Plating | Overgrowth",
        },
        "skill_order": "R > W > E > Q (farm Q UNIQUEMENT)",
        "starting_items": "Doran's Shield + Health Potion",
        "build_paths": {
            "standard": {
                "ordre": ["Trinity Force", "Sterak's Gage", "Warmog's Armor", "Thornmail", "Force of Nature", "Hullbreaker"],
                "chemins": {
                    "Trinity Force (3333g)": "Phage → Sheen → Stinger → Trinity Force — Sheen = Q one-shot",
                    "Sterak's Gage (3100g)": "Kindlegem → Giant's Belt → Sterak's",
                    "Warmog's Armor (3000g)": "Giant's Belt → Warmog's — regen passive",
                    "Hullbreaker (3000g)": "Long Sword → Pickaxe → Hullbreaker — splitpush inaccessible",
                },
            },
        },
        "tips": [
            "Farm Q sur tout — minions, jungle, objectives. Objectif : 300+ stacks avant 20 min.",
            "Wither (W) : slow AS et MS massif — colle l'ADC avec ça.",
            "Joue ultra safe early pour farmer. Splitpush en side lane à partir du lvl 11.",
        ],
    },

    "Sett": {
        "role": "Top Lane / Support / Jungle",
        "playstyle": "Juggernaut tank, tanky fighter, W one-shot avec true damage.",
        "summoner_spells": "Flash + Ignite (ou Teleport)",
        "runes": {
            "primary_keystone": "Conqueror (Precision)",
            "precision": "Triumph | Legend: Tenacity | Last Stand",
            "secondary_tree": "Resolve",
            "secondary": "Bone Plating | Overgrowth",
        },
        "skill_order": "R > W > Q > E",
        "starting_items": "Doran's Shield + Health Potion",
        "build_paths": {
            "standard": {
                "ordre": ["Trinity Force", "Sterak's Gage", "Death's Dance", "Thornmail", "Force of Nature", "Guardian Angel"],
                "chemins": {
                    "Trinity Force (3333g)": "Phage → Sheen → Stinger → Trinity Force",
                    "Sterak's Gage (3100g)": "Kindlegem → Giant's Belt → Sterak's",
                    "Death's Dance (3300g)": "Caulfield's → Chain Vest → Death's Dance",
                },
            },
        },
        "tips": [
            "The Show Stopper (R) : grab + smash. Lance un ennemi dans ses propres alliés.",
            "Haymaker (W) : accumule grit (dégâts reçus), release = true damage + bouclier.",
            "Stack le grit en prenant des dégâts, puis W pour le burst en true damage.",
        ],
    },

    "Tryndamere": {
        "role": "Top Lane / Jungle",
        "playstyle": "Splitpush inaccessible, invincible avec R, hypercarry crit.",
        "summoner_spells": "Flash + Ignite (ou Ghost + Ignite)",
        "runes": {
            "primary_keystone": "Conqueror (Precision)",
            "precision": "Triumph | Legend: Alacrity | Last Stand",
            "secondary_tree": "Resolve",
            "secondary": "Bone Plating | Unflinching",
        },
        "skill_order": "R > E > Q > W",
        "starting_items": "Doran's Blade + Health Potion",
        "build_paths": {
            "standard": {
                "ordre": ["Kraken Slayer", "Phantom Dancer", "Infinity Edge", "Mortal Reminder", "Guardian Angel", "Death's Dance"],
                "chemins": {
                    "Kraken Slayer (3200g)": "Long Sword → Pickaxe → Kraken Slayer",
                    "Phantom Dancer (2600g)": "Zeal → Phantom Dancer — bouclier + AS",
                    "Infinity Edge (3400g)": "BF Sword → Pickaxe → Cloak → IE — attend 60% crit",
                },
            },
        },
        "tips": [
            "Undying Rage (R) : invincible 5s. Active sous 1 HP pour survivre et tuer.",
            "Splitpush en side lane — tu coupes les tours inaccessible 1v1.",
            "Spinning Slash (E) : dash sur l'ennemi ou fuite. Reset CD si tu kills.",
        ],
    },

    "Volibear": {
        "role": "Top Lane / Jungle",
        "playstyle": "Tank-fighter engage, jump avec R sur une tourelle, fort en teamfight.",
        "summoner_spells": "Flash + Teleport (ou Ignite)",
        "runes": {
            "primary_keystone": "Grasp of the Undying (Resolve)",
            "resolve": "Demolish | Bone Plating | Overgrowth",
            "secondary_tree": "Precision",
            "secondary": "Legend: Tenacity | Last Stand",
        },
        "skill_order": "R > Q > W > E",
        "starting_items": "Doran's Shield + Health Potion",
        "build_paths": {
            "standard": {
                "ordre": ["Heartsteel", "Sunfire Aegis", "Warmog's Armor", "Thornmail", "Force of Nature", "Sterak's Gage"],
                "chemins": {
                    "Heartsteel (2800g)": "Crystalline Bracer → Giant's Belt → Heartsteel — HP massif",
                    "Sunfire Aegis (3200g)": "Bami's Cinder → Chain Vest → Sunfire",
                    "Warmog's Armor (3000g)": "Giant's Belt → Warmog's",
                    "Thornmail (2700g)": "Chain Vest → Bami's → Thornmail",
                },
            },
        },
        "tips": [
            "The Relentless Storm (R) : jump qui désactive les tourelles. Engage sous tour en sécurité.",
            "Sky Splitter (E) : cage lightning — CC + bouclier si tu es dans la zone.",
            "Thundering Smash (Q) : charge + stun si l'ennemi est slow. Combo Q → W (bite).",
        ],
    },

    # ══════════════════════════════════════════════════════════════════════════
    # JUNGLE SUPPLÉMENTAIRES
    # ══════════════════════════════════════════════════════════════════════════

    "Kayn": {
        "role": "Jungle",
        "playstyle": "Deux formes : Rhaast (tank) ou Shadow Assassin (assassin). S'adapte à l'ennemi.",
        "summoner_spells": "Flash + Smite",
        "runes": {
            "primary_keystone": "Conqueror (Precision) — Rhaast | Electrocute (Domination) — SA",
            "precision": "Triumph | Legend: Tenacity | Last Stand (Rhaast)",
            "domination": "Sudden Impact | Eyeball Collection | Treasure Hunter (SA)",
            "secondary_tree": "Sorcery",
            "secondary": "Celerity | Waterwalking",
        },
        "skill_order": "R > Q > E > W",
        "starting_items": "Mosstomper Seedling (jungle item) + Health Potion",
        "build_paths": {
            "Rhaast (tank, vs full AD/tanky)": {
                "ordre": ["Goredrinker", "Sterak's Gage", "Death's Dance", "Thornmail", "Force of Nature", "Guardian Angel"],
                "chemins": {
                    "Goredrinker (3300g)": "Caulfield's → Kindlegem → Goredrinker — AoE heal",
                    "Sterak's Gage (3100g)": "Kindlegem → Giant's Belt → Sterak's",
                    "Death's Dance (3300g)": "Caulfield's → Chain Vest → Death's Dance",
                },
                "note": "Rhaast : farm les champions AD/tanky en lane pour transformer plus vite.",
            },
            "Shadow Assassin (vs squishy/AP)": {
                "ordre": ["The Collector", "Serpent's Fang", "Edge of Night", "Serylda's Grudge", "Lord Dominik's Regards", "Guardian Angel"],
                "chemins": {
                    "The Collector (3000g)": "Serrated Dirk → Pickaxe → The Collector",
                    "Serpent's Fang (2600g)": "Serrated Dirk → Long Sword → Serpent's Fang — anti-boucliers",
                    "Edge of Night (2900g)": "Serrated Dirk → Long Sword → Edge of Night",
                },
                "note": "SA : farm les mages/assassins pour transformer. Playstyle one-shot.",
            },
        },
        "tips": [
            "Farm les bons champions pour orienter ta transformation (AD → Rhaast, AP → SA).",
            "Umbral Trespass (R) : entre dans un ennemi, heal si Rhaast, burst si SA.",
            "Darkin Scythe (Q) : passe à travers les murs. Mobility jungle extrême.",
        ],
    },

    "Kha'Zix": {
        "role": "Jungle",
        "playstyle": "Assassin isolate, one-shot les cibles seules, évolue ses sorts.",
        "summoner_spells": "Flash + Smite",
        "runes": {
            "primary_keystone": "Electrocute (Domination)",
            "domination": "Sudden Impact | Eyeball Collection | Treasure Hunter",
            "secondary_tree": "Precision",
            "secondary": "Triumph | Legend: Tenacity",
        },
        "skill_order": "R > Q > W > E",
        "starting_items": "Mosstomper Seedling (jungle item) + Health Potion",
        "build_paths": {
            "standard": {
                "ordre": ["The Collector", "Serpent's Fang", "Edge of Night", "Serylda's Grudge", "Lord Dominik's Regards", "Guardian Angel"],
                "chemins": {
                    "The Collector (3000g)": "Serrated Dirk → Pickaxe → The Collector — exécute sous 5%",
                    "Serpent's Fang (2600g)": "Serrated Dirk → Long Sword → Serpent's — anti-boucliers",
                    "Edge of Night (2900g)": "Serrated Dirk → Long Sword → Edge of Night — spell shield",
                },
                "evolution": "1er évolution : Q (Taste Their Fear) — dégâts isolate x2. 2e : E (Leap) — reset sur kill. 3e : W (Void Spike) — heal massif.",
            },
        },
        "tips": [
            "Isolate : cible toujours un ennemi SEUL (passif). Dégâts doublés.",
            "Evolved Q = one-shot quasi garanti sur une cible isolée.",
            "Void Assault (R) : invisibilité 3 charges. Utilise pour entrer/sortir d'un fight.",
        ],
    },

    "Hecarim": {
        "role": "Jungle",
        "playstyle": "Engage rapide, MS = dégâts, tank-fighter, fort ganks lvl 3.",
        "summoner_spells": "Flash (ou Ghost) + Smite",
        "runes": {
            "primary_keystone": "Phase Rush (Sorcery)",
            "sorcery": "Nimbus Cloak | Celerity | Waterwalking",
            "secondary_tree": "Resolve",
            "secondary": "Bone Plating | Overgrowth",
        },
        "skill_order": "R > Q > W > E",
        "starting_items": "Gustwalker Hatchling (jungle item) + Health Potion",
        "build_paths": {
            "standard": {
                "ordre": ["Trinity Force", "Sterak's Gage", "Dead Man's Plate", "Force of Nature", "Warmog's Armor", "Guardian Angel"],
                "chemins": {
                    "Trinity Force (3333g)": "Phage → Sheen → Stinger → Trinity Force — MS + dégâts passif",
                    "Sterak's Gage (3100g)": "Kindlegem → Giant's Belt → Sterak's",
                    "Dead Man's Plate (2900g)": "Chain Vest → Giant's Belt → Dead Man's — MS + engage",
                    "Force of Nature (2900g)": "Negatron Cloak → Force of Nature — si AP lourde",
                },
            },
        },
        "tips": [
            "Rampage (Q) : AoE rapide, stack = encore plus rapide. Farm rapide.",
            "Devastating Charge (E) : accélération + knockback. Lance tes ganks avec E → R.",
            "Onslaught of Shadows (R) : engage AoE fear. Vise le groupe ennemi.",
        ],
    },

    "Graves": {
        "role": "Jungle",
        "playstyle": "Fighter jungler, DPS burst, safe avec dash, fort duel.",
        "summoner_spells": "Flash + Smite",
        "runes": {
            "primary_keystone": "Conqueror (Precision)",
            "precision": "Triumph | Legend: Alacrity | Last Stand",
            "secondary_tree": "Resolve",
            "secondary": "Bone Plating | Overgrowth",
        },
        "skill_order": "R > Q > E > W",
        "starting_items": "Mosstomper Seedling (jungle item) + Health Potion",
        "build_paths": {
            "standard": {
                "ordre": ["Trinity Force", "Sterak's Gage", "Death's Dance", "Guardian Angel", "Lord Dominik's Regards", "Serylda's Grudge"],
                "chemins": {
                    "Trinity Force (3333g)": "Phage → Sheen → Stinger → Trinity Force",
                    "Sterak's Gage (3100g)": "Kindlegem → Giant's Belt → Sterak's",
                    "Death's Dance (3300g)": "Caulfield's → Chain Vest → Death's Dance",
                },
            },
        },
        "tips": [
            "Smoke Screen (W) : zone aveugle + slow. Pose dans les pieds de l'ennemi en fight.",
            "Quickdraw (E) : dash qui recharge 1 cartouche. Kite et dash intelligemment.",
            "Graves ne peut tirer qu'avec 2 cartouches — recharge entre chaque burst.",
        ],
    },

    # ══════════════════════════════════════════════════════════════════════════
    # SUPPORT SUPPLÉMENTAIRES
    # ══════════════════════════════════════════════════════════════════════════

    "Leona": {
        "role": "Support",
        "playstyle": "Tank engage, CC chain massive, frontline inaccessible.",
        "summoner_spells": "Flash + Ignite",
        "runes": {
            "primary_keystone": "Aftershock (Resolve)",
            "resolve": "Font of Life | Bone Plating | Overgrowth",
            "secondary_tree": "Inspiration",
            "secondary": "Biscuit Delivery | Cosmic Insight",
        },
        "skill_order": "R > E > W > Q",
        "starting_items": "Spellthief's Edge + Health Potion x2",
        "build_paths": {
            "standard": {
                "ordre": ["Locket of the Iron Solari", "Zeke's Convergence", "Warmog's Armor", "Thornmail", "Force of Nature", "Knight's Vow"],
                "chemins": {
                    "Locket of the Iron Solari (2500g)": "Kindlegem → Crystalline Bracer → Locket",
                    "Zeke's Convergence (2400g)": "Kindlegem → Null-Magic Mantle → Zeke's",
                    "Warmog's Armor (3000g)": "Giant's Belt → Warmog's",
                },
            },
        },
        "tips": [
            "Combo engage : E (Zenith Blade) → W (Shield of Daybreak) pour le stun immédiat.",
            "Solar Flare (R) : AoE CC. Vise sur le carry ennemi ou dans le groupe.",
            "Tank tout — ton rôle est de prendre les dégâts et CC le maximum.",
        ],
    },

    "Nautilus": {
        "role": "Support / Jungle",
        "playstyle": "Engage tank, hook (Q), CC chain énorme, frontline.",
        "summoner_spells": "Flash + Ignite (ou Exhaust)",
        "runes": {
            "primary_keystone": "Aftershock (Resolve)",
            "resolve": "Font of Life | Bone Plating | Overgrowth",
            "secondary_tree": "Inspiration",
            "secondary": "Biscuit Delivery | Cosmic Insight",
        },
        "skill_order": "R > W > E > Q",
        "starting_items": "Spellthief's Edge + Health Potion x2",
        "build_paths": {
            "standard": {
                "ordre": ["Locket of the Iron Solari", "Zeke's Convergence", "Warmog's Armor", "Thornmail", "Force of Nature", "Redemption"],
                "chemins": {
                    "Locket of the Iron Solari (2500g)": "Kindlegem → Crystalline Bracer → Locket",
                    "Zeke's Convergence (2400g)": "Kindlegem → Null-Magic Mantle → Zeke's",
                    "Warmog's Armor (3000g)": "Giant's Belt → Warmog's",
                    "Thornmail (2700g)": "Chain Vest → Bami's → Thornmail — si heal ennemi",
                },
            },
        },
        "tips": [
            "Dredge Line (Q) : hook sur ennemi ou terrain. Pratique le hook à travers les murs.",
            "Depth Charge (R) : CC global qui suit l'ennemi. Utilise sur le carry ennemi.",
            "Passif : première auto sur chaque ennemi = root. Colle-les et auto d'abord.",
        ],
    },

    "Morgana": {
        "role": "Support / Mid Lane",
        "playstyle": "CC long (Q), bouclier anti-CC (E), utility tank.",
        "summoner_spells": "Flash + Exhaust (support) | Flash + Ignite (mid)",
        "runes": {
            "primary_keystone": "Arcane Comet (Sorcery)",
            "sorcery": "Manaflow Band | Transcendence | Scorch",
            "secondary_tree": "Resolve",
            "secondary": "Font of Life | Revitalize",
        },
        "skill_order": "R > W > Q > E",
        "starting_items": "Spellthief's Edge + Health Potion x2",
        "build_paths": {
            "support": {
                "ordre": ["Locket of the Iron Solari", "Redemption", "Zhonya's Hourglass", "Mikael's Blessing", "Ardent Censer", "Knight's Vow"],
                "chemins": {
                    "Locket of the Iron Solari (2500g)": "Kindlegem → Crystalline Bracer → Locket",
                    "Redemption (2300g)": "Kindlegem → Crystalline Bracer → Redemption",
                    "Zhonya's Hourglass (2900g)": "Seeker's Armguard → Zhonya's — stase pendant R",
                },
            },
        },
        "tips": [
            "Dark Binding (Q) : root 3s le plus long du jeu. Visée critique à maîtriser.",
            "Black Shield (E) : bouclier anti-CC sur allié. Timing crucial contre engage.",
            "Soul Shackles (R) : AoE CC chain. Reste dans le groupe — Zhonya's pour survivre.",
        ],
    },

    "Soraka": {
        "role": "Support",
        "playstyle": "Heal bot, sustain extrême, Silence (E), ult global (R).",
        "summoner_spells": "Flash + Exhaust (ou Ignite si agressif)",
        "runes": {
            "primary_keystone": "Summon Aery (Sorcery)",
            "sorcery": "Manaflow Band | Transcendence | Scorch",
            "secondary_tree": "Resolve",
            "secondary": "Font of Life | Revitalize",
        },
        "skill_order": "R > Q > E > W",
        "starting_items": "Spellthief's Edge + Health Potion x2",
        "build_paths": {
            "standard": {
                "ordre": ["Moonstone Renewer", "Staff of Flowing Water", "Ardent Censer", "Redemption", "Mikael's Blessing", "Chemtech Putrifier"],
                "chemins": {
                    "Moonstone Renewer (2500g)": "Kindlegem → Amplifying Tome → Moonstone",
                    "Staff of Flowing Water (2300g)": "Forbidden Idol → Amplifying Tome → Staff",
                    "Ardent Censer (2300g)": "Forbidden Idol → Amplifying Tome → Ardent",
                    "Chemtech Putrifier (2300g)": "Forbidden Idol → Amplifying Tome → Chemtech — Grievous Wounds sur heal",
                },
                "note": "Prends Chemtech Putrifier si l'ennemi a beaucoup de heal.",
            },
        },
        "tips": [
            "Astral Infusion (W) : coûte 10% HP max. Heal sans limite si tu restes en vie.",
            "Wish (R) : heal global. Utilise dès qu'un allié est en danger partout sur la map.",
            "Equinox (E) : Silence AoE + zone. Utilise pour stopper les engages ou les recalls.",
        ],
    },

    "Nami": {
        "role": "Support",
        "playstyle": "Enchanteur engage/peel, heal, buff AA alliés, fort CC avec Q.",
        "summoner_spells": "Flash + Exhaust",
        "runes": {
            "primary_keystone": "Summon Aery (Sorcery)",
            "sorcery": "Manaflow Band | Transcendence | Scorch",
            "secondary_tree": "Resolve",
            "secondary": "Font of Life | Revitalize",
        },
        "skill_order": "R > W > Q > E",
        "starting_items": "Spellthief's Edge + Health Potion x2",
        "build_paths": {
            "standard": {
                "ordre": ["Moonstone Renewer", "Staff of Flowing Water", "Ardent Censer", "Redemption", "Mikael's Blessing", "Shurelya's Battlesong"],
                "chemins": {
                    "Moonstone Renewer (2500g)": "Kindlegem → Amplifying Tome → Moonstone",
                    "Staff of Flowing Water (2300g)": "Forbidden Idol → Amplifying Tome → Staff",
                    "Ardent Censer (2300g)": "Forbidden Idol → Amplifying Tome → Ardent",
                },
            },
        },
        "tips": [
            "Aqua Prison (Q) : bubble qui stun. Vise au sol, difficile à toucher — entraîne-toi.",
            "Tidecaller's Blessing (E) : buff AA allié avec slow + dégâts. Pose sur l'ADC en fight.",
            "Tidal Wave (R) : slow AoE global. Utilise pour engage depuis loin ou disengage.",
        ],
    },

    "Pyke": {
        "role": "Support / Mid Lane",
        "playstyle": "Assassin support, hook, execute avec R (or pour toute l'équipe), roam.",
        "summoner_spells": "Flash + Ignite",
        "runes": {
            "primary_keystone": "Electrocute (Domination)",
            "domination": "Sudden Impact | Eyeball Collection | Treasure Hunter",
            "secondary_tree": "Precision",
            "secondary": "Presence of Mind | Legend: Tenacity",
        },
        "skill_order": "R > Q > E > W",
        "starting_items": "Spellthief's Edge + Health Potion x2",
        "build_paths": {
            "standard": {
                "ordre": ["Umbral Glaive", "Serrated Dirk", "Edge of Night", "Serpent's Fang", "Axiom Arc", "Sorcerer's Shoes"],
                "chemins": {
                    "Umbral Glaive (2300g)": "Serrated Dirk → Long Sword → Umbral Glaive — ward clearer",
                    "Edge of Night (2900g)": "Serrated Dirk → Long Sword → Edge of Night — spell shield",
                    "Axiom Arc (3000g)": "Caulfield's → Serrated Dirk → Axiom Arc — réduit CD ultime sur kill",
                },
            },
        },
        "tips": [
            "Death from Below (R) : exécute sous le seuil HP. L'allié qui assist reçoit aussi l'or.",
            "Bone Skewer (Q) : hold = lancer, tap = pull. Pull en buisson pour l'engage.",
            "Regen rapide hors combat — reste à la frontline pour tanker puis regen.",
        ],
    },
}


def builds_to_chunks() -> list[tuple[str, str]]:
    """Convertit BUILDS en (id, texte) pour ChromaDB."""
    result = []
    for champ, data in BUILDS.items():
        slug = champ.lower().replace(" ", "_").replace("'", "")

        # Chunk principal : résumé du champion
        main = [
            f"BUILD COMPLET — {champ} ({data['role']}) :",
            f"Playstyle : {data['playstyle']}",
            f"Summoner Spells : {data['summoner_spells']}",
            f"Runes keystone : {data['runes'].get('primary_keystone', '?')}",
        ]
        prec = data['runes'].get('precision') or data['runes'].get('domination') or data['runes'].get('resolve') or data['runes'].get('sorcery', '')
        if prec:
            main.append(f"Runes lignes : {prec}")
        sec = data['runes'].get('secondary_tree', '')
        sec2 = data['runes'].get('secondary', '')
        if sec:
            main.append(f"Arbre secondaire : {sec} — {sec2}")
        main.append(f"Ordre sorts : {data['skill_order']}")
        main.append(f"Items de départ : {data['starting_items']}")

        tips = data.get('tips', [])
        if tips:
            main.append("Tips : " + " | ".join(tips if isinstance(tips, list) else [tips]))

        result.append((f"build_main_{slug}", "\n".join(main)))

        # Chunks par variante de build
        for variant_name, variant in data.get("build_paths", {}).items():
            lines = [f"BUILD {champ} — variante '{variant_name}' :"]
            ordre = variant.get("ordre", [])
            if ordre:
                lines.append(f"Ordre des items : {' → '.join(ordre)}")
            premier = variant.get("premier_retour", "")
            if premier:
                lines.append(f"Premier retour : {premier}")
            note = variant.get("note", "")
            if note:
                lines.append(f"Note : {note}")
            chemins = variant.get("chemins", {})
            for item, chemin in chemins.items():
                lines.append(f"  • {item} : {chemin}")
            result.append((f"build_{slug}_{variant_name[:20].replace(' ', '_')}", "\n".join(lines)))

        # Chunk matchup spécifique si présent
        for key, val in data.items():
            if key.startswith("matchup_"):
                result.append((f"{key}_{slug}", f"MATCHUP {champ} — {key.replace('matchup_', '')} :\n{val}"))

        # Counters / strong_vs
        if data.get("counters"):
            result.append((f"counters_{slug}", f"Counters de {champ} : {data['counters']}"))
        if data.get("strong_vs"):
            result.append((f"strong_{slug}", f"{champ} est fort contre : {data['strong_vs']}"))

    return result
