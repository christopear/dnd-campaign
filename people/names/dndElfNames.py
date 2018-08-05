from random import choice

from people.names.swearCheck import testSwear

nm1 = ["Ad", "Ae", "Bal", "Bei", "Car", "Cra", "Dae", "Dor", "El", "Ela", "Er", "Far", "Fen", "Gen", "Glyn", "Hei",
       "Her", "Ian", "Ili", "Kea", "Kel", "Leo", "Lu", "Mira", "Mor", "Nae", "Nor", "Olo", "Oma", "Pa", "Per", "Pet",
       "Qi", "Qin", "Ralo", "Ro", "Sar", "Syl", "The", "Tra", "Ume", "Uri", "Va", "Vir", "Waes", "Wran", "Yel", "Yin",
       "Zin", "Zum"]
nm2 = ["balar", "beros", "can", "ceran", "dan", "dithas", "faren", "fir", "geiros", "golor", "hice", "horn", "jeon",
       "jor", "kas", "kian", "lamin", "lar", "len", "maer", "maris", "menor", "myar", "nan", "neiros", "nelis", "norin",
       "peiros", "petor", "qen", "quinal", "ran", "ren", "ric", "ris", "ro", "salor", "sandoral", "toris", "tumal",
       "valur", "ven", "warin", "wraek", "xalim", "xidor", "yarus", "ydark", "zeiros", "zumin"]
nm3 = ["Ad", "Ara", "Bi", "Bry", "Cai", "Chae", "Da", "Dae", "Eil", "En", "Fa", "Fae", "Gil", "Gre", "Hele", "Hola",
       "Iar", "Ina", "Jo", "Key", "Kris", "Lia", "Lora", "Mag", "Mia", "Neri", "Ola", "Ori", "Phi", "Pres", "Qi", "Qui",
       "Rava", "Rey", "Sha", "Syl", "Tor", "Tris", "Ula", "Uri", "Val", "Ven", "Wyn", "Wysa", "Xil", "Xyr", "Yes",
       "Ylla", "Zin", "Zyl"]
nm4 = ["banise", "bella", "caryn", "cyne", "di", "dove", "fiel", "fina", "gella", "gwyn", "hana", "harice", "jyre",
       "kalyn", "krana", "lana", "lee", "leth", "lynn", "moira", "mys", "na", "nala", "phine", "phyra", "qirelle", "ra",
       "ralei", "rel", "rie", "rieth", "rona", "rora", "roris", "satra", "stina", "sys", "thana", "thyra", "tris", "is",
       "vyre", "wenys", "wynn", "xina", "xisys", "ynore", "yra", "zana", "zorwyn"]


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
