from people.Person import *


class MindFlayer(Person):
	nm1 = ["", "", "", "c", "d", "dr", "g", "gr", "k", "l", "q", "qh", "r", "s", "sr", "sv", "sl", "t", "th", "tr", "v",
		   "z"]
	nm2 = ["a", "e", "u", "a", "e", "u", "a", "e", "u", "a", "e", "u", "a", "e", "u", "a", "e", "u", "a", "e", "u", "a",
		   "e", "u", "a", "e", "u", "a", "e", "u", "o", "o", "i", "au", "uoo", "ua", "uo", "ao"]
	nm3 = ["b", "br", "d", "dr", "dd", "g", "gg", "gr", "gch", "gl", "l", "ll", "lb", "ld", "nk", "nch", "ng", "ph",
		   "phr",
		   "r", "rd", "rb", "rg", "rds", "s", "ss", "sg", "sr", "sd", "sb", "z", "zz"]
	nm4 = ["a", "e", "i", "u", "a", "e", "i", "u", "o"]
	nm5 = ["b", "d", "g", "l", "m", "n", "ng", "r", "v", "y", "z"]
	nm6 = ["a", "e", "o", "u", "a", "e", "o", "u", "a", "e", "o", "u", "a", "e", "o", "u", "a", "e", "o", "u", "i",
		   "au",
		   "ua", "ao", "uo"]
	nm7 = ["k", "kt", "ks", "l", "ll", "lt", "m", "n", "r", "sk", "ss", "ssk", "x"]

	def generate_masculine(self):
		i = choice(range(0, 4))
		name_component = choice(self.nm1)
		name_component2 = choice(self.nm2)
		name_component3 = choice(self.nm7)
		if i == 0:
			while name_component < 3 or name_component == name_component3:
				name_component = choice(self.nm1)

			nMs = name_component + name_component2 + name_component3
		else:
			name_component4 = choice(self.nm3)
			name_component5 = choice(self.nm4)
			while name_component4 == name_component or name_component4 == name_component3:
				name_component4 = choice(self.nm3)

			if i == 1:
				nMs = name_component + name_component2 + name_component4 + name_component5 + name_component3
			else:
				name_component6 = choice(self.nm5)
				name_component7 = choice(self.nm6)
				while name_component6 == name_component4 or name_component6 == name_component3:
					name_component6 = choice(self.nm5)

				if i == 2:
					nMs = name_component + name_component2 + name_component4 + name_component5 + name_component6 + name_component7 + name_component3
				else:
					name_component8 = choice(self.nm5)
					name_component9 = choice(self.nm4)
					while name_component8 == name_component6:
						name_component8 = choice(self.nm5)

					nMs = name_component + name_component2 + name_component4 + name_component5 + name_component6 + name_component7 + name_component8 + name_component9

		return nMs

	def race_check(self):
		pass


