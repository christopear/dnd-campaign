from random import choice

from people.names.swearCheck import testSwear

nm1 = ["", "", "", "b", "d", "f", "h", "j", "l", "m", "n", "p", "r", "s", "t", "v", "w", "y"]
nm2 = ["a", "i", "o", "u", "a", "i", "o", "u", "a", "i", "o", "u", "a", "i", "o", "u", "ee", "ie", "ea", "ae", "ai",
       "oo", "ou"]
nm3 = ["c", "g", "gs", "k", "ks", "kt", "m", "n", "rx", "rt", "rs", "s", "sk", "t", "ts", "x", "z"]

br = ""


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


def nameMas():
    name_component = choice(nm1)
    name_component2 = choice(nm2)
    name_component3 = choice(nm3)
    while name_component == name_component3:
        name_component3 = choice(nm3)

    nMs = name_component + name_component2 + name_component3
    return testSwear(nMs)
