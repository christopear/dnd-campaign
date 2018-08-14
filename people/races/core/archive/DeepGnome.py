from random import choice

from people.Person import Person


class DeepGnome(Person):
    nm1 = ["b", "br", "d", "dr", "fr", "g", "gh", "gr", "k", "kh", "kr", "sch", "schn", "sn", "sh", "t", "th", "w", "z",
           "zh"]
    nm2 = ["a", "e", "i", "o", "u", "a", "e", "i", "o", "u", "a", "e", "i", "o", "u", "a", "e", "i", "o", "u", "a", "e",
           "i", "o", "u", "ie", "ee", "ai", "aa", "ei"]
    nm3 = ["ck", "ckt", "ckh", "cn", "dg", "dl", "ddl", "dm", "g", "gg", "gn", "gl", "ggl", "kt", "kth", "kl", "kn", "lsch",
           "lw", "lth", "lk", "lkr", "ltr", "ll", "ld", "ldr", "nth", "nt", "nd", "ndr", "ntr", "rbl", "rthm", "rt", "rdr",
           "t", "tt", "tl", "ttl", "tr", "thr", "th"]
    nm4 = ["a", "e", "i", "u"]
    nm5 = ["", "", "", "c", "ck", "d", "g", "l", "ll", "ld", "n", "nd", "nk", "r", "rs", "t"]

    nm6 = ["", "", "", "", "", "b", "d", "fr", "gh", "gr", "h", "k", "kh", "kr", "l", "m", "n", "s", "sh", "sn", "sch",
           "schn", "t", "th", "y", "w", "z"]
    nm7 = ["a", "e", "i", "u"]
    nm8 = ["ckn", "d", "dl", "dd", "g", "gg", "gd", "gn", "gh", "l", "ll", "lg", "lm", "lv", "ls", "lsch", "lsh", "m", "mk",
           "mg", "n", "nn", "nt", "ny", "ng", "nk", "rb", "rg", "rl", "rsh", "rv", "rt", "rth", "rs", "s", "ss", "sh", "sn",
           "sk", "sg", "sl", "th", "t", "tr", "thr", "v", "vr", "vy", "z"]
    nm9 = ["a", "e", "i", "a", "e", "i", "a", "e", "i", "a", "e", "i", "ee", "ie", "ei", "ai", "ia"]
    nm10 = ["d", "dd", "l", "ll", "ld", "ln", "lk", "n", "nn", "r", "rr", "ry", "rt", "sh", "sch"]
    nm11 = ["a", "e", "i", "a", "i", "a", "i"]
    nm12 = ["", "", "", "", "", "", "", "d", "dd", "h", "l", "ll", "n", "nn", "s", "ss"]

    nm13 = ["adamant", "agate", "alabaster", "alloy", "amethyst", "basalt", "bedrock", "block", "boulder", "brass", "brick",
            "bronze", "clay", "cobalt", "cobble", "copper", "crag", "crystal", "deposit", "diamond", "dirt", "dust",
            "emerald", "flint", "fossil", "garnet", "gem", "geo", "geode", "gold", "granite", "gravel", "grime", "ground",
            "ingot", "iron", "jade", "jewel", "joint", "lapis", "lazuli", "lead", "lime", "lodge", "lump", "marble",
            "mason", "metal", "mill", "mineral", "mold", "nickel", "nugget", "obsidian", "onyx", "opal", "ore", "pebble",
            "pellet", "peridot", "pit", "quartz", "rock", "rough", "rubble", "ruby", "sand", "sapphire", "scrap", "seam",
            "shelf", "silver", "slab", "slate", "smelt", "soil", "spinel", "steel", "stone", "stony", "sturdy", "terra",
            "tile", "tin", "topaz", "turf", "wedge", "wire", "zinc", "zircon"]
    nm14 = ["back", "basher", "bender", "biter", "bleacher", "bone", "bones", "brander", "breaker", "bringer", "browser",
            "brusher", "carrier", "carver", "catcher", "checker", "cheek", "chest", "chewer", "chin", "chiseler", "cleaner",
            "cleanser", "collector", "counter", "crusher", "cutter", "designer", "digger", "duster", "ear", "eye", "eyes",
            "face", "feet", "finder", "finger", "fingers", "fist", "foot", "forger", "gatherer", "gazer", "getter",
            "grasper", "grinder", "hand", "head", "heart", "hewer", "holder", "knuckle", "leg", "legs", "lifter", "loader",
            "maker", "marker", "mask", "melter", "mender", "merger", "molder", "moulder", "mug", "neck", "nose", "packer",
            "presser", "pusher", "rater", "recorder", "rinser", "saver", "scanner", "scratcher", "sealer", "searcher",
            "seeker", "seizer", "senser", "shaper", "shoveler", "skin", "smasher", "smelter", "snatcher", "sniffer",
            "sorter", "splitter", "stamper", "stasher", "stocker", "surveyor", "sweeper", "switcher", "teeth", "temperer",
            "tooth", "trader", "twirler", "twister", "vein", "viewer", "warper", "watcher"]

    def generate_surname(self):
        name_component = choice(self.nm13)
        name_component2 = choice(self.nm14)
        nMs = name_component + name_component2
        return nMs

    def generate_feminine(self):
        i = choice(range(0, 2))
        name_component = choice(self.nm6)
        name_component2 = choice(self.nm7)
        name_component3 = choice(self.nm8)
        name_component4 = choice(self.nm9)
        if i == 0:
            name_component5 = choice(self.nm12)

            while name_component3 == name_component or name_component3 == name_component5:
                name_component3 = choice(self.nm8)

            nMs = name_component + name_component2 + name_component3 + name_component4 + name_component5
        else:
            name_component5 = choice(self.nm10)
            name_component6 = choice(self.nm11)

            while name_component5 == name_component3 or name_component3 == name_component:
                name_component3 = choice(self.nm8)

            nMs = name_component + name_component2 + name_component3 + name_component4 + name_component5 + name_component6

        return nMs

    def generate_masculine(self):
        name_component = choice(self.nm1)
        name_component2 = choice(self.nm2)
        name_component3 = choice(self.nm3)
        name_component4 = choice(self.nm4)
        name_component5 = choice(self.nm5)
        while name_component3 == name_component or name_component3 == name_component5:
            name_component3 = choice(self.nm3)

        nMs = name_component + name_component2 + name_component3 + name_component4 + name_component5
        return nMs
