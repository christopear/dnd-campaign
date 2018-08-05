from random import choice

from people.names.swearCheck import testSwear

nm1 = ["c", "d", "dh", "j", "jh", "k", "kh", "m", "n", "r", "v", "z"]
nm2 = ["a", "e", "i", "o", "u"]
nm3 = ["d", "dd", "g", "gl", "hn", "hl", "hr", "l", "lg", "lm", "ld", "ln", "lz", "m", "mn", "mr", "n", "nn", "nd",
	   "nl", "nr", "nv", "r", "rl", "rn", "rv", "rz", "v", "vn", "z"]

nm4 = ["", "", "", "", "", "", "", "", "b", "bh", "d", "dh", "f", "fl", "h", "l", "m", "n", "s", "sh", "vl", "w", "wh",
	   "y"]
nm5 = ["a", "e", "o", "u", "a", "e", "o", "u", "i"]
nm6 = ["d", "dd", "dr", "gr", "gl", "hl", "hn", "l", "lr", "lt", "lth", "ml", "nl", "nth", "nr", "r", "rn", "rl", "rr",
	   "s", "sh", "st", "sl", "sn", "t", "th", "tr", "thr", "tl", "thl"]
nm7 = ["d", "h", "l", "m", "n", "r"]
nm8 = ["e", "y", "y", "y", "y", "y", "y"]

nm9 = ["", "", "", "b", "bh", "d", "dh", "j", "g", "l", "m", "n", "p", "r", "s", "v", "z"]
nm10 = ["a", "u", "a", "u", "a", "u", "e", "o"]
nm11 = ["b", "d", "g", "gh", "hl", "hn", "hm", "hr", "l", "n", "m", "r", "v"]
nm12 = ["a", "o", "a", "o", "e", "u"]
nm13 = ["d", "g", "l", "ll", "ln", "lm", "lv", "m", "mn", "n", "ns", "nz", "r", "rs", "s", "sn", "x", "z"]

br = ""

def nameGen(type):
	#	$(.'#placeholder').css('textTransform', 'capitalize')
	tp = type
	#	element = document..createElement("div")
	#	element..setAttribute("id", "result")

	for i in range(0, 10):
		name_component = choice(nm9)
		name_component2 = choice(nm10)
		name_component3 = choice(nm11)
		name_component4 = choice(nm12)
		name_component5 = choice(nm13)
		while name_component3 == name_component or name_component3 == name_component5:
			name_component3 = choice(nm11)

		nSr = name_component + name_component2 + name_component3 + name_component4 + name_component5 + "ath"
		if tp == 1:
			nameFem()
			while nFm == "":
				nameFem()

			names = nFm + " " + nSr
		else:
			nameMas()
			while nMs == "":
				nameMas()

			names = nMs + " " + nSr


# br = document..createElement('br')
#		element.appendChild(document..createTextNode(names))
#		element..appendChild(br)

#	if document..getElementById("result"):
#		document.getElementById("placeholder").removeChild(document..getElementById("result"))

#	document..getElementById("placeholder").appendChild(element)


def nameFem():
	name_component = choice(nm4)
	name_component2 = choice(nm5)
	name_component3 = choice(nm6)
	name_component4 = choice(nm8)
	while name_component3 == name_component:
		name_component3 = choice(nm6)

	if i < 5:
		nFm = name_component + name_component2 + name_component3 + name_component4 + "n"
	else:
		name_component5 = choice(nm5)
		name_component6 = choice(nm7)
		while name_component6 == name_component3:
			name_component6 = choice(nm7)

		nFm = name_component + name_component2 + name_component3 + name_component5 + name_component6 + name_component4 + "n"

	testSwear(nFm)


def nameMas():
	name_component = choice(nm1)
	name_component2 = choice(nm2)
	name_component3 = choice(nm3)
	while name_component == name_component3:
		name_component3 = choice(nm3)

	name_component4 = choice(nm2)
	nMs = name_component + name_component2 + name_component3 + name_component2 + "s"
	testSwear(nMs)
