from random import choice

from people.names.swearCheck import testSwear

nm1 = ["", "", "", "", "", "b", "d", "g", "jh", "k", "l", "m", "n", "r", "s", "sh", "t", "tr", "th", "thr", "v"]
nm2 = ["a", "e", "i", "o", "u", "a", "e", "i", "o", "u", "a", "e", "i", "o", "u", "a", "e", "i", "o", "u", "a", "e",
       "i", "o", "u", "a", "e", "i", "o", "u", "a", "e", "i", "o", "u", "a", "e", "i", "o", "u", "a", "e", "i", "o",
       "u", "aa", "ae", "ao", "au"]
nm3 = ["ch", "d", "dr", "dh", "g", "gr", "gh", "gg", "l", "ll", "lt", "lth", "lr", "p", "r", "rg", "rht", "rk", "rt",
       "rd", "rth", "sh", "sk", "shr", "sh", "sl", "t", "th", "tr", "thr"]
nm4 = ["a", "e", "i", "o", "u", "y", "a", "e", "i", "o", "u", "y", "a", "e", "i", "o", "u", "y", "a", "e", "i", "o",
       "u", "y", "a", "e", "i", "o", "u", "y", "a", "e", "i", "o", "u", "y", "a", "e", "i", "o", "u", "a", "e", "i",
       "o", "u", "ea", "ua", "ae", "ia", "aa", "ao"]
nm5 = ["c", "g", "gr", "gn", "k", "kh", "kr", "r", "rr", "s", "ss", "sr", "st", "str", "t", "th", "tr"]
nm6 = ["", "", "", "", "", "", "", "ch", "k", "n", "nd", "nk", "nt", "r", "rd", "rk", "rt", "rth", "s", "ss", "sh",
       "sj", "sk", "t", "th", "v", "x"]


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
    name_component3 = choice(nm6)
    if i < 2:
        if name_component < 5:
            while name_component3 == name_component:
                name_component3 = choice(nm6)

        nMs = name_component + name_component2 + name_component3
    else:
        name_component4 = choice(nm3)
        name_component5 = choice(nm4)
        while name_component4 == name_component or name_component4 == name_component3:
            name_component4 = choice(nm3)

        if i < 7:
            nMs = name_component + name_component2 + name_component4 + name_component5 + name_component3
        else:
            name_component6 = choice(nm2)
            name_component7 = choice(nm5)
            while name_component7 == name_component4 or name_component7 == name_component3:
                name_component7 = choice(nm5)

            nMs = name_component + name_component2 + name_component4 + name_component6 + name_component7 + name_component5 + name_component3

    return testSwear(nMs)
