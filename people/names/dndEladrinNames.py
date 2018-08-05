from random import choice

from people.names.swearCheck import testSwear

nm1 = ["Ara", "Aran", "Ber", "Bran", "Cor", "Cru", "Da", "Daye", "Elro", "Ere", "Far", "Fyla", "Gal", "Galin", "Ha",
       "Hor", "Im", "Ira", "Ja", "Jor", "Kru", "Kuo", "Lan", "Lic", "Mar", "Min", "Nal", "Nark", "Ola", "Otir", "Pae",
       "Pan", "Qua", "Quo", "Rel", "Riar", "Sarn", "Sove", "Tav", "Trin", "Uri", "Veth", "Vic", "Wal", "Wrug", "Xan",
       "Yan", "Yor", "Zen", "Zor"]
nm2 = ["aris", "aster", "baver", "bin", "card", "corin", "dan", "darai", "dartis", "don", "emin", "erta", "fis", "fros",
       "geon", "grephor", "heros", "horn", "ikul", "iver", "kris", "kul", "lias", "liss", "mendi", "meral", "mil",
       "morn", "neiros", "nis", "okas", "oros", "peiros", "prath", "ratra", "reth", "rian", "rion", "sirak", "ster",
       "thas", "tihr", "torin", "urian", "uvir", "van", "vis", "wirn", "worn", "xeral", "xis", "ykos", "yth", "zeiros",
       "zion"]
nm3 = ["Al", "An", "Anas", "Be", "Bri", "Cae", "Cyl", "Dris", "Dur", "Eil", "Ena", "Fae", "Fan", "Gru", "Gyl", "Hen",
       "Hyl", "Illa", "Ire", "Jar", "Jelen", "Kai", "Kora", "Les", "Lyv", "Mag", "Me", "Nai", "Neri", "Ol", "Ori", "Pi",
       "Prys", "Qi", "Que", "Ri", "Rol", "Sa", "Sha", "Thei", "Tri", "Ul", "Ura", "Va", "Vela", "Wes", "Wre", "Xyr",
       "Ylla", "Zen"]
nm4 = ["bis", "bynn", "cahne", "caryn", "celle", "cena", "diel", "dys", "faera", "fyra", "glyn", "grys", "hanna",
       "hyssa", "kiries", "kyrath", "lenae", "lenna", "lyn", "lynna", "meiv", "miris", "mynis", "nairra", "neth",
       "parys", "prana", "qirith", "qis", "raste", "rastra", "riele", "rynna", "sanna", "shana", "sys", "thaea", "tora",
       "trianna", "a", "viryn", "vyre", "wena", "wyse", "xana", "xis", "yana", "yeira", "zane", "zora"]


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
    name_component = choice(nm3)
    name_component2 = choice(nm4)
    nMs = name_component + name_component2
    testSwear(nMs)


def nameMas():
    name_component = choice(nm1)
    name_component2 = choice(nm2)
    nMs = name_component + name_component2
    testSwear(nMs)
