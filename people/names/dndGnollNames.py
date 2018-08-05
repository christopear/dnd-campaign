from random import choice

from people.names.swearCheck import testSwear

nm1 = ["a", "e", "i", "o", "u"]
nm2 = ["b", "br", "d", "dr", "dn", "gn", "gr", "l", "ld", "lg", "lb", "lt", "lth", "mm", "mn", "md", "nd", "nr", "r",
       "rb", "rd", "rg", "rr", "rt", "rth", "st", "sn", "sm", "t", "th", "y"]
nm3 = ["a", "e", "o", "u", "a"]
nm4 = ["b", "d", "g", "k", "kh", "l", "lk", "m", "r", "rk", "t", "th"]

nm5 = ["Abandoned", "Aberrant", "Abyssal", "Adamant", "Angry", "Attacking", "Barging", "Barking", "Barren", "Battling",
       "Berserk", "Berserking", "Bickering", "Biting", "Bitter", "Blaring", "Bleeding", "Blood", "Bloody", "Bribing",
       "Broken", "Burning", "Burrowing", "Bursting", "Charging", "Chasing", "Cheating", "Conquering", "Corrupted",
       "Corrupting", "Cowering", "Crawling", "Crazed", "Crazy", "Crooked", "Dark", "Decayed", "Defiant", "Defiling",
       "Dire", "Disobedient", "Enraged", "Fading", "Feeding", "Fierce", "Fighting", "Forging", "Forsaken",
       "Frightening", "Gazing", "Ghastly", "Glaring", "Gloating", "Grave", "Grim", "Grimacing", "Growling", "Grumbling",
       "Grunting", "Heckling", "Hideous", "Hissing", "Hoarding", "Hollow", "Howling", "Hulking", "Hungry", "Hunting",
       "Impish", "Infamous", "Infernal", "Jaded", "Jealous", "Juvenile", "Laughing", "Lone", "Lost", "Lurking", "Mad",
       "Marked", "Meddling", "Menacing", "Mumbling", "Muttering", "Noisy", "Noxious", "Outlandish", "Pacing", "Proud",
       "Prowling", "Putrid", "Quick", "Rabid", "Ragged", "Rambling", "Ravaging", "Rebel", "Reckless", "Reigning",
       "Repulsing", "Retched", "Roaming", "Roaring", "Rotted", "Rotten", "Rustling", "Ruthless", "Scrawny", "Screaming",
       "Shady", "Shaggy", "Shallow", "Shifting", "Silent", "Skeletal", "Smirking", "Snarling", "Stark", "Stout",
       "Swift", "Thrifty", "Thundering", "Torn", "Trampling", "Twisting", "Twitching", "Vagabond", "Vengeful",
       "Vicious", "Violent", "Volatile", "Wicked", "Wrathful", "Wretched"]
nm6 = ["Assassins", "Barbarians", "Battlers", "Beasts", "Boors", "Bootleggers", "Brawlers", "Bruisers", "Brutes",
       "Bullies", "Butchers", "Chasers", "Critters", "Devils", "Executioners", "Exterminators", "Ferals", "Fiends",
       "Finks", "Freaks", "Gluttons", "Gorgers", "Harbingers", "Hellions", "Heralds", "Hogs", "Hoodlums", "Hunters",
       "Killers", "Loafers", "Massacrers", "Mavericks", "Mercenaries", "Miscreants", "Miscreations", "Mongrels",
       "Monsters", "Mutilators", "Mutts", "Outcasts", "Outlaws", "Pugilists", "Ramblers", "Rascals", "Rats", "Ravagers",
       "Rovers", "Sadists", "Savagages", "Slayers", "Stalkers", "Trappers", "Vagabonds", "Vagrants", "Vandals",
       "Varmints", "Vermin", "Wanderers", "Warlords", "Wildlings"]


def nameGen(gender, has_last_name=True):
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


def nameSur():
    return "of the " + choice(nm5) + " " + choice(nm6)



def nameMas():
    name_component = choice(nm1)
    name_component2 = choice(nm2)
    name_component3 = choice(nm3)
    name_component4 = choice(nm4)
    while name_component2 == name_component4:
        name_component4 = choice(nm4)

    nMs = name_component + name_component2 + name_component3 + name_component4
    testSwear(nMs)
