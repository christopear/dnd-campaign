from random import choice

from people.Person import Person
from tools.swearCheck import testSwear


class StandardPerson(Person):
	def nameFem(self):
		name_component = choice(self.nm3)
		name_component2 = choice(self.nm4)
		nMs = name_component + name_component2
		return testSwear(nMs)

	def nameMas(self):
		name_component = choice(self.nm1)
		name_component2 = choice(self.nm2)
		nMs = name_component + name_component2
		return testSwear(nMs)


class Shardmind(StandardPerson):
	nm1 = ["Adu", "Ama", "Ani", "Ar", "Arsha", "Ashi", "Ashtu", "Bala", "Bara", "Basha", "Beles", "Delu", "Di", "Dura",
		   "Duru", "Enu", "Eri", "Eshu", "Hua", "Hun", "Il", "Ilu", "Ira", "Ish", "Ku", "Kua", "Kuba", "Lu", "Mani",
		   "Mara",
		   "Mashi", "Na", "Nara", "Nashi", "Nu", "Rua", "Run", "Sana", "Sari", "Selu", "Shir", "Suma", "Tab", "Tin",
		   "Tiru",
		   "Uba", "Uku", "Ura", "Ut", "Zaki"]
	nm2 = ["ba", "bam", "bani", "bu", "ha", "hara", "hu", "ka", "ku", "lazu", "lua", "mea", "nar", "nara", "naram",
		   "naru",
		   "nashtu", "ni", "niri", "nu", "nua", "pana", "ram", "ranu", "rashi", "raya", "ri", "rin", "runu", "shara",
		   "shari", "shi", "shti", "shtu", "shu", "sunu", "ta", "tana", "tani", "tari", "ti", "tira", "tiru", "tua",
		   "tum",
		   "wia", "ya", "yara", "yua", "zu"]

	def nameFem(self):
		pass


class Halfling(StandardPerson):
	nm1 = ["An", "Ar", "Bar", "Bel", "Con", "Cor", "Dan", "Dav", "El", "Er", "Fal", "Fin", "Flyn", "Gar", "Go", "Hal",
		   "Hor", "Ido", "Ira", "Jan", "Jo", "Kas", "Kor", "La", "Lin", "Mar", "Mer", "Ne", "Nor", "Ori", "Os", "Pan",
		   "Per", "Pim", "Quin", "Quo", "Ri", "Ric", "San", "Shar", "Tar", "Te", "Ul", "Uri", "Val", "Vin", "Wen",
		   "Wil",
		   "Xan", "Xo", "Yar", "Yen", "Zal", "Zen"]
	nm2 = ["ace", "amin", "bin", "bul", "dak", "dal", "der", "don", "emin", "eon", "fer", "fire", "gin", "hace", "horn",
		   "kas", "kin", "lan", "los", "min", "mo", "nad", "nan", "ner", "orin", "os", "pher", "pos", "ras", "ret",
		   "ric",
		   "rich", "rin", "ry", "ser", "sire", "ster", "ton", "tran", "umo", "ver", "vias", "von", "wan", "wrick",
		   "yas",
		   "yver", "zin", "zor", "zu"]
	nm3 = ["An", "Ari", "Bel", "Bre", "Cal", "Chen", "Dar", "Dia", "Ei", "Eo", "Eli", "Era", "Fay", "Fen", "Fro", "Gel",
		   "Gra", "Ha", "Hil", "Ida", "Isa", "Jay", "Jil", "Kel", "Kith", "Le", "Lid", "Mae", "Mal", "Mar", "Ne", "Ned",
		   "Odi", "Ora", "Pae", "Pru", "Qi", "Qu", "Ri", "Ros", "Sa", "Shae", "Syl", "Tham", "Ther", "Tryn", "Una",
		   "Uvi",
		   "Va", "Ver", "Wel", "Wi", "Xan", "Xi", "Yes", "Yo", "Zef", "Zen"]
	nm4 = ["alyn", "ara", "brix", "byn", "caryn", "cey", "da", "dove", "drey", "elle", "eni", "fice", "fira", "grace",
		   "gwen", "haly", "jen", "kath", "kis", "leigh", "la", "lie", "lile", "lienne", "lyse", "mia", "mita", "ne",
		   "na",
		   "ni", "nys", "ola", "ora", "phina", "prys", "rana", "ree", "ri", "ris", "sica", "sira", "sys", "tina",
		   "trix",
		   "ula", "vira", "vyre", "wyn", "wyse", "yola", "yra", "zana", "zira"]