class Beholder(Person):
	nm1 = ["", "", "", "", "", "b", "c", "ch", "d", "dh", "f", "g", "gh", "j", "kh", "l", "m", "n", "q", "qh", "r", "s",
		   "th", "v", "x", "z"]
	nm2 = ["a", "e", "i", "o", "a", "e", "i", "o", "a", "e", "i", "o", "a", "e", "i", "o", "a", "e", "i", "o", "a", "e",
		   "i", "o", "a", "e", "i", "o", "a", "e", "i", "o", "a", "e", "i", "o", "a", "e", "i", "o", "a", "e", "i", "o",
		   "aa", "oa", "ua", "ia", "au", "ao", "ou"]
	nm3 = ["d", "dd", "dr", "dl", "dh", "dtr", "dthr", "g", "gh", "gth", "k", "kk", "kh", "kht", "l", "ld", "ldr", "lb",
		   "lbr", "lm", "ln", "ls", "lsh", "lth", "lthdr", "lx", "m", "ml", "md", "mdr", "mn", "n", "nt", "nth", "nthr",
		   "ndr", "ntr", "r", "rb", "rd", "rg", "rgr", "rt", "rthr", "rth", "rl", "rn", "rm", "t", "th", "thr", "thdr",
		   "tr", "z", "zd", "zdr"]
	nm4 = ["a", "i", "o", "u", "a", "i", "o", "u", "y"]
	nm5 = ["c", "k", "ks", "q", "qs", "r", "rs", "rx", "s", "sc", "sk", "x", "z"]
	nm6 = ["a", "e", "i", "a", "e", "i", "a", "e", "i", "a", "e", "i", "a", "e", "i", "a", "e", "i", "o", "o", "ia",
		   "ai",
		   "ie", "ee", "io", "ae", "ea"]
	nm7 = ["", "", "", "", "", "ch", "cs", "csh", "hl", "hm", "hn", "hx", "hs", "hsh", "ks", "ksh", "ll", "lm", "ln",
		   "lk",
		   "lks", "ls", "lsh", "lx", "ph", "r", "rq", "rv", "s", "sh", "x"]

	def generate_masculine(self, i):
		i = choice(range(0, 4))
		name_component = choice(self.nm1)

		name_component2 = choice(self.nm2)
		name_component3 = choice(self.nm7)
		if i == 0:
			while name_component == name_component3:
				name_component3 = choice(self.nm7)

			nMs = name_component + name_component2 + name_component3
		else:
			name_component4 = choice(self.nm3)
			name_component5 = choice(self.nm4)
			if i == 1:
				while name_component4 == name_component or name_component4 == name_component3:
					name_component4 = choice(self.nm3)

				nMs = name_component + name_component2 + name_component4 + name_component5 + name_component3
			else:
				name_component6 = choice(self.nm5)
				name_component7 = choice(self.nm6)
				if i == 2:
					while name_component6 == name_component4 or name_component6 == name_component3:
						name_component6 = choice(self.nm5)

					nMs = name_component + name_component2 + name_component4 + name_component5 + name_component6 + name_component7 + name_component3
				else:
					name_component8 = choice(self.nm5)
					name_component9 = choice(self.nm6)
					while name_component8 == name_component6:
						name_component8 = choice(self.nm5)

					nMs = name_component + name_component2 + name_component4 + name_component5 + name_component6 + name_component7 + name_component8 + name_component9

		return nMs

	def race_check(self):
		pass


class Gnoll(Person):
	nm1 = ["a", "e", "i", "o", "u"]
	nm2 = ["b", "br", "d", "dr", "dn", "gn", "gr", "l", "ld", "lg", "lb", "lt", "lth", "mm", "mn", "md", "nd", "nr",
		   "r",
		   "rb", "rd", "rg", "rr", "rt", "rth", "st", "sn", "sm", "t", "th", "y"]
	nm3 = ["a", "e", "o", "u", "a"]
	nm4 = ["b", "d", "g", "k", "kh", "l", "lk", "m", "r", "rk", "t", "th"]

	nm5 = ["Abandoned", "Aberrant", "Abyssal", "Adamant", "Angry", "Attacking", "Barging", "Barking", "Barren",
		   "Battling",
		   "Berserk", "Berserking", "Bickering", "Biting", "Bitter", "Blaring", "Bleeding", "Blood", "Bloody",
		   "Bribing",
		   "Broken", "Burning", "Burrowing", "Bursting", "Charging", "Chasing", "Cheating", "Conquering", "Corrupted",
		   "Corrupting", "Cowering", "Crawling", "Crazed", "Crazy", "Crooked", "Dark", "Decayed", "Defiant", "Defiling",
		   "Dire", "Disobedient", "Enraged", "Fading", "Feeding", "Fierce", "Fighting", "Forging", "Forsaken",
		   "Frightening", "Gazing", "Ghastly", "Glaring", "Gloating", "Grave", "Grim", "Grimacing", "Growling",
		   "Grumbling",
		   "Grunting", "Heckling", "Hideous", "Hissing", "Hoarding", "Hollow", "Howling", "Hulking", "Hungry",
		   "Hunting",
		   "Impish", "Infamous", "Infernal", "Jaded", "Jealous", "Juvenile", "Laughing", "Lone", "Lost", "Lurking",
		   "Mad",
		   "Marked", "Meddling", "Menacing", "Mumbling", "Muttering", "Noisy", "Noxious", "Outlandish", "Pacing",
		   "Proud",
		   "Prowling", "Putrid", "Quick", "Rabid", "Ragged", "Rambling", "Ravaging", "Rebel", "Reckless", "Reigning",
		   "Repulsing", "Retched", "Roaming", "Roaring", "Rotted", "Rotten", "Rustling", "Ruthless", "Scrawny",
		   "Screaming",
		   "Shady", "Shaggy", "Shallow", "Shifting", "Silent", "Skeletal", "Smirking", "Snarling", "Stark", "Stout",
		   "Swift", "Thrifty", "Thundering", "Torn", "Trampling", "Twisting", "Twitching", "Vagabond", "Vengeful",
		   "Vicious", "Violent", "Volatile", "Wicked", "Wrathful", "Wretched"]
	nm6 = ["Assassins", "Barbarians", "Battlers", "Beasts", "Boors", "Bootleggers", "Brawlers", "Bruisers", "Brutes",
		   "Bullies", "Butchers", "Chasers", "Critters", "Devils", "Executioners", "Exterminators", "Ferals", "Fiends",
		   "Finks", "Freaks", "Gluttons", "Gorgers", "Harbingers", "Hellions", "Heralds", "Hogs", "Hoodlums", "Hunters",
		   "Killers", "Loafers", "Massacrers", "Mavericks", "Mercenaries", "Miscreants", "Miscreations", "Mongrels",
		   "Monsters", "Mutilators", "Mutts", "Outcasts", "Outlaws", "Pugilists", "Ramblers", "Rascals", "Rats",
		   "Ravagers",
		   "Rovers", "Sadists", "Savagages", "Slayers", "Stalkers", "Trappers", "Vagabonds", "Vagrants", "Vandals",
		   "Varmints", "Vermin", "Wanderers", "Warlords", "Wildlings"]

	def generate_surname(self):
		return "of the " + choice(self.nm5) + " " + choice(self.nm6)

	def generate_masculine(self):
		name_component = choice(self.nm1)
		name_component2 = choice(self.nm2)
		name_component3 = choice(self.nm3)
		name_component4 = choice(self.nm4)
		while name_component2 == name_component4:
			name_component4 = choice(self.nm4)

		nMs = name_component + name_component2 + name_component3 + name_component4
		return nMs

	def race_check(self):
		pass


