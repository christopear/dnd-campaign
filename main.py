from people.Person import Gender
from people.races.Races import HUMANS

# p = [choice(HUMANS)() for i in range(0, 1000)]
#
# for person in p:
# 	print(str(person))


p1 = HUMANS[0](gender=Gender.male)
p2 = HUMANS[2](gender=Gender.male)

p1.marry(p2)
p3 = p1.create_child()

print(p1)
print(p2)
print(p3)

print(p1.children)
print(p2.children)
print(p3.father)
print(p3.mother)
