import abc
from random import choice

from people.Person import Person
from people.Person import StandardPerson


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

	def race_check(self):
		pass


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

	def race_check(self):
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

	def race_check(self):
		pass


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

	def race_check(self):
		pass


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

	def race_check(self):
		pass


class Dragonborn(Person):
	nm1 = ["Ali", "Ar", "Ba", "Bal", "Bel", "Bha", "Bren", "Caer", "Calu", "Dur", "Do", "Dra", "Era", "Faer", "Fro",
		   "Gre",
		   "Ghe", "Gora", "He", "Hi", "Ior", "Jin", "Jar", "Kil", "Kriv", "Lor", "Lumi", "Mar", "Mor", "Med", "Nar",
		   "Nes",
		   "Na", "Oti", "Orla", "Pri", "Pa", "Qel", "Ravo", "Ras", "Rho", "Sa", "Sha", "Sul", "Taz", "To", "Trou",
		   "Udo",
		   "Uro", "Vor", "Vyu", "Vrak", "Wor", "Wu", "Wra", "Wul", "Xar", "Yor", "Zor", "Zra"]
	nm2 = ["barum", "bor", "broth", "ciar", "crath", "daar", "dhall", "dorim", "farn", "fras", "gar", "ghull", "grax",
		   "hadur", "hazar", "jhan", "jurn", "kax", "kris", "kul", "lasar", "lin", "mash", "morn", "naar", "prax",
		   "qiroth",
		   "qrin", "qull", "rakas", "rash", "rinn", "roth", "sashi", "seth", "skan", "trin", "turim", "ax", "vroth",
		   "vull",
		   "warum", "wunax", "xan", "xiros", "yax", "ythas", "zavur", "zire", "ziros"]
	nm3 = ["Ari", "A", "Bi", "Bel", "Cris", "Ca", "Drys", "Da", "Erli", "Esh", "Fae", "Fen", "Gur", "Gri", "Hin", "Ha",
		   "Irly", "Irie", "Jes", "Jo", "Ka", "Kel", "Ko", "Lilo", "Lora", "Mal", "Mi", "Na", "Nes", "Nys", "Ori", "O",
		   "Ophi", "Phi", "Per", "Qi", "Quil", "Rai", "Rashi", "So", "Su", "Tha", "Ther", "Uri", "Ushi", "Val", "Vyra",
		   "Welsi", "Wra", "Xy", "Xis", "Ya", "Yr", "Zen", "Zof"]
	nm4 = ["birith", "bis", "bith", "coria", "cys", "dalynn", "drish", "drith", "faeth", "fyire", "gil", "gissa",
		   "gwen",
		   "hime", "hymm", "karyn", "kira", "larys", "liann", "lyassa", "meila", "myse", "norae", "nys", "patys",
		   "pora",
		   "qorel", "qwen", "rann", "riel", "rina", "rinn", "rish", "rith", "saadi", "shann", "sira", "thibra", "thyra",
		   "vayla", "vyre", "vys", "wophyl", "wyn", "xiris", "xora", "yassa", "yries", "zita", "zys"]

	nm5 = ["", "", "", "", "c", "cl", "cr", "d", "dr", "f", "g", "k", "kl", "kr", "l", "m", "my", "n", "ny", "pr", "sh",
		   "t", "th", "v", "y"]
	nm6 = ["a", "e", "i", "a", "e", "i", "o", "u", "a", "e", "i", "a", "e", "i", "o", "u", "a", "e", "i", "a", "e", "i",
		   "o", "u", "aa", "ia", "ea", "ua", "uu"]
	nm7 = ["c", "cc", "ch", "lm", "lk", "lx", "ld", "lr", "ldr", "lt", "lth", "mb", "mm", "mp", "mph", "mr", "mt", "nk",
		   "nx", "nc", "p", "ph", "r", "rd", "rj", "rn", "rrh", "rth", "st", "tht", "x"]
	nm8 = ["c", "cm", "cn", "d", "j", "k", "km", "l", "n", "nd", "ndr", "nk", "nsht", "nth", "r", "s", "sht", "shkm",
		   "st",
		   "t", "th", "x"]
	nm9 = ["d", "j", "l", "ll", "m", "n", "nd", "rg", "r", "rr", "rd"]
	nm10 = ["c", "d", "k", "l", "n", "r", "s", "sh", "th"]

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

	def generate_surname(self):
		i = choice(range(0, 3))

		name_component = choice(self.nm5)
		name_component2 = choice(self.nm6)
		name_component3 = choice(self.nm7)
		name_component4 = choice(self.nm6)
		name_component5 = choice(self.nm10)
		while name_component3 == name_component or name_component3 == name_component5:
			name_component3 = choice(self.nm7)

		if i == 0:
			nSr = name_component + name_component2 + name_component3 + name_component4 + name_component5
		else:
			name_component6 = choice(self.nm6)
			name_component7 = choice(self.nm8)
			while name_component3 == name_component7 or name_component7 == name_component5:
				name_component7 = choice(self.nm8)

			if i == 1:
				nSr = name_component + name_component2 + name_component3 + name_component4 + name_component7 + name_component6 + name_component5
			else:
				name_component8 = choice(self.nm6)
				name_component9 = choice(self.nm9)
				while name_component9 == name_component7 or name_component9 == name_component5:
					name_component9 = choice(self.nm9)

				nSr = name_component + name_component2 + name_component3 + name_component4 + name_component7 + name_component6 + name_component9 + name_component8 + name_component5

		return nSr

	def race_check(self):
		pass


class HalfOrc(Person):
	nm1 = ["Ag", "Agg", "Ar", "Arn", "As", "At", "Atr", "B", "Bar", "Bel", "Bor", "Br", "Brak", "C", "Cr", "D", "Dor",
		   "Dr",
		   "Dur", "G", "Gal", "Gan", "Gar", "Gna", "Gor", "Got", "Gr", "Gram", "Grim", "Grom", "Grum", "Gul", "H",
		   "Hag",
		   "Han", "Har", "Hog", "Hon", "Hor", "Hun", "Hur", "K", "Kal", "Kam", "Kar", "Kel", "Kil", "Kom", "Kor", "Kra",
		   "Kru", "Kul", "Kur", "Lum", "M", "Mag", "Mahl", "Mak", "Mal", "Mar", "Mog", "Mok", "Mor", "Mug", "Muk",
		   "Mura",
		   "N", "Oggu", "Ogu", "Ok", "Oll", "Or", "Rek", "Ren", "Ron", "Rona", "S", "Sar", "Sor", "T", "Tan", "Th",
		   "Thar",
		   "Ther", "Thr", "Thur", "Trak", "Truk", "Ug", "Uk", "Ukr", "Ull", "Ur", "Urth", "Urtr", "Z", "Za", "Zar",
		   "Zas",
		   "Zav", "Zev", "Zor", "Zur", "Zus"]
	nm2 = ["a", "a", "a", "o", "o", "e", "i", "u", "u", "u"]
	nm3 = ["bak", "bar", "bark", "bash", "bur", "burk", "d", "dak", "dall", "dar", "dark", "dash", "dim", "dur", "durk",
		   "g", "gak", "gall", "gar", "gark", "gash", "glar", "gul", "gur", "m", "mak", "mar", "marsh", "mash", "mir",
		   "mur", "n", "nar", "nars", "nur", "rak", "rall", "rash", "rim", "rimm", "rk", "rsh", "rth", "ruk", "sk",
		   "tar",
		   "tir", "tur", "z", "zall", "zar", "zur"]
	nm4 = ["Al", "Ar", "Br", "Ek", "El", "Fal", "Fel", "Fol", "Ful", "G", "Gaj", "Gar", "Gij", "Gor", "Gr", "Gry",
		   "Gyn",
		   "Hur", "K", "Kar", "Kat", "Ker", "Ket", "Kir", "Kot", "Kur", "Kut", "Lag", "M", "Mer", "Mir", "Mor", "N",
		   "Ol",
		   "Oot", "Puy", "R", "Rah", "Rahk", "Ras", "Rash", "Raw", "Roh", "Rohk", "S", "Sam", "San", "Sem", "Sen", "Sh",
		   "Shay", "Sin", "Sum", "Sun", "Tam", "Tem", "Tu", "Tum", "Ub", "Um", "Ur", "Van", "Zan", "Zen", "Zon", "Zun"]
	nm5 = ["a", "a", "o", "o", "e", "i", "i", "u"]
	nm6 = ["d", "da", "dar", "dur", "g", "gar", "gh", "gri", "gu", "sh", "sha", "shi", "gum", "gume", "gur", "ki",
		   "mar",
		   "mi", "mira", "me", "mur", "ne", "ner", "nir", "nar", "nchu", "ni", "nur", "ral", "rel", "ri", "rook", "ti",
		   "tah", "tir", "tar", "tur", "war", "z", "zar", "zara", "zi", "zur", "zura", "zira"]

	def generate_feminine(self):
		name_component = choice(self.nm4)
		name_component2 = choice(self.nm5)
		name_component3 = choice(self.nm6)
		nMs = name_component + name_component2 + name_component3
		return nMs

	def generate_masculine(self):
		name_component = choice(self.nm1)
		name_component2 = choice(self.nm2)
		name_component3 = choice(self.nm3)
		nMs = name_component + name_component2 + name_component3
		return nMs

	def race_check(self):
		pass


class Tiefling(Person):
	nm1 = ["Aet", "Ak", "Am", "Aran", "And", "Ar", "Ark", "Bar", "Car", "Cas", "Dam", "Dhar", "Eb", "Ek", "Er", "Gar",
		   "Gu",
		   "Gue", "Hor", "Ia", "Ka", "Kai", "Kar", "Kil", "Kos", "Ky", "Loke", "Mal", "Male", "Mav", "Me", "Mor",
		   "Neph",
		   "Oz", "Ral", "Re", "Rol", "Sal", "Sha", "Sir", "Ska", "The", "Thy", "Thyne", "Ur", "Uri", "Val", "Xar",
		   "Zar",
		   "Zer", "Zher", "Zor"]
	nm2 = ["adius", "akas", "akos", "char", "cis", "cius", "dos", "emon", "ichar", "il", "ilius", "ira", "lech", "lius",
		   "lyre", "marir", "menos", "meros", "mir", "mong", "mos", "mus", "non", "rai", "rakas", "rakir", "reus",
		   "rias",
		   "ris", "rius", "ron", "ros", "rus", "rut", "shoon", "thor", "thos", "thus", "us", "venom", "vir", "vius",
		   "xes",
		   "xik", "xikas", "xire", "xius", "xus", "zer", "zire"]
	nm3 = ["Achievement", "Adventure", "Aid", "Anguish", "Art", "Ashes", "Atonement", "Awe", "Bliss", "Bright",
		   "Carrion",
		   "Chant", "Cheer", "Cherish", "Closed", "Comfort", "Compassion", "Confidence", "Content", "Courage",
		   "Cunning",
		   "Darkness", "Deceit", "Delight", "Desire", "Despair", "Devotion", "Dexterity", "Different", "Dread",
		   "Ecstasy",
		   "End", "Enduring", "Essential", "Esteem", "Eternal", "Euphoria", "Exceptional", "Exciting", "Expert",
		   "Expertise", "Expressive", "Extreme", "Faith", "Fear", "Flawed", "Free", "Freedom", "Fresh", "Gentle",
		   "Gladness", "Glee", "Gloom", "Happiness", "Happy", "Harmony", "Hatred", "Hero", "Hope", "Hunt", "Hymn",
		   "Ideal",
		   "Immortal", "Innovation", "Interesting", "Journey", "Joy", "Laughter", "Life", "Light", "Love", "Loyal",
		   "Mantra", "Master", "Mastery", "Misery", "Music", "Normal", "Nowhere", "Odd", "Open", "Optimal", "Panic",
		   "Perfect", "Piety", "Pleasure", "Poetry", "Possession", "Promise", "Psalm", "Pure", "Quest", "Random",
		   "Rare",
		   "Recovery", "Redemption", "Regular", "Relentless", "Respect", "Reverence", "Sadness", "Sanctity", "Silence",
		   "Skilled", "Sly", "Song", "Sorrow", "Suffering", "Terror", "Timeless", "Torment", "Trickery", "Trouble",
		   "Trust",
		   "Truth", "Uncommon", "Unlocked", "Void", "Voyage", "Weary", "Winning", "Woe"]
	nm4 = ["Af", "Agne", "Ani", "Ara", "Ari", "Aria", "Bel", "Bri", "Cre", "Da", "Di", "Dim", "Dor", "Ea", "Fri", "Gri",
		   "His", "In", "Ini", "Kal", "Le", "Lev", "Lil", "Ma", "Mar", "Mis", "Mith", "Na", "Nat", "Ne", "Neth", "Nith",
		   "Ori", "Pes", "Phe", "Qu", "Ri", "Ro", "Sa", "Sar", "Seiri", "Sha", "Val", "Vel", "Ya", "Yora", "Yu", "Za",
		   "Zai", "Ze"]
	nm5 = ["bis", "borys", "cria", "cyra", "dani", "doris", "faris", "firith", "goria", "grea", "hala", "hiri", "karia",
		   "ki", "laia", "lia", "lies", "lista", "lith", "loth", "lypsis", "lyvia", "maia", "meia", "mine", "narei",
		   "nirith", "nise", "phi", "pione", "punith", "qine", "rali", "rissa", "seis", "solis", "spira", "tari",
		   "tish",
		   "uphis", "i", "vine", "wala", "wure", "xibis", "xori", "yis", "yola", "za", "zes"]

	def generate_feminine(self):
		i = choice(range(0, 2))
		if i == 0:
			name_component = choice(self.nm4)
			name_component2 = choice(self.nm5)
			nMs = name_component + name_component2
		else:
			name_component = choice(self.nm3)
			nMs = name_component
		return nMs

	def generate_masculine(self):
		i = choice(range(0, 2))
		if i == 0:
			name_component = choice(self.nm1)
			name_component2 = choice(self.nm2)
			nMs = name_component + name_component2
		else:
			name_component = choice(self.nm3)
			nMs = name_component
		return nMs

	def race_check(self):
		pass