class Hag(Person):
	nm1 = ["Acrid", "Ancient", "Angry", "Antique", "Antsy", "Arrogant", "Auntie", "Babbling", "Baggy", "Batty", "Bawdy",
		   "Bickering", "Biting", "Bitter", "Bizarre", "Black", "Blaring", "Blathering", "Bony", "Bumbling", "Bumpy",
		   "Cackling", "Cheeky", "Chittering", "Chuckling", "Cold", "Cooking", "Coughing", "Crabby", "Crackling",
		   "Crafty",
		   "Craven", "Crazy", "Crinkling", "Croaking", "Crooked", "Cruel", "Crumbling", "Delirious", "Demonic",
		   "Depraved",
		   "Deranged", "Despicable", "Disfigured", "Dismal", "Dread", "Dreaming", "Drooling", "Dusty", "Erratic",
		   "Feeble",
		   "Feisty", "Filthy", "Flaky", "Frail", "Frantic", "Gabby", "Giddy", "Giggling", "Gloomy", "Glum", "Granny",
		   "Gray", "Greasy", "Greedy", "Grouchy", "Grubby", "Haunting", "Heckling", "Humming", "Hungry", "Icky",
		   "Jaded",
		   "Jolly", "Knobby", "Knotty", "Laughing", "Lone", "Lonely", "Lurking", "Mad", "Moldy", "Murky", "Muttering",
		   "Nosy", "Nutty", "Old", "Outlandish", "Pale", "Paltry", "Pesky", "Putrid", "Ragged", "Raggedy", "Rambling",
		   "Rickety", "Rotten", "Salty", "Sassy", "Screeching", "Shabby", "Shady", "Shaggy", "Shaky", "Shoddy",
		   "Shrieking",
		   "Silent", "Silver", "Singing", "Skinny", "Sleeping", "Slumbering", "Smelly", "Snappy", "Snickering",
		   "Snoopy",
		   "Stinking", "Stumbling", "Twitching", "Vicious", "Volatile", "Weary", "Whistling", "Wicked", "Wild",
		   "Wretched",
		   "Wrinkling"]
	nm2 = ["Ada", "Addie", "Adeline", "Agnes", "Alberta", "Alice", "Alicia", "Allie", "Alma", "Alta", "Amanda",
		   "Amelia",
		   "Amy", "Andrea", "Angela", "Anita", "Ann", "Anna", "Anne", "Annette", "Annie", "Antoinette", "April",
		   "Arlene",
		   "Audrey", "Barbara", "Beatrice", "Becky", "Belinda", "Bernice", "Bertha", "Bessie", "Beth", "Bette",
		   "Bettie",
		   "Betty", "Beulah", "Beverly", "Billie", "Blanche", "Bobbie", "Bonnie", "Brenda", "Carla", "Carmen", "Carol",
		   "Carole", "Caroline", "Carolyn", "Carrie", "Catherine", "Cathy", "Cecelia", "Celia", "Charlene", "Charlotte",
		   "Cheryl", "Christina", "Christine", "Cindy", "Claire", "Clara", "Claudia", "Cleo", "Colleen", "Connie",
		   "Constance", "Cora", "Crystal", "Cynthia", "Daisy", "Dana", "Darlene", "Dawn", "Deanna", "Debbie", "Deborah",
		   "Debra", "Della", "Delores", "Denise", "Diana", "Diane", "Dianne", "Dolores", "Donna", "Dora", "Doreen",
		   "Doris",
		   "Dorothea", "Dorothy", "Edith", "Edna", "Effie", "Eileen", "Elaine", "Eleanor", "Eliza", "Elizabeth", "Ella",
		   "Ellen", "Eloise", "Elsie", "Elva", "Emily", "Emma", "Erma", "Essie", "Estella", "Estelle", "Esther",
		   "Ethel",
		   "Etta", "Eula", "Eunice", "Eva", "Evelyn", "Fannie", "Faye", "Felicia", "Fern", "Flora", "Florence",
		   "Flossie",
		   "Frances", "Freda", "Frieda", "Gail", "Gayle", "Geneva", "Genevieve", "Georgia", "Geraldine", "Gertrude",
		   "Gina",
		   "Gladys", "Glenda", "Gloria", "Goldie", "Grace", "Gwendolyn", "Hannah", "Harriet", "Hattie", "Hazel",
		   "Heather",
		   "Heidi", "Helen", "Henrietta", "Hilda", "Holly", "Ida", "Imogene", "Ina", "Inez", "Irene", "Irma", "Isabel",
		   "Isabelle", "Iva", "Jackie", "Jacqueline", "Jamie", "Jan", "Jane", "Janet", "Janice", "Janie", "Janis",
		   "Jean",
		   "Jeanette", "Jeanne", "Jeannette", "Jennie", "Jennifer", "Jessie", "Jill", "Jo", "Joan", "Joann", "Joanne",
		   "Jodi", "Jody", "Johnnie", "Josephine", "Joy", "Joyce", "Juanita", "Judith", "Judy", "Julia", "Julie",
		   "June",
		   "Karen", "Karla", "Katherine", "Kathleen", "Kathryn", "Kathy", "Katie", "Kay", "Kelly", "Kim", "Kimberly",
		   "Kristen", "Kristin", "Kristine", "Laura", "Laurie", "Laverne", "Lela", "Lena", "Leola", "Leona", "Leslie",
		   "Lila", "Lillian", "Lillie", "Linda", "Lisa", "Lizzie", "Lois", "Lola", "Lorene", "Loretta", "Lori",
		   "Lorraine",
		   "Lottie", "Louise", "Lucile", "Lucille", "Lucy", "Luella", "Lula", "Lydia", "Lynda", "Lynn", "Lynne",
		   "Mabel",
		   "Mable", "Madeline", "Mae", "Maggie", "Mamie", "Marcella", "Marcia", "Margaret", "Margie", "Marguerite",
		   "Maria",
		   "Marian", "Marianne", "Marie", "Marilyn", "Marion", "Marjorie", "Marlene", "Marsha", "Martha", "Mary",
		   "Maryann",
		   "Matilda", "Mattie", "Maude", "Maureen", "Maxine", "May", "Melanie", "Melinda", "Melissa", "Melody",
		   "Michele",
		   "Michelle", "Mildred", "Minnie", "Miriam", "Mollie", "Monica", "Muriel", "Myrna", "Myrtle", "Nancy",
		   "Nannie",
		   "Naomi", "Natalie", "Nell", "Nellie", "Nettie", "Nicole", "Nina", "Nora", "Norma", "Ola", "Olga", "Olive",
		   "Ollie", "Opal", "Ora", "Pam", "Pamela", "Pat", "Patricia", "Patsy", "Patti", "Patty", "Paula", "Paulette",
		   "Pauline", "Pearl", "Peggy", "Penny", "Phyllis", "Priscilla", "Rachel", "Ramona", "Rebecca", "Regina",
		   "Renee",
		   "Rhonda", "Rita", "Roberta", "Robin", "Rosa", "Rosalie", "Rose", "Rosemarie", "Rosemary", "Rosie", "Roxanne",
		   "Ruby", "Ruth", "Sadie", "Sallie", "Sally", "Sandra", "Sandy", "Sara", "Sarah", "Shannon", "Shari", "Sharon",
		   "Sheila", "Shelia", "Shelley", "Shelly", "Sheri", "Sherri", "Sherry", "Sheryl", "Shirley", "Sonya", "Sophia",
		   "Sophie", "Stacey", "Stacy", "Stella", "Stephanie", "Sue", "Susan", "Susie", "Suzanne", "Sylvia", "Tamara",
		   "Tami", "Tammie", "Tammy", "Tanya", "Teresa", "Terri", "Terry", "Thelma", "Theresa", "Tina", "Toni", "Tonya",
		   "Tracey", "Traci", "Tracy", "Valerie", "Vanessa", "Velma", "Vera", "Verna", "Veronica", "Vicki", "Vickie",
		   "Vicky", "Victoria", "Viola", "Violet", "Virgie", "Virginia", "Vivian", "Wanda", "Wendy", "Willie", "Wilma",
		   "Winifred", "Yolanda", "Yvette", "Yvonne"]
	nm3 = ["Beast", "Beetle", "Bitter", "Blind", "Blood", "Bog", "Bone", "Boulder", "Branch", "Chain", "Chalk",
		   "Chicken",
		   "Clot", "Cold", "Creep", "Critter", "Crypt", "Dark", "Dead", "Devil", "Dirt", "Doll", "Dreck", "Dust",
		   "Fang",
		   "Filth", "Fire", "Flame", "Flesh", "Fowl", "Frog", "Gnat", "Grave", "Grease", "Green", "Grim", "Grime",
		   "Gristle", "Gunk", "Horn", "Ink", "Knuckle", "Lard", "Light", "Marble", "Marsh", "Meat", "Mire", "Moon",
		   "Mouse",
		   "Muck", "Mud", "Nerve", "Night", "Ooze", "Pest", "Pig", "Powder", "Quill", "Rat", "Raw", "Red", "Rock",
		   "Rodent",
		   "Root", "Rubble", "Salt", "Scale", "Scrap", "Silt", "Slime", "Slop", "Smoke", "Snail", "Snake", "Soil",
		   "Soot",
		   "Spider", "Spite", "Spot", "Sprig", "Stew", "Stitch", "Stone", "Swamp", "Tallow", "Tear", "Thatch", "Titch",
		   "Toad", "Toe", "Twig", "Twist", "Vein", "Vermin", "Waste", "Wax", "Web", "Wood", "Wrinkle"]
	nm4 = ["chewer", "wart", "teeth", "gums", "bones", "wallow", "tooth", "willow", "stealer", "mouth", "wiggle",
		   "back",
		   "bend", "bite", "biter", "bone", "breath", "cheek", "cheeks", "chin", "cough", "cougher", "counter",
		   "cracker",
		   "finger", "fingers", "foot", "feet", "growth", "hand", "hands", "heart", "hide", "hook", "joint", "joints",
		   "knee", "knees", "leg", "legs", "mask", "mind", "mouth", "body", "sister", "face", "babbler", "baker",
		   "belcher",
		   "boggle", "bristle", "cackle", "carver", "cleaver", "cobble", "coddler", "crackle", "cradle", "cradler",
		   "crinkle", "croaker", "dabble", "dangler", "dipper", "dribble", "dribbler", "fiddle", "fidget", "giggle",
		   "giggler", "goggle", "jangle", "jiggle", "jumbler", "lurker", "meddler", "mingle", "mingler", "mumbler",
		   "mutterer", "nibbler", "nuzzle", "paddle", "paddler", "prattler", "rambler", "ramble", "rattle", "rattler",
		   "rumbler", "scrambler", "scratcher", "shifter", "shuffler", "sifter", "singer", "skewer", "soother",
		   "spitter",
		   "startler", "startle", "squirmer", "stumbler", "stumble", "surge", "switcher", "tangler", "tickler",
		   "tinkerer",
		   "toppler", "trampler", "tremble", "trembler", "trick", "trickle", "tumbler", "twitch", "twitcher", "waddle",
		   "waggle", "whistle", "whistler", "whittle", "wiggle", "wrangle", "wrangler"]

	def generate_surname(self):
		name_component3 = choice(self.nm3)
		name_component4 = choice(self.nm4)
		return name_component3 + name_component4

	def generate_feminine(self):
		name_component = choice(self.nm1)
		name_component2 = choice(self.nm2)
		return name_component + " " + name_component2

	def race_check(self):
		pass


