from random import choice

from people.Person import Person
from tools.swearCheck import testSwear


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
		return testSwear(nMs)

	def generate_masculine(self):
		i = choice(range(0, 2))
		if i == 0:
			name_component = choice(self.nm1)
			name_component2 = choice(self.nm2)
			nMs = name_component + name_component2
		else:
			name_component = choice(self.nm3)
			nMs = name_component
		return testSwear(nMs)
