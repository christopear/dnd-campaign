from random import choice

from people.Person import Person
from tools.swearCheck import testSwear


class Kobolds(Person):
    nm1 = ["", "", "", "", "d", "g", "h", "k", "m", "n", "r", "s", "sn", "t", "v", "z"]
    nm2 = ["a", "e", "i", "o", "u"]
    nm3 = ["b", "bl", "d", "dr", "g", "gg", "gl", "gn", "gr", "hz", "hr", "hl", "hs", "k", "kk", "kr", "kl", "kb", "kd",
           "l", "ld", "lb", "lt", "ll", "lp", "lg", "p", "pl", "pp", "r", "rt", "rp", "rb", "rk", "t", "tr", "tl", "v",
           "vl", "vn"]
    nm4 = ["", "", "", "", "", "d", "g", "gs", "k", "ks", "m", "n", "r", "rn", "s", "ss", "tt", "v", "x"]



    def nameMas(self):
        name_component = choice(Kobolds.nm1)
        name_component2 = choice(Kobolds.nm2)
        name_component4 = choice(Kobolds.nm4)
        if i < 4:
            while name_component < 4:
                name_component = choice(Kobolds.nm1)

            while name_component4 < 5 or name_component4 == name_component:
                name_component4 = choice(Kobolds.nm4)

            nMs = name_component + name_component2 + name_component4
        else:
            name_component3 = choice(Kobolds.nm3)
            name_component5 = choice(Kobolds.nm2)
            if name_component < 4:
                while name_component4 < 5:
                    name_component4 = choice(Kobolds.nm4)

            while name_component3 == name_component or name_component3 == name_component4:
                name_component3 = choice(Kobolds.nm3)

            nMs = name_component + name_component2 + name_component3 + name_component5 + name_component2

        return testSwear(nMs)
