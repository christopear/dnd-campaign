from random import choice

from people.Person import Person
from tools.swearCheck import testSwear


class Triton(Person):
    nm1 = ["c", "d", "dh", "j", "jh", "k", "kh", "m", "n", "r", "v", "z"]
    nm2 = ["a", "e", "i", "o", "u"]
    nm3 = ["d", "dd", "g", "gl", "hn", "hl", "hr", "l", "lg", "lm", "ld", "ln", "lz", "m", "mn", "mr", "n", "nn", "nd",
           "nl", "nr", "nv", "r", "rl", "rn", "rv", "rz", "v", "vn", "z"]

    nm4 = ["", "", "", "", "", "", "", "", "b", "bh", "d", "dh", "f", "fl", "h", "l", "m", "n", "s", "sh", "vl", "w",
           "wh",
           "y"]
    nm5 = ["a", "e", "o", "u", "a", "e", "o", "u", "i"]
    nm6 = ["d", "dd", "dr", "gr", "gl", "hl", "hn", "l", "lr", "lt", "lth", "ml", "nl", "nth", "nr", "r", "rn", "rl",
           "rr",
           "s", "sh", "st", "sl", "sn", "t", "th", "tr", "thr", "tl", "thl"]
    nm7 = ["d", "h", "l", "m", "n", "r"]
    nm8 = ["e", "y", "y", "y", "y", "y", "y"]

    nm9 = ["", "", "", "b", "bh", "d", "dh", "j", "g", "l", "m", "n", "p", "r", "s", "v", "z"]
    nm10 = ["a", "u", "a", "u", "a", "u", "e", "o"]
    nm11 = ["b", "d", "g", "gh", "hl", "hn", "hm", "hr", "l", "n", "m", "r", "v"]
    nm12 = ["a", "o", "a", "o", "e", "u"]
    nm13 = ["d", "g", "l", "ll", "ln", "lm", "lv", "m", "mn", "n", "ns", "nz", "r", "rs", "s", "sn", "x", "z"]

    def nameFem(self):
        name_component = choice(Triton.nm4)
        name_component2 = choice(Triton.nm5)
        name_component3 = choice(Triton.nm6)
        name_component4 = choice(Triton.nm8)
        while name_component3 == name_component:
            name_component3 = choice(Triton.nm6)

        if i < 5:
            nFm = name_component + name_component2 + name_component3 + name_component4 + "n"
        else:
            name_component5 = choice(Triton.nm5)
            name_component6 = choice(Triton.nm7)
            while name_component6 == name_component3:
                name_component6 = choice(Triton.nm7)

            nFm = name_component + name_component2 + name_component3 + name_component5 + name_component6 + name_component4 + "n"

        testSwear(nFm)

    def nameMas(self):
        name_component = choice(Triton.nm1)
        name_component2 = choice(Triton.nm2)
        name_component3 = choice(Triton.nm3)
        while name_component == name_component3:
            name_component3 = choice(Triton.nm3)

        name_component4 = choice(Triton.nm2)
        nMs = name_component + name_component2 + name_component3 + name_component2 + "s"
        testSwear(nMs)
