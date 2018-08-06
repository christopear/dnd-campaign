from random import choice

from people.Person import Person
from tools.swearCheck import testSwear


class Aasimar(Person):
    nm1 = ["", "", "", "", "b", "br", "c", "cr", "h", "l", "m", "n", "p", "r", "t", "v", "w", "z"]
    nm2 = ["a", "e", "i", "o", "u", "y", "a", "e", "i", "o", "u", "y", "a", "e", "i", "o", "u", "y", "au", "ai", "ea", "ei"]
    nm3 = ["d", "dr", "g", "gg", "gr", "gw", "k", "kr", "kl", "l", "ld", "lg", "lw", "lr", "lt", "n", "nr", "nw", "nl", "r",
           "rn", "rr", "rw", "rl", "v", "vr", "w"]
    nm4 = ["a", "i", "a", "i", "a", "i", "a", "i", "a", "i", "a", "i", "e", "a", "i", "e", "a", "i", "e", "o", "o", "u",
           "u", "ee", "ia", "ie", "ai", "ei"]
    nm5 = ["d", "l", "m", "n", "t", "v"]
    nm6 = ["l", "m", "n", "nt", "r"]

    nm7 = ["", "", "", "", "", "br", "d", "dr", "h", "l", "m", "n", "ph", "r", "rh", "th", "v", "w", "z"]
    nm8 = ["a", "i", "o", "a", "i", "o", "a", "i", "o", "a", "i", "o", "a", "i", "o", "a", "i", "o", "e", "e", "ia", "io",
           "ea", "eo"]
    nm9 = ["d", "j", "l", "ld", "ldr", "lv", "ll", "lt", "m", "mm", "mn", "n", "nr", "nv", "nl", "ndr", "nm", "r", "rd",
           "rk", "rs", "s", "sr", "sl", "v"]
    nm10 = ["a", "e", "i", "o", "a", "e", "i", "o", "a", "e", "i", "o", "a", "e", "i", "o", "a", "e", "i", "o", "ea", "ia",
            "ie"]
    nm11 = ["l", "m", "n", "r", "s", "z"]
    nm12 = ["a", "e", "i", "a", "e", "i", "a", "e", "i", "a", "e", "i", "a", "e", "i", "au", "ou", "oe"]
    nm13 = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "h", "l", "m", "n", "r"]


    def nameFem(self):
        name_component = choice(Aasimar.nm7)
        name_component2 = choice(Aasimar.nm8)
        name_component3 = choice(Aasimar.nm9)
        name_component4 = choice(Aasimar.nm10)
        name_component5 = choice(Aasimar.nm13)
        if i < 6:
            while name_component3 == name_component or name_component3 == name_component5:
                name_component3 = choice(Aasimar.nm9)

            nMs = name_component + name_component2 + name_component3 + name_component4 + name_component5
        else:
            name_component6 = choice(Aasimar.nm11)
            name_component7 = choice(Aasimar.nm12)
            while name_component6 == name_component3 or name_component6 == name_component5:
                name_component6 = choice(Aasimar.nm11)

            nMs = name_component + name_component2 + name_component3 + name_component4 + name_component6 + name_component7 + name_component5

        testSwear(nMs)


    def nameMas(self):
        name_component = choice(Aasimar.nm1)
        name_component2 = choice(Aasimar.nm2)
        name_component3 = choice(Aasimar.nm3)
        name_component4 = choice(Aasimar.nm4)
        name_component5 = choice(Aasimar.nm6)
        if i < 6:
            while name_component3 == name_component or name_component3 == name_component5:
                name_component3 = choice(Aasimar.nm3)

            nMs = name_component + name_component2 + name_component3 + name_component4 + name_component5
        else:
            name_component6 = choice(Aasimar.nm5)
            name_component7 = choice(Aasimar.nm4)
            while name_component6 == name_component3 or name_component6 == name_component5:
                name_component6 = choice(Aasimar.nm5)

            nMs = name_component + name_component2 + name_component3 + name_component4 + name_component6 + name_component7 + name_component5

            return testSwear(nMs)