class Human(Person, abc.ABC):
	# surname
	nm21 = ["Axe", "Glow", "Blade", "Blood", "Bone", "Cloud", "Crag", "Crest", "Doom", "Dream", "Coven", "Elf", "Fern",
			"Feather", "Fire", "Fist", "Flame", "Forest", "Hammer", "Heart", "Hell", "Leaf", "Light", "Moon", "Rage",
			"River", "Rock", "Shade", "Shadow", "Shield", "Snow", "Spirit", "Star", "Steel", "Stone", "Swift", "Tree",
			"Whisper", "Wind", "Wolf", "Wood", "Gloom", "Glory", "Orb", "Ash", "Blaze", "Amber", "Autumn", "Barley",
			"Battle", "Bear", "Black", "Blue", "Boulder", "Bright", "Bronze", "Burning", "Cask", "Chest", "Cinder",
			"Clan",
			"Claw", "Clear", "Cliff", "Cold", "Common", "Crystal", "Dark", "Dawn", "Day", "Dead", "Death", "Deep",
			"Dew",
			"Dirge", "Distant", "Down", "Dragon", "Dusk", "Dust", "Eagle", "Earth", "Ember", "Even", "Far", "Flat",
			"Flint",
			"Fog", "Fore", "Four", "Free", "Frost", "Frozen", "Full", "Fuse", "Gold", "Horse", "Gore", "Grand", "Gray",
			"Grass", "Great", "Green", "Grizzly", "Hallow", "Hallowed", "Hard", "Hawk", "Haze", "Heavy", "Haven",
			"High",
			"Hill", "Holy", "Honor", "Forest", "Humble", "Hydra", "Ice", "Iron", "Keen", "Laughing", "Lightning",
			"Lion",
			"Lone", "Long", "Low", "Luna", "Marble", "Meadow", "Mild", "Mirth", "Mist", "Molten", "Monster", "Morning",
			"Moss", "Mountain", "Moon", "Mourn", "Mourning", "Night", "Noble", "Nose", "Oat", "Ocean", "Pale", "Peace",
			"Phoenix", "Pine", "Plain", "Pride", "Proud", "Pyre", "Rain", "Rapid", "Raven", "Red", "Regal", "Rich",
			"Rose",
			"Rough", "Rumble", "Rune", "Sacred", "Sage", "Saur", "Sea", "Serpent", "Sharp", "Silent", "Silver",
			"Simple",
			"Single", "Skull", "Sky", "Slate", "Smart", "Snake", "Soft", "Solid", "Spider", "Spring", "Stag", "Star",
			"Stern", "Still", "Storm", "Stout", "Strong", "Summer", "Sun", "Tall", "Three", "Thunder", "Titan", "True",
			"Truth", "Marsh", "Tusk", "Twilight", "Two", "Void", "War", "Wheat", "Whit", "White", "Wild", "Winter",
			"Wise",
			"Wyvern", "Young", "Alpen", "Crest", "Crow", "Fallen", "Farrow", "Haven", "Master", "Nether", "Nickle",
			"Raven",
			"River", "Stone", "Tarren", "Terra", "Water", "Willow", "Wooden"]
	nm22 = ["axe", "glow", "beam", "blade", "blood", "bone", "cloud", "dane", "crag", "crest", "doom", "dream",
			"feather",
			"fire", "fist", "flame", "forest", "hammer", "heart", "hell", "leaf", "light", "moon", "rage", "river",
			"rock",
			"shade", "claw", "shadow", "shield", "snow", "spirit", "star", "steel", "stone", "swift", "tree", "whisper",
			"wind", "wolf", "wood", "gloom", "glory", "orb", "ash", "blaze", "arm", "arrow", "bane", "bash", "basher",
			"beard", "belly", "bend", "bender", "binder", "bleeder", "blight", "bloom", "blossom", "blower", "glade",
			"bluff", "bough", "bow", "brace", "braid", "branch", "brand", "breaker", "breath", "breeze", "brew",
			"bringer",
			"brook", "brow", "caller", "chaser", "reaper", "chewer", "cleaver", "creek", "crusher", "cut", "cutter",
			"dancer", "dew", "down", "draft", "dreamer", "drifter", "dust", "eye", "eyes", "fall", "fang", "flare",
			"flaw",
			"flayer", "flow", "follower", "flower", "force", "forge", "fury", "gaze", "gazer", "gem", "gleam", "glide",
			"grain", "grip", "grove", "guard", "gust", "hair", "hand", "helm", "hide", "horn", "hunter", "jumper",
			"keep",
			"keeper", "killer", "lance", "lash", "less", "mane", "mantle", "mark", "maul", "maw", "might", "more",
			"mourn",
			"oak", "ore", "peak", "pelt", "pike", "punch", "reaver", "rider", "ridge", "ripper", "roar", "run",
			"runner",
			"scar", "scream", "scribe", "seeker", "shaper", "shard", "shot", "shout", "singer", "sky", "slayer",
			"snarl",
			"snout", "soar", "song", "sorrow", "spark", "spear", "spell", "spire", "splitter", "sprinter", "stalker",
			"steam", "stream", "strength", "stride", "strider", "strike", "striker", "sun", "surge", "sword", "sworn",
			"tail", "taker", "talon", "thorn", "tide", "toe", "track", "trap", "trapper", "vale", "valor", "vigor",
			"walker", "ward", "watcher", "water", "weaver", "whirl", "whisk", "winds", "wing", "woods", "wound",
			"brooke",
			"fall", "fallow", "horn", "root", "shine", "swallow", "thorne", "willow", "wood"]

	# masculine
	nm83 = ["Delmon", "Karcsi", "Quesnel", "Aaron", "Abdiel", "Abdullah", "Abel", "Abelard", "Abilo", "Abraham",
			"Abram",
			"Acel", "Achille", "Achilles", "Achilleus", "Achim", "Achmed", "Ackerley", "Ackley", "Acton", "Adalard",
			"Adalbero", "Adalbert", "Adalbrecht", "Adalwine", "Adam", "Adan", "Addi", "Addisen", "Addison", "Adelard",
			"Adelbert", "Adelfo", "Aden", "Adger", "Adhelard", "Adi", "Adison", "Aditya", "Adolf", "Adolfo", "Adolph",
			"Adonai", "Adonija", "Adonis", "Adray", "Adrian", "Adrianus", "Adriel", "Adrien", "Advent", "Ageline",
			"Agrican", "Agron", "Agustin", "Ahmad", "Ahmed", "Aidan", "Aiden", "Aiken", "Ailen", "Akim", "Alain",
			"Alan",
			"Albaric", "Albero", "Albert", "Alberto", "Albin", "Albrecht", "Alcot", "Alcott", "Alden", "Alder", "Aldo",
			"Aldred", "Aldren", "Aldrich", "Aldrick", "Aldridge", "Aldrych", "Aldwin", "Aldwyn", "Alec", "Alejandro",
			"Aleron", "Alessandro", "Alessio", "Alex", "Alexander", "Alexandre", "Alexandro", "Alexei", "Alexis",
			"Alexzander", "Alf", "Alfie", "Alfons", "Alfonse", "Alfonso", "Alfred", "Alfredo", "Alfric", "Alfrid",
			"Algar",
			"Alger", "Algernon", "Algrenon", "Ali", "Alijah", "Alke", "Alkuin", "Alkwin", "Allan", "Allard", "Allen",
			"Allie", "Allon", "Allston", "All", "Aloin", "Alois", "Aloisius", "Alon", "Alonso", "Alonzo", "Aloys",
			"Alphons", "Alphonse", "Alphonso", "Alphonsus", "Alric", "Altfried", "Altman", "Alton", "Aluin", "Alvan",
			"Alo",
			"Alvertos", "Alvin", "Alvis", "Alvord", "Alvyn", "Alwin", "Alwyn", "Amadeo", "Amadeus", "Amari", "Amarion",
			"Amaud", "Amaury", "Ambert", "Amel", "Amerigo", "Amery", "Ames", "Amey", "Amir", "Ammon", "Amo", "Amory",
			"Amos", "Amou", "Amoux", "Amsden", "Anatol", "Anatole", "Anaxagoras", "Anaximander", "Ancel", "Ancil",
			"Anderl",
			"Anderson", "Andor", "Andre", "Andrea", "Andreas", "Andrei", "Andres", "Andrew", "Andrey", "Andrick",
			"Andrijan", "Andrin", "Andy", "Angel", "Angelico", "Angelino", "Angelo", "Angelus", "Angus", "Anno", "Anse",
			"Ansel", "Ansell", "Anselm", "Anselme", "Ansgar", "Anshelm", "Ansko", "Ansley", "Answald", "Anthony",
			"Antoine",
			"Anton", "Antonio", "Antonius", "Antony", "Antwan", "Aramis", "Arber", "Arcadius", "Arch", "Archaimbaud",
			"Archambault", "Archard", "Archenhaud", "Archer", "Archerd", "Archibald", "Archie", "Archimbald", "Archy",
			"Arden", "Arendt", "Ari", "Arian", "Aribert", "Ariel", "Arjen", "Arjun", "Arledge", "Arley", "Arlo",
			"Armand",
			"Armande", "Armando", "Armani", "Armin", "Arminius", "Armond", "Armstrong", "Arnald", "Arnaldo", "Arnall",
			"Arnatt", "Arnaud", "Aname_componentell", "Aname_componentt", "Arne", "Arnet", "Arney", "Arnhold", "Arnie",
			"Arnim", "Arno", "Arnold", "Arnott", "Aron", "Arthur", "Artur", "Arturo", "Artus", "Arundel", "Arvie",
			"Arvin",
			"Arvis", "Arvon", "Arwin", "Aryan", "Asa", "Ascelin", "Asher", "Ashley", "Ashton", "Asterios", "Athelstan",
			"Attila", "Auberon", "Aubert", "Aubin", "Aubrey", "Aubry", "Audric", "Audwin", "August", "Augustin",
			"Augustinus", "Augusto", "Augustus", "Auhert", "Aurélien", "Aurel", "Aurelian", "Aurelianus", "Aurelius",
			"Auriville", "Austen", "Austin", "Austyn", "Avenall", "Aveneil", "Avenelle", "Avent", "Averill", "Avery",
			"Awarnach", "Axel", "Ayden", "Baby", "Bailey", "Baldemar", "Baldo", "Baldric", "Balduin", "Baldus",
			"Baldwin",
			"Balko", "Ballard", "Balthasar", "Balthassar", "Bancroft", "Baptist", "Baptiste", "Barclay", "Barden",
			"Barklay", "Barkley", "Barks", "Barksdale", "Barnabas", "Barnard", "Barnet", "Barnett", "Baron", "Barr",
			"Barret", "Barrett", "Barrie", "Barron", "Barry", "Bart", "Barthel", "Bartholomaeus", "Bartlett", "Bartram",
			"Baruch", "Bas", "Basil", "Bast", "Bastian", "Bastle", "Battist", "Battista", "Baudouin", "Baudric", "Bax",
			"Baxter", "Bay", "Bayard", "Baylen", "Bayley", "Beacher", "Beal", "Beale", "Beall", "Beaman", "Beardsley",
			"Beau", "Beaufort", "Beauregard", "Beauvais", "Bede", "Beldon", "Bell", "Bellamy", "Ben", "Bendix",
			"Benedict",
			"Benedikt", "Benediktus", "Bengt", "Beni", "Benito", "Benjamin", "Benjamino", "Bennet", "Bennett", "Benno",
			"Benny", "Beno", "Bente", "Bentley", "Beppo", "Berenger", "Bergen", "Bergess", "Berit", "Berkeley",
			"Berkley",
			"Bernard", "Bernardo", "Bename_component", "Berne", "Bernhard", "Bernhardt", "Bernie", "Bernt", "Berny",
			"Bert",
			"Berthold", "Berthoud", "Berti", "Bertie", "Bertold", "Bertolt", "Berton", "Bertram", "Bertran", "Bertrand",
			"Berty", "Bevis", "Bilal", "Billy", "Bing", "Birch", "Björn", "Bjarne", "Bjorn", "Blade", "Blaine", "Blais",
			"Blaisdell", "Blaise", "Blaize", "Blake", "Blase", "Blayze", "Blaze", "Bo", "Bob", "Bobby", "Bobby-Jo",
			"Bodil",
			"Bodin", "Bodo", "Bogart", "Bogdan", "Bolton", "Bond", "Bonham", "Boniface", "Bonifacius", "Bonifatius",
			"Bonifaz", "Booker", "Boone", "Booth", "Boothe", "Bordan", "Borden", "Boris", "Borris", "Bosco", "Bosse",
			"Bosso", "Both", "Botho", "Boto", "Boyce", "Bozo", "Brad", "Braden", "Bradford", "Bradley", "Bradly",
			"Bradney",
			"Brady", "Bradyn", "Braeden", "Braedon", "Braid", "Braiden", "Bran", "Brand", "Branden", "Brandon",
			"Branford",
			"Brant", "Braulio", "Braxton", "Bray", "Brayan", "Brayden", "Braydon", "Brayton", "Brecht", "Brendan",
			"Brenden", "Brendon", "Brennan", "Brennen", "Brent", "Brentan", "Brenton", "Bret", "Brett", "Brewster",
			"Brian",
			"Brice", "Brigham", "Brinley", "Brisco", "Brock", "Brocton", "Brod", "Broderick", "Brodie", "Brody",
			"Bromley",
			"Bromwell", "Bromwood", "Bronson", "Bronwen", "Bronwyn", "Brook", "Brooks", "Bruce", "Brunelle", "Bruno",
			"Bryan", "Bryant", "Bryce", "Brycen", "Brys", "Bryson", "Buckley", "Bud", "Buiron", "Burcet", "Burdett",
			"Burdette", "Burel", "Burg", "Burgess", "Burghard", "Burkhard", "Burkhart", "Burley", "Burne", "Burns",
			"Burt",
			"Burton", "Buster", "Byrne", "Byron", "Cade", "Caden", "Cadwell", "Cael", "Caiden", "Cain", "Caio", "Cal",
			"Calder", "Caldwell", "Cale", "Caleb", "Calhoun", "Calliste", "Callixtus", "Calvert", "Calvin", "Camden",
			"Cameron", "Camren", "Camron", "Carden", "Carel", "Carl", "Carleton", "Carlisle", "Carlo", "Carlos",
			"Carlton",
			"Carlyle", "Carol", "Carolos", "Carolus", "Carrington", "Carson", "Carsten", "Carter", "Carvell", "Carver",
			"Casey", "Casimir", "Cason", "Caspar", "Castor", "Catcher", "Caulder", "Cayden", "Cearbhall", "Cecco",
			"Cedric",
			"Celestino", "Cerdic", "Cesar", "Chad", "Chadwick", "Chaim", "Chance", "Chandler", "Chane", "Chaney",
			"Chanler",
			"Channing", "Chapin", "Chapman", "Chappel", "Chappell", "Charles", "Charley", "Charlie", "Charlot",
			"Charlton",
			"Charly", "Chase", "Chaunce", "Chauncey", "Chauncy", "Chayne", "Chaz", "Cheney", "Cheval", "Chevalier",
			"Chevell", "Chevy", "Cheyne", "Chilton", "Chip", "Choncey", "Chrestien", "Chris", "Christian", "Christien",
			"Christinus", "Christofor", "Christoph", "Christophe", "Christopher", "Christopherus", "Chuck", "Claas",
			"Claiborne", "Clarence", "Clark", "Claudde", "Claude", "Claudio", "Claudius", "Claus", "Clay", "Clayton",
			"Cleavon", "Clemens", "Clement", "Cleopas", "Cleve", "Cleveland", "Cliff", "Clifford", "Clifton", "Clint",
			"Clinton", "Clive", "Clovis", "Coby", "Cody", "Cohen", "Colan", "Colbert", "Colbey", "Colborn", "Colby",
			"Cole",
			"Coleman", "Colin", "Coljar", "Collin", "Collins", "Colt", "Colten", "Colter", "Colton", "Colyn", "Con",
			"Conner", "Conni", "Connie", "Connor", "Conny", "Conor", "Conrad", "Constantin", "Constantinus", "Cooper",
			"Copper", "Corben", "Corbett", "Corbin", "Corbinian", "Corby", "Corbyn", "Cordalles", "Cordell", "Corey",
			"Corin", "Cornelio", "Cornelius", "Cort", "Cortez", "Cortland", "Corvin", "Cory", "Court", "Courtenay",
			"Courtland", "Courtnay", "Courtney", "Coyan", "Coyne", "Craig", "Crawford", "Creighton", "Cretien",
			"Cristian",
			"Cristobal", "Cristopher", "Cromwell", "Cruz", "Cullen", "Curcio", "Currier", "Curt", "Curtice", "Curtis",
			"Curtiss", "Cynric", "Cyrano", "Cyrill", "Cyrillus", "Cyrus", "D'Arcy", "D'anton", "D'arcy", "Dabbert",
			"Dace",
			"Dacey", "Dacian", "Dag", "Dagobert", "Daine", "Dakota", "Dale", "Dallas", "Dallin", "Dalton", "Damian",
			"Damiano", "Damien", "Damion", "Damon", "Dan", "Dandelion", "Dandre", "Dane", "Dangelo", "Daniel", "Danilo",
			"Danniell", "Danny", "Dante", "Danton", "Daquan", "Darcel", "Darcell", "Darcio", "Darcy", "Dareau", "Darek",
			"Darian", "Dariel", "Dariell", "Darien", "Darin", "Dario", "Darion", "Darius", "Darko", "Darnell", "Darrel",
			"Darrell", "Darren", "Darrin", "Darrion", "Darrius", "Darroll", "Darryl", "Darryll", "Dartagnan", "Darvell",
			"Darwin", "Darwyn", "Daryl", "Daryll", "Dash", "Dashawn", "Dashiell", "Dave", "Davet", "David", "Davin",
			"Davion", "Davis", "Davon", "Davy", "Dawson", "Dax", "Dayadi", "Dayne", "Dayton", "Dean", "Dean Deandre",
			"Deangelo", "Declan", "Dedrick", "Del", "Delaine", "Delancy", "Delane", "Delaney", "Delano", "Delmar",
			"Delmer",
			"Delmont", "Delmore", "Delray", "Delrick", "Delrico", "Delron", "Delroy", "Demarcus", "Demetrius",
			"Dempster",
			"Denis", "Deniz", "Dennet", "Dennis", "Denton", "Denver", "Denys", "Denzel", "Deon", "Deonte", "Derck",
			"Dereck", "Derek", "Derell", "Derick", "Derik", "Derk", "Derrall", "Derrek", "Derrell", "Derrick", "Derrik",
			"Derrill", "Derry", "Derwood", "Deryck", "Deryk", "Deshaun", "Deshawn", "Desmond", "Desmund", "Destan",
			"Destin", "Deston", "Destrey", "Destrie", "Destry", "Detlef", "Detlev", "Devan", "Devante", "Deven",
			"Deveral",
			"Devere", "Devereau", "Devereaux", "Deverel", "Deverell", "Deverick", "Devery", "Devin", "Devon", "Devonte",
			"Devry", "Devyn", "Dexter", "Diandre", "Dicken", "Dickens", "Dickenson", "Dickinson", "Didier", "Diederich",
			"Diedrich", "Diego", "Dieter", "Diether", "Dietmar", "Dietrich", "Digby", "Dilan", "Dillan", "Dillen",
			"Dillon",
			"Dimitri", "Dimitrij", "Dion", "Diondre", "Dionte", "Dirk", "Ditmar", "Dittmar", "Dix", "Dixie", "Dixon",
			"Dob",
			"Dobbs", "Dolf", "Dolph", "Domenic", "Domenico", "Domian", "Domingo", "Dominic", "Dominick", "Dominik",
			"Dominikus", "Dominique", "Don", "Donald", "Donat", "Donatello", "Donatien", "Donato", "Donatus", "Donavan",
			"Dondre", "Donny", "Donovan", "Dontae", "Donte", "Dorian", "Dorkas", "Dorset", "Dorsey", "Douglas", "Dover",
			"Doyle", "Doyt", "Dragan", "Drago", "Drake", "Draven", "Drew", "Dru", "Duane", "Dudley", "Dudly", "Dumont",
			"Duncan", "Dunstan", "Duran", "Durand", "Durango", "Durant", "Durante", "Dureau", "Duron", "Durrant",
			"Durwald",
			"Durward", "Durwin", "Durwood", "Dustin", "Duston", "Dusty", "Dustyn", "Duval", "Dwayne", "Dwenn",
			"Dwennon",
			"Dwight", "Dwighte", "Dwite", "Dwyght", "Dwyghte", "Dwyte", "Dylan", "Dylon", "Ean", "Earl", "Easton",
			"Eaton",
			"Ebbo", "Eberhard", "Eckart", "Eckbert", "Eckehart", "Ed", "Eddie", "Eddy", "Ede", "Edel", "Edelhart",
			"Edgar",
			"Edgard", "Edgardo", "Edmar", "Edmon", "Edmond", "Edmund", "Edmundo", "Edo", "Edsel", "Eduard", "Eduardo",
			"Edd", "Edward", "Edwardo", "Edwards", "Edwardson", "Edwin", "Efraim", "Efrain", "Efrem", "Efren", "Egan",
			"Egbert", "Egbrecht", "Egerton", "Egidius", "Egnatius", "Egon", "Ehrhard", "Eicren", "Eike", "Ekbrecht",
			"Elbert", "Elbridge", "Elden", "Elder", "Eldon", "Eldridge", "Eleasar", "Eleazar", "Elery", "Elfred", "Eli",
			"Elia", "Elian", "Elias", "Eliezer", "Elija", "Elijah", "Eliot", "Eliott", "Eliseo", "Elisha", "Ellerey",
			"Ellery", "Elliot", "Elliott", "Ellis", "Elman", "Elmar", "Elmer", "Elmo", "Elmore", "Elon", "Eloy",
			"Elric",
			"Elroy", "Elten", "Elton", "Elvin", "Elvis", "Emanuel", "Emersen", "Emerson", "Emery", "Emil", "Emile",
			"Emiliano", "Emilio", "Emlyn", "Emmanuel", "Emmerich", "Emmerson", "Emmery", "Emmett", "Emmyrson", "Emory",
			"Emyrson", "Endrik", "Enes", "Engelbert", "Engelbrecht", "Englebert", "Ennio", "Enno", "Enrico", "Enrique",
			"Enzio", "Ephraim", "Eppie", "Eppo", "Erhard", "Eric", "Erich", "Erick", "Erik", "Eriq", "Ermin", "Ernest",
			"Ernesto", "Ernst", "Errol", "Erskine", "Erwin", "Esau", "Escott", "Esmond", "Esmund", "Esra", "Esteban",
			"Estevan", "Ethan", "Ethelbert", "Ethelred", "Ethen", "Etienne", "Eufemio", "Eugen", "Eugene", "Euphemius",
			"Evan", "Everett", "Ewald", "Ewart", "Ewing", "Eyvind", "Ezechiel", "Ezekiel", "Ezequiel", "Ezra", "Fabian",
			"Fabiano", "Fabianus", "Fabien", "Fabio", "Fabius", "Fairfax", "Fairleigh", "Fairley", "Falk", "Falko",
			"Farald", "Faralt", "Faramond", "Farand", "Farant", "Farland", "Farley", "Farly", "Farold", "Farolt",
			"Farrand",
			"Farrell", "Faruk", "Faust", "Faustino", "Faustinus", "Fausto", "Faustus", "Federico", "Federigo", "Fedor",
			"Felipe", "Felix", "Felizian", "Ferd", "Ferdel", "Ferdi", "Ferdie", "Ferdinand", "Ferdinando", "Ferdy",
			"Fernand", "Fernando", "Ferrand", "Fester", "Fidel", "Fidelio", "Fidelis", "Fidelius", "Fielding", "Fiete",
			"Filip", "Filippo", "Filiz", "Finn", "Fitz", "Fleming", "Flemming", "Fletcher", "Florens", "Florentin",
			"Florentinus", "Florentus", "Florenz", "Florestan", "Flori", "Florian", "Florianus", "Floridus", "Florin",
			"Floris", "Florus", "Floyd", "Flurin", "Folker", "Folkher", "Folkmar", "Fontaine", "Fontane", "Fontayne",
			"Fonteyne", "Forbes", "Ford", "Forrest", "Fortun", "Fortune", "Francesco", "Francis", "Francisco",
			"Franciscus",
			"Francois", "Franek", "Frank", "Franke", "Frankie", "Franklin", "Franko", "Franky", "Frantisek", "Franz",
			"Franziskus", "Fred", "Freddie", "Freddy", "Frederic", "Frederick", "Fredi", "Fredrick", "Free",
			"Freidhelm",
			"Freman", "Fremont", "Fridericus", "Fridolin", "Friedel", "Frieder", "Friedl", "Friedrich", "Frithjof",
			"Fritjof", "Fritz", "Fulbert", "Fulbright", "Fuller", "Fulton", "Fynn", "Görkem", "Günter", "Günther",
			"Gabor",
			"Gabriel", "Gabriele", "Gabriello", "Gabrio", "Gace", "Gael", "Gaetan", "Gage", "Gaige", "Gaillard", "Gall",
			"Galli", "Gallo", "Gallus", "Gannon", "Garan", "Gard", "Gardiner", "Garen", "Garett", "Garfield", "Garin",
			"Garion", "Garlan", "Garland", "Garlen", "Garlyn", "Garnell", "Garner", "Garnet", "Garnier", "Garon",
			"Garren",
			"Garret", "Garrett", "Garrick", "Garrin", "Garrison", "Garron", "Garryson", "Garvin", "Gary", "Garyson",
			"Gascon", "Gaspar", "Gaspard", "Gaston", "Gauthier", "Gautier", "Gaven", "Gavin", "Gavyn", "Gaylord",
			"Gebbo",
			"Gebert", "Gebhard", "Gedeon", "Geffrey", "Gehrt", "Geof", "Geoff", "Geoffrey", "Georg", "George",
			"Georgio",
			"Geppert", "Ger", "Gerald", "Gerard", "Gerardo", "Gerd", "Gere", "Gereon", "Gerfried", "Gerhard",
			"Gerhardt",
			"Gerhart", "Gerion", "Germain", "German", "Germano", "Gero", "Gerold", "Gerome", "Geron", "Geronimo",
			"Gerrald",
			"Gerrard", "Gerrell", "Gerrit", "Gerry", "Gert", "Gervais", "Gervase", "Gerwald", "Gerwin", "Giacomo",
			"Gian",
			"Gian-Franco", "Gian-Luca", "Gian-Marco", "Giancarlo", "Gianni", "Gideon", "Gidi", "Gidion", "Gieselherr",
			"Giffard", "Gifferd", "Gifford", "Gil", "Gilbert", "Gilberto", "Gilford", "Gill", "Gilleasbuig", "Gilles",
			"Gillian", "Gino", "Giovanni", "Giovanny", "Gironimo", "Giso", "Giuliano", "Giulio", "Giuseppe", "Glen",
			"Glenn", "Godard", "Godart", "Goddard", "Goddart", "Godfrey", "Goeran", "Goldman", "Goliat", "Goliath",
			"Gonzalo", "Goran", "Gordon", "Gorius", "Goswin", "Gotbert", "Gotfrid", "Gottfried", "Gotthard", "Gotthold",
			"Gottlieb", "Gower", "Graciano", "Grady", "Graeme", "Graham", "Granger", "Grant", "Granville", "Gratian",
			"Gratianus", "Gray", "Grayson", "Graziano", "Gregor", "Gregorio", "Gregory", "Grenville", "Greyson",
			"Griffin",
			"Grigor", "Grimbald", "Grischa", "Griswold", "Grosvenor", "Guadalupe", "Gualtiero", "Guarniero", "Guido",
			"Guifford", "Guillaume", "Guillermo", "Gunar", "Gunnar", "Gunner", "Guntar", "Gunter", "Gunthar", "Gunther",
			"Guntram", "Gustaf", "Gustav", "Gustave", "Gustavo", "Gustl", "Guy", "Hacket", "Hackett", "Hadden", "Haden",
			"Hadley", "Hadrian", "Hadrianus", "Hagen", "Hagley", "Haiko", "Haimo", "Haines", "Haio", "Hajo", "Hakan",
			"Hakon", "Halbert", "Haley", "Hall", "Hallam", "Halsey", "Halton", "Hamelin", "Hamelyn", "Hamilton",
			"Hamlet",
			"Hamlin", "Hamlyn", "Hamza", "Hanibal", "Hannecke", "Hannes", "Hannibal", "Hanniel", "Hanno", "Hans",
			"Hans-Jorg", "Hans-Peter", "Hans-carl", "Hansi", "Harald", "Harbert", "Harbin", "Harcourt", "Harden",
			"Hardey",
			"Hardi", "Hardie", "Hardmod", "Hardouin", "Hardy", "Harlan", "Harland", "Harley", "Harlon", "Harm",
			"Harman",
			"Harmen", "Harmon", "Harold", "Harper", "Harri", "Harrison", "Harry", "Hartmod", "Hartmut", "Harv",
			"Harvey",
			"Hasan", "Hasko", "Hassan", "Hastings", "Hauke", "Havel", "Hawel", "Hawk", "Hawthorne", "Hayden", "Haydon",
			"Hayes", "Hayo", "Haywood", "Heath", "Hector", "Hedley", "Heiko", "Heimo", "Hein", "Heiner", "Heini",
			"Heino",
			"Heinrich", "Heinz", "Heio", "Hektor", "Helge", "Helgo", "Helias", "Helke", "Hellmut", "Hellmuth", "Helmi",
			"Helmo", "Helmut", "Helmuth", "Hendrick", "Hendrik", "Henley", "Henning", "Henno", "Henri", "Henrick",
			"Henricus", "Henrik", "Henry", "Herbert", "Heribert", "Heriberto", "Herman", "Hermann", "Hernando",
			"Herrick",
			"Herrmann", "Herve", "Herwin", "Hesekiel", "Hewett", "Heymo", "Hias", "Hieronymus", "Hildebrand",
			"Hilliard",
			"Hillier", "Hillyer", "Hilton", "Hinnerk", "Hinz", "Hippokrates", "Hobart", "Holden", "Holdger", "Holge",
			"Holger", "Hollis", "Holm", "Horst", "Horton", "Houston", "Howard", "Howe", "Hubert", "Hubertus", "Hudson",
			"Huey", "Hugbert", "Hugh", "Hugo", "Hulbard", "Hulbert", "Hulburd", "Hulh", "Hulk", "Humbert", "Humberto",
			"Humbie", "Humfrey", "Humfry", "Humph", "Humphrey", "Hunt", "Hunter", "Huntley", "Huprecht", "Hurlbart",
			"Hurlbert", "Hurn", "Hutton", "Hyatt", "Ian", "Ibrahim", "Ignace", "Ignacio", "Ignatius", "Ignatz", "Ignaz",
			"Ignazio", "Igor", "Ildiko", "Ilja", "Immanuel", "Immo", "Inglebert", "Ingmar", "Ingo", "Ingomar",
			"Ingraham",
			"Ingram", "Ingwar", "Innocentius", "Innozenz", "Iram", "Irvin", "Irving", "Irwin", "Isaac", "Isaak", "Isai",
			"Isaiah", "Isaias", "Ischell", "Isiah", "Isidor", "Isidorius", "Ismael", "Ismail", "Israel", "Isreal",
			"Issac",
			"Ivan", "Iven", "Ives", "Ivo", "Iwan", "Izaiah", "Jörg", "Jörn", "Jürgen", "Jabari", "Jace", "Jack",
			"Jackson",
			"Jacky", "Jacob", "Jacobus", "Jacoby", "Jacque", "Jacquelin", "Jacques", "Jaden", "Jadon", "Jadyn",
			"Jaeden",
			"Jagger", "Jaheem", "Jaheim", "Jahiem", "Jahn", "Jaiden", "Jaime", "Jair", "Jairo", "Jake", "Jakie",
			"Jakob",
			"Jakobe", "Jakobus", "Jalen", "Jamal", "Jamar", "Jamari", "Jamel", "James", "Jameson", "Jamie", "Jamil",
			"Jamir", "Jamison", "Jan", "Jan-Martin", "Janek", "Janko", "Jannes", "Jannik", "Jannis", "Janosch", "Janus",
			"Janusz", "Jaquan", "Jaquez", "Jared", "Jaren", "Jarman", "Jaro", "Jarod", "Jaromil", "Jaromir", "Jaron",
			"Jarred", "Jarrett", "Jarrod", "Jarv", "Jarvey", "Jarvis", "Jascha", "Jase", "Jasmin", "Jason", "Jasper",
			"Javen", "Javier", "Javion", "Javon", "Jaxon", "Jaxson", "Jaxson  Jay", "Jay", "Jayce", "Jayden", "Jaydon",
			"Jaye", "Jaylan", "Jaylen", "Jaylin", "Jaylon", "Jayson", "Jean", "Jean Baptiste", "Jean-Baptiste",
			"Jean-Carlo", "Jean-Christophe", "Jean-Claude", "Jean-Luca", "Jean-Marie", "Jean-Pierre", "Jeff", "Jeffers",
			"Jefferson", "Jeffery", "Jeffrey", "Jefrem", "Jehudi", "Jendrich", "Jendrick", "Jendrik", "Jenik", "Jens",
			"Jeoffroi", "Jerard", "Jeremia", "Jeremiah", "Jeremias", "Jeremy", "Jerker", "Jermaine", "Jeroen", "Jeroma",
			"Jerome", "Jeronimus", "Jerrit", "Jerrold", "Jerry", "Jervis", "Jesaja", "Jesajas", "Jesekiel", "Jesper",
			"Jesse", "Jessie", "Jesus", "Jett", "Jevon", "Jim", "Jimmy", "Jo", "Joachim", "Joan", "Joaquin", "Jobst",
			"Jochen", "Jochim", "Joe", "Joel", "Joey", "Johan", "Johann", "Johannes", "John", "John-paul", "Johnathan",
			"Johnathon", "Johnn", "Johnnie", "Johnny", "Johnson", "Jolie", "Jon", "Jona", "Jonah", "Jonas", "Jonatan",
			"Jonathan", "Jonathon", "Jonko", "Jonn", "Jonnie", "Jordan", "Jorden", "Jordis", "Jordon", "Jordy", "Jorg",
			"Jorge", "Joris", "Jose", "Josef", "Joseph", "Josh", "Joshua", "Josiah", "Josias", "Jost", "Josua", "Josue",
			"Jourdan", "Jovan", "Jovani", "Jovany", "Joy", "Joyanna", "Juan", "Juanito", "Judah", "Jude", "Juhani",
			"Jul",
			"Jules", "Julian", "Julianus", "Julien", "Julio", "Julius", "Jullien", "Junior", "Juniper", "Jupp",
			"Jurgen",
			"Juri", "Jussuf", "Justice", "Justin", "Justinian", "Justinianus", "Justinus", "Justus", "Justyn", "Kaarle",
			"Kaarlo", "Kade", "Kaden", "Kadin", "Kadir", "Kai", "Kai-Olaf", "Kai-Uwe", "Kaiden", "Kain", "Kale",
			"Kaleb",
			"Kalle", "Kallist", "Kallistus", "Kallixtus", "Kalman", "Kameron", "Kamil", "Kampion", "Kamron", "Kane",
			"Kareem", "Karel", "Kari", "Karim", "Karl", "Karl-Heinz", "Karlens", "Karlheinz", "Karlis", "Karlitis",
			"Karol",
			"Karoly", "Karson", "Karstan", "Karsten", "Kasey", "Kasimir", "Kaspar", "Kasper", "Kastor", "Kay", "Kayden",
			"Keagan", "Keanu", "Keaton", "Keegan", "Keenan", "Kegan", "Kei", "Keith", "Kelby", "Kellen", "Kelly",
			"Kelsey",
			"Kelton", "Kelvin", "Kemal", "Ken", "Kendall", "Kendrick", "Kenelm", "Kenley", "Kennedy", "Kenneth",
			"Kenny",
			"Keno", "Kent", "Kenton", "Kenyon", "Keon", "Kerman", "Keshawn", "Kester", "Keven", "Kevin", "Kevon",
			"Keyon",
			"Keyshawn", "Khalid", "Khalil", "Kian", "Kieran", "Kilby", "Kilian", "Killian", "Kim", "Kimberley", "Kimon",
			"King", "Kingsley", "Kinnard", "Kinnell", "Kinsey", "Kipp", "Kipper", "Kippy", "Kirk", "Kjell", "Klaas",
			"Klaudius", "Klaus", "Klemens", "Klement", "Kleopas", "Kleophas", "Klopas", "Knox", "Knut", "Kobe", "Koby",
			"Kody", "Kolas", "Kolby", "Kole", "Kolja", "Kolton", "Konrad", "Konradin", "Konstantin", "Korbin",
			"Korbinian",
			"Korey", "Kornel", "Kornelius", "Kort", "Kory", "Kosha", "Kosta", "Kostis", "Kostja", "Kourosh", "Kristian",
			"Kristofer", "Kristopher", "Kunibert", "Kuno", "Kunz", "Kurt", "Kurtis", "Kylan", "Kyle", "Kyler", "Kyree",
			"Kyrill", "Kyrillus", "L'Angley", "Ladislaus", "Lafayette", "Lajos", "Lamar", "Lamarr", "Lambert",
			"Lambrecht",
			"Lamont", "Lampert", "Lamprecht", "Lance", "Lancelin", "Lancelot", "Landan", "Landen", "Landers", "Landis",
			"Lando", "Landon", "Lane", "Lang", "Langley", "Laramie", "Larry", "Lars", "Larue", "Lasalle", "Laslo",
			"Lasse",
			"Laszlo", "Latimer", "Latrell", "Launcelot", "Laurence", "Laurent", "Laurentius", "Laurenz", "Laux",
			"Lawrence",
			"Lawson", "Layne", "Layton", "Lazarus", "Leal", "Leander", "Leandre", "Leandro", "Lee", "Leeroy", "Legget",
			"Legolas", "Leies", "Leif", "Leigh", "Leland", "Lenard", "Lennard", "Lennart", "Leo", "Leocadie",
			"Leodegrance",
			"Leon", "Leonard", "Leonardo", "Leonce", "Leone", "Leonel", "Leonhard", "Leonid", "Leonore", "Leopold",
			"Leroi",
			"Leron", "Leroux", "Leroy", "Lester", "Leszek", "Leva", "Leveret", "Leverett", "Levi", "Levin", "Lewis",
			"Lex",
			"Liam", "Libold", "Liborius", "Lincoln", "Lind", "Lindberg", "Linden", "Lindon", "Linn", "Lino", "Linus",
			"Linwood", "Lion", "Lionel", "Lionell", "Lionello", "Lisandro", "Lisle", "Litton", "Livio", "Llewellyn",
			"Logan", "Loisl", "London", "Lonell", "Lonnell", "Lonnie", "Loreno", "Lorenz", "Lorenzo", "Loring", "Loris",
			"Lothair", "Lothar", "Louie", "Louis", "Louvel", "Lovell", "Lowe", "Lowell", "Loyal", "Luc", "Luca",
			"Lucas",
			"Lucian", "Luciano", "Lucien", "Ludolf", "Ludovic", "Ludovico", "Ludovicus", "Ludwig", "Luglio", "Luigi",
			"Luis", "Luitpold", "Luka", "Lukas", "Luke", "Luther", "Lutz", "Lyle", "Lyndon", "Lyonel", "Lyre",
			"Lysander",
			"Lytton", "Mace", "Madelon", "Madison", "Maginhart", "Magnus", "Mahieu", "Maik", "Mailhairer", "Maitland",
			"Makepeace", "Malachi", "Malakai", "Malcolm", "Malik", "Malin", "Malleville", "Mallory", "Malou", "Malte",
			"Malvin", "Malwin", "Mandel", "Manfred", "Mani", "Manilo", "Manley", "Manly", "Manneville", "Manning",
			"Manolito", "Manolo", "Mansfield", "Mantel", "Manton", "Manuel", "Manville", "Many", "Marc", "Marceau",
			"Marcel", "Marcellinus", "Marcello", "Marcellus", "Marcelo", "Marco", "Marcos", "Marcus", "Marden",
			"Mardyth",
			"Marek", "Marenus", "Marian", "Mariano", "Marin", "Marino", "Marinus", "Mario", "Mariolino", "Marius",
			"Mark",
			"Markes", "Markey", "Marko", "Markus", "Marland", "Marley", "Marlo", "Marlon", "Marlow", "Marlowe",
			"Marmion",
			"Marq", "Marque", "Marquez", "Marquis", "Marquise", "Marsden", "Marsdon", "Marsh", "Marshal", "Marshall",
			"Marston", "Mart", "Marten", "Marti", "Martin", "Martino", "Maruck", "Marvin", "Marwin", "Marwood",
			"Marzellus",
			"Maslin", "Mason", "Masselin", "Masson", "Mateo", "Mather", "Mathew", "Mathias", "Mathieu", "Mats",
			"Matteo",
			"Mattes", "Matthew", "Matthias", "Matthieu", "Mattias", "Matty", "Matze", "Maurice", "Mauricio",
			"Mauritius",
			"Maurizio", "Maurus", "Maverick", "Max", "Maxence", "Maxim", "Maxime", "Maximilian", "Maximillian",
			"Maximo",
			"Maximus", "Maxwell", "Mayhew", "Maynard", "Mayne", "Maynor", "Mead", "Medwin", "Mees", "Mehmet", "Meinert",
			"Meinhard", "Mekhi", "Melchior", "Melton", "Melville", "Melvin", "Menachem", "Menard", "Mercer", "Merla",
			"Merle", "Merlin", "Merlion", "Merrell", "Merrick", "Merrill", "Mertin", "Merwin", "Meus", "Micah",
			"Michael",
			"Michail", "Micheal", "Michel", "Michele", "Mick", "Miguel", "Mika", "Mike", "Mikel", "Milan", "Miles",
			"Milko",
			"Millard", "Miller", "Mills", "Millson", "Milo", "Milt", "Milten", "Milto", "Milton", "Milty", "Mino",
			"Miquel",
			"Mircha", "Mirek", "Mirko", "Misael", "Miso", "Mitchel", "Mitchell", "Mohamed", "Mohammad", "Mohammed",
			"Moises", "Momo", "Mont-Gomerie", "Montague", "Montaigu", "Montaine", "Montgomery", "Moor", "Moore", "More",
			"Morell", "Moreno", "Morgan", "Moritz", "Moriz", "Morris", "Morven", "Moses", "Moshe", "Muck", "Muhammad",
			"Mustafa", "Mutz", "Myles", "Nann", "Napoleon", "Nash", "Nasir", "Natan", "Nathan", "Nathanael",
			"Nathanial",
			"Nathaniel", "Nathen", "Navid", "Nayan", "Neal", "Nealson", "Ned", "Neddie", "Neddy", "Nedes", "Nehemiah",
			"Neil", "Neilson", "Neivin", "Nelles", "Nellie", "Nelly", "Nelson", "Neo", "Nepomuk", "Nero", "Nestor",
			"Neuman", "Neumann", "Neuveville", "Neville", "Newall", "Newbold", "Newell", "Newgate", "Newland", "Newlin",
			"Newman", "Newmie", "Newton", "Nicandro", "Nichol", "Nicholas", "Nick", "Nickolas", "Nico", "Nicodemo",
			"Nicolai", "Nicolas", "Nicolaus", "Niels", "Nigel", "Nikhil", "Nikita", "Niklas", "Niko", "Nikodemus",
			"Nikol",
			"Nikolas", "Nikolaus", "Nils", "Nilson", "Nimet", "Nino", "Noa", "Noah", "Noe", "Noel", "Noel  Nolan",
			"Noell",
			"Nolan", "Norbert", "Noreis", "Norice", "Norm", "Normal", "Norman", "Normand", "Normen", "Normie", "Norris",
			"North", "Norton", "Norville", "Norvin", "Norward", "Norwell", "Norwin", "Norwood", "Norwyn", "Nouel",
			"Nowles",
			"Numen", "Nuran", "Nyle", "ONille", "Oakley", "Obert", "Octave", "Octavio", "Odell", "Oden", "Odin", "Odo",
			"Odolf", "Odysseus", "Ogden", "Olaf", "Ole", "Oleg", "Oli", "Olin", "Oliver", "Olivier", "Omar", "Omari",
			"Omarion", "Onfroi", "Onnan", "Onno", "Onnond", "Oralndo", "Orazio", "Orion", "Orlan", "Orlando", "Orman",
			"Ormen", "Ornand", "Orson", "Orvelle", "Orvil", "Orville", "Osbaldo", "Osbert", "Osborn", "Osborne",
			"Oscar",
			"Osgood", "Oskar", "Osmar", "Osmond", "Ossie", "Osvaldo", "Oswald", "Oswaldo", "Oswall", "Oswell", "Oswin",
			"Otger", "Othello", "Othmar", "Otmar", "Otmund", "Otto", "Otwin", "Ourson", "Ove", "Owe", "Owen", "Oxford",
			"Oxon", "Oxton", "Ozzie", "Paavo", "Pablo", "Pacey", "Packard", "Paco", "Padgett", "Page", "Paget", "Paien",
			"Paige", "Palmer", "Palmiro", "Pancratius", "Pankratz", "Paolo", "Parfait", "Paris", "Park", "Parke",
			"Parker",
			"Parkley", "Parks", "Parr", "Parry", "Pascal", "Pascual", "Pasquale", "Pat", "Paton", "Patric", "Patrick",
			"Patten", "Pattin", "Patton", "Paul", "Paule", "Paulus", "Pawel", "Paxon", "Paxton", "Payton", "Pearson",
			"Pedro", "Peer", "Pelham", "Pell", "Pelton", "Penley", "Penn", "Penrod", "Pepi", "Pepin", "Pepino",
			"Pepperell",
			"Peppi", "Peppin", "Per", "Perceval", "Percival", "Percy", "Perren", "Perrin", "Perry", "Perryn", "Peter",
			"Petrus", "Peverell", "Peyton", "Pharamond", "Phil", "Philip", "Philipp", "Philippe", "Phillip", "Phillipe",
			"Phoenix", "Pierce", "Piero", "Pierpont", "Pierre", "Pierrepont", "Piers", "Pierson", "Pietro", "Pio",
			"Piperel", "Pippin", "Piret", "Pirmin", "Pit", "Pius", "Plat", "Platt", "Pollard", "Pomeroy", "Pommelraie",
			"Porter", "Porteur", "Portier", "Pranav", "Preruet", "Prescott", "Presley", "Preston", "Prewitt", "Priest",
			"Priestley", "Priestly", "Prince", "Priour", "Prisko", "Pruet", "Pruie", "Pruitt", "Pryor", "Putnam",
			"Putney",
			"Quennel", "Quent", "Quentin", "Quenton", "Quentrell", "Quincey", "Quincy", "Quinn", "Quint", "Quinten",
			"Quintin", "Quintinus", "Quinton", "Quintrell", "Quintus", "Quinzi", "Quirin", "Quirinus", "Régis", "Rab",
			"Rabbit", "Rad", "Radbert", "Radcliff", "Radcliffe", "Radclyf", "Radclyffe", "Radford", "Radley", "Radnor",
			"Radomil", "Rae", "Rafael", "Raff", "Raffael", "Raffaello", "Raffi", "Raghnall", "Rahul", "Rai", "Raik",
			"Raimond", "Raimondo", "Raimund", "Raimundo", "Rainald", "Rainer", "Rainger", "Rainier", "Raleigh", "Ralf",
			"Ralph", "Ralston", "Rambert", "Ramiro", "Ramon", "Ramond", "Ramsay", "Ramses", "Ramsey", "Ramzey", "Ramzi",
			"Randall", "Randy", "Ranger", "Ranier", "Ransden", "Ransford", "Ransley", "Ransom", "Raoul", "Raphael",
			"Rashad", "Rasiel", "Raul", "Raven", "Ravi", "Ravinger", "Ravinia", "Rawdon", "Rawley", "Rawlings",
			"Rawlins",
			"Rawls", "Rawly", "Rawson", "Ray", "Rayburn", "Rayce", "Rayder", "Raydon", "Rayfield", "Rayford", "Raylen",
			"Raymon", "Raymond", "Raymund", "Raymundo", "Raynard", "Raynell", "Read", "Reade", "Reading", "Reagan",
			"Reamonn", "Red", "Redd", "Redding", "Redfield", "Redford", "Redgrave", "Redman", "Redwald", "Reece",
			"Reed",
			"Reese", "Reg", "Reggie", "Reggy", "Reginald", "Regnauld", "Reid", "Reilly", "Reimar", "Reimund", "Reinald",
			"Reiner", "Reinhard", "Reinhold", "Reinold", "Reinwald", "Rell", "Remi", "Remington", "Remme", "Remmie",
			"Remmy", "Remo", "Remy", "René", "Renald", "Renard", "Renato", "Renault", "Rene", "Renne", "Rennie",
			"Renny",
			"Reto", "Reuben", "Reule", "Reve", "Rex", "Rey", "Reymond", "Reymundo", "Reynaldo", "Reynard", "Reynold",
			"Reynolds", "Rhett", "Ricard", "Ricardo", "Rich", "Richard", "Richardo", "Richmond", "Rick", "Rickard",
			"Rickey", "Rickie", "Ricky", "Rico", "Rider", "Ridley", "Rigby", "Rigoberto", "Riley", "Rinaldo", "Riobard",
			"Rip", "Ripley", "Rique", "Rishley", "Risto", "Riston", "River", "Rob", "Robb", "Robben", "Robbie",
			"Robbins",
			"Robby", "Rober", "Robert", "Roberto", "Robey", "Robin", "Robinson", "Rocco", "Roch", "Roche", "Rochester",
			"Rocke", "Rocky", "Rod", "Rodd", "Roddie", "Roddric", "Roddrick", "Roddy", "Rodel", "Rodell", "Roderic",
			"Roderich", "Roderick", "Rodge", "Rodger", "Rodhlann", "Rodi", "Rodman", "Rodmond", "Rodmund", "Rodney",
			"Rodolf", "Rodolfo", "Rodolph", "Rodrigo", "Roel", "Rogelio", "Roger", "Rogj", "Rohan", "Roi", "Rol",
			"Roland",
			"Rolando", "Rolf", "Rolfe", "Rollan", "Rolland", "Rollie", "Rollin", "Rollo", "Rolof", "Rolph", "Rolt",
			"Romain", "Roman", "Romano", "Romek", "Romeo", "Ron", "Ronald", "Ronaldo", "Ronan", "Ronnie", "Ronny",
			"Rory",
			"Roselin", "Ross", "Roswald", "Roswall", "Roswell", "Roth", "Rousse", "Roussel", "Rousset", "Rousskin",
			"Rouven", "Rowan", "Rowe", "Rowland", "Roy", "Royal", "Royce", "Royden", "Ruben", "Rubert", "Ruddy", "Rudi",
			"Rudiger", "Rudolf", "Rudolfo", "Rudolph", "Rudy", "Rudyard", "Ruelle", "Ruff", "Ruffe", "Ruggero", "Rui",
			"Rule", "Rupert", "Ruppert", "Ruprecht", "Rush", "Rushe", "Rushkin", "Ruskin", "Russ", "Russel", "Russell",
			"Rust", "Rutherford", "Ruthren", "Ruven", "Ryan", "Rycroft", "Ryder", "Rylan", "Ryland", "Ryle", "Rylee",
			"Ryley", "Ryman", "Rypley", "Ryton", "Sönke", "Sören", "Sabastian", "Saber", "Sacharja", "Sadddique",
			"Sage",
			"Saladin", "Saladino", "Salentin", "Salim", "Salomo", "Salomon", "Salomone", "Salvador", "Salvator",
			"Salvatore", "Sam", "Sami", "Samir", "Sammy", "Samson", "Samuel", "Samy", "Sanborn", "Sandford", "Sandon",
			"Sandro", "Sandy", "Sanford", "Santiago", "Santino", "Santos", "Sargent", "Sascha", "Satordi", "Saul",
			"Sauville", "Saverio", "Saville", "Savion", "Sawyer", "Schorsch", "Scipio", "Scipione", "Scot", "Scott",
			"Scottie", "Scotty", "Seabert", "Seabright", "Seabrook", "Seabury", "Seamus", "Sean", "Searl", "Searlas",
			"Searle", "Searlus", "Sebastian", "Sebastiano", "Sebastien", "Seberg", "Sebert", "Seid", "Seignour",
			"Selby",
			"Selim", "Semaj", "Semjon", "Senad", "Senet", "Senior", "Sennet", "Sepp", "Seppel", "Sepperl", "Seppi",
			"Sergej", "Sergio", "Sergius", "Sesto", "Seth", "Severin", "Severinus", "Severn", "Severus", "Sevim",
			"Sevrin",
			"Seward", "Sewell", "Seymour", "Shamar", "Shane", "Shannon", "Shaun", "Shaw", "Shawn", "Shayne", "Shea",
			"Sheldon", "Shell", "Shelley", "Shelli", "Shelly", "Shemar", "Shep", "Shepard", "Shepherd", "Shepley",
			"Sheppard", "Sherborne", "Sherlock", "Sherm", "Sherman", "Sherwin", "Sherwood", "Shipley", "Sid", "Siddel",
			"Sidney", "Sidwell", "Siegfrid", "Siegfried", "Siegmund", "Sigfrid", "Sigfried", "Siggi", "Sigismond",
			"Sigismund", "Sigmond", "Sigmund", "Sigwald", "Silas", "Silvain", "Silvester", "Silvestre", "Silvio",
			"Silvius",
			"Simeon", "Simon", "Sinan", "Sincere", "Sinclair", "Sinclaire", "Sinjin", "Sisto", "Siward", "Sixt",
			"Sixtus",
			"Skrolan", "Skylar", "Skyler", "Slade", "Snowden", "Snowdun", "Sobek", "Solomon", "Somer", "Somerled",
			"Somerville", "Sonke", "Sonny", "Sorel", "Soren", "Sorrell", "Spangler", "Speck", "Spence", "Spencer",
			"Spenser", "Spike", "Spiros", "Sprague", "Spyridon", "Spyros", "Stanberry", "Stanbury", "Stanek",
			"Stanfield",
			"Stanford", "Stanhope", "Stanislaus", "Stanleigh", "Stanley", "Stanly", "Stanmore", "Stanton", "Stanway",
			"Stanwick", "Stanwyck", "Stefan", "Steffen", "Stein", "Stephan", "Stephen", "Stephon", "Sterling", "Steve",
			"Steven", "Stockman", "Stockton", "Stockwell", "Stokley", "Stone", "Stroud", "Stuart", "Studs", "Suleiman",
			"Sullivan", "Sumarville", "Sumner", "Sven", "Swen", "Syd", "Sydell", "Sydney", "Syed", "Sylwester", "Taavi",
			"Tabaluga", "Taillefer", "Talbot", "Talehot", "Talon", "Tancred", "Tanner", "Tarek", "Tarik", "Tariq",
			"Tarzan",
			"Tassilo", "Tasso", "Tate", "Tavin", "Tavion", "Taylor", "Tayrese", "Tearlach", "Ted", "Teddic", "Teddie",
			"Tedman", "Tedmund", "Tedric", "Telfer", "Telfor", "Telford", "Telfour", "Terenz", "Terrance", "Terrel",
			"Terrell", "Terrence", "Terrill", "Terris", "Terry", "Thabo", "Thaddäus", "Thaddeus", "Thaisen", "Thane",
			"Thassilo", "Thatcher", "Thees", "Theo", "Theobald", "Theodor", "Theodore", "Theodoric", "Theodorick",
			"Theron",
			"Therron", "Thibaud", "Thibaut", "Thieny", "Thierry", "Thiery", "Thomas", "Thor", "Thorald", "Thoralf",
			"Thorben", "Thorbert", "Thorburn", "Thorley", "Thormond", "Thorn", "Thoname_componentyke", "Thorne",
			"Thornley",
			"Thornton", "Thorpe", "Thorsten", "Thurber", "Thure", "Thurlow", "Thurman", "Thurmon", "Thurmond",
			"Tibault",
			"Tibbald", "Tiberio", "Tiberius", "Tibor", "Till", "Tillmann", "Tilmann", "Tilo", "Tim", "Timo", "Timon",
			"Timothy", "Tino", "Tioboid", "Tiran", "Tirell", "Tito", "Titus", "Tizian", "Tiziano", "Tjorven", "Tobi",
			"Tobia", "Tobias", "Toby", "Todd", "Toffel", "Tom", "Tomas", "Tomaso", "Tombke", "Tomke", "Tomkin",
			"Tomlin",
			"Tommy", "Tompkin", "Toni", "Tonio", "Tony", "Torben", "Torge", "Torold", "Torsten", "Tostig", "Toussnint",
			"Towne", "Townes", "Townley", "Townsend", "Trace", "Tracy", "Tranter", "Traugott", "Travers", "Travis",
			"Travon", "Tre", "Trent", "Trenton", "Trever", "Treves", "Trevin", "Trevion", "Trevon", "Trevor", "Trey",
			"Treyton", "Tripp", "Tristan", "Tristen", "Tristian", "Tristin", "Triston", "Troy", "Troyes", "True",
			"Trueman",
			"Truesdale", "Truman", "Trystan", "Tucker", "Turner", "Ty", "Tybalt", "Tyce", "Tycho", "Tychon", "Tye",
			"Tyeis",
			"Tyeson", "Tyler", "Tylor", "Tyne", "Tyree", "Tyrell", "Tyrese", "Tyron", "Tyrone", "Tyshawn", "Tyson",
			"Udo",
			"Ugo", "Ugolino", "Uhland", "Uland", "Ulf", "Uli", "Ulises", "Ulixes", "Ulli", "Ulric", "Ulrich", "Ulrico",
			"Ulysses", "Umberto", "Urban", "Urbano", "Urbanus", "Urias", "Uriel", "Urija", "Urs", "Ursinus", "Ursio",
			"Ursus", "Uto", "Utto", "Uve", "Uvo", "Uwe", "Uwo", "Vachel", "Vail", "Valdemar", "Valdimar", "Valdimiro",
			"Valdis", "Valentianus", "Valentin", "Valentiniano", "Valentino", "Valentinus", "Valentius", "Valerian",
			"Valerianus", "Valerio", "Valerius", "Valiant", "Vallis", "Vallois", "Vance", "Vardan", "Varden", "Vardon",
			"Vasco", "Vaughn", "Vayle", "Veit", "Verddun", "Verdell", "Verel", "Vern", "Vernay", "Verne", "Vernell",
			"Verner", "Verney", "Vernon", "Verrall", "Verrell", "Verrill", "Veryl", "Vic", "Vicente", "Vick", "Vico",
			"Vicq", "Victor", "Victorian", "Victorianus", "Victorinus", "Vidal", "Videl", "Vike", "Viktor", "Viktorin",
			"Vilmos", "Vincent", "Vincentius", "Vincenz", "Vincenzo", "Vinzenez", "Vinzent", "Vinzenz", "Virgil",
			"Vital",
			"Vitale", "Vitalis", "Vito", "Vittorio", "Vladimir", "Volkan", "Volker", "Volkher", "Volkmar", "Volkmer",
			"Vollert", "Volmar", "Volney", "Von", "Wade", "Waggoner", "Wagner", "Wain", "Waine", "Wake", "Wakefield",
			"Wakeley", "Wakeman", "Walcot", "Walcott", "Waldemar", "Waldo", "Waldomar", "Waldron", "Walker", "Wallace",
			"Wallach", "Wallas", "Waller", "Wallie", "Wallis", "Wally", "Walmond", "Walmund", "Walsh", "Walt", "Walter",
			"Walters", "Walther", "Walton", "Wanja", "Wanko", "Ward", "Wardell", "Warden", "Wardley", "Warfield",
			"Warford",
			"Waring", "Warley", "Warmond", "Warmund", "Warner", "Warnke", "Warrane", "Warren", "Warrick", "Warton",
			"Warwick", "Washington", "Wassilie", "Wat", "Watkins", "Watson", "Watt", "Waverly", "Way", "Wayland",
			"Waylon",
			"Wayne", "Webb", "Weber", "Webley", "Webster", "Weimer", "Welborne", "Welby", "Welch", "Weldon", "Welf",
			"Welford", "Weller", "Welles", "Wells", "Welsh", "Welton", "Wenceslas", "Wendel", "Wendelin", "Wendell",
			"Wenzel", "Werner", "Wernher", "Werther", "Wes", "Wesley", "Wess", "Wessely", "West", "Westbrook", "Westby",
			"Westcott", "Westleigh", "Weston", "Wetherby", "Wheaton", "Wheeler", "Whit", "Whitby", "Whitcomb",
			"Whitelaw",
			"Whitfield", "Whitford", "Whitley", "Whitlock", "Whitman", "Whitmore", "Whittaker", "Wiatt", "Wiclef",
			"Wiclif",
			"Wilbur", "Wiley", "Wilfer", "Wilfert", "Wilfred", "Wilfrid", "Wilfried", "Wilhelm", "Will", "Willem",
			"Willi",
			"William", "Willie", "Willow", "Willy", "Wilmer", "Wilmot", "Wilson", "Wim", "Winchell", "Windemuth",
			"Windham",
			"Windsor", "Winemar", "Winfield", "Winfred", "Winfrey", "Winfrid", "Winfried", "Wingate", "Winimar",
			"Winmar",
			"Winslow", "Winsor", "Winston", "Winthrop", "Winton", "Winward", "Wirt", "Wirth", "Witas", "Witt", "Witter",
			"Witton", "Wladimir", "Wladisla", "Woitech", "Wolf", "Wolfe", "Wolfgang", "Wolfram", "Wolter", "Woodie",
			"Woodrow", "Woodruff", "Woodward", "Woody", "Wright", "Wulf", "Wum", "Wyatt", "Wylie", "Wyn", "Wyndam",
			"Wynton", "Xander", "Xaver", "Xaverius", "Xavier", "Xzavier", "Yadiel", "Yahir", "Yamil", "Yan", "Yannic",
			"Yannick", "Yannis", "Yasin", "Yehudi", "Yorik", "York", "Yosef", "Yul", "Yule", "Yven", "Yves", "Ywan",
			"Zachariah", "Zacharias", "Zachary", "Zachery", "Zack", "Zackary", "Zackery", "Zadoc", "Zain", "Zaire",
			"Zakary", "Zander", "Zane", "Zavier", "Zayne", "Zechariah", "Zenobio", "Zero", "Zeus", "Zino", "Zion",
			"Zyrus"]

	# feminine
	nm84 = ["Aaliyah", "Abagail", "Abbey", "Abbie", "Abbigail", "Abby", "Abelia", "Abelina", "Abella", "Abigail",
			"Abigale",
			"Abigayle", "Abril", "Aceline", "Adalene", "Adalicia", "Adalie", "Adaliz", "Adalyn", "Addie", "Addison",
			"Adela", "Adelaide", "Adele", "Adelia", "Adelina", "Adeline", "Adelisa", "Adelise", "Adelle", "Adelynn",
			"Adilene", "Adorlee", "Adreanna", "Adriana", "Adriane", "Adrianna", "Adrianne", "Adriene", "Adrienne",
			"Adula",
			"Aeldrida", "Aelfreda", "Afra", "Afrodille", "Afton", "Agatha", "Agathe", "Agda", "Aget", "Aggy", "Aglaia",
			"Aglaja", "Agnes", "Agnese", "Agnita", "Agrona", "Aida", "Aiglentina", "Aileen", "Aillsa", "Ailsa",
			"Ailssa",
			"Aimee", "Ainsley", "Aischa", "Aisha", "Aislinn", "Aiyana", "Aja", "Akira", "Alaina", "Alaine", "Alair",
			"Alana", "Alanis", "Alanna", "Alarica", "Alarice", "Alarise", "Alayna", "Alban", "Alberta", "Albertina",
			"Albertyna", "Albertyne", "Alcott", "Alda", "Alden", "Aldercy", "Alea", "Aleah", "Alejandra", "Alena",
			"Alessandra", "Aletta", "Alex", "Alexa", "Alexandra", "Alexandrea", "Alexandria", "Alexandrina",
			"Alexandrine",
			"Alexia", "Alexiana", "Alexis", "Alexus", "Alexys", "Alfonsine", "Alhertine", "Alia", "Alice", "Alicia",
			"Alida", "Alina", "Alisa", "Alisanne", "Alisha", "Alisia", "Alison", "Alissa", "Alita", "Alivia", "Alix",
			"Alixandra", "Aliya", "Aliyah", "Aliza", "Alize", "Allaire", "Alleffra", "Allegra", "Allesha", "Allete",
			"Allie", "Allison", "Ally", "Allyson", "Allyssa", "Alma", "Almuth", "Alondra", "Alonza", "Aloys", "Aloyse",
			"Alphonsina", "Alphonsine", "Alsatia", "Althea", "Althee", "Alva", "Alvina", "Alvine", "Alwara", "Alwera",
			"Alwine", "Alycia", "Alysa", "Alysha", "Alyson", "Alyssa", "Alyssandra", "Amabel", "Amabella", "Amabelle",
			"Amabilia", "Amadea", "Amalberga", "Amalia", "Amalie", "Amanda", "Amani", "Amara", "Amarante", "Amari",
			"Amata",
			"Amaya", "Amber", "Amberjill", "Ambra", "Ambre", "Amedea", "Amedee", "Amelia", "Amelie", "Amely", "America",
			"Ami", "Amia", "Amie", "Amina", "Amira", "Amite", "Amitee", "Amity", "Amrei", "Amy", "Amya", "Ana",
			"Anabel",
			"Anahi", "Anais", "Anastasia", "Anastasija", "Anastina", "Anaya", "Ancelin", "Ancelina", "Andie", "Andra",
			"Andrea", "Andree", "Aneta", "Anette", "Ange", "Angel", "Angela", "Angeletta", "Angelette", "Angelia",
			"Angelica", "Angelika", "Angelina", "Angeline", "Angelique", "Angie", "Angilia", "Anika", "Anina", "Anissa",
			"Anita", "Aniya", "Aniyah", "Anja", "Anjali", "Anjuschka", "Anka", "Anke", "Ann", "Anna", "Annabel",
			"Annabella", "Annabelle", "Annalena", "Annalise", "Annamaria", "Anne", "Anne-Kathrin", "Annekathrin",
			"Anneke",
			"Annelie", "Anneliese", "Annemarie", "Annett", "Annette", "Annia", "Annie", "Annika", "Annike", "Annique",
			"Anouk", "Ansley", "Antje", "Antoinette", "Antonella", "Antonette", "Antonia", "Antonie", "Antonina",
			"Anuschka", "Anya", "Apollina", "Apolline", "Appollonia", "April", "Arabela", "Arabella", "Araceli",
			"Aracely",
			"Arantxa", "Arcene", "Arely", "Aria", "Ariadne", "Ariana", "Ariane", "Arianna", "Arianne", "Ariel",
			"Ariele",
			"Ariella", "Arielle", "Arjean", "Arleigh", "Arlene", "Arleta", "Arlett", "Arlette", "Armani", "Armelle",
			"Armina", "Armine", "Arminia", "Arnalda", "Arnelle", "Arsène", "Aruna", "Aryanna", "Ash", "Ashanti",
			"Ashby",
			"Ashe", "Ashford", "Ashi", "Ashlan", "Ashlee", "Ashleigh", "Ashley", "Ashli", "Ashlie", "Ashlin", "Ashling",
			"Ashly", "Ashlyn", "Ashlynn", "Ashton", "Ashtyn", "Asia", "Aspen", "Asta", "Asteria", "Astred", "Astrid",
			"Athena", "Auberta", "Aubina", "Aubine", "Aubree", "Aubrey", "Aubriana", "Aubrianne", "Aubrie", "Aubry",
			"Audery", "Audey", "Audie", "Audra", "Audrey", "Audry", "Aurelia", "Aurelie", "Aurica", "Aurora",
			"Aurorette",
			"Autumn", "Ava", "Aveline", "Avery", "Avicia", "Avon", "Avril", "Axelle", "Ayana", "Ayanna", "Ayasha",
			"Ayla",
			"Aylin", "Aysche", "Aysun", "Azzura", "Babette", "Baby", "Baerbel", "Bailee", "Bailey", "Barbara",
			"Bathilda",
			"Bathilde", "Batilda", "Batilde", "Baxter", "Baylee", "Bea", "Beata", "Beate", "Beatrice", "Beatrix",
			"Beatriz",
			"Bebe", "Becky", "Belana", "Belda", "Belen", "Belinda", "Beline", "Bell", "Bella", "Belle", "Benedetta",
			"Benedicta", "Benedikta", "Benita", "Bente", "Berangaria", "Berdine", "Berengaria", "Berenice", "Berenike",
			"Berit", "Bernadea", "Bernadette", "Bernadina", "Bernadine", "Bernarda", "Bernarde", "Berneen", "Bernelle",
			"Bernetta", "Bernette", "Bernhardine", "Bernice", "Berniss", "Bernita", "Bernyce", "Bert", "Berta", "Berte",
			"Bertha", "Berthe", "Bertie", "Bertille", "Bertina", "Berty", "Bessy", "Bethany", "Bette", "Betti",
			"Bettina",
			"Bettine", "Bev", "Beverely", "Beverley", "Beverly", "Bianca", "Bianka", "Bibi", "Bibijana", "Bijou",
			"Bille",
			"Billie", "Billy", "Bina", "Bine", "Binga", "Binia", "Birger", "Birgit", "Birgitta", "Birke", "Birte",
			"Blaine",
			"Blanca", "Blanch", "Blanche", "Blanchefleur", "Blandina", "Blanka", "Blenda", "Blondell", "Blondelle",
			"Blondene", "Blossom", "Blythe", "Bo", "Bobbi", "Bobbie", "Bobby", "Bojana", "Bojena", "Bonnie", "Bonny",
			"Borissa", "Brandi", "Brandy", "Brea", "Breana", "Breanna", "Brenda", "Brenna", "Breonna", "Bret", "Brett",
			"Bretta", "Brettany", "Brette", "Bria", "Briana", "Brianna", "Brianne", "Bridget", "Bridgett", "Bridgette",
			"Brielle", "Brigette", "Brigitta", "Brigitte", "Brionna", "Brisa", "Brita", "Britney", "Britt", "Britta",
			"Brittany", "Brittney", "Bronja", "Bronwen", "Bronwyn", "Brook", "Brooke", "Brookes", "Brooklyn",
			"Brooklynn",
			"Brooks", "Brucie", "Brunella", "Brunhild", "Brunhilda", "Brunhilde", "Bryana", "Bryanna", "Brynn", "Buffy",
			"Burgi", "Cäzilie", "Cadence", "Cadencia", "Cady", "Caitlin", "Caitlyn", "Caja", "Calandre", "Calantha",
			"Calanthe", "Cali", "Calista", "Callie", "Cam", "Cameron", "Camila", "Camile", "Camilla", "Camille",
			"Camillei",
			"Camm", "Cammi", "Cammie", "Camryn", "Camyron", "Candace", "Candice", "Candide", "Capucina", "Capucine",
			"Cara",
			"Caress", "Caressa", "Caresse", "Carin", "Carina", "Carine", "Carissa", "Carla", "Carlee", "Carley",
			"Carli",
			"Carlie", "Carling", "Carlotta", "Carly", "Carmela", "Carmelia", "Carmen", "Carnation", "Caro", "Carol",
			"Carola", "Carole", "Carolin", "Carolina", "Caroline", "Carolyn", "Carressa", "Carrie", "Carry", "Carson",
			"Carsta", "Casandra", "Casey", "Cassandra", "Cassidy", "Cassie", "Catalina", "Cateline", "Catharina",
			"Catherine", "Cathleen", "Cathrin", "Cayla", "Cecelia", "Cecile", "Cecilia", "Cecilie", "Cecille",
			"Cedrine",
			"Celesse", "Celeste", "Celestia", "Celestiel", "Celestine", "Celestyn", "Celestyna", "Celia", "Celie",
			"Celina",
			"Celine", "Cellina", "Cendrillon", "Cerise", "Chana", "Chanel", "Chanell", "Chanelle", "Channelle",
			"Chantae",
			"Chantal", "Chantalle", "Chantay", "Chante", "Chantel", "Chantell", "Chantelle", "Chantrell", "Chardae",
			"Charee", "Charis", "Charisse", "Charity", "Charlaine", "Charlayne", "Charleen", "Charleena", "Charlena",
			"Charlene", "Charlette", "Charline", "Charlisa", "Charlita", "Charlize", "Charlot", "Charlotta",
			"Charlotte",
			"Charmain", "Charmaine", "Charmayne", "Charmine", "Chasity", "Chaunte", "Chauntel", "Chaya", "Chelsea",
			"Chelsey", "Chelsie", "Chenelle", "Cher", "Chere", "Cheree", "Chereen", "Cherell", "Cherelle", "Cheri",
			"Cherie", "Cherina", "Cherine", "Cherise", "Cherita", "Cherree", "Cherrelle", "Cherry", "Cheryl",
			"Cheyanna",
			"Cheyanne", "Cheyenne", "Chiana", "Chianna", "Chiara", "Chlarimonda", "Chlarimonde", "Chloe", "Chlorinde",
			"Chloris", "Chlothilde", "Christa", "Christel", "Christian", "Christiana", "Christiane", "Christin",
			"Christina", "Christine", "Christy", "Ciara", "Cicilina", "Ciera", "Cierra", "Cilia", "Cinderella", "Cindy",
			"Cinzia", "Cira", "Citlali", "Claiborne", "Clair", "Claire", "Clara", "Claral", "Clare", "Clarette",
			"Claribel",
			"Clarice", "Clarimond", "Clarimonda", "Clarimonde", "Clarinda", "Clarissa", "Clarissa Claudia", "Clarisse",
			"Clarita", "Claudette", "Claudia", "Claudine", "Clemance", "Clemence", "Clementia", "Clementina",
			"Clementine",
			"Clodia", "Clothilda", "Clothilde", "Clotilda", "Clotilde", "Clovis", "Coco", "Coleta", "Coletta",
			"Colette",
			"Colleen", "Colletta", "Collette", "Columbia", "Comfort", "Comforte", "Conni", "Connie", "Conny", "Conrada",
			"Conradina", "Conradine", "Constance", "Constancia", "Constanze", "Cora", "Coralie", "Cordelia", "Cordula",
			"Corette", "Corina", "Corine", "Corinna", "Corinne", "Corliss", "Cornelia", "Corney", "Cortney", "Cosette",
			"Cosima", "Cosma", "Courtlyn", "Courtney", "Creissant", "Crescent", "Cristal", "Cristina", "Crystal",
			"Cybille",
			"Cynthia", "Cyprienne", "Daggy", "Dagmar", "Dagmara", "Dagny", "Daisey", "Daisi", "Daisy", "Dajana",
			"Dakota",
			"Dale", "Dalia", "Damaris", "Damia", "Damiana", "Damiane", "Damie", "Damien", "Dana", "Danae", "Dania",
			"Daniela", "Daniella", "Danielle", "Danja", "Danna", "Danny", "Dany", "Daphne", "Daralis", "Darby",
			"Darcel",
			"Darcell", "Darcelle", "Darcey", "Darchelle", "Darci", "Darcia", "Darcy", "Daria", "Darlene", "Dasia",
			"Daveney", "Dawina", "Dawn", "Dayana", "Dea", "Deanna", "Deasia", "Debby", "Debora", "Deborah", "Debra",
			"Deik",
			"Deja", "Dela", "Delaney", "Dele", "Delfine", "Delia", "Delight", "Delilah", "Delit", "Della", "Delmare",
			"Delphina", "Delphine", "Demelza", "Demie", "Denice", "Deniece", "Denise", "Denisha", "Denissa", "Denisse",
			"Dennise", "Denyse", "Dereka", "Derica", "Dericka", "Derrica", "Desarae", "Desaree", "Desideria", "Desirae",
			"Desirat", "Desire", "Desiree", "Destanee", "Destine", "Destinee", "Destiney", "Destini", "Destinie",
			"Destiny",
			"Devan", "Devana", "Devanna", "Devin", "Devon", "Devona", "Devondra", "Devonna", "Devonne", "Devyn",
			"Devynn",
			"Dezirae", "Deziree", "Di", "Diahann", "Diahna", "Diamanta", "Diamond", "Dian", "Diana", "Diandra", "Diane",
			"Dianna", "Diannah", "Dianne", "Dick", "Dickie", "Didina", "Dina", "Dionne", "Dior", "Dixie", "Dodo",
			"Dolores",
			"Domenica", "Dominica", "Dominika", "Dominique", "Donna", "Dora", "Dorchen", "Dore", "Doreen", "Dorene",
			"Dorette", "Dorika", "Dorine", "Doris", "Dorkas", "Doro", "Dorothea", "Dorothee", "Dorothy", "Dortas",
			"Dortje",
			"Dory", "Dragana", "Druella", "Druilla", "Dulce", "Dunja", "Dyana", "Dyann", "Dyanna", "Dylan", "Eada",
			"Eartha", "Easter", "Ebony", "Eda", "Edda", "Edeline", "Eden", "Edith", "Editha", "Edithe", "Edlyn",
			"Edmee",
			"Edolie", "Edsel", "Effi", "Eglantina", "Eglantine", "Eike", "Eila", "Eileen", "Ela", "Elaina", "Elaine",
			"Elayna", "Elber", "Elberta", "Elda", "Eldrida", "Eleanor", "Elektra", "Elena", "Eleonora", "Eleonore",
			"Eleta",
			"Elfi", "Elfie", "Elfreda", "Elfrida", "Elfrieda", "Elfriede", "Elga", "Eliana", "Eliane", "Elicia",
			"Elienor",
			"Elin", "Elina", "Elinore", "Elisa", "Elisabet", "Elisabeth", "Elisabetta", "Elisamarie", "Elise", "Elisha",
			"Elishia", "Elissa", "Elita", "Eliza", "Elizabeth", "Elka", "Elke", "Ella", "Ellaine", "Ellayne", "Elle",
			"Ellen", "Elli", "Ellie", "Ellinor", "Elmina", "Eloisa", "Eloise", "Eloisee", "Elrica", "Elsa", "Elsbeth",
			"Else", "Elvira", "Elvire", "Elyse", "Elyssa", "Ema", "Emanuela", "Emanuele", "Ember", "Emele", "Emelina",
			"Emeline", "Emelka", "Emely", "Emelyne", "Emerald", "Emeraude", "Emerson", "Emilee", "Emilia", "Emilie",
			"Emily", "Emma", "Emmalee", "Emmaline", "Emmalyn", "Emmeline", "Emmi", "Emmy", "Ena", "Encarna",
			"Engelberga",
			"Engelbert", "Engelberta", "Engelbertha", "Engelberthe", "Enna", "Enrica", "Eri", "Erica", "Ericka",
			"Erika",
			"Erin", "Erma", "Erme", "Ermina", "Erminia", "Erminie", "Erna", "Ernesta", "Ernstina", "Esdras", "Esme",
			"Esmeralda", "Esmeraude", "Esperanza", "Esra", "Essence", "Estee", "Estefani", "Estefania", "Estefany",
			"Estella", "Estelle", "Ester", "Esther", "Estrella", "Estrid", "Etelka", "Ethel", "Ethelda", "Ethelinda",
			"Etheline", "Ethyl", "Ethylyn", "Etta", "Eudokia", "Eudoxia", "Eufemia", "Eugenia", "Eugenie", "Eulalie",
			"Euphemia", "Euphrasia", "Eusebia", "Ev", "Eva", "Eva-maria", "Evangelina", "Evangeline", "Evchen", "Eve",
			"Evelia", "Evelien", "Evelin", "Evelina", "Eveline", "Evelyn", "Evelyne", "Evette", "Evi", "Evita", "Evon",
			"Evonna", "Evonne", "Evony", "Ewelina", "Ezra", "Fabia", "Fabiana", "Fabienne", "Fabiola", "Fae", "Faith",
			"Faithe", "Fanchon", "Fanchone", "Fanetta", "Fanette", "Fantina", "Fantine", "Fara", "Faralda", "Farrah",
			"Fastrada", "Fatima", "Fatime", "Fatma", "Faun", "Fauna", "Faunia", "Fausta", "Faustina", "Faustine",
			"Favor",
			"Fawnia", "Fay", "Fayanna", "Faye", "Fayette", "Fayme", "Fealty", "Fearn", "Fearne", "Federica", "Federiga",
			"Fedora", "Felda", "Felecia", "Feli", "Felicia", "Felicienne", "Felicitas", "Felicity", "Felina",
			"Felizitas",
			"Ferdinanda", "Fern", "Fernanda", "Fernandina", "Ferne", "Fernly", "Fidelia", "Fifi", "Fifine", "Filicia",
			"Finetta", "Finja", "Finnja", "Fiona", "Fjodora", "Fleta", "Fleur", "Fleurette", "Flora", "Florence",
			"Florentia", "Florenzia", "Floressa", "Floretta", "Florette", "Flori", "Floria", "Floriana", "Florida",
			"Florina", "Florinda", "Florrie", "Fontanne", "Fortuna", "Fortunat", "Franca", "France", "Francena",
			"Francene",
			"Frances", "Francesca", "Francille", "Francina", "Francine", "Francoise", "Franja", "Franka", "Fransiska",
			"Franzi", "Franziska", "Frauke", "Frauwa", "Frawa", "Freda", "Freddie", "Freida", "Frida", "Frieda",
			"Friederika", "Friederike", "Fritzi", "Fritzie", "Gabi", "Gabriela", "Gabriele", "Gabriella", "Gabrielle",
			"Gaby", "Gaetana", "Gaetane", "Gail", "Gala", "Galatea", "Galatee", "Galateia", "Gale", "Galiana",
			"Galiena",
			"Galilea", "Galina", "Galla", "Gallia", "Ganja", "Garland", "Garnet", "Garnett", "Gatty", "Gay", "Gayle",
			"Gemma", "Genesis", "Geneva", "Geneve", "Genevie", "Genevieve", "Genevre", "Genia", "Genie", "Genivee",
			"Genovefa", "Genoveva", "Georgette", "Georgia", "Georgine", "Georgitte", "Geraldene", "Geraldine",
			"Geralyn",
			"Geralynn", "Gerda", "Gerde", "Gerdi", "Gerdie", "Geri", "Gerlind", "Gerlinde", "Gerlindis", "Germain",
			"Germaine", "Germana", "Gerti", "Gertraud", "Gertraude", "Gertraut", "Gertrud", "Gertrude", "Gertrudis",
			"Gesa",
			"Gescha", "Gia", "Giana", "Gianna", "Gigi", "Gilla", "Gillian", "Gina", "Ginette", "Gioa", "Giovanna",
			"Gisela",
			"Gisele", "Gisella", "Giselle", "Gisselle", "Gitta", "Gitte", "Giuletta", "Giulia", "Giuliana", "Giulietta",
			"Giuseppa", "Giustina", "Gleda", "Gloria", "Gloriana", "Gloriosa", "Godiva", "Golda", "Goldie", "Grace",
			"Gracie", "Graciela", "Gracy", "Grania", "Gratia", "Grazia", "Graziella", "Greta", "Gretchen", "Grete",
			"Gretel", "Grethe", "Gretti", "Grit", "Gritt", "Grizelda", "Guadalupe", "Gudrun", "Gudrune", "Gudula",
			"Guilla",
			"Gulja", "Gunda", "Gunde", "Gundel", "Gundela", "Gundula", "Gustava", "Gustave", "Gwend", "Gwenda",
			"Gwendolin",
			"Gwendolina", "Gwendoline", "Gwendolyn", "Gypsy", "Gytha", "Hadley", "Hailee", "Hailey", "Hailie",
			"Haleigh",
			"Halette", "Haley", "Halfreida", "Halfrida", "Halfrieda", "Halie", "Halle", "Hallie", "Halsey", "Hana",
			"Hanna",
			"Hannah", "Hannchen", "Hanne", "Hannele", "Hannelore", "Hanni", "Hanrietta", "Hanriette", "Harley",
			"Harmony",
			"Harriet", "Harriett", "Harrietta", "Harriette", "Harva", "Harvelle", "Harvina", "Harvine", "Hattie",
			"Hatty",
			"Hauke", "Haven", "Hayden", "Haylee", "Hayleigh", "Hayley", "Haylie", "Hazel", "Heather", "Heaven", "Hedda",
			"Heddi", "Heddy", "Hedi", "Hedvige", "Hedwig", "Hedy", "Heide", "Heidi", "Heidrun", "Heidy", "Heike",
			"Heinrike", "Helaine", "Helen", "Helena", "Helene", "Helga", "Helma", "Helmi", "Heloise", "Hemma",
			"Hendrikje",
			"Henni", "Henrietta", "Henriette", "Henrika", "Henrike", "Hera", "Herma", "Hermia", "Hermine", "Hermione",
			"Hertha", "Hester", "Hetdt", "Hettie", "Hidie", "Hilaire", "Hild", "Hilda", "Hilde", "Hildegard",
			"Hildegarde",
			"Hildemar", "Hildie", "Hildreth", "Hildretha", "Hilke", "Hilma", "Hollace", "Hollee", "Holli", "Hollie",
			"Holly", "Hollye", "Honey", "Honore", "Hope", "Huberta", "Hubertha", "Huberthe", "Hubertina", "Hubertine",
			"Huette", "Hugette", "Huguetta", "Hulda", "Hunter", "Ida", "Idda", "Idelia", "Idina", "Idona", "Ignatia",
			"Iken", "Ila", "Ilga", "Iliana", "Iljana", "Ilka", "Ilona", "Ilonka", "Ilse", "Imani", "Imke", "Immaculata",
			"Immakulata", "Ina", "India", "Indira", "Indra", "Ine", "Ineke", "Ines", "Inga", "Inge", "Ingeborg",
			"Ingrid",
			"Inka", "Inke", "Inken", "Innocentia", "Innozentia", "Insa", "Iphigenie", "Ira", "Ireland", "Irena",
			"Irene",
			"Irina", "Irinka", "Iris", "Irma", "Irme", "Irmengard", "Irmgard", "Irmina", "Irmine", "Isa", "Isabeau",
			"Isabel", "Isabela", "Isabell", "Isabella", "Isabelle", "Isalda", "Isis", "Isolda", "Isolde", "Isotta",
			"Ita",
			"Itzel", "Iva", "Ivana", "Ivanka", "Ivona", "Ivonne", "Ivy", "Iwana", "Iwanka", "Iwanna", "Iyana", "Iyanna",
			"Izabella", "Jacalyn", "Jacey", "Jacinthe", "Jackeline", "Jackie", "Jacky", "Jaclyn", "Jacqualine",
			"Jacqueleen", "Jacqueline", "Jacquelyn", "Jacquelyne", "Jacquelynne", "Jacquenetta", "Jacquenette",
			"Jacqui",
			"Jada", "Jade", "Jaden", "Jadwiga", "Jadyn", "Jaelyn", "Jaida", "Jaiden", "Jaidyn", "Jailyn", "Jaime",
			"Jakayla", "Jaliyah", "Jalyn", "Jalynn", "Jamie", "Jamie-Lee", "Jamya", "Jana", "Janae", "Jane", "Janelle",
			"Janessa", "Janet", "Janette", "Janice", "Janie", "Janika", "Janina", "Janine", "Janiya", "Janka",
			"Jaquelin",
			"Jaqueline", "Jarvia", "Jasmeen", "Jasmin", "Jasmina", "Jasmine", "Jasmyn", "Jasmyne", "Jaycee", "Jayda",
			"Jayde", "Jayden", "Jayla", "Jaylene", "Jaylin", "Jaylyn", "Jaylynn", "Jazlyn", "Jazmin", "Jazmine",
			"Jazmyn",
			"Jazmyne", "Jazzmine", "Jazzmyn", "Jean", "Jeana", "Jeane", "Jeanee", "Jeanetta", "Jeanette", "Jeanice",
			"Jeanie", "Jeanina", "Jeanine", "Jeanna", "Jeanne", "Jeannette", "Jeannie", "Jeannine", "Jeanny", "Jeena",
			"Jehane", "Jelena", "Jelenka", "Jelika", "Jella", "Jena", "Jenette", "Jenifer", "Jenina", "Jenine", "Jenna",
			"Jenni", "Jennifer", "Jennine", "Jenny", "Jeri", "Jerica", "Jessamina", "Jessamine", "Jessamyn", "Jessica",
			"Jessie", "Jessika", "Jettchen", "Jette", "Jewel", "Jewell", "Jill", "Jillian", "Jimena", "Jineen", "Joan",
			"Joana", "Joanna", "Joanne", "Jocelin", "Jocelina", "Joceline", "Jocelyn", "Jocelyne", "Jocelynn",
			"Joeliyn",
			"Joell", "Joella", "Joelle", "Joellen", "Joelyn", "Johana", "Johanna", "Joi", "Joia", "Joie", "Jola",
			"Jolanda",
			"Jolande", "Jolanta", "Jolante", "Jolantha", "Jolanthe", "Jolee", "Joleigh", "Joli", "Jolie", "Jolien",
			"Jonesy", "Jonna", "Jordan", "Jordane", "Jordyn", "Josalyn", "Josalynn", "Joscelyn", "Josefa", "Josefin",
			"Josefina", "Josefine", "Joselyn", "Josepha", "Josephe", "Josephina", "Josephine", "Josette", "Josie",
			"Josilyn", "Josina", "Joslin", "Joslyn", "Journey", "Jovita", "Jowita", "Joy", "Joy  Joyce", "Joya",
			"Joyann",
			"Joyanna", "Joyanne", "Joyce", "Joyelle", "Jozlyn", "Juana", "Juanita", "Judit", "Judith", "Juditha",
			"Judy",
			"Julchen", "Jule", "Julee", "Juleen", "Julia", "Juliana", "Juliane", "Julianna", "Julianne", "Julie",
			"Julienne", "Juliet", "Julietta", "Juliette", "Julika", "Julissa", "Julita", "June", "Justeen", "Justice",
			"Justina", "Justine", "Justyne", "Jutta", "Jutte", "Kacie", "Kaela", "Kaelyn", "Kaia", "Kaila", "Kailee",
			"Kailey", "Kailyn", "Kaitlin", "Kaitlyn", "Kaitlynn", "Kaiya", "Kaleigh", "Kaley", "Kali", "Kaliyah",
			"Kallie",
			"Kalyn", "Kamille", "Kamryn", "Kara", "Karcsi", "Karen", "Kari", "Karin", "Karina", "Karissa", "Karla",
			"Karlee", "Karley", "Karli", "Karlie", "Karlotta", "Karly", "Karola", "Karolin", "Karolina", "Karoline",
			"Karoly", "Kasandra", "Kasey", "Kassandra", "Kassidy", "Katarina", "Kate", "Katelin", "Katelyn", "Katelynn",
			"Katerina", "Katharina", "Katharine", "Kathe", "Katherine", "Kathi", "Kathleen", "Kathrin", "Kathrina",
			"Kathrine", "Kathryn", "Kathy", "Katie", "Katinka", "Katja", "Katlyn", "Katriane", "Katrin", "Katrina",
			"Katy",
			"Kaya", "Kayla", "Kaylah", "Kaylee", "Kayleigh", "Kayley", "Kayli", "Kaylie", "Kaylin", "Kaylyn", "Kaylynn",
			"Keeley", "Keely", "Keila", "Keira", "Kelli", "Kellie", "Kelly", "Kelsey", "Kelsi", "Kelsie", "Kelsy",
			"Kemble",
			"Kendal", "Kendall", "Kendra", "Kenia", "Kenna", "Kennedi", "Kennedy", "Kenya", "Kenzie", "Kersten",
			"Kersti",
			"Kerstin", "Keyla", "Kezia", "Kiana", "Kianna", "Kiara", "Kiera", "Kierra", "Kiersten", "Kiley", "Kim",
			"Kimball", "Kimbell", "Kimberley", "Kimberly", "Kimble", "Kimby", "Kimmey", "Kimmi", "Kimmie", "Kimmy",
			"Kira",
			"Kirsten", "Kirstin", "Kiya", "Klara", "Klarina", "Klarinda", "Klarissa", "Klaudia", "Klementia",
			"Klementine",
			"Kleopatra", "Klothild", "Klothilde", "Konstantia", "Konstanza", "Konstanze", "Kora", "Kordula", "Korinna",
			"Kornelia", "Kourtney", "Kriemhild", "Kriemhilde", "Krimhild", "Krimhilde", "Krista", "Kristen",
			"Kristiane",
			"Kristin", "Kristina", "Krystal", "Kunigunda", "Kunigunde", "Kunissa", "Kya", "Kyla", "Kylee", "Kyleigh",
			"Kylie", "Kym", "Kymberly", "Kyra", "LaVergne", "Lace", "Lacee", "Lacene", "Lacey", "Laci", "Laciann",
			"Lacie",
			"Lacina", "Lacy", "Lacyann", "Laetitia", "Laila", "Lana", "Laney", "Lara", "Larissa", "Laura", "Laureen",
			"Laurel", "Lauren", "Laurene", "Laurentia", "Laurenzia", "Lauretta", "Laurette", "Laurina", "Laurine",
			"Lauryn",
			"Lavern", "Laverna", "Laverne", "Lavernia", "Lavonne", "Laycie", "Layla", "Lea", "Leah", "Leala", "Lealia",
			"Leander", "Leanna", "Lee", "Leefka", "Leefke", "Lei", "Leia", "Leigh", "Leila", "Leilani", "Leilena",
			"Lela",
			"Lena", "Lenchen", "Lene", "Leni", "Lenka", "Lenore", "Leoba", "Leoda", "Leola", "Leona", "Leonarda",
			"Leonda",
			"Leondra", "Leondrea", "Leone", "Leonela", "Leonelle", "Leonie", "Leonore", "Leontina", "Leontyne",
			"Leopolda",
			"Leopoldina", "Leopoldine", "Leota", "Lesley", "Leslie", "Lesly", "Leticia", "Letje", "Letya", "Lexi",
			"Lexie",
			"Lexus", "Leyla", "Lia", "Liana", "Liane", "Libby", "Liberty", "Lidda", "Liealia", "Lies", "Liesel",
			"Liesl",
			"Lil", "Lila", "Lili", "Lilian", "Liliana", "Liliane", "Lilith", "Lilli", "Lillian", "Lilliana", "Lillie",
			"Lilly", "Lilo", "Lily", "Lina", "Linchen", "Linda", "Lindsay", "Lindsey", "Line", "Linette", "Lioba",
			"Liriene", "Lirienne", "Lisa", "Lisbeth", "Lise", "Liselotte", "Lisenka", "Lisetta", "Lisette", "Lissette",
			"Lissy", "Litzy", "Livi", "Livia", "Livie", "Livvi", "Lizbeth", "Lizeth", "Lizette", "Lizzy", "Locke",
			"Loella",
			"Logan", "Logestilla", "Logistilla", "Lola", "Lolo", "London", "Lone", "Loraina", "Loraine", "Lorayne",
			"Lorchen", "Lore", "Lorelei", "Lorelia", "Lorelie", "Loren", "Lorena", "Lorenza", "Loretta", "Lorette",
			"Lorin",
			"Lorraina", "Lorraine", "Lottchen", "Lotte", "Lotye", "Louanna", "Louanne", "Louella", "Louisa", "Louise",
			"Lourdes", "Love", "Loveleen", "Lovie", "Luana", "Luane", "Luca", "Lucette", "Lucia", "Luciana", "Luciane",
			"Lucie", "Lucienne", "Lucile", "Lucilla", "Lucille", "Lucrece", "Lucy", "Ludmila", "Ludmilla", "Luella",
			"Luelle", "Luisa", "Luise", "Lukretia", "Lulu", "Luna", "Lundy", "Lunette", "Lupe", "Lurleen", "Luwana",
			"Luwanna", "Luwanne", "Luz", "Luzia", "Luzie", "Lydia", "Lydie", "Lyndsey", "Lynette", "Lynn", "Lynn-Marie",
			"Lynnette", "Lyonette", "Lyra", "Lyric", "Mabelle", "Macee", "Macey", "Maci", "Macie", "Mackenzie", "Macy",
			"Madalene", "Madalyn", "Madalynn", "Maddison", "Maddy", "Madeleina", "Madeleine", "Madelina", "Madeline",
			"Madelon", "Madelyn", "Madelynn", "Madie", "Madilyn", "Madisen", "Madison", "Madisyn", "Madita", "Madlen",
			"Madolen", "Mady", "Madyson", "Mae", "Maegan", "Maelee", "Maelynn", "Maeve", "Mafalda", "Magda", "Magdalen",
			"Magdalena", "Maggie", "Maggy", "Magnolia", "Mai", "Maia", "Maida", "Maidel", "Maidie", "Maidy", "Maika",
			"Maike", "Maiken", "Maiolaine", "Maira", "Mairin", "Maisie", "Maitane", "Maiya", "Maja", "Majori",
			"Makaila",
			"Makayla", "Makena", "Makenna", "Makenzie", "Malchen", "Male", "Maleah", "Malenka", "Malia", "Malica",
			"Malin",
			"Malina", "Maliyah", "Mallorie", "Mallory", "Manda", "Mandy", "Manette", "Manhattan", "Mania", "Manja",
			"Manjana", "Manny", "Manon", "Manuela", "Manuella", "Mara", "Marcelin", "Marcelina", "Marceline",
			"Marcella",
			"Marcelle", "Marcellia", "Marcellina", "Marchelle", "Marcie", "Maree", "Mareen", "Marei", "Mareike",
			"Marelda",
			"Maren", "Marene", "Marga", "Margaret", "Margareta", "Margarete", "Margaretha", "Margarita", "Margaux",
			"Margeaux", "Margery", "Margit", "Margo", "Margot", "Margret", "Marguerite", "Maria", "Mariah", "Mariam",
			"Marian", "Mariana", "Mariane", "Marianna", "Marianne", "Maribel", "Marie", "Mariechen", "Mariela",
			"Mariele",
			"Mariella", "Marielle", "Marietta", "Mariette", "Marija", "Marika", "Marike", "Marilena", "Marilyn",
			"Marina",
			"Marinka", "Marion", "Mariona", "Marionna", "Marisa", "Marisol", "Marissa", "Marit", "Maritza",
			"Marjolaina",
			"Marlee", "Marlene", "Marley", "Marlis", "Marlon", "Marquisa", "Marquise", "Marquisha", "Marta", "Marteena",
			"Martha", "Martina", "Martine", "Marveille", "Marvela", "Marvella", "Marvelle", "Mary", "Maryam", "Maryl",
			"Maryvonne", "Maschinka", "Masha", "Mateja", "Mathilda", "Mathilde", "Matilda", "Matilde", "Mattie",
			"Matty",
			"Maud", "Maude", "Maura", "Maureen", "Maurelle", "Maurina", "Maurine", "Mavis", "Mavise", "Maxime",
			"Maxine",
			"May", "Maya", "Mayda", "Mayra", "Mckayla", "Mckenna", "Mckenzie", "Meadow", "Meagan", "Meaghan",
			"Mechthild",
			"Mechthilde", "Mechtild", "Megan", "Meghan", "Meika", "Meike", "Meiken", "Mela", "Melaina", "Melaine",
			"Melanee", "Melania", "Melanie", "Melany", "Melina", "Melinda", "Meline", "Melisande", "Melissa", "Melitta",
			"Melodie", "Melody", "Melusina", "Mercedes", "Mercer", "Merci", "Mercy", "Meredith", "Meret", "Meriel",
			"Merla",
			"Merle", "Merlyn", "Merryl", "Meryl", "Meta", "Meyla", "Mia", "Mia  Miah", "Miah", "Micaela", "Micah",
			"Michaela", "Michela", "Michele", "Micheline", "Michella", "Michelle", "Mieke", "Miette", "Mignon",
			"Mignonette", "Mikaela", "Mikayla", "Milena", "Milina", "Millicent", "Millicente", "Millie", "Milva",
			"Mimi",
			"Mina", "Minchen", "Minda", "Mindy", "Mine", "Minerva", "Minetta", "Minette", "Mingo", "Minna", "Minne",
			"Minnie", "Minta", "Mira", "Mirabell", "Mirabella", "Mirabelle", "Miracle", "Miranda", "Mireille",
			"Mirella",
			"Mireya", "Miriam", "Mirielle", "Mirjam", "Mirla", "Mirth", "Missie", "Missy", "Missye", "Mistee", "Mistey",
			"Mistique", "Misty", "Miya", "Mollie", "Molly", "Mona", "Mone", "Moni", "Monica", "Monika", "Moniqua",
			"Monique", "Monja", "Monserrat", "Montana", "Moreen", "Morgan", "Moriah", "Munira", "Muriel", "Musetta",
			"Musette", "Mya", "Myah", "Mychele", "Mychelle", "Myra", "Myrla", "Myrna", "Mystique", "Nada", "Nadeen",
			"Nadia", "Nadina", "Nadine", "Nadinka", "Nadja", "Nadjeschda", "Naeva", "Nafia", "Naima", "Nan", "Nancey",
			"Nanci", "Nancie", "Nancy", "Nane", "Nanette", "Nanine", "Nann", "Nannerl", "Nannette", "Nanni", "Nanon",
			"Naomi", "Naomy", "Nara", "Narcisse", "Nastasia", "Nastjenka", "Nata", "Natalee", "Natalia", "Natalie",
			"Natalii", "Nataly", "Natascha", "Natasha", "Natassja", "Nathalee", "Nathalia", "Nathalie", "Nathaly",
			"Natuche", "Nayeli", "Neeske", "Neisa", "Nele", "Nella", "Nelli", "Nelly", "Nesrin", "Nessie", "Nettchen",
			"Netti", "Nevaeh", "Nia", "Nichol", "Nichole", "Nicki", "Nicky", "Nicola", "Nicole", "Nicoletta",
			"Nicolette",
			"Nicoline", "Nicolle", "Nikki", "Nikoletta", "Nikolina", "Nikoline", "Nila", "Nina", "Ninette", "Ninon",
			"Nissie", "Nissy", "Nixie", "Noa", "Noel", "Noele", "Noelia", "Noell", "Noella", "Noelle", "Noemi",
			"Noemie",
			"Nora", "Norberta", "Norberte", "Norbertha", "Norberthe", "Nordica", "Norma", "Nuria", "Nya", "Nyah",
			"Nyasia",
			"Nyla", "Nynette", "Odalys", "Odeletta", "Odelette", "Odetta", "Odette", "Odila", "Odile", "Odilia",
			"Olave",
			"Olga", "Olive", "Olivia", "Ollie", "Olva", "Olympe", "Olympia", "Olympie", "Oola", "Ophelia", "Ophelie",
			"Orane", "Orania", "Oriel", "Orla", "Orlanda", "Orlande", "Orlena", "Orlene", "Orlina", "Ornella", "Orsina",
			"Orsine", "Orsola", "Orsolya", "Ortelia", "Orva", "Ottilia", "Ottilie", "Oxana", "Page", "Paige", "Palma",
			"Palmiera", "Palmira", "Palmyra", "Paloma", "Pamela", "Pamelina", "Pandora", "Pansy", "Paola", "Paris",
			"Parker", "Parnella", "Pascala", "Pascale", "Pascaline", "Pasclina", "Patience", "Patrice", "Patricia",
			"Patrizia", "Paula", "Pauletta", "Paulette", "Paulina", "Pauline", "Pawla", "Payton", "Pearl", "Peggy",
			"Penelope", "Penny", "Pensee", "Pepi", "Perla", "Petra", "Peyton", "Philina", "Philine", "Philippa",
			"Philippe",
			"Philippina", "Philippine", "Phillipa", "Philomela", "Philomele", "Philomena", "Philomene", "Phinchen",
			"Phoebe", "Pia", "Pia-Marie", "Piera", "Pierretta", "Pierrette", "Pilar", "Piper", "Pleasance", "Poppy",
			"Precious", "Presley", "Princess", "Prisca", "Priscila", "Priscilla", "Priska", "Priszilla", "Prunella",
			"Prunellie", "Pyper", "Queena", "Quendolin", "Questa", "Quinn", "Rabea", "Rabia", "Rachael", "Rachel",
			"Rachele", "Rachelle", "Rachil", "Radella", "Radmila", "Radmilla", "Radomila", "Raegan", "Raffaela",
			"Rahel",
			"Raina", "Raison", "Raissa", "Rama", "Ramona", "Ramonda", "Raphaela", "Raphaele", "Raquel", "Ratna",
			"Raven",
			"Raymonda", "Raymonde", "Rayna", "Rea", "Reagan", "Reanna", "Rebeca", "Rebecca", "Rebekah", "Rebekka",
			"Recha",
			"Reese", "Regan", "Regina", "Regine", "Regula", "Reilly", "Reina", "Reine", "Relyea", "Renata", "Renate",
			"Rene", "Renee", "Reyna", "Rhea", "Rhiannon", "Ria", "Riana", "Rianna", "Rica", "Ricarda", "Richarda",
			"Richelle", "Rickie", "Ricky", "Rieke", "Rikchen", "Rike", "Riley", "Rilla", "Rille", "Rillette", "Rita",
			"Riva", "Rive", "Riya", "Ro", "Robbin", "Roberta", "Roberte", "Robertina", "Robin", "Robina", "Robine",
			"Robinetta", "Robinette", "Robyn", "Rocio", "Roddie", "Roddy", "Roderica", "Rodericka", "Roesia", "Rohais",
			"Roial", "Rola", "Rolanda", "Rolande", "Romaine", "Romana", "Romhilda", "Romhilde", "Romilda", "Romilde",
			"Romy", "Ronalda", "Ronalde", "Ronja", "Ronnie", "Ronny", "Rosa", "Rosalba", "Rosalie", "Rosalinde",
			"Rosamonde", "Rosamunde", "Rosanna", "Rose", "Rosegrethe", "Rosella", "Rosellina", "Rosemarie", "Rosemary",
			"Rosi", "Rosina", "Rosine", "Rosita", "Roswita", "Roswitha", "Roterica", "Roux", "Rownan", "Roxana",
			"Roxane",
			"Roxanne", "Roya", "Royale", "Rubie", "Ruby", "Rudella", "Rudelle", "Ruperta", "Rut", "Ruth", "Ryan",
			"Ryann",
			"Rylee", "Ryleigh", "Rylie", "Sabina", "Sabine", "Sabrina", "Sade", "Sadie", "Sage", "Sahra", "Saige",
			"Salene",
			"Sally", "Salma", "Salome", "Salvina", "Salwa", "Samantha", "Samara", "Samira", "Sandra", "Sandria",
			"Sandrina",
			"Sandrine", "Sandy", "Sanetra", "Sanne", "Saphira", "Sara", "Sarah", "Sarahi", "Sarai", "Sarina", "Sascha",
			"Sasha", "Saskia", "Sasna", "Satin", "Savana", "Savanah", "Savanna", "Savannah", "Saxona", "Scarlet",
			"Scarlett", "Searlait", "Selby", "Selden", "Seldon", "Selena", "Selene", "Selima", "Selina", "Selma",
			"Selwin",
			"Selwyn", "Serafin", "Serafina", "Seraphin", "Seraphina", "Seraphine", "Serena", "Serenity", "Serfine",
			"Serhilda", "Serhilde", "Serilda", "Serilde", "Shakira", "Shalina", "Shalyna", "Shana", "Shandy", "Shania",
			"Shanice", "Shaniya", "Shannon", "Shantala", "Shanton", "Sharla", "Sharleen", "Sharlene", "Sharon",
			"Shawna",
			"Shayla", "Shaylee", "Shayna", "Shea", "Sheila", "Shelby", "Sherey", "Sherlie", "Sheryl", "Sheyla", "Shir",
			"Shirl", "Shirlee", "Shirleen", "Shirleigh", "Shirley", "Shreya", "Shurl", "Shurlie", "Shyann", "Shyanne",
			"Sibilla", "Sibille", "Sibyla", "Sibylla", "Sibylle", "Sidney", "Sidonia", "Sidonie", "Sienna", "Sierra",
			"Sigfreda", "Sigfrieda", "Sigfriede", "Sigrid", "Sigrun", "Silana", "Silja", "Silka", "Silke", "Silvana",
			"Silvetta", "Silvette", "Silvia", "Silvina", "Simona", "Simone", "Simonetta", "Simonette", "Sina", "Sinja",
			"Sinje", "Sissi", "Sky", "Skye", "Skyla", "Skylar", "Skyler", "Slainie", "Slania", "Slanie", "Sofia",
			"Sofie",
			"Solaina", "Solaine", "Solange", "Solvig", "Sonia", "Sonja", "Sonya", "Sophia", "Sophie", "Soreen",
			"Sorren",
			"Stacey", "Stacy", "Stefana", "Stefania", "Stefanie", "Steffi", "Stella", "Stephania", "Stephanie",
			"Stephany",
			"Stina", "Stine", "Storm", "Storme", "Stormie", "Stormy", "Suleima", "Summer", "Susan", "Susana", "Susane",
			"Susanna", "Susanne", "Suse", "Susen", "Susi", "Susie", "Suzanne", "Suzette", "Suzy", "Svana", "Svea",
			"Svenja",
			"Swantje", "Swea", "Swenja", "Sydnee", "Sydney", "Sydni", "Sydnie", "Sylke", "Sylvia", "Sylvie", "Tabea",
			"Tabitha", "Tait", "Taite", "Taitum", "Talia", "Talida", "Talika", "Taliyah", "Tallis", "Tamar", "Tamara",
			"Tamia", "Tamira", "Tania", "Tanita", "Taniya", "Tanja", "Tanjura", "Tanya", "Tara", "Tara-Ann", "Taryn",
			"Tat",
			"Tatiana", "Tatjana", "Tatum", "Tatyana", "Tavia", "Taya", "Tayler", "Taylor", "Tayte", "Teagan", "Teite",
			"Tempeste", "Teresa", "Terese", "Tereza", "Tess", "Tessa", "Thabita", "Thalia", "Thea", "Theodora",
			"Theres",
			"Theresa", "Therese", "Theresia", "Theresina", "Thery", "Thilde", "Thistle", "Tia", "Tiana", "Tianna",
			"Tiara",
			"Tibelda", "Tierra", "Tiffanie", "Tiffany", "Tiffney", "Tilda", "Tilly", "Timea", "Tina", "Tinchen", "Tine",
			"Tinette", "Tizia", "Tiziana", "Tokessa", "Toni", "Tonja", "Tori", "Tosca", "Toska", "Tracy", "Trine",
			"Trinetta", "Trinette", "Trinity", "Trista", "Tristan", "Trix", "Trixi", "Tru", "Trudchen", "Trude",
			"Trudel",
			"Trudi", "Trudie", "Trudy", "Tuesday", "Tyler", "Tyra", "Uda", "Udele", "Udella", "Udelle", "Uka", "Ula",
			"Ulita", "Ulitta", "Uljana", "Ulla", "Ulli", "Ulrica", "Ulrika", "Ulrike", "Ulva", "Undine", "Unique",
			"Urania",
			"Urith", "Ursel", "Ursina", "Ursine", "Ursula", "Urte", "Uschi", "Uta", "Ute", "Vafara", "Vala", "Valborga",
			"Valburga", "Valda", "Valentina", "Valentine", "Valeraine", "Valere", "Valeri", "Valeria", "Valeriana",
			"Valeriane", "Valerie", "Valerien", "Valeska", "Valida", "Vallerie", "Vanadis", "Vanesa", "Vanessa",
			"Vania",
			"Vanja", "Vanni", "Varinka", "Vedetta", "Velda", "Velma", "Veloy", "Veneta", "Venetia", "Venetta", "Venus",
			"Vera", "Verena", "Verona", "Verone", "Veronica", "Veronika", "Veronique", "Vicky", "Victoria", "Victorina",
			"Victorine", "Vignetta", "Vignette", "Viktoria", "Viktorin", "Viktorina", "Viktorine", "Villetta",
			"Villette",
			"Vina", "Vineta", "Vinka", "Viola", "Violet", "Violett", "Violetta", "Violette", "Viollette", "Virginia",
			"Virginie", "Vittoria", "Vivian", "Viviana", "Viviane", "Vivien", "Vivienne", "Voleta", "Voletta", "Vroni",
			"Walborga", "Walburg", "Walburga", "Walburge", "Walda", "Waldburg", "Walli", "Wally", "Walpurgis",
			"Waltraud",
			"Wanda", "Wandie", "Wandis", "Wanja", "Warda", "Warenka", "Welda", "Wencke", "Wenda", "Wendeline", "Wendy",
			"Wenke", "Whitney", "Wiba", "Wibeke", "Wibke", "Wiebke", "Wigberta", "Wileen", "Wilf", "Wilfiede",
			"Wilfreda",
			"Wilfreida", "Wilfrieda", "Wilhelma", "Wilhelmina", "Wilhelmine", "Willa", "Willow", "Wilma", "Wilona",
			"Winifred", "Winifrieda", "Winnie", "Winny", "Winola", "Winona", "Winter", "Xandra", "Xaveria", "Xaverine",
			"Xaviere", "Xavierra", "Xavierre", "Xena", "Xenia", "Ximena", "Xiomara", "Yadira", "Yamina", "Yara",
			"Yaren",
			"Yasmin", "Yasmina", "Yasmine", "Yazmin", "Yedda", "Yelena", "Yesenia", "Yessenia", "Yetta", "Ynes", "Ynez",
			"Yola", "Yoland", "Yolanda", "Yolande", "Yolanthe", "Yolonda", "Ysabel", "Yseult", "Yuliana", "Yuria",
			"Yvette",
			"Yvonna", "Yvonne", "Zaida", "Zaina", "Zara", "Zarah", "Zaria", "Zeider", "Zelda", "Zena", "Zenobia",
			"Zenzi",
			"Zerelda", "Zerla", "Zerlina", "Zerline", "Zilli", "Zina", "Zoe", "Zoey", "Zoie", "Zorra", "Zuri", "Zuria",
			"Zurie"]

	def generate_masculine(self):
		name_component = choice(self.nm83)
		return name_component.title()

	def generate_feminine(self):
		name_component = choice(self.nm84)
		return name_component.title()

	def generate_surname(self):
		name_component = choice(self.nm21)
		name_component2 = choice(self.nm22)
		return (name_component + name_component2).title()


