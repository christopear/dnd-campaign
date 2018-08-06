from random import choice

from people.Person import Person
from tools.swearCheck import testSwear


class Shardmind(Person):
    nm1 = ["Adu", "Ama", "Ani", "Ar", "Arsha", "Ashi", "Ashtu", "Bala", "Bara", "Basha", "Beles", "Delu", "Di", "Dura",
           "Duru", "Enu", "Eri", "Eshu", "Hua", "Hun", "Il", "Ilu", "Ira", "Ish", "Ku", "Kua", "Kuba", "Lu", "Mani", "Mara",
           "Mashi", "Na", "Nara", "Nashi", "Nu", "Rua", "Run", "Sana", "Sari", "Selu", "Shir", "Suma", "Tab", "Tin", "Tiru",
           "Uba", "Uku", "Ura", "Ut", "Zaki"]
    nm2 = ["ba", "bam", "bani", "bu", "ha", "hara", "hu", "ka", "ku", "lazu", "lua", "mea", "nar", "nara", "naram", "naru",
           "nashtu", "ni", "niri", "nu", "nua", "pana", "ram", "ranu", "rashi", "raya", "ri", "rin", "runu", "shara",
           "shari", "shi", "shti", "shtu", "shu", "sunu", "ta", "tana", "tani", "tari", "ti", "tira", "tiru", "tua", "tum",
           "wia", "ya", "yara", "yua", "zu"]


    def nameMas(self):
        name_component = choice(Shardmind.nm1)
        name_component2 = choice(Shardmind.nm2)
        nMs = name_component + name_component2
        return testSwear(nMs)
