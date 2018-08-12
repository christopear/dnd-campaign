from random import choice

from people.Person import Person
from tools.swearCheck import testSwear


class Wilden(Person):
    nmMFf = ["Ban", "Bar", "Dal", "Dam", "Dun", "Dur", "Fas", "Fin", "Kan", "Kin", "Kor", "Lan", "Lim", "Lon", "Man",
             "Mar",
             "Mas", "Mid", "Mor", "Mur", "Nam", "Nor", "Rad", "Ran", "Ras", "Rod", "San", "Sin", "Tor", "Tum"]
    nmMFl = ["darras", "darris", "dommar", "donnir", "durrun", "farran", "fidden", "garron", "kammin", "karran",
             "lammir",
             "larrin", "mannor", "marden", "mennar", "mennor", "mindin", "mirron", "morrin", "murrin", "norren",
             "norten",
             "rammas", "sammas", "sannim", "sarrin", "sarris", "sorran", "tarrin", "torrin"]
    nmMSf = ["Barrun", "Burrin", "Darras", "Farran", "Farrin", "Fidden", "Garrin", "Harren", "Harrun", "Karrat",
             "Karren",
             "Ketten", "Korrin", "Larras", "Lommir", "Lorrin", "Marrad", "Mirren", "Mirrun", "Morrin", "Parran",
             "Purren",
             "Tarris", "Torren", "Torrim", "Turrus", "Venner", "Vunnar", "Zakkan", "Zarrak"]
    nmMSl = ["bar", "bor", "bun", "das", "din", "dun", "dur", "fas", "fum", "gar", "gun", "kas", "kin", "las", "lis",
             "mar",
             "mas", "min", "mur", "nas", "nim", "nor", "pan", "rak", "ras", "tor", "tur", "zad", "zim", "zor"]
    nmFF = ["Allin", "Ashin", "Bunn", "Dann", "Darn", "Diss", "Enn", "Eril", "Fenn", "Fert", "Firr", "Fiss", "Genn",
            "Grin",
            "Kalk", "Kenn", "Kers", "Krin", "Lerm", "Less", "Linn", "Lorr", "Minn", "Mirt", "Mist", "Nem", "Niss",
            "Shall",
            "Shan", "Shenn", "Tarr", "Taz", "Tell", "Tin", "Tirr", "Tris", "Wenn", "Zar", "Zaz", "Zell"]
    nmFL = ["ahai", "akei", "alin", "amai", "anai", "annar", "annas", "arris", "arrel", "arresh", "artish", "asha",
            "atish",
            "elbis", "embin", "enna", "ennash", "entah", "eris", "erla", "erlis", "imai", "imbel", "imei", "immesh",
            "inah",
            "inash", "inda", "inna", "innem", "irrah", "ishai", "issa", "itas", "onnes", "onteh", "orda", "oren",
            "oris",
            "orren"]

	def generate_feminine(self):
        name_component = choice(self.nmFF)
        name_component2 = choice(self.nmFL)
        nMs = name_component + name_component2
        return testSwear(nMs)

	def generate_masculine(self):
        i = choice(range(0, 2))
        if i == 0:
            name_component = choice(self.nmMFf)
            name_component2 = choice(self.nmMFl)
            nMs = name_component + name_component2
        else:
            name_component = choice(self.nmMSf)
            name_component2 = choice(self.nmMSl)
            nMs = name_component + name_component2

        return testSwear(nMs)
