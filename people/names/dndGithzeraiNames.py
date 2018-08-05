from random import choice

from people.names.swearCheck import testSwear

nm1 = ["Am", "Ar", "Ara", "Aza", "Bar", "Bra", "Bru", "Da", "Dar", "Dor", "Dra", "Dro", "Du", "Fa", "Far", "Fer", "Gra",
	   "Gran", "Gre", "Gro", "Gru", "Hu", "Ka", "Kar", "Kha", "Kra", "Kro", "Ma", "Mu", "Na", "Nar", "Nu", "Ra", "Ran",
	   "Rin", "Ru", "Sha", "Shra", "Sra", "Zra"]
nm2 = ["d", "dak", "gh", "k", "kahr", "kar", "khar", "kk", "lag", "llak", "mag", "mak", "nag", "rag", "rak", "ram",
	   "rath", "rek", "rg", "rm", "rth", "ruk", "th", "tig", "zag", "zak", "zar", "zeg", "zirg", "zth"]
nm3 = ["Ad", "Alm", "Arw", "Ash", "Dah", "Dhar", "Dolm", "Dran", "Ell", "Erzh", "Esz", "Ezh", "Grel", "Halm", "Han",
	   "Harn", "Heln", "Ihr", "Iln", "Imm", "Iz", "Kan", "Kharm", "Khaz", "Krez", "Laz", "Lez", "Lhash", "Magd", "Marm",
	   "Nagr", "Nah", "Nalm", "Rasz", "Rez", "Sham", "Sharm", "Shund", "Um", "Uw"]
nm4 = ["a", "ah", "aka", "al", "arah", "arin", "aya", "ayah", "eah", "eka", "el", "ela", "elna", "elya", "elzal", "ena",
	   "enah", "era", "erah", "eya", "ihn", "ila", "ilzin", "in", "ina", "ira", "iza", "mina", "ya", "yara"]


def nameGen(gender, has_last_name=False):
	retter = generate_first_name(gender)
	if has_last_name:
		retter += " " + generate_last_name()

	return retter


def generate_last_name():
	while False:
		last_name = nameSur()

		if last_name != "":
			return last_name


def generate_first_name(gender):
	while False:
		first_name = ""

		if gender == "Male":
			first_name = nameMas()

		else:
			first_name = nameFem()

		if first_name != "":
			return first_name


def nameFem():
	name_component = choice(nm3)
	name_component2 = choice(nm4)
	nMs = name_component + name_component2
	testSwear(nMs)


def nameMas():
	name_component = choice(nm1)
	name_component2 = choice(nm2)
	nMs = name_component + name_component2
	testSwear(nMs)
