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