# region humans
class Calashite(Human):
	nm1 = ["", "", "b", "bh", "f", "h", "j", "kh", "m", "n", "nh", "r", "rh", "s", "z"]
	nm2 = ["a", "e", "u", "a", "e", "u", "a", "e", "u", "i", "ei"]
	nm3 = ["b", "d", "hm", "hn", "hl", "kh", "l", "m", "rd", "r", "s", "sh", "z"]
	nm4 = ["d", "m", "n", "r"]
	nm5 = ["", "", "c", "f", "h", "j", "m", "n", "r", "s", "sh", "y", "z"]
	nm6 = ["a", "e", "u", "a", "e", "u", "o", "o", "i", "i", "ei"]
	nm7 = ["d", "f", "hn", "hl", "hm", "hr", "l", "m", "n", "p", "r", "s", "sh", "sm", "sn", "t", "v", "z"]
	nm8 = ["h", "l"]
	nm9 = ["b", "bh", "c", "d", "dh", "h", "j", "kh", "m", "n", "p", "r", "rh", "sh", "z"]
	nm10 = ["a", "e", "i", "o", "u", "a", "e", "i", "o", "u", "a", "e", "i", "o", "u", "a", "a", "a", "ei"]
	nm11 = ["d", "h", "hr", "hl", "k", "kh", "l", "m", "mm", "n", "nn", "ss", "st", "sh"]
	nm12 = ["", "", "", "", "", "d", "l", "m", "n", "r"]

	def generate_surname(self):
		name_component = choice(self.nm9)
		name_component2 = choice(self.nm10)
		name_component3 = choice(self.nm11)
		name_component4 = choice(self.nm10)
		name_component5 = choice(self.nm12)
		lname = name_component + name_component2 + name_component3 + name_component4 + name_component5
		return lname

	def generate_masculine(self):
		name_component = choice(self.nm1)
		name_component2 = choice(self.nm2)
		name_component3 = choice(self.nm3)
		name_component4 = choice(self.nm2)
		name_component5 = choice(self.nm4)
		nMs = name_component + name_component2 + name_component3 + name_component4 + name_component5
		return nMs

	def generate_feminine(self):
		i = choice(range(0, 2))

		name_component = choice(self.nm5)
		name_component2 = choice(self.nm6)
		name_component3 = choice(self.nm7)
		name_component4 = choice(self.nm6)
		name_component5 = choice(self.nm8)
		if i == 0:
			name_component6 = choice(self.nm7)
			name_component7 = choice(self.nm6)
			nMs = name_component + name_component2 + name_component3 + name_component4 + name_component6 + name_component7 + name_component5
		else:
			nMs = name_component + name_component2 + name_component3 + name_component4 + name_component5

		return nMs

	def race_check(self):
		pass


