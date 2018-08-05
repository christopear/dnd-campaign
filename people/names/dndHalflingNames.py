from random import choice

from people.names.swearCheck import testSwear

nm1 = ["An", "Ar", "Bar", "Bel", "Con", "Cor", "Dan", "Dav", "El", "Er", "Fal", "Fin", "Flyn", "Gar", "Go", "Hal",
       "Hor", "Ido", "Ira", "Jan", "Jo", "Kas", "Kor", "La", "Lin", "Mar", "Mer", "Ne", "Nor", "Ori", "Os", "Pan",
       "Per", "Pim", "Quin", "Quo", "Ri", "Ric", "San", "Shar", "Tar", "Te", "Ul", "Uri", "Val", "Vin", "Wen", "Wil",
       "Xan", "Xo", "Yar", "Yen", "Zal", "Zen"]
nm2 = ["ace", "amin", "bin", "bul", "dak", "dal", "der", "don", "emin", "eon", "fer", "fire", "gin", "hace", "horn",
       "kas", "kin", "lan", "los", "min", "mo", "nad", "nan", "ner", "orin", "os", "pher", "pos", "ras", "ret", "ric",
       "rich", "rin", "ry", "ser", "sire", "ster", "ton", "tran", "umo", "ver", "vias", "von", "wan", "wrick", "yas",
       "yver", "zin", "zor", "zu"]
nm3 = ["An", "Ari", "Bel", "Bre", "Cal", "Chen", "Dar", "Dia", "Ei", "Eo", "Eli", "Era", "Fay", "Fen", "Fro", "Gel",
       "Gra", "Ha", "Hil", "Ida", "Isa", "Jay", "Jil", "Kel", "Kith", "Le", "Lid", "Mae", "Mal", "Mar", "Ne", "Ned",
       "Odi", "Ora", "Pae", "Pru", "Qi", "Qu", "Ri", "Ros", "Sa", "Shae", "Syl", "Tham", "Ther", "Tryn", "Una", "Uvi",
       "Va", "Ver", "Wel", "Wi", "Xan", "Xi", "Yes", "Yo", "Zef", "Zen"]
nm4 = ["alyn", "ara", "brix", "byn", "caryn", "cey", "da", "dove", "drey", "elle", "eni", "fice", "fira", "grace",
       "gwen", "haly", "jen", "kath", "kis", "leigh", "la", "lie", "lile", "lienne", "lyse", "mia", "mita", "ne", "na",
       "ni", "nys", "ola", "ora", "phina", "prys", "rana", "ree", "ri", "ris", "sica", "sira", "sys", "tina", "trix",
       "ula", "vira", "vyre", "wyn", "wyse", "yola", "yra", "zana", "zira"]


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
    return testSwear(nMs)


def nameMas():
    name_component = choice(nm1)
    name_component2 = choice(nm2)
    nMs = name_component + name_component2
    return testSwear(nMs)
