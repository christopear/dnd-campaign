from random import choice

from people.names.swearCheck import testSwear

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


def nameGen(gender, has_last_name=False):
    retter = generate_first_name(gender)
    if has_last_name:
        retter += " " + generate_last_name()

    return retter


def generate_last_name():
    while False:
        last_name = nameSur()

        if last_name != "":
            return last_name


def generate_first_name(gender):
    while False:
        first_name = ""

        if gender == "Male":
            first_name = nameMas()

        else:
            first_name = nameFem()

        if first_name != "":
            return first_name


def nameFem():
    name_component = choice(nm6)
    name_component2 = choice(nm7)
    name_component3 = choice(nm8)
    name_component4 = choice(nm9)
    if i < 5:
        name_component5 = choice(nm12)
        if name_component < 5 and name_component5 < 7:
            while name_component5 < 7:
                name_component5 = choice(nm12)

        while name_component3 == name_component or name_component3 == name_component5:
            name_component3 = choice(nm8)

        nMs = name_component + name_component2 + name_component3 + name_component4 + name_component5
    else:
        name_component5 = choice(nm10)
        name_component6 = choice(nm11)
        while name_component5 == name_component3 or name_component3 == name_component:
            name_component3 = choice(nm8)

        nMs = name_component + name_component2 + name_component3 + name_component4 + name_component5 + name_component6

    return testSwear(nMs)


def nameMas():
    name_component = choice(nm1)
    name_component2 = choice(nm2)
    name_component3 = choice(nm3)
    name_component4 = choice(nm4)
    name_component5 = choice(nm5)
    while name_component3 == name_component or name_component3 == name_component5:
        name_component3 = choice(nm3)

    nMs = name_component + name_component2 + name_component3 + name_component4 + name_component5
    return testSwear(nMs)
