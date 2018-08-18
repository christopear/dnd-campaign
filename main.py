from people.Person import Gender
from race.Race import HUMANS

# p = [choice(HUMANS)() for i in range(0, 1000)]
#
# for person in p:
# 	print(str(person))


p1 = HUMANS[0](gender=Gender.male)

print(p1.description())