class Halfelf(StandardPerson):
	nm1 = ["Al", "Aro", "Bar", "Bel", "Cor", "Cra", "Dav", "Dor", "Eir", "El", "Fal", "Fril", "Gaer", "Gra", "Hal",
		   "Hor",
		   "Ian", "Ilo", "Jam", "Kev", "Kri", "Leo", "Lor", "Mar", "Mei", "Nil", "Nor", "Ori", "Os", "Pan", "Pet",
		   "Quo",
		   "Raf", "Ri", "Sar", "Syl", "Tra", "Tyr", "Uan", "Ul", "Van", "Vic", "Wal", "Wil", "Xan", "Xav", "Yen", "Yor",
		   "Zan", "Zyl"]
	nm2 = ["avor", "ben", "borin", "coril", "craes", "deyr", "dithas", "elor", "enas", "faelor", "faerd", "finas",
		   "fyr",
		   "gotin", "gretor", "homin", "horn", "kas", "koris", "lamir", "lanann", "lumin", "minar", "morn", "nan",
		   "neak",
		   "neiros", "orin", "o", "parin", "phanis", "qarim", "qinor", "reak", "ril", "ros", "sariph", "staer", "torin",
		   "tumil", "valor", "voril", "warith", "word", "xian", "xiron", "yeras", "ynor", "zaphir", "zaren"]
	nm3 = ["Alu", "Aly", "Ar", "Bren", "Byn", "Car", "Co", "Dar", "Del", "El", "Eli", "Fae", "Fha", "Gal", "Gif",
		   "Haly",
		   "Ho", "Ile", "Iro", "Jen", "Jil", "Kri", "Kys", "Les", "Lora", "Ma", "Mar", "Mare", "Neri", "Nor", "Ol",
		   "Ophi",
		   "Phaye", "Pri", "Qi", "Que", "Rel", "Res", "Sael", "Saf", "Syl", "Ther", "Tyl", "Una", "Uri", "Ven", "Vyl",
		   "Win", "Wol", "Xil", "Xyr", "Yes", "Yll", "Zel", "Zin"]
	nm4 = ["aerys", "anys", "bellis", "bwynn", "cerys", "charis", "diane", "dove", "elor", "enyphe", "faen", "fine",
		   "galyn", "gwynn", "hana", "hophe", "kaen", "kilia", "lahne", "lynn", "mae", "malis", "mythe", "nalore",
		   "noa",
		   "nys", "ona", "phira", "pisys", "qarin", "qwyn", "rila", "rora", "seris", "stine", "sys", "thana", "theris",
		   "tihne", "trana", "viel", "vyre", "walyn", "waris", "xaris", "xipha", "yaries", "yra", "zenya", "zira"]


