from people.races.Races import CORE
from people.races.core.Races import *

p = [choice(CORE)() for i in range(0, 100)]

for person in p:
	print(str(person))