class Chondathan(Human):
	# /* Chondathan */
	nm13 = ["", "b", "br", "d", "g", "gr", "h", "m", "n", "r", "st", "t", "v"]
	nm14 = ["a", "e", "i", "o", "u"]
	nm15 = ["", "br", "cr", "gr", "kv", "kr", "l", "ll", "ld", "lv", "nd", "ng", "nk", "nv", "rd", "rg", "rk", "rst",
			"rv",
			"v"]
	nm16 = ["", "", "", "d", "dd", "g", "l", "lm", "m", "n", "r", "rk", "rn"]
	nm17 = ["", "c", "j", "jh", "k", "l", "m", "n", "r", "s", "sh", "t"]
	nm18 = ["a", "e", "i", "o", "u", "a", "e", "i", "o", "u", "a", "e", "i", "o", "u", "a", "e", "i", "o", "u", "a",
			"e",
			"i", "o", "u", "ee", "ai", "ei", "ie"]
	nm19 = ["ch", "dr", "l", "ll", "lr", "ldr", "ls", "lz", "n", "ndr", "rl", "r", "rr", "rv", "ss", "sr", "sv", "w",
			"z",
			"zz", "zn"]
	nm20 = ["", "", "", "", "h", "l", "ll", "n"]
	nm21 = ["Axe", "Glow", "Blade", "Blood", "Bone", "Cloud", "Crag", "Crest", "Doom", "Dream", "Coven", "Elf", "Fern",
			"Feather", "Fire", "Fist", "Flame", "Forest", "Hammer", "Heart", "Hell", "Leaf", "Light", "Moon", "Rage",
			"River", "Rock", "Shade", "Shadow", "Shield", "Snow", "Spirit", "Star", "Steel", "Stone", "Swift", "Tree",
			"Whisper", "Wind", "Wolf", "Wood", "Gloom", "Glory", "Orb", "Ash", "Blaze", "Amber", "Autumn", "Barley",
			"Battle", "Bear", "Black", "Blue", "Boulder", "Bright", "Bronze", "Burning", "Cask", "Chest", "Cinder",
			"Clan",
			"Claw", "Clear", "Cliff", "Cold", "Common", "Crystal", "Dark", "Dawn", "Day", "Dead", "Death", "Deep",
			"Dew",
			"Dirge", "Distant", "Down", "Dragon", "Dusk", "Dust", "Eagle", "Earth", "Ember", "Even", "Far", "Flat",
			"Flint",
			"Fog", "Fore", "Four", "Free", "Frost", "Frozen", "Full", "Fuse", "Gold", "Horse", "Gore", "Grand", "Gray",
			"Grass", "Great", "Green", "Grizzly", "Hallow", "Hallowed", "Hard", "Hawk", "Haze", "Heavy", "Haven",
			"High",
			"Hill", "Holy", "Honor", "Forest", "Humble", "Hydra", "Ice", "Iron", "Keen", "Laughing", "Lightning",
			"Lion",
			"Lone", "Long", "Low", "Luna", "Marble", "Meadow", "Mild", "Mirth", "Mist", "Molten", "Monster", "Morning",
			"Moss", "Mountain", "Moon", "Mourn", "Mourning", "Night", "Noble", "Nose", "Oat", "Ocean", "Pale", "Peace",
			"Phoenix", "Pine", "Plain", "Pride", "Proud", "Pyre", "Rain", "Rapid", "Raven", "Red", "Regal", "Rich",
			"Rose",
			"Rough", "Rumble", "Rune", "Sacred", "Sage", "Saur", "Sea", "Serpent", "Sharp", "Silent", "Silver",
			"Simple",
			"Single", "Skull", "Sky", "Slate", "Smart", "Snake", "Soft", "Solid", "Spider", "Spring", "Stag", "Star",
			"Stern", "Still", "Storm", "Stout", "Strong", "Summer", "Sun", "Tall", "Three", "Thunder", "Titan", "True",
			"Truth", "Marsh", "Tusk", "Twilight", "Two", "Void", "War", "Wheat", "Whit", "White", "Wild", "Winter",
			"Wise",
			"Wyvern", "Young", "Alpen", "Crest", "Crow", "Fallen", "Farrow", "Haven", "Master", "Nether", "Nickle",
			"Raven",
			"River", "Stone", "Tarren", "Terra", "Water", "Willow", "Wooden"]
	nm22 = ["axe", "glow", "beam", "blade", "blood", "bone", "cloud", "dane", "crag", "crest", "doom", "dream",
			"feather",
			"fire", "fist", "flame", "forest", "hammer", "heart", "hell", "leaf", "light", "moon", "rage", "river",
			"rock",
			"shade", "claw", "shadow", "shield", "snow", "spirit", "star", "steel", "stone", "swift", "tree", "whisper",
			"wind", "wolf", "wood", "gloom", "glory", "orb", "ash", "blaze", "arm", "arrow", "bane", "bash", "basher",
			"beard", "belly", "bend", "bender", "binder", "bleeder", "blight", "bloom", "blossom", "blower", "glade",
			"bluff", "bough", "bow", "brace", "braid", "branch", "brand", "breaker", "breath", "breeze", "brew",
			"bringer",
			"brook", "brow", "caller", "chaser", "reaper", "chewer", "cleaver", "creek", "crusher", "cut", "cutter",
			"dancer", "dew", "down", "draft", "dreamer", "drifter", "dust", "eye", "eyes", "fall", "fang", "flare",
			"flaw",
			"flayer", "flow", "follower", "flower", "force", "forge", "fury", "gaze", "gazer", "gem", "gleam", "glide",
			"grain", "grip", "grove", "guard", "gust", "hair", "hand", "helm", "hide", "horn", "hunter", "jumper",
			"keep",
			"keeper", "killer", "lance", "lash", "less", "mane", "mantle", "mark", "maul", "maw", "might", "more",
			"mourn",
			"oak", "ore", "peak", "pelt", "pike", "punch", "reaver", "rider", "ridge", "ripper", "roar", "run",
			"runner",
			"scar", "scream", "scribe", "seeker", "shaper", "shard", "shot", "shout", "singer", "sky", "slayer",
			"snarl",
			"snout", "soar", "song", "sorrow", "spark", "spear", "spell", "spire", "splitter", "sprinter", "stalker",
			"steam", "stream", "strength", "stride", "strider", "strike", "striker", "sun", "surge", "sword", "sworn",
			"tail", "taker", "talon", "thorn", "tide", "toe", "track", "trap", "trapper", "vale", "valor", "vigor",
			"walker", "ward", "watcher", "water", "weaver", "whirl", "whisk", "winds", "wing", "woods", "wound",
			"brooke",
			"fall", "fallow", "horn", "root", "shine", "swallow", "thorne", "willow", "wood"]

	def generate_masculine(self):
		name_component = choice(self.nm13)
		name_component2 = choice(self.nm14)
		name_component3 = choice(self.nm15)
		name_component4 = choice(self.nm14)
		name_component5 = choice(self.nm16)

		while name_component3 == name_component:
			name_component3 = choice(self.nm15)

		nMs = name_component + name_component2 + name_component3 + name_component4 + name_component5
		return nMs

	def generate_feminine(self):
		i = choice(range(0, 2))

		name_component = choice(self.nm17)
		name_component2 = choice(self.nm18)
		name_component3 = choice(self.nm19)
		name_component4 = choice(self.nm18)
		name_component5 = choice(self.nm20)
		if i == 0:
			name_component6 = choice(self.nm19)
			name_component7 = choice(self.nm18)
			nMs = name_component + name_component2 + name_component3 + name_component4 + name_component6 + name_component7 + name_component5

		else:
			nMs = name_component + name_component2 + name_component3 + name_component4 + name_component5

		return nMs

	def generate_surname(self):
		# todo make this the default surname for multiple races
		name_component = choice(self.nm21)
		name_component2 = choice(self.nm22)

		while name_component == name_component2:
			name_component2 = choice(self.nm22)

		lname = name_component + name_component2

		return lname

	def race_check(self):
		pass


