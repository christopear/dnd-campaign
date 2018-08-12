from random import choice

from people.Person import Person
from tools.swearCheck import testSwear


class YuanTi(Person):
	nm1 = ["", "", "", "", "", "h", "m", "n", "s", "sh", "ss", "ssh", "sz", "t", "th", "y", "z", "zh", "zs"]
	nm2 = ["a", "e", "i", "o", "u", "a", "e", "i", "o", "u", "a", "e", "i", "o", "u", "a", "e", "i", "o", "u", "a", "e",
		   "i", "o", "u", "oa", "ui"]
	nm3 = ["h", "hl", "htl", "hl", "hs", "hsh", "k", "kh", "kl", "ktl", "ks", "l", "lk", "ls", "ltl", "lts", "lsh", "m",
		   "n", "s", "sh", "ss", "st", "stl", "sz", "sk", "t", "tl", "ts", "tsh", "tsz", "tz", "tstl", "zs", "zh",
		   "zsh",
		   "zt", "ztl"]
	nm4 = ["h", "hs", "hl", "l", "ll", "s", "sh", "ss", "shl", "t", "th", "y", "z", "zh"]
	nm5 = ["a", "i", "u", "a", "i", "u", "a", "i", "u", "a", "i", "u", "a", "i", "u", "a", "i", "u", "ie", "ia", "ei",
		   "ee",
		   "iu", "ui"]
	nm6 = ["", "", "", "", "", "", "", "", "h", "h", "l", "ll", "s", "ss", "sh"]

	def generate_masculine(self):
		i = choice(range(0, 2))

		name_component = choice(self.nm1)
		name_component2 = choice(self.nm2)
		name_component3 = choice(self.nm3)
		name_component4 = choice(self.nm5)
		name_component5 = choice(self.nm6)
		if i == 0:
			while name_component == name_component3 or name_component3 == name_component5:
				name_component3 = choice(self.nm3)

			nMs = name_component + name_component2 + name_component3 + name_component4 + name_component5
		else:
			name_component6 = choice(self.nm4)
			name_component7 = choice(self.nm2)
			while name_component4 == name_component6 or name_component6 == name_component5:
				name_component6 = choice(self.nm4)

			nMs = name_component + name_component2 + name_component3 + name_component7 + name_component6 + name_component4 + name_component5

		return testSwear(nMs)
