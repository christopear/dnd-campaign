from people.races.Races import HUMANS
from people.races.core.Races import *

p = [choice(HUMANS)() for i in range(0, 1000)]

for person in p:
	print(str(person))
