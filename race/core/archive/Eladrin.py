from random import choice

from people.Person import Race


class Eladrin(Race):
    nm1 = ["Ara", "Aran", "Ber", "Bran", "Cor", "Cru", "Da", "Daye", "Elro", "Ere", "Far", "Fyla", "Gal", "Galin", "Ha",
           "Hor", "Im", "Ira", "Ja", "Jor", "Kru", "Kuo", "Lan", "Lic", "Mar", "Min", "Nal", "Nark", "Ola", "Otir", "Pae",
           "Pan", "Qua", "Quo", "Rel", "Riar", "Sarn", "Sove", "Tav", "Trin", "Uri", "Veth", "Vic", "Wal", "Wrug", "Xan",
           "Yan", "Yor", "Zen", "Zor"]
    nm2 = ["aris", "aster", "baver", "bin", "card", "corin", "dan", "darai", "dartis", "don", "emin", "erta", "fis", "fros",
           "geon", "grephor", "heros", "horn", "ikul", "iver", "kris", "kul", "lias", "liss", "mendi", "meral", "mil",
           "morn", "neiros", "nis", "okas", "oros", "peiros", "prath", "ratra", "reth", "rian", "rion", "sirak", "ster",
           "thas", "tihr", "torin", "urian", "uvir", "van", "vis", "wirn", "worn", "xeral", "xis", "ykos", "yth", "zeiros",
           "zion"]
    nm3 = ["Al", "An", "Anas", "Be", "Bri", "Cae", "Cyl", "Dris", "Dur", "Eil", "Ena", "Fae", "Fan", "Gru", "Gyl", "Hen",
           "Hyl", "Illa", "Ire", "Jar", "Jelen", "Kai", "Kora", "Les", "Lyv", "Mag", "Me", "Nai", "Neri", "Ol", "Ori", "Pi",
           "Prys", "Qi", "Que", "Ri", "Rol", "Sa", "Sha", "Thei", "Tri", "Ul", "Ura", "Va", "Vela", "Wes", "Wre", "Xyr",
           "Ylla", "Zen"]

    def race_check(self):
        pass

    nm4 = ["bis", "bynn", "cahne", "caryn", "celle", "cena", "diel", "dys", "faera", "fyra", "glyn", "grys", "hanna",
           "hyssa", "kiries", "kyrath", "lenae", "lenna", "lyn", "lynna", "meiv", "miris", "mynis", "nairra", "neth",
           "parys", "prana", "qirith", "qis", "raste", "rastra", "riele", "rynna", "sanna", "shana", "sys", "thaea", "tora",
           "trianna", "a", "viryn", "vyre", "wena", "wyse", "xana", "xis", "yana", "yeira", "zane", "zora"]

    def generate_feminine(self):
        name_component = choice(self.nm3)
        name_component2 = choice(self.nm4)
        nMs = name_component + name_component2
        return nMs

    def generate_masculine(self):
        name_component = choice(self.nm1)
        name_component2 = choice(self.nm2)
        nMs = name_component + name_component2
        return nMs
