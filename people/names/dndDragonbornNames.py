from random import choice

from people.names.swearCheck import testSwear

nm1 = ["Ali", "Ar", "Ba", "Bal", "Bel", "Bha", "Bren", "Caer", "Calu", "Dur", "Do", "Dra", "Era", "Faer", "Fro", "Gre",
       "Ghe", "Gora", "He", "Hi", "Ior", "Jin", "Jar", "Kil", "Kriv", "Lor", "Lumi", "Mar", "Mor", "Med", "Nar", "Nes",
       "Na", "Oti", "Orla", "Pri", "Pa", "Qel", "Ravo", "Ras", "Rho", "Sa", "Sha", "Sul", "Taz", "To", "Trou", "Udo",
       "Uro", "Vor", "Vyu", "Vrak", "Wor", "Wu", "Wra", "Wul", "Xar", "Yor", "Zor", "Zra"]
nm2 = ["barum", "bor", "broth", "ciar", "crath", "daar", "dhall", "dorim", "farn", "fras", "gar", "ghull", "grax",
       "hadur", "hazar", "jhan", "jurn", "kax", "kris", "kul", "lasar", "lin", "mash", "morn", "naar", "prax", "qiroth",
       "qrin", "qull", "rakas", "rash", "rinn", "roth", "sashi", "seth", "skan", "trin", "turim", "ax", "vroth", "vull",
       "warum", "wunax", "xan", "xiros", "yax", "ythas", "zavur", "zire", "ziros"]
nm3 = ["Ari", "A", "Bi", "Bel", "Cris", "Ca", "Drys", "Da", "Erli", "Esh", "Fae", "Fen", "Gur", "Gri", "Hin", "Ha",
       "Irly", "Irie", "Jes", "Jo", "Ka", "Kel", "Ko", "Lilo", "Lora", "Mal", "Mi", "Na", "Nes", "Nys", "Ori", "O",
       "Ophi", "Phi", "Per", "Qi", "Quil", "Rai", "Rashi", "So", "Su", "Tha", "Ther", "Uri", "Ushi", "Val", "Vyra",
       "Welsi", "Wra", "Xy", "Xis", "Ya", "Yr", "Zen", "Zof"]
nm4 = ["birith", "bis", "bith", "coria", "cys", "dalynn", "drish", "drith", "faeth", "fyire", "gil", "gissa", "gwen",
       "hime", "hymm", "karyn", "kira", "larys", "liann", "lyassa", "meila", "myse", "norae", "nys", "patys", "pora",
       "qorel", "qwen", "rann", "riel", "rina", "rinn", "rish", "rith", "saadi", "shann", "sira", "thibra", "thyra",
       "vayla", "vyre", "vys", "wophyl", "wyn", "xiris", "xora", "yassa", "yries", "zita", "zys"]

nm5 = ["", "", "", "", "c", "cl", "cr", "d", "dr", "f", "g", "k", "kl", "kr", "l", "m", "my", "n", "ny", "pr", "sh",
       "t", "th", "v", "y"]
nm6 = ["a", "e", "i", "a", "e", "i", "o", "u", "a", "e", "i", "a", "e", "i", "o", "u", "a", "e", "i", "a", "e", "i",
       "o", "u", "aa", "ia", "ea", "ua", "uu"]
nm7 = ["c", "cc", "ch", "lm", "lk", "lx", "ld", "lr", "ldr", "lt", "lth", "mb", "mm", "mp", "mph", "mr", "mt", "nk",
       "nx", "nc", "p", "ph", "r", "rd", "rj", "rn", "rrh", "rth", "st", "tht", "x"]
nm8 = ["c", "cm", "cn", "d", "j", "k", "km", "l", "n", "nd", "ndr", "nk", "nsht", "nth", "r", "s", "sht", "shkm", "st",
       "t", "th", "x"]
nm9 = ["d", "j", "l", "ll", "m", "n", "nd", "rg", "r", "rr", "rd"]
nm10 = ["c", "d", "k", "l", "n", "r", "s", "sh", "th"]


def nameGen(gender, has_last_name=True):
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


def nameSur():
    name_component = choice(nm5)
    name_component2 = choice(nm6)
    name_component3 = choice(nm7)
    name_component4 = choice(nm6)
    name_component5 = choice(nm10)
    while name_component3 == name_component or name_component3 == name_component5:
        name_component3 = choice(nm7)

    if i < 4:
        nSr = name_component + name_component2 + name_component3 + name_component4 + name_component5
    else:
        name_component6 = choice(nm6)
        name_component7 = choice(nm8)
        while name_component3 == name_component7 or name_component7 == name_component5:
            name_component7 = choice(nm8)

        if i < 7:
            nSr = name_component + name_component2 + name_component3 + name_component4 + name_component7 + name_component6 + name_component5
        else:
            name_component8 = choice(nm6)
            name_component9 = choice(nm9)
            while name_component9 == name_component7 or name_component9 == name_component5:
                name_component9 = choice(nm9)

            nSr = name_component + name_component2 + name_component3 + name_component4 + name_component7 + name_component6 + name_component9 + name_component8 + name_component5

    return testSwear(nSr)
