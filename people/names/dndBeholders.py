from random import choice

from people.names.swearCheck import testSwear

nm1 = ["", "", "", "", "", "b", "c", "ch", "d", "dh", "f", "g", "gh", "j", "kh", "l", "m", "n", "q", "qh", "r", "s",
       "th", "v", "x", "z"]
nm2 = ["a", "e", "i", "o", "a", "e", "i", "o", "a", "e", "i", "o", "a", "e", "i", "o", "a", "e", "i", "o", "a", "e",
       "i", "o", "a", "e", "i", "o", "a", "e", "i", "o", "a", "e", "i", "o", "a", "e", "i", "o", "a", "e", "i", "o",
       "aa", "oa", "ua", "ia", "au", "ao", "ou"]
nm3 = ["d", "dd", "dr", "dl", "dh", "dtr", "dthr", "g", "gh", "gth", "k", "kk", "kh", "kht", "l", "ld", "ldr", "lb",
       "lbr", "lm", "ln", "ls", "lsh", "lth", "lthdr", "lx", "m", "ml", "md", "mdr", "mn", "n", "nt", "nth", "nthr",
       "ndr", "ntr", "r", "rb", "rd", "rg", "rgr", "rt", "rthr", "rth", "rl", "rn", "rm", "t", "th", "thr", "thdr",
       "tr", "z", "zd", "zdr"]
nm4 = ["a", "i", "o", "u", "a", "i", "o", "u", "y"]
nm5 = ["c", "k", "ks", "q", "qs", "r", "rs", "rx", "s", "sc", "sk", "x", "z"]
nm6 = ["a", "e", "i", "a", "e", "i", "a", "e", "i", "a", "e", "i", "a", "e", "i", "a", "e", "i", "o", "o", "ia", "ai",
       "ie", "ee", "io", "ae", "ea"]
nm7 = ["", "", "", "", "", "ch", "cs", "csh", "hl", "hm", "hn", "hx", "hs", "hsh", "ks", "ksh", "ll", "lm", "ln", "lk",
       "lks", "ls", "lsh", "lx", "ph", "r", "rq", "rv", "s", "sh", "x"]


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


def nameMas(i):
    name_component = choice(nm1)
    name_component2 = choice(nm2)
    name_component3 = choice(nm7)
    if i < 2:
        while name_component == name_component3:
            name_component3 = choice(nm7)

        nMs = name_component + name_component2 + name_component3
    else:
        name_component4 = choice(nm3)
        name_component5 = choice(nm4)
        if i < 6:
            while name_component4 == name_component or name_component4 == name_component3:
                name_component4 = choice(nm3)

            nMs = name_component + name_component2 + name_component4 + name_component5 + name_component3
        else:
            name_component6 = choice(nm5)
            name_component7 = choice(nm6)
            if i < 9:
                while name_component6 == name_component4 or name_component6 == name_component3:
                    name_component6 = choice(nm5)

                nMs = name_component + name_component2 + name_component4 + name_component5 + name_component6 + name_component7 + name_component3
            else:
                name_component8 = choice(nm5)
                name_component9 = choice(nm6)
                while name_component8 == name_component6:
                    name_component8 = choice(nm5)

                nMs = name_component + name_component2 + name_component4 + name_component5 + name_component6 + name_component7 + name_component8 + name_component9

    return testSwear(nMs)