class Kobolds(Person):
	nm1 = ["", "", "", "", "d", "g", "h", "k", "m", "n", "r", "s", "sn", "t", "v", "z"]
	nm2 = ["a", "e", "i", "o", "u"]
	nm3 = ["b", "bl", "d", "dr", "g", "gg", "gl", "gn", "gr", "hz", "hr", "hl", "hs", "k", "kk", "kr", "kl", "kb", "kd",
		   "l", "ld", "lb", "lt", "ll", "lp", "lg", "p", "pl", "pp", "r", "rt", "rp", "rb", "rk", "t", "tr", "tl", "v",
		   "vl", "vn"]
	nm4 = ["", "", "", "", "", "d", "g", "gs", "k", "ks", "m", "n", "r", "rn", "s", "ss", "tt", "v", "x"]

	def generate_masculine(self):
		i = choice(range(0, 2))
		name_component = choice(self.nm1)
		name_component2 = choice(self.nm2)
		name_component4 = choice(self.nm4)
		if i == 0:
			while name_component4 == name_component:
				name_component4 = choice(self.nm4)

			nMs = name_component + name_component2 + name_component4
		else:
			name_component3 = choice(self.nm3)
			name_component5 = choice(self.nm2)

			while name_component3 == name_component or name_component3 == name_component4:
				name_component3 = choice(self.nm3)

			nMs = name_component + name_component2 + name_component3 + name_component5 + name_component2

		return nMs

	def race_check(self):
		pass