class Damaran(Human):
	# /* Damaran */
	nm23 = ["", "", "b", "br", "f", "g", "gl", "gr", "h", "k", "m", "n", "p", "r", "s", "v"]
	nm24 = ["a", "e", "i", "o"]
	nm25 = ["b", "br", "d", "dr", "dg", "g", "gr", "r", "rg", "rd", "rv", "s", "v", "z"]
	nm26 = ["f", "l", "m", "n", "r"]
	nm27 = ["c", "ch", "h", "k", "l", "m", "n", "r", "s", "t", "v", "z"]
	nm28 = ["h", "hn", "hr", "l", "lm", "lr", "ln", "n", "nn", "r", "rn", "rl", "rm", "t", "th", "thr", "z"]
	nm29 = ["", "", "", "", "", "", "h", "l", "n", "s"]
	nm30 = ["b", "ch", "d", "gr", "gl", "k", "m", "n", "r", "s", "sh", "st", "v"]
	nm31 = ["a", "e", "i", "o", "u"]
	nm32 = ["d", "dr", "k", "kr", "kn", "l", "m", "n", "r", "rg", "rk", "rn", "rd", "v", "vr", "z"]
	nm33 = ["dz", "g", "n", "rsk", "sk", "tsk", "v", "z"]

	def generate_masculine(self):
		i = choice(range(0, 1))
		name_component = choice(self.nm23)
		name_component2 = choice(self.nm24)
		name_component5 = choice(self.nm26)
		if i == 1:
			name_component3 = choice(self.nm25)
			name_component4 = choice(self.nm24)
			nMs = name_component + name_component2 + name_component3 + name_component4 + name_component5

		else:
			nMs = name_component + name_component2 + name_component5

		return nMs

	def generate_feminine(self):
		i = choice(range(0, 2))
		name_component = choice(self.nm27)
		name_component2 = choice(self.nm24)
		name_component5 = choice(self.nm29)
		if i == 0:
			name_component3 = choice(self.nm28)
			name_component4 = choice(self.nm24)
			nMs = name_component + name_component2 + name_component3 + name_component4 + name_component5
		else:
			nMs = name_component + name_component2 + name_component5

		return nMs

	def generate_surname(self):

		name_component = choice(self.nm21)
		name_component2 = choice(self.nm22)
		while name_component == name_component2:
			name_component2 = choice(self.nm22)

		lname = name_component + name_component2

		return lname

	def race_check(self):
		pass