class Gnome(StandardPerson):
	nm1 = ["Al", "Ari", "Bil", "Bri", "Cal", "Cor", "Dav", "Dor", "Eni", "Er", "Far", "Fel", "Ga", "Gra", "His", "Hor",
		   "Ian", "Ipa", "Je", "Jor", "Kas", "Kel", "Lan", "Lo", "Man", "Mer", "Nes", "Ni", "Or", "Oru", "Pana", "Po",
		   "Qua", "Quo", "Ras", "Ron", "Sa", "Sal", "Sin", "Tan", "To", "Tra", "Um", "Uri", "Val", "Vor", "War", "Wil",
		   "Wre", "Xal", "Xo", "Ye", "Yos", "Zan", "Zil"]
	nm2 = ["bar", "ben", "bis", "corin", "cryn", "don", "dri", "fan", "fiz", "gim", "grim", "hik", "him", "ji", "jin",
		   "kas", "kur", "len", "lin", "min", "mop", "morn", "nan", "ner", "ni", "pip", "pos", "rick", "ros", "rug",
		   "ryn",
		   "ser", "ston", "tix", "tor", "ver", "vyn", "win", "wor", "xif", "xim", "ybar", "yur", "ziver", "zu"]
	nm3 = ["Alu", "Ari", "Ban", "Bree", "Car", "Cel", "Daphi", "Do", "Eili", "El", "Fae", "Fen", "Fol", "Gal", "Gren",
		   "Hel", "Hes", "Ina", "Iso", "Jel", "Jo", "Klo", "Kri", "Lil", "Lori", "Min", "My", "Ni", "Ny", "Oda", "Or",
		   "Phi", "Pri", "Qi", "Que", "Re", "Rosi", "Sa", "Sel", "Spi", "Ta", "Tifa", "Tri", "Ufe", "Uri", "Ven", "Vo",
		   "Wel", "Wro", "Xa", "Xyro", "Ylo", "Yo", "Zani", "Zin"]
	nm4 = ["bi", "bys", "celi", "ci", "dira", "dysa", "fi", "fyx", "gani", "gyra", "hana", "hani", "kasys", "kini",
		   "la",
		   "li", "lin", "lys", "mila", "miphi", "myn", "myra", "na", "niana", "noa", "nove", "phina", "pine", "qaryn",
		   "qys", "rhana", "roe", "sany", "ssa", "sys", "tina", "tra", "wyn", "wyse", "xi", "xis", "yaris", "yore",
		   "za",
		   "zyre"]


class Githzerai(StandardPerson):
	nm1 = ["Am", "Ar", "Ara", "Aza", "Bar", "Bra", "Bru", "Da", "Dar", "Dor", "Dra", "Dro", "Du", "Fa", "Far", "Fer",
		   "Gra",
		   "Gran", "Gre", "Gro", "Gru", "Hu", "Ka", "Kar", "Kha", "Kra", "Kro", "Ma", "Mu", "Na", "Nar", "Nu", "Ra",
		   "Ran",
		   "Rin", "Ru", "Sha", "Shra", "Sra", "Zra"]
	nm2 = ["d", "dak", "gh", "k", "kahr", "kar", "khar", "kk", "lag", "llak", "mag", "mak", "nag", "rag", "rak", "ram",
		   "rath", "rek", "rg", "rm", "rth", "ruk", "th", "tig", "zag", "zak", "zar", "zeg", "zirg", "zth"]
	nm3 = ["Ad", "Alm", "Arw", "Ash", "Dah", "Dhar", "Dolm", "Dran", "Ell", "Erzh", "Esz", "Ezh", "Grel", "Halm", "Han",
		   "Harn", "Heln", "Ihr", "Iln", "Imm", "Iz", "Kan", "Kharm", "Khaz", "Krez", "Laz", "Lez", "Lhash", "Magd",
		   "Marm",
		   "Nagr", "Nah", "Nalm", "Rasz", "Rez", "Sham", "Sharm", "Shund", "Um", "Uw"]
	nm4 = ["a", "ah", "aka", "al", "arah", "arin", "aya", "ayah", "eah", "eka", "el", "ela", "elna", "elya", "elzal",
		   "ena",
		   "enah", "era", "erah", "eya", "ihn", "ila", "ilzin", "in", "ina", "ira", "iza", "mina", "ya", "yara"]


