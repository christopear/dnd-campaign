from random import choice

from people.names.swearCheck import testSwear

nm1 = ["", "", "", "", "", "c", "cl", "cr", "d", "g", "gr", "h", "k", "kh", "kl", "kr", "q", "qh", "ql", "qr", "r",
       "rh", "s", "y", "z"]
nm2 = ["a", "e", "i", "u", "a", "e", "i", "u", "a", "e", "i", "u", "a", "e", "i", "u", "a", "e", "i", "u", "a", "e",
       "i", "u", "a", "e", "i", "u", "ae", "aia", "ee", "oo", "ou", "ua", "uie"]
nm3 = ["c", "cc", "k", "kk", "l", "ll", "q", "r", "rr"]
nm4 = ["a", "e", "i", "a", "e", "i", "a", "e", "i", "a", "e", "i", "a", "e", "i", "aa", "ea", "ee", "ia", "ie"]
nm5 = ["", "", "", "", "c", "ck", "d", "f", "g", "hk", "k", "l", "r", "rr", "rc", "rk", "rrk", "s", "ss"]


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
    name_component3 = choice(nm5)
    if i < 5:
        while name_component == name_component3:
            name_component3 = choice(nm5)

        nMs = name_component + name_component2 + name_component3
    else:
        name_component4 = choice(nm3)
        name_component5 = choice(nm4)
        nMs = name_component + name_component2 + name_component4 + name_component5 + name_component3

    return testSwear(nMs)


def nameFem():
    pass
