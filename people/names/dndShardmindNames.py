from random import choice

from people.names.swearCheck import testSwear

nm1 = ["Adu", "Ama", "Ani", "Ar", "Arsha", "Ashi", "Ashtu", "Bala", "Bara", "Basha", "Beles", "Delu", "Di", "Dura",
       "Duru", "Enu", "Eri", "Eshu", "Hua", "Hun", "Il", "Ilu", "Ira", "Ish", "Ku", "Kua", "Kuba", "Lu", "Mani", "Mara",
       "Mashi", "Na", "Nara", "Nashi", "Nu", "Rua", "Run", "Sana", "Sari", "Selu", "Shir", "Suma", "Tab", "Tin", "Tiru",
       "Uba", "Uku", "Ura", "Ut", "Zaki"]
nm2 = ["ba", "bam", "bani", "bu", "ha", "hara", "hu", "ka", "ku", "lazu", "lua", "mea", "nar", "nara", "naram", "naru",
       "nashtu", "ni", "niri", "nu", "nua", "pana", "ram", "ranu", "rashi", "raya", "ri", "rin", "runu", "shara",
       "shari", "shi", "shti", "shtu", "shu", "sunu", "ta", "tana", "tani", "tari", "ti", "tira", "tiru", "tua", "tum",
       "wia", "ya", "yara", "yua", "zu"]


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


def nameMas():
    name_component = choice(nm1)
    name_component2 = choice(nm2)
    nMs = name_component + name_component2
    return testSwear(nMs)
