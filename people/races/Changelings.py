from random import choice

from people.Person import Person
from tools.swearCheck import testSwear


class Changelings(Person):
	nm1 = ["", "", "", "b", "d", "f", "h", "j", "l", "m", "n", "p", "r", "s", "t", "v", "w", "y"]
	nm2 = ["a", "i", "o", "u", "a", "i", "o", "u", "a", "i", "o", "u", "a", "i", "o", "u", "ee", "ie", "ea", "ae", "ai",
		   "oo", "ou"]
	nm3 = ["c", "g", "gs", "k", "ks", "kt", "m", "n", "rx", "rt", "rs", "s", "sk", "t", "ts", "x", "z"]

	def nameMas(self):
		name_component = choice(self.nm1)
		name_component2 = choice(self.nm2)
		name_component3 = choice(self.nm3)
		while name_component == name_component3:
			name_component3 = choice(self.nm3)

		nMs = name_component + name_component2 + name_component3
		return testSwear(nMs)
