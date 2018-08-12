from random import choice

from people.Person import Person
from tools.swearCheck import testSwear


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

        return testSwear(nSr)

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

        return testSwear(nFm)

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

        return testSwear(nMs)
