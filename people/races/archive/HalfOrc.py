from random import choice

from people.Person import Person
from tools.swearCheck import testSwear


class Orc(Person):
    nm1 = ["Ag", "Agg", "Ar", "Arn", "As", "At", "Atr", "B", "Bar", "Bel", "Bor", "Br", "Brak", "C", "Cr", "D", "Dor", "Dr",
           "Dur", "G", "Gal", "Gan", "Gar", "Gna", "Gor", "Got", "Gr", "Gram", "Grim", "Grom", "Grum", "Gul", "H", "Hag",
           "Han", "Har", "Hog", "Hon", "Hor", "Hun", "Hur", "K", "Kal", "Kam", "Kar", "Kel", "Kil", "Kom", "Kor", "Kra",
           "Kru", "Kul", "Kur", "Lum", "M", "Mag", "Mahl", "Mak", "Mal", "Mar", "Mog", "Mok", "Mor", "Mug", "Muk", "Mura",
           "N", "Oggu", "Ogu", "Ok", "Oll", "Or", "Rek", "Ren", "Ron", "Rona", "S", "Sar", "Sor", "T", "Tan", "Th", "Thar",
           "Ther", "Thr", "Thur", "Trak", "Truk", "Ug", "Uk", "Ukr", "Ull", "Ur", "Urth", "Urtr", "Z", "Za", "Zar", "Zas",
           "Zav", "Zev", "Zor", "Zur", "Zus"]
    nm2 = ["a", "a", "a", "o", "o", "e", "i", "u", "u", "u"]
    nm3 = ["bak", "bar", "bark", "bash", "bur", "burk", "d", "dak", "dall", "dar", "dark", "dash", "dim", "dur", "durk",
           "g", "gak", "gall", "gar", "gark", "gash", "glar", "gul", "gur", "m", "mak", "mar", "marsh", "mash", "mir",
           "mur", "n", "nar", "nars", "nur", "rak", "rall", "rash", "rim", "rimm", "rk", "rsh", "rth", "ruk", "sk", "tar",
           "tir", "tur", "z", "zall", "zar", "zur"]
    nm4 = ["Al", "Ar", "Br", "Ek", "El", "Fal", "Fel", "Fol", "Ful", "G", "Gaj", "Gar", "Gij", "Gor", "Gr", "Gry", "Gyn",
           "Hur", "K", "Kar", "Kat", "Ker", "Ket", "Kir", "Kot", "Kur", "Kut", "Lag", "M", "Mer", "Mir", "Mor", "N", "Ol",
           "Oot", "Puy", "R", "Rah", "Rahk", "Ras", "Rash", "Raw", "Roh", "Rohk", "S", "Sam", "San", "Sem", "Sen", "Sh",
           "Shay", "Sin", "Sum", "Sun", "Tam", "Tem", "Tu", "Tum", "Ub", "Um", "Ur", "Van", "Zan", "Zen", "Zon", "Zun"]
    nm5 = ["a", "a", "o", "o", "e", "i", "i", "u"]
    nm6 = ["d", "da", "dar", "dur", "g", "gar", "gh", "gri", "gu", "sh", "sha", "shi", "gum", "gume", "gur", "ki", "mar",
           "mi", "mira", "me", "mur", "ne", "ner", "nir", "nar", "nchu", "ni", "nur", "ral", "rel", "ri", "rook", "ti",
           "tah", "tir", "tar", "tur", "war", "z", "zar", "zara", "zi", "zur", "zura", "zira"]



    def nameFem(self):
        name_component = choice(self.nm4)
        name_component2 = choice(self.nm5)
        name_component3 = choice(self.nm6)
        nMs = name_component + name_component2 + name_component3
        return testSwear(nMs)


    def nameMas(self):
        name_component = choice(self.nm1)
        name_component2 = choice(self.nm2)
        name_component3 = choice(self.nm3)
        nMs = name_component + name_component2 + name_component3
        return testSwear(nMs)