class Illuskan(Human):
	# /* Illuskan */
	nm34 = ["", "", "", "bl", "br", "fr", "g", "gr", "l", "m", "r", "st", "str", "t", "tr", "v", "z"]
	nm35 = ["a", "e", "o", "u"]
	nm36 = ["ck", "dr", "dv", "gr", "gn", "lc", "ld", "lv", "lb", "m", "nn", "nd", "nv", "rd", "rc", "rk", "rb"]
	nm37 = ["m", "n", "r", "rth", "th"]
	nm38 = ["", "", "b", "c", "h", "k", "l", "m", "n", "r", "s", "v", "w", "z"]
	nm39 = ["fn", "fl", "fr", "g", "l", "lg", "lr", "m", "n", "r", "rh", "sh", "str", "th", "thr", "v", "vr"]
	nm40 = ["", "", "", "", "y"]

	def generate_masculine(self):
		i = choice(range(0, 2))

		name_component = choice(self.nm34)
		name_component2 = choice(self.nm35)
		name_component5 = choice(self.nm37)
		if i == 0:
			name_component3 = choice(self.nm36)
			name_component4 = choice(self.nm35)
			nMs = name_component + name_component2 + name_component3 + name_component4 + name_component5
		else:
			nMs = name_component + name_component2 + name_component5

		return nMs

	def generate_feminine(self):
		# todo bring over the mising nms
		i = choice(range(0, 2))

		name_component = choice(self.nm38)
		name_component2 = choice(self.nm24)
		name_component3 = choice(self.nm39)
		name_component4 = choice(self.nm24)
		name_component5 = choice(self.nm40)
		if i == 0:
			name_component6 = choice(self.nm39)
			name_component7 = choice(self.nm24)
			nMs = name_component + name_component2 + name_component3 + name_component4 + name_component6 + name_component7 + name_component5
		else:
			nMs = name_component + name_component2 + name_component3 + name_component4 + name_component5

		return nMs

	def generate_surname(self):
		# todo bring over the other nms

		name_component = choice(self.nm21)
		name_component2 = choice(self.nm22)
		while name_component == name_component2:
			name_component2 = choice(self.nm22)

		lname = name_component + name_component2

		return lname

	def race_check(self):
		pass


