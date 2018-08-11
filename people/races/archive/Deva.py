from random import choice

from people.Person import Person
from tools.swearCheck import testSwear


class Deva(Person):
    nm1 = ["Ad", "Ans", "Ars", "Ay", "Bav", "Ber", "Dar", "Eb", "Ely", "Er", "Ery", "Gal", "Gam", "Gar", "Hiy", "Iann",
           "Ker", "Mah", "Mahr", "Man", "Mar", "Math", "Mor", "Nat", "Neh", "Ner", "Ob", "Or", "Rah", "Ron", "Sam", "Sav",
           "Ser", "Sor", "Tar", "Tav", "Vat", "Ver", "Zach", "Zay"]
    nm2 = ["ab", "ach", "ad", "ahk", "ahm", "ahn", "ahr", "ak", "al", "am", "an", "ar", "as", "ath", "eb", "ech", "ed",
           "ehr", "ek", "el", "em", "en", "er", "es", "iah", "ihm", "ihn", "im", "in", "ir", "is"]
    nm3 = ["Ab", "Ad", "An", "Ar", "Ash", "Chan", "Dan", "Dar", "Dav", "Din", "Elk", "Eran", "Eys", "Han", "Hav", "Hen",
           "Idr", "Is", "Jan", "Jen", "Kal", "Kan", "Kay", "Len", "Lih", "Mah", "Mar", "Nal", "Nav", "Nom", "Paz", "Rav",
           "Ren", "Riy", "Sad", "Shar", "Sir", "Tar", "Tel", "Tir"]
    nm4 = ["a", "ael", "aen", "ah", "ahne", "ana", "anaeh", "anael", "anah", "ane", "anel", "aniah", "ara", "araeh", "are",
           "ariah", "ea", "ehl", "ek", "el", "ele", "elle", "era", "ey", "eya", "i", "ia", "iah", "im", "ima"]

    nm1 = ["", "", "", "", "b", "d", "g", "h", "k", "m", "n", "r", "s", "t", "v", "z"]
    nm2 = ["a", "e", "i", "o", "a", "e", "i", "o", "a", "e", "i", "o", "a", "e", "i", "o", "a", "e", "i", "o", "a", "e",
           "i", "o", "ia", "ie", "ea", "ei"]
    nm3 = ["b", "ch", "d", "h", "hr", "l", "ly", "m", "n", "nn", "ns", "r", "rs", "ry", "t", "th", "v", "y"]
    nm4 = ["a", "e", "i"]
    nm5 = ["b", "ch", "d", "h", "hk", "hm", "hn", "hr", "k", "l", "m", "n", "r", "s", "th"]

    nm6 = ["", "", "", "", "", "ch", "d", "h", "j", "k", "l", "m", "n", "p", "r", "s", "sh", "t", "th"]
    nm7 = ["a", "e", "i"]
    nm8 = ["b", "d", "dr", "h", "l", "lk", "m", "n", "r", "s", "sh", "v", "y", "ys", "z"]
    nm9 = ["a", "e", "i", "a", "e", "i", "a", "e", "i", "a", "e", "i", "a", "e", "i", "a", "e", "i", "ia", "ae", "ea"]
    nm10 = ["hn", "l", "ll", "m", "n", "r", "y"]
    nm11 = ["", "", "", "", "", "", "h", "h", "hl", "k", "l", "l", "n", "n", "m", "m"]

    def nameFem(self):
        i = choice(range(0, 2))

        name_component = choice(self.nm6)
        name_component2 = choice(self.nm7)
        name_component3 = choice(self.nm8)
        name_component4 = choice(self.nm9)
        name_component5 = choice(self.nm11)

        while name_component3 == name_component or name_component3 == name_component5:
            name_component3 = choice(self.nm8)

        if i == 0:
            nMs = name_component + name_component2 + name_component3 + name_component4 + name_component5
        else:
            name_component6 = choice(self.nm10)
            name_component7 = choice(self.nm9)

            while name_component6 == name_component5 or name_component6 == name_component3:
                name_component6 = choice(self.nm10)

            nMs = name_component + name_component2 + name_component3 + name_component4 + name_component6 + name_component7 + name_component5

        return testSwear(nMs)


    def nameMas(self):
        name_component = choice(self.nm1)
        name_component2 = choice(self.nm2)
        name_component3 = choice(self.nm3)
        name_component4 = choice(self.nm4)
        name_component5 = choice(self.nm5)
        while name_component3 == name_component or name_component3 == name_component5:
            name_component3 = choice(self.nm3)

        nMs = name_component + name_component2 + name_component3 + name_component4 + name_component5
        return testSwear(nMs)