class Eladrin(StandardPerson):
	nm1 = ["Ara", "Aran", "Ber", "Bran", "Cor", "Cru", "Da", "Daye", "Elro", "Ere", "Far", "Fyla", "Gal", "Galin", "Ha",
		   "Hor", "Im", "Ira", "Ja", "Jor", "Kru", "Kuo", "Lan", "Lic", "Mar", "Min", "Nal", "Nark", "Ola", "Otir",
		   "Pae",
		   "Pan", "Qua", "Quo", "Rel", "Riar", "Sarn", "Sove", "Tav", "Trin", "Uri", "Veth", "Vic", "Wal", "Wrug",
		   "Xan",
		   "Yan", "Yor", "Zen", "Zor"]
	nm2 = ["aris", "aster", "baver", "bin", "card", "corin", "dan", "darai", "dartis", "don", "emin", "erta", "fis",
		   "fros",
		   "geon", "grephor", "heros", "horn", "ikul", "iver", "kris", "kul", "lias", "liss", "mendi", "meral", "mil",
		   "morn", "neiros", "nis", "okas", "oros", "peiros", "prath", "ratra", "reth", "rian", "rion", "sirak", "ster",
		   "thas", "tihr", "torin", "urian", "uvir", "van", "vis", "wirn", "worn", "xeral", "xis", "ykos", "yth",
		   "zeiros",
		   "zion"]
	nm3 = ["Al", "An", "Anas", "Be", "Bri", "Cae", "Cyl", "Dris", "Dur", "Eil", "Ena", "Fae", "Fan", "Gru", "Gyl",
		   "Hen",
		   "Hyl", "Illa", "Ire", "Jar", "Jelen", "Kai", "Kora", "Les", "Lyv", "Mag", "Me", "Nai", "Neri", "Ol", "Ori",
		   "Pi",
		   "Prys", "Qi", "Que", "Ri", "Rol", "Sa", "Sha", "Thei", "Tri", "Ul", "Ura", "Va", "Vela", "Wes", "Wre", "Xyr",
		   "Ylla", "Zen"]
	nm4 = ["bis", "bynn", "cahne", "caryn", "celle", "cena", "diel", "dys", "faera", "fyra", "glyn", "grys", "hanna",
		   "hyssa", "kiries", "kyrath", "lenae", "lenna", "lyn", "lynna", "meiv", "miris", "mynis", "nairra", "neth",
		   "parys", "prana", "qirith", "qis", "raste", "rastra", "riele", "rynna", "sanna", "shana", "sys", "thaea",
		   "tora",
		   "trianna", "a", "viryn", "vyre", "wena", "wyse", "xana", "xis", "yana", "yeira", "zane", "zora"]


class Dwarf(StandardPerson):
	nm1 = ["Ad", "Am", "Arm", "Baer", "Daer", "Bal", "Ban", "Bar", "Bel", "Ben", "Ber", "Bhal", "Bhar", "Bhel", "Bram",
		   "Bran", "Brom", "Brum", "Bun", "Dal", "Dar", "Dol", "Dul", "Eb", "Em", "Erm", "Far", "Gal", "Gar", "Ger",
		   "Gim",
		   "Gral", "Gram", "Gran", "Grem", "Gren", "Gril", "Gry", "Gul", "Har", "Hjal", "Hjol", "Hjul", "Hor", "Hul",
		   "Hur",
		   "Kar", "Khar", "Kram", "Krom", "Krum", "Mag", "Mal", "Mel", "Mor", "Muir", "Mur", "Rag", "Ran", "Reg", "Rot",
		   "Thal", "Thar", "Thel", "Ther", "Tho", "Thor", "Thul", "Thur", "Thy", "Tor", "Ty", "Um", "Urm", "Von"]
	nm2 = ["adin", "bek", "brek", "dahr", "dain", "dal", "dan", "dar", "dek", "dir", "dohr", "dor", "drak", "dram",
		   "dren",
		   "drom", "drum", "drus", "duhr", "dur", "dus", "garn", "gram", "gran", "grim", "grom", "gron", "grum", "grun",
		   "gurn", "gus", "iggs", "kahm", "kam", "kohm", "kom", "kuhm", "kum", "kyl", "man", "mand", "mar", "mek",
		   "miir",
		   "min", "mir", "mond", "mor", "mun", "mund", "mur", "mus", "myl", "myr", "nam", "nar", "nik", "nir", "nom",
		   "num",
		   "nur", "nus", "nyl", "rak", "ram", "ren", "rig", "rigg", "rik", "rim", "rom", "ron", "rum", "rus", "ryl",
		   "tharm", "tharn", "thran", "thrum", "thrun"]
	nm3 = ["An", "Ar", "Baer", "Bar", "Bel", "Belle", "Bon", "Bonn", "Braen", "Bral", "Bralle", "Bran", "Bren", "Bret",
		   "Bril", "Brille", "Brol", "Bron", "Brul", "Bryl", "Brylle", "Bryn", "Bryt", "Byl", "Bylle", "Daer", "Dear",
		   "Dim", "Ed", "Ein", "El", "Gem", "Ger", "Gwan", "Gwen", "Gwin", "Gwyn", "Gym", "Ing", "Jen", "Jenn", "Jin",
		   "Jyn", "Kait", "Kar", "Kat", "Kath", "Ket", "Las", "Lass", "Les", "Less", "Lyes", "Lys", "Lyss", "Maer",
		   "Maev",
		   "Mar", "Mis", "Mist", "Myr", "Mys", "Myst", "Naer", "Nal", "Nas", "Nass", "Nes", "Nis", "Nys", "Raen", "Ran",
		   "Red", "Reyn", "Run", "Ryn", "Sar", "Sol", "Tas", "Taz", "Tis", "Tish", "Tiz", "Tor", "Tys", "Tysh"]
	nm4 = ["belle", "bera", "delle", "deth", "dielle", "dille", "dish", "dora", "dryn", "dyl", "giel", "glia", "glian",
		   "gwyn", "la", "leen", "leil", "len", "lin", "linn", "lyl", "lyn", "lynn", "ma", "mera", "mora", "mura",
		   "myl",
		   "myla", "nan", "nar", "nas", "nera", "nia", "nip", "nis", "niss", "nora", "nura", "nyl", "nys", "nyss", "ra",
		   "ras", "res", "ri", "ria", "rielle", "rin", "ris", "ros", "ryl", "ryn", "sael", "selle", "sora", "syl",
		   "thel",
		   "thiel", "tin", "tyn", "va", "van", "via", "vian", "waen", "win", "wyn", "wynn"]