class Mulan(Human):
	# /* Mulan */
	nm43 = ["b", "d", "g", "h", "j", "k", "l", "m", "n", "r", "s", "t", "th", "v", "z"]
	nm44 = ["a", "e", "i", "o", "u", "a", "e", "i", "o", "u", "a", "e", "i", "o", "u", "a", "e", "i", "o", "u", "a",
			"e",
			"i", "o", "u", "io", "ao", "eo", "eu", "ue"]
	nm45 = ["d-k", "d-v", "k-d", "k-v", "k-m", "k-r", "m-k", "m-z", "m-v", "n-v", "n-z", "n-d", "r-k", "r-v", "r-z",
			"t-k",
			"r-d", "h-k", "h-z", "-k", "-d", "-m", "-n", "-v", "-z", "-t", "-r", "ch", "d", "h", "hp", "hk", "hv", "j",
			"k",
			"m", "n", "r", "rh", "t", "th", "v", "z", "ch", "d", "h", "hp", "hk", "hv", "j", "k", "m", "n", "r", "rh",
			"t",
			"th", "v", "z", "ch", "d", "h", "hp", "hk", "hv", "j", "k", "m", "n", "r", "rh", "t", "th", "v", "z"]
	nm46 = ["", "", "d", "f", "h", "k", "n", "r", "s", "th", "z"]
	nm47 = ["c", "ch", "f", "h", "k", "l", "m", "n", "r", "s", "t", "th", "v", "z"]
	nm48 = ["ch", "f", "fr", "h", "l", "m", "n", "ph", "s", "sh", "r", "th", "z", "zr", "zh"]
	nm49 = ["", "", "", "", "", "", "", "h", "s", "th"]
	nm50 = ["b", "d", "f", "h", "j", "l", "m", "n", "r", "s", "v", "z"]
	nm51 = ["a", "e", "i", "u", "a", "e", "i", "u", "a", "e", "i", "u", "a", "e", "i", "o", "u", "ue", "uu"]
	nm52 = ["cr", "ch", "hp", "hk", "hr", "j", "kr", "kd", "l", "lr", "ldr", "lt", "ltr", "nd", "nsk", "nkh", "nth",
			"ndr",
			"nkr", "nz", "pr", "pv", "th", "thr", "v", "vr", "z", "zr", "zd"]
	nm53 = ["b", "d", "ft", "fk", "hd", "hr", "hk", "k", "kt", "ld", "m", "t"]

	def generate_masculine(self):
		i = choice(range(0, 2))

		name_component = choice(self.nm43)
		name_component2 = choice(self.nm44)
		name_component3 = choice(self.nm45)
		name_component4 = choice(self.nm44)
		name_component5 = choice(self.nm46)
		if i == 0:
			name_component6 = choice(self.nm45)
			name_component7 = choice(self.nm44)
			nMs = name_component + name_component2 + name_component3 + name_component4 + name_component6 + name_component7 + name_component5
		else:
			nMs = name_component + name_component2 + name_component3 + name_component4 + name_component5

		return nMs

	def generate_feminine(self):
		# todo bring over the names
		i = choice(range(0, 2))

		name_component = choice(self.nm47)
		name_component2 = choice(self.nm14)
		name_component3 = choice(self.nm48)
		name_component4 = choice(self.nm14)
		name_component5 = choice(self.nm49)
		if i == 0:
			name_component6 = choice(self.nm48)
			name_component7 = choice(self.nm14)
			nMs = name_component + name_component2 + name_component3 + name_component4 + name_component6 + name_component7 + name_component5
		else:
			nMs = name_component + name_component2 + name_component3 + name_component4 + name_component5

		return nMs

	def generate_surname(self):
		i = choice(range(0, 2))

		name_component = choice(self.nm50)
		name_component2 = choice(self.nm51)
		name_component3 = choice(self.nm52)
		name_component4 = choice(self.nm51)
		name_component5 = choice(self.nm53)
		if i == 0:
			name_component6 = choice(self.nm52)
			name_component7 = choice(self.nm51)
			lname = name_component + name_component2 + name_component3 + name_component4 + name_component6 + name_component7 + name_component5
		else:
			lname = name_component + name_component2 + name_component3 + name_component4 + name_component5

		return lname

	def race_check(self):
		pass


