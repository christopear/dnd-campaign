from random import choice

from people.Person import Person
from tools.swearCheck import testSwear


class Minotaur(Person):
	nmFF = ["Aam", "Ane", "Are", "Ase", "Duu", "Em", "Enti", "Este", "Fen", "Hene", "Hes", "Hila", "Hine", "Ias", "Ire",
			"Ki", "Kia", "Kuo", "Laan", "Line", "Loo", "Muu", "Nan", "Nea", "Neo", "Noo", "Nuo", "Oen", "Oes", "Raas",
			"Ras", "Sees", "Seo", "Sina", "Tee", "Tes", "Tia", "Tina", "Uova", "Weo"]
	nmFL = ["dra", "fin", "kane", "kea", "la", "las", "len", "lin", "lo", "mas", "me", "mi", "min", "na", "nan", "nas",
			"nim", "nu", "pen", "pe", "ra", "ren", "res", "rin", "ris", "ru", "sen", "sia", "ta", "ter", "tin", "tra",
			"tred", "tri", "trin", "tris", "ven", "vena", "vera", "vin"]
	nmMF = ["Ar", "Are", "Aste", "Bjor", "Car", "Cod", "Da", "Djar", "Djun", "Doen", "Dor", "Dur", "Foos", "Gar", "Goe",
			"Gra", "Gran", "Gun", "Hun", "Ja", "Jar", "Kar", "Kin", "Kir", "Koo", "Koor", "Krum", "Kur", "Man", "Min",
			"Mir", "Noo", "Pod", "Rak", "Te", "Toon", "Trak", "Tur", "Zam", "Zun"]
	nmML = ["ban", "baran", "bur", "dak", "daran", "dor", "fajar", "faruk", "furan", "gajan", "garak", "gur", "jar",
			"kan",
			"kar", "karat", "kun", "kurat", "kus", "manuk", "maruk", "nark", "narun", "paran", "raduk", "rak", "rakar",
			"ranak", "rapak", "ras", "rat", "rios", "ron", "rus", "rut", "tagar", "taruk", "toron", "turok", "tus"]
	nmSF = ["Agile", "Bear", "Bold", "Boulder", "Brave", "Bright", "Fearless", "Fist", "Glory", "Goblin", "Great",
			"Heavy",
			"Honor", "Iron", "Jagged", "Keen", "Nimble", "Orc", "Rock", "Rugged", "Sharp", "Silent", "Single", "Steady",
			"Steel", "Stone", "Storm", "Stout", "Strong", "Swift", "Thick", "Thunder", "Tough", "Truth", "Valiant",
			"Vigil",
			"Wolf"]
	nmSL = ["bane", "body", "eye", "fighter", "fist", "fury", "hand", "heart", "hide", "hoof", "horn", "horns",
			"hunter",
			"leader", "mind", "pelt", "roar", "runner", "skin", "skull", "slash", "slayer", "speaker", "step",
			"striker",
			"vigor", "walker", "warrior"]

	def nameSur(self):
		name_component = choice(self.nmSF)
		name_component2 = choice(self.nmSL)
		return testSwear(name_component + name_component2)

	def nameFem(self):
		name_component = choice(self.nmFF)
		name_component2 = choice(self.nmFL)
		nMs = name_component + name_component2

		return testSwear(nMs)

	def nameMas(self):
		i = choice(range(0, 2))
		if i == 0:
			name_component = choice(self.nmFF)
			name_component2 = choice(self.nmFL)
			nMs = name_component + name_component2
		else:
			name_component = choice(self.nmMF)
			name_component2 = choice(self.nmML)
			nMs = name_component + name_component2

		return testSwear(nMs)