class Orcs(Person):
	nm1 = ["", "", "", "b", "bh", "br", "d", "dh", "dr", "g", "gh", "gr", "j", "l", "m", "n", "r", "rh", "sh", "z",
		   "zh"]
	nm2 = ["a", "o", "u"]
	nm3 = ["b", "br", "bz", "d", "dd", "dz", "dg", "dr", "g", "gg", "gr", "gz", "gv", "hr", "hz", "j", "kr", "kz", "m",
		   "mz", "mv", "n", "ng", "nd", "nz", "r", "rt", "rz", "rd", "rl", "rz", "t", "tr", "v", "vr", "z", "zz"]
	nm4 = ["b", "d", "g", "g", "k", "k", "kk", "kk", "l", "ll", "n", "r"]

	nm5 = ["", "", "", "", "b", "bh", "d", "dh", "g", "gh", "h", "k", "m", "n", "r", "rh", "s", "sh", "v", "z"]
	nm6 = ["a", "e", "i", "o", "u", "a", "e", "i", "o", "u", "a", "e", "i", "o", "u", "a", "e", "i", "o", "u", "a", "e",
		   "i", "o", "u", "a", "e", "i", "o", "u", "ee", "au", "ye", "ie", "aa", "ou", "ua", "ao"]
	nm7 = ["d", "dd", "dk", "dg", "dv", "g", "gg", "gn", "gv", "gz", "l", "ll", "lv", "lz", "m", "md", "mz", "mv", "ng",
		   "nk", "ns", "nz", "t", "thr", "th", "v", "vn", "vr", "vg", "vd", "wnk", "wg", "wn"]
	nm8 = ["", "", "", "", "", "f", "h", "k", "l", "m", "n", "ng", "v", "z"]

	nm9 = ["Aberrant", "Ancient", "Angry", "Anguished", "Arrogant", "Barbarian", "Barbaric", "Barren", "Berserk",
		   "Bitter",
		   "Bloody", "Broad", "Broken", "Brutal", "Brute", "Butcher", "Coarse", "Cold", "Colossal", "Crazy", "Crooked",
		   "Cruel", "Dark", "Defiant", "Delirious", "Deranged", "Disfigured", "Enormous", "Enraged", "Fearless",
		   "Feisty",
		   "Fierce", "Filthy", "Forsaken", "Frantic", "Gargantuan", "Giant", "Glorious", "Grand", "Grave", "Grim",
		   "Gross",
		   "Gruesome", "Hollow", "Infernal", "Lethal", "Lost", "Loyal", "Macabre", "Mad", "Maniac", "Merciless",
		   "Mighty",
		   "Miscreant", "Noxious", "Outlandish", "Powerful", "Prime", "Proud", "Putrid", "Radical", "Reckless",
		   "Repulsive",
		   "Rotten", "Ruthless", "Shady", "Sick", "Silent", "Simple", "Smug", "Spiteful", "Swift", "Turbulent", "Ugly",
		   "Unsightly", "Vengeful", "Venomous", "Vicious", "Violent", "Vivid", "Volatile", "Vulgar", "Warped", "Wicked",
		   "Wild", "Worthless", "Wrathful", "Wretched"]
	nm10 = ["Anger", "Ankle", "Ash", "Battle", "Beast", "Bitter", "Black", "Blood", "Bone", "Brain", "Brass", "Breath",
			"Chaos", "Chest", "Chin", "Cold", "Dark", "Death", "Dirt", "Doom", "Dream", "Elf", "Eye", "Fang", "Feet",
			"Fiend", "Finger", "Flame", "Flesh", "Foot", "Ghost", "Giant", "Gnoll", "Gnome", "Gore", "Hand", "Hate",
			"Head",
			"Heart", "Heel", "Hell", "Horror", "Iron", "Joint", "Kidney", "Kill", "Knee", "Muscle", "Nose", "Pest",
			"Poison", "Power", "Pride", "Rib", "Scale", "Skin", "Skull", "Slave", "Smoke", "Sorrow", "Spine", "Spite",
			"Steel", "Storm", "Talon", "Teeth", "Throat", "Thunder", "Toe", "Tooth", "Vein", "Venom", "Vermin", "War"]
	nm11 = ["Axe", "Blade", "Brand", "Breaker", "Bruiser", "Burster", "Butcher", "Carver", "Chopper", "Cleaver",
			"Clobberer", "Conquerer", "Cracker", "Cruncher", "Crusher", "Cutter", "Dagger", "Defacer", "Despoiler",
			"Destroyer", "Dissector", "Ender", "Flayer", "Gasher", "Glaive", "Gouger", "Hacker", "Hammer", "Killer",
			"Lance", "Marauder", "Masher", "Mutilator", "Piercer", "Pummel", "Quasher", "Quelcher", "Queller", "Razer",
			"Render", "Ripper", "Saber", "Sabre", "Scalper", "Shatterer", "Skinner", "Slayer", "Slicer", "Smasher",
			"Snapper", "Spear", "Splitter", "Squasher", "Squelcher", "Squisher", "Strangler", "Sunderer", "Sword",
			"Trampler", "Trasher", "Vanquisher", "Wrecker"]

	def generate_surname(self):
		i = choice(range(0, 2))
		if i == 0:
			nSr = "The " + choice(self.nm9)
		else:
			nSr = choice(self.nm10) + " " + choice(self.nm11)

		return nSr

	def generate_feminine(self):
		i = choice(range(0, 2))
		name_component = choice(self.nm5)
		name_component2 = choice(self.nm6)
		name_component3 = choice(self.nm8)
		if i == 0:
			while name_component3 == name_component:
				name_component3 = choice(self.nm8)

			nFm = name_component + name_component2 + name_component3
		else:
			name_component4 = choice(self.nm7)
			name_component5 = choice(self.nm6)

			while name_component4 == name_component3:
				name_component4 = choice(self.nm7)

			nFm = name_component + name_component2 + name_component4 + name_component5 + name_component3

		return nFm

	def generate_masculine(self):
		i = choice(range(0, 2))
		name_component = choice(self.nm1)
		name_component2 = choice(self.nm2)
		name_component3 = choice(self.nm4)
		if i == 0:
			while name_component == name_component3:
				name_component = choice(self.nm1)

			nMs = name_component + name_component2 + name_component3
		else:
			name_component4 = choice(self.nm3)
			name_component5 = choice(self.nm2)
			while name_component4 == name_component or name_component4 == name_component3:
				name_component4 = choice(self.nm3)

			nMs = name_component + name_component2 + name_component4 + name_component5 + name_component3

		return nMs

	def race_check(self):
		pass


class YuanTi(Person):
	def race_check(self):
		pass

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

		return nMs