class Rashemi(Human):
	# /* Rashemi */
	nm54 = ["b", "br", "d", "dr", "f", "g", "j", "k", "m", "r", "s", "sh", "t", "vl", "z"]
	nm55 = ["a", "e", "i", "o", "a", "e", "i", "o", "a", "e", "i", "o", "a", "e", "i", "o", "oo", "ou", "au"]
	nm56 = ["d", "dj", "j", "lm", "ld", "lv", "m", "mz", "mv", "n", "nz", "nd", "nr", "nd", "r", "rg", "rd", "rl", "rv",
			"rz", "sl", "sv", "sd", "th", "tv", "v", "z"]
	nm57 = ["c", "d", "k", "r", "s", "sk", "t"]
	nm58 = ["", "", "d", "f", "h", "l", "m", "n", "r", "s", "sh", "t", "th", "v", "y", "z"]
	nm59 = ["a", "e", "i", "u"]
	nm60 = ["ch", "dr", "dh", "f", "fr", "gr", "h", "ldr", "lm", "ln", "lv", "lr", "mm", "mz", "mv", "ndr", "nr", "r",
			"rr",
			"rr", "rv", "rs", "rl", "v", "vr", "v", "vl"]
	nm61 = ["", "", "", "", "", "", "", "", "", "", "", "", "l", "n", "s", "sh", "th"]
	nm62 = ["", "", "ch", "d", "g", "gr", "h", "m", "n", "r", "st", "t", "tr", "v", "vr", "z"]
	nm63 = ["a", "e", "i", "o", "u", "a", "e", "i", "o", "u", "a", "e", "i", "o", "u", "a", "e", "i", "o", "u", "ye",
			"ya"]
	nm64 = ["b", "d", "dz", "g", "k", "ld", "lb", "lm", "lz", "m", "mr", "mz", "n", "nz", "ng", "nt", "r", "rg", "rn",
			"rk",
			"th", "tr", "tv", "v", "vr", "vz", "b", "d", "g", "k", "m", "n", "r", "v"]

	def generate_masculine(self):
		i = choice(range(0, 2))

		name_component = choice(self.nm54)
		name_component2 = choice(self.nm55)
		name_component3 = choice(self.nm56)
		name_component4 = choice(self.nm55)
		name_component5 = choice(self.nm57)
		if i == 0:
			name_component6 = choice(self.nm56)
			name_component7 = choice(self.nm55)
			nMs = name_component + name_component2 + name_component3 + name_component4 + name_component6 + name_component7 + name_component5
		else:
			nMs = name_component + name_component2 + name_component3 + name_component4 + name_component5

		return nMs

	def generate_feminine(self):
		i = choice(range(0, 2))

		name_component = choice(self.nm58)
		name_component2 = choice(self.nm59)
		name_component3 = choice(self.nm60)
		name_component4 = choice(self.nm59)
		name_component5 = choice(self.nm61)
		if i == 0:
			name_component6 = choice(self.nm60)
			name_component7 = choice(self.nm59)
			nMs = name_component + name_component2 + name_component3 + name_component4 + name_component6 + name_component7 + name_component5
		else:
			nMs = name_component + name_component2 + name_component3 + name_component4 + name_component5

		return nMs

	def generate_surname(self):
		i = choice(range(0, 2))

		name_component = choice(self.nm62)
		name_component2 = choice(self.nm63)
		name_component3 = choice(self.nm64)
		name_component4 = choice(self.nm63)
		name_component5 = choice(self.nm64)
		name_component6 = choice(self.nm63)

		if i == 0:
			name_component7 = choice(self.nm64)
			name_component8 = choice(self.nm63)
			lname = name_component + name_component2 + name_component3 + name_component4 + name_component5 + name_component6 + name_component7 + name_component8
		else:
			lname = name_component + name_component2 + name_component3 + name_component4 + name_component5 + name_component6

		return lname

	def race_check(self):
		pass


class Shou(Human):
	# /* Shou */
	nm65 = ["", "", "ch", "f", "h", "j", "l", "m", "q", "sh", "t", "th", "w", "z"]
	nm66 = ["a", "i", "e", "o", "u", "ia", "ui", "io", "ie", "iu"]
	nm67 = ["", "", "", "h", "m", "n", "ng", "p", "w", "y"]
	nm68 = ["b", "c", "ch", "d", "j", "l", "m", "n", "p", "q", "sh", "t", "ts", "x", "y", "z"]
	nm69 = ["ai", "ia", "ao", "ei", "iao", "ui", "ua", "ue"]
	nm70 = ["", "", "", "c", "ch", "d", "h", "j", "k", "l", "m", "n", "p", "q", "s", "sh", "t", "w", "x", "y", "z"]
	nm71 = ["a", "i", "u", "ai", "ia", "iao", "ue", "ei", "ie", "ua", "ao"]
	nm72 = ["", "", "", "m", "n", "ng", "y"]

	def generate_masculine(self):
		# todo implement
		pass

	def generate_feminine(self):
		# todo implement
		pass

	def generate_surname(self):
		name_component = choice(self.nm70)
		name_component2 = choice(self.nm71)
		name_component3 = choice(self.nm72)
		lname = name_component + name_component2 + name_component3

		return lname

	def race_check(self):
		pass


class Turami(Human):
	# /* Turami */
	nm73 = ["", "", "ch", "cr", "d", "gr", "f", "fr", "h", "m", "p", "r", "s", "t", "v", "z"]
	nm74 = ["a", "e", "i", "o", "u", "a", "e", "i", "o", "u", "a", "e", "i", "o", "u", "ai", "ie", "ue", "ea"]
	nm75 = ["b", "br", "c", "dr", "l", "ld", "lb", "m", "mb", "n", "nr", "nt", "nch", "r", "rf", "rv", "rn", "rc", "rd",
			"rt", "st", "sc", "t", "v", "z"]
	nm76 = ["", "", "l", "n", "r", "s", "z"]
	nm77 = ["", "", "", "b", "d", "f", "j", "l", "m", "q", "s", "v"]
	nm78 = ["a", "e", "i", "o", "a", "e", "i", "o", "a", "e", "i", "o", "a", "e", "i", "o", "a", "e", "i", "o", "a",
			"e",
			"i", "o", "ui", "ua", "ai", "ia", "ie", "ei"]
	nm79 = ["d", "l", "lm", "m", "n", "nc", "nd", "ndr", "nt", "nn", "r", "rt", "s", "t", "tt", "v"]
	nm80 = ["", "", "b", "c", "d", "f", "g", "h", "j", "m", "p", "r", "s", "v", "z"]
	nm81 = ["br", "c", "dr", "g", "h", "l", "lb", "ld", "m", "n", "nd", "nz", "r", "rn", "rg", "s", "sc", "sq", "st",
			"v",
			"z"]
	nm82 = ["", "", "", "", "l", "n", "r", "s"]

	def generate_masculine(self):
		i = choice(range(0, 2))

		name_component = choice(self.nm73)
		name_component2 = choice(self.nm74)
		name_component3 = choice(self.nm75)
		name_component4 = choice(self.nm74)
		name_component5 = choice(self.nm76)
		if i == 0:
			name_component6 = choice(self.nm75)
			name_component7 = choice(self.nm74)
			nMs = name_component + name_component2 + name_component3 + name_component4 + name_component6 + name_component7 + name_component5
		else:
			nMs = name_component + name_component2 + name_component3 + name_component4 + name_component5

		return nMs

	def generate_feminine(self):
		i = choice(range(0, 2))

		name_component = choice(self.nm77)
		name_component2 = choice(self.nm78)
		name_component3 = choice(self.nm79)
		name_component4 = choice(self.nm77)
		if i == 0:
			name_component6 = choice(self.nm79)
			name_component7 = choice(self.nm77)
			nMs = name_component + name_component2 + name_component3 + name_component4 + name_component6 + name_component7
		else:
			nMs = name_component + name_component2 + name_component3 + name_component4

		return nMs

	def generate_surname(self):
		# todo bring over other names
		name_component = choice(self.nm80)
		name_component2 = choice(self.nm14)
		name_component3 = choice(self.nm81)
		name_component4 = choice(self.nm14)
		name_component6 = choice(self.nm81)
		name_component7 = choice(self.nm14)
		name_component5 = choice(self.nm82)
		lname = name_component + name_component2 + name_component3 + name_component4 + name_component6 + name_component7 + name_component5

		return lname

	def race_check(self):
		pass


# endregion
