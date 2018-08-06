from random import choice

from people.Person import Person
from tools.swearCheck import testSwear


class Goliath(Person):
    nmFF = ["Age", "Ane", "Gau", "Ge", "Ina", "Kau", "Ke", "Ki", "Kuo", "La", "Le", "Maa", "Man", "Mau", "Me", "Na", "Nal",
            "Ni", "One", "Ori", "Paa", "Pau", "Pe", "Tha", "The", "Thu", "Vaa", "Vau", "Ve", "Vu"]
    nmFL = ["gea", "geo", "gia", "gu", "kea", "keo", "ki", "kia", "kio", "la", "lai", "lane", "lea", "leo", "lo", "lu",
            "meo", "mi", "mia", "ne", "nea", "neo", "ni", "nia", "nu", "peo", "peu", "pu", "rea", "ri", "ria", "the",
            "thea", "thia", "thio", "thu", "vea", "vi", "via", "vu"]
    nmMF = ["Ag", "Apa", "Au", "Aug", "Eg", "Gau", "Gea", "Gha", "Ili", "Kana", "Kava", "Keo", "Khu", "La", "Ma", "Mau",
            "Mea", "Mo", "Na", "Neo", "Pa", "Pu", "Tha", "Thava", "Tho", "Va", "Vau", "Vega", "Vi", "Vo"]
    nmML = ["gak", "gal", "gan", "gath", "ghan", "gith", "glath", "gun", "kan", "kein", "khal", "kin", "kon", "lath", "lig",
            "lok", "mahg", "mahk", "mahl", "mak", "man", "mith", "mul", "nak", "nath", "nihl", "noth", "path", "phak",
            "thag", "thak", "tham", "thi", "thok", "veith", "vek", "vhal", "vhik", "vith", "voi"]
    nmMdF = ["Adept", "Bear", "Brave", "Bright", "Dawn", "Day", "Deer", "Dream", "Flint", "Fearless", "Flower", "Food",
             "Fright", "Goat", "Hard", "Hide", "High", "Honest", "Horn", "Keen", "Lone", "Long", "Low", "Lumber", "Master",
             "Mind", "Mountain", "Night", "Rain", "River", "Rock", "Root", "Silent", "Sky", "Sly", "Smart", "Steady",
             "Stone", "Storm", "Strong", "Swift", "Thread", "Thunder", "Tree", "Tribe", "True", "Truth", "Wander", "Wild",
             "Wise", "Wound"]
    nmMdL = ["aid", "bearer", "breaker", "caller", "carver", "chaser", "climber", "cook", "dream", "drifter", "eye",
             "finder", "fist", "friend", "frightener", "guard", "hand", "hauler", "heart", "herder", "hunter", "jumper",
             "killer", "lander", "leader", "leaper", "logger", "maker", "mender", "picker", "runner", "shot", "smasher",
             "speaker", "stalker", "striker", "tanner", "twister", "vigor", "walker", "wanderer", "warrior", "watcher",
             "weaver", "worker"]
    nmSF = ["Agu-Ul", "Agu-V", "Anakal", "Apuna-M", "Athun", "Egena-V", "Egum", "Elan", "Ganu-M", "Gathak", "Gean", "Inul",
            "Kalag", "Kaluk", "Katho-Ol", "Kolae-G", "Kolak", "Kulan", "Kulum", "Lakum", "Maluk", "Munak", "Muthal",
            "Nalak", "Nola-K", "Nugal", "Nulak", "Ogol", "Oveth", "Thenal", "Thul", "Thunuk", "Ugun", "Uthenu-K",
            "Vaimei-L", "Valu-N", "Vathun", "Veom", "Vuma-Th", "Vunak"]
    nmSL = ["aga", "ageane", "akane", "akanu", "akume", "alathi", "amino", "amune", "anathi", "atake", "athai", "athala",
            "atho", "avea", "avi", "avone", "eaku", "ekali", "elo", "iaga", "iago", "iala", "iano", "igala", "igane",
            "igano", "igo", "igone", "ileana", "ithino", "olake", "ugate", "ugoni", "ukane", "ukate", "ukena", "ulane",
            "upine", "utha", "uthea"]



    def nameSur(self):
        name_component = choice(Goliath.nmMdF)
        name_component2 = choice(Goliath.nmMdL)
        name_component3 = choice(Goliath.nmSF)
        name_component4 = choice(Goliath.nmSL)
        return testSwear(name_component + name_component2 + " " + name_component3 + name_component4)


    def nameFem(self):
        name_component = choice(Goliath.nmFF)
        name_component2 = choice(Goliath.nmFL)
        nMs = name_component + name_component2
        return testSwear(nMs)


    def nameMas(self):
        name_component = choice(Goliath.nmMF)
        name_component2 = choice(Goliath.nmML)
        nMs = name_component + name_component2
        return testSwear(nMs)
