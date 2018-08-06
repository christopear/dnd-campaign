from random import choice

from people.Person import Person
from tools.swearCheck import testSwear


class Lizardfolk(Person):
    nm1 = ["", "", "", "", "", "b", "d", "g", "jh", "k", "l", "m", "n", "r", "s", "sh", "t", "tr", "th", "thr", "v"]
    nm2 = ["a", "e", "i", "o", "u", "a", "e", "i", "o", "u", "a", "e", "i", "o", "u", "a", "e", "i", "o", "u", "a", "e",
           "i", "o", "u", "a", "e", "i", "o", "u", "a", "e", "i", "o", "u", "a", "e", "i", "o", "u", "a", "e", "i", "o",
           "u", "aa", "ae", "ao", "au"]
    nm3 = ["ch", "d", "dr", "dh", "g", "gr", "gh", "gg", "l", "ll", "lt", "lth", "lr", "p", "r", "rg", "rht", "rk",
           "rt",
           "rd", "rth", "sh", "sk", "shr", "sh", "sl", "t", "th", "tr", "thr"]
    nm4 = ["a", "e", "i", "o", "u", "y", "a", "e", "i", "o", "u", "y", "a", "e", "i", "o", "u", "y", "a", "e", "i", "o",
           "u", "y", "a", "e", "i", "o", "u", "y", "a", "e", "i", "o", "u", "y", "a", "e", "i", "o", "u", "a", "e", "i",
           "o", "u", "ea", "ua", "ae", "ia", "aa", "ao"]
    nm5 = ["c", "g", "gr", "gn", "k", "kh", "kr", "r", "rr", "s", "ss", "sr", "st", "str", "t", "th", "tr"]
    nm6 = ["", "", "", "", "", "", "", "ch", "k", "n", "nd", "nk", "nt", "r", "rd", "rk", "rt", "rth", "s", "ss", "sh",
           "sj", "sk", "t", "th", "v", "x"]

    def nameMas(self):
        name_component = choice(Lizardfolk.nm1)
        name_component2 = choice(Lizardfolk.nm2)
        name_component3 = choice(Lizardfolk.nm6)
        if i < 2:
            if name_component < 5:
                while name_component3 == name_component:
                    name_component3 = choice(Lizardfolk.nm6)

            nMs = name_component + name_component2 + name_component3
        else:
            name_component4 = choice(Lizardfolk.nm3)
            name_component5 = choice(Lizardfolk.nm4)
            while name_component4 == name_component or name_component4 == name_component3:
                name_component4 = choice(Lizardfolk.nm3)

            if i < 7:
                nMs = name_component + name_component2 + name_component4 + name_component5 + name_component3
            else:
                name_component6 = choice(Lizardfolk.nm2)
                name_component7 = choice(Lizardfolk.nm5)
                while name_component7 == name_component4 or name_component7 == name_component3:
                    name_component7 = choice(Lizardfolk.nm5)

                nMs = name_component + name_component2 + name_component4 + name_component6 + name_component7 + name_component5 + name_component3

        return testSwear(nMs)