class Elf(StandardPerson):
	nm1 = ["Ad", "Ae", "Bal", "Bei", "Car", "Cra", "Dae", "Dor", "El", "Ela", "Er", "Far", "Fen", "Gen", "Glyn", "Hei",
		   "Her", "Ian", "Ili", "Kea", "Kel", "Leo", "Lu", "Mira", "Mor", "Nae", "Nor", "Olo", "Oma", "Pa", "Per",
		   "Pet",
		   "Qi", "Qin", "Ralo", "Ro", "Sar", "Syl", "The", "Tra", "Ume", "Uri", "Va", "Vir", "Waes", "Wran", "Yel",
		   "Yin",
		   "Zin", "Zum"]
	nm2 = ["balar", "beros", "can", "ceran", "dan", "dithas", "faren", "fir", "geiros", "golor", "hice", "horn", "jeon",
		   "jor", "kas", "kian", "lamin", "lar", "len", "maer", "maris", "menor", "myar", "nan", "neiros", "nelis",
		   "norin",
		   "peiros", "petor", "qen", "quinal", "ran", "ren", "ric", "ris", "ro", "salor", "sandoral", "toris", "tumal",
		   "valur", "ven", "warin", "wraek", "xalim", "xidor", "yarus", "ydark", "zeiros", "zumin"]
	nm3 = ["Ad", "Ara", "Bi", "Bry", "Cai", "Chae", "Da", "Dae", "Eil", "En", "Fa", "Fae", "Gil", "Gre", "Hele", "Hola",
		   "Iar", "Ina", "Jo", "Key", "Kris", "Lia", "Lora", "Mag", "Mia", "Neri", "Ola", "Ori", "Phi", "Pres", "Qi",
		   "Qui",
		   "Rava", "Rey", "Sha", "Syl", "Tor", "Tris", "Ula", "Uri", "Val", "Ven", "Wyn", "Wysa", "Xil", "Xyr", "Yes",
		   "Ylla", "Zin", "Zyl"]
	nm4 = ["banise", "bella", "caryn", "cyne", "di", "dove", "fiel", "fina", "gella", "gwyn", "hana", "harice", "jyre",
		   "kalyn", "krana", "lana", "lee", "leth", "lynn", "moira", "mys", "na", "nala", "phine", "phyra", "qirelle",
		   "ra",
		   "ralei", "rel", "rie", "rieth", "rona", "rora", "roris", "satra", "stina", "sys", "thana", "thyra", "tris",
		   "is",
		   "vyre", "wenys", "wynn", "xina", "xisys", "ynore", "yra", "zana", "zorwyn"]
