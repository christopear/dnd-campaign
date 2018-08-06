from random import choice

from people.Person import Person
from tools.swearCheck import testSwear


class Aarakocra(Person):
    nm1 = ["", "", "", "", "", "c", "cl", "cr", "d", "g", "gr", "h", "k", "kh", "kl", "kr", "q", "qh", "ql", "qr", "r",
           "rh", "s", "y", "z"]
    nm2 = ["a", "e", "i", "u", "a", "e", "i", "u", "a", "e", "i", "u", "a", "e", "i", "u", "a", "e", "i", "u", "a", "e",
           "i", "u", "a", "e", "i", "u", "ae", "aia", "ee", "oo", "ou", "ua", "uie"]
    nm3 = ["c", "cc", "k", "kk", "l", "ll", "q", "r", "rr"]
    nm4 = ["a", "e", "i", "a", "e", "i", "a", "e", "i", "a", "e", "i", "a", "e", "i", "aa", "ea", "ee", "ia", "ie"]
    nm5 = ["", "", "", "", "c", "ck", "d", "f", "g", "hk", "k", "l", "r", "rr", "rc", "rk", "rrk", "s", "ss"]


    def nameMas(self):
        name_component = choice(Aarakocra.nm1)
        name_component2 = choice(Aarakocra.nm2)
        name_component3 = choice(Aarakocra.nm5)
        if i < 5:
            while name_component == name_component3:
                name_component3 = choice(Aarakocra.nm5)

            nMs = name_component + name_component2 + name_component3
        else:
            name_component4 = choice(Aarakocra.nm3)
            name_component5 = choice(Aarakocra.nm4)
            nMs = name_component + name_component2 + name_component4 + name_component5 + name_component3

        return testSwear(nMs)
