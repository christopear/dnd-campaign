from random import choice

from people.Person import Person
from tools.swearCheck import testSwear


class MindFlayer(Person):
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
        i = choice(range(0, 4))
        name_component = choice(self.nm1)
        name_component2 = choice(self.nm2)
        name_component3 = choice(self.nm7)
        if i == 0:
            while name_component < 3 or name_component == name_component3:
                name_component = choice(self.nm1)

            nMs = name_component + name_component2 + name_component3
        else:
            name_component4 = choice(self.nm3)
            name_component5 = choice(self.nm4)
            while name_component4 == name_component or name_component4 == name_component3:
                name_component4 = choice(self.nm3)

            if i == 1:
                nMs = name_component + name_component2 + name_component4 + name_component5 + name_component3
            else:
                name_component6 = choice(self.nm5)
                name_component7 = choice(self.nm6)
                while name_component6 == name_component4 or name_component6 == name_component3:
                    name_component6 = choice(self.nm5)

                if i == 2:
                    nMs = name_component + name_component2 + name_component4 + name_component5 + name_component6 + name_component7 + name_component3
                else:
                    name_component8 = choice(self.nm5)
                    name_component9 = choice(self.nm4)
                    while name_component8 == name_component6:
                        name_component8 = choice(self.nm5)

                    nMs = name_component + name_component2 + name_component4 + name_component5 + name_component6 + name_component7 + name_component8 + name_component9

        return testSwear(nMs)
