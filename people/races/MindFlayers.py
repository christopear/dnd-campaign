from random import choice

from people.Person import Person
from tools.swearCheck import testSwear


class MindFlayers(Person):
    nm1 = ["", "", "", "c", "d", "dr", "g", "gr", "k", "l", "q", "qh", "r", "s", "sr", "sv", "sl", "t", "th", "tr", "v",
           "z"]
    nm2 = ["a", "e", "u", "a", "e", "u", "a", "e", "u", "a", "e", "u", "a", "e", "u", "a", "e", "u", "a", "e", "u", "a",
           "e", "u", "a", "e", "u", "a", "e", "u", "o", "o", "i", "au", "uoo", "ua", "uo", "ao"]
    nm3 = ["b", "br", "d", "dr", "dd", "g", "gg", "gr", "gch", "gl", "l", "ll", "lb", "ld", "nk", "nch", "ng", "ph",
           "phr",
           "r", "rd", "rb", "rg", "rds", "s", "ss", "sg", "sr", "sd", "sb", "z", "zz"]
    nm4 = ["a", "e", "i", "u", "a", "e", "i", "u", "o"]
    nm5 = ["b", "d", "g", "l", "m", "n", "ng", "r", "v", "y", "z"]
    nm6 = ["a", "e", "o", "u", "a", "e", "o", "u", "a", "e", "o", "u", "a", "e", "o", "u", "a", "e", "o", "u", "i",
           "au",
           "ua", "ao", "uo"]
    nm7 = ["k", "kt", "ks", "l", "ll", "lt", "m", "n", "r", "sk", "ss", "ssk", "x"]

    def nameMas(self):
        name_component = choice(MindFlayers.nm1)
        name_component2 = choice(MindFlayers.nm2)
        name_component3 = choice(MindFlayers.nm7)
        if i < 2:
            while name_component < 3 or name_component == name_component3:
                name_component = choice(MindFlayers.nm1)

            nMs = name_component + name_component2 + name_component3
        else:
            name_component4 = choice(MindFlayers.nm3)
            name_component5 = choice(MindFlayers.nm4)
            while name_component4 == name_component or name_component4 == name_component3:
                name_component4 = choice(MindFlayers.nm3)

            if i < 6:
                nMs = name_component + name_component2 + name_component4 + name_component5 + name_component3
            else:
                name_component6 = choice(MindFlayers.nm5)
                name_component7 = choice(MindFlayers.nm6)
                while name_component6 == name_component4 or name_component6 == name_component3:
                    name_component6 = choice(MindFlayers.nm5)

                if i < 9:
                    nMs = name_component + name_component2 + name_component4 + name_component5 + name_component6 + name_component7 + name_component3
                else:
                    name_component8 = choice(MindFlayers.nm5)
                    name_component9 = choice(MindFlayers.nm4)
                    while name_component8 == name_component6:
                        name_component8 = choice(MindFlayers.nm5)

                    nMs = name_component + name_component2 + name_component4 + name_component5 + name_component6 + name_component7 + name_component8 + name_component9

        return testSwear(nMs)
