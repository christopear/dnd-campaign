from enum import Enum
from random import choice

from constructs.DeathAge import get_death_age
from constructs.gender import Gender


class Gender(Enum):
	female = 1
	male = 2


class AgeExpectation:
	def __init__(self, alpha, beta):
		self.alpha = alpha
		self.beta = beta

class Person:
	def __init__(self
				 , mother=None
				 , father=None
				 , gender=None
				 , age=None
				 ):

		self.death_age = get_death_age()
		self.age = age
		self.gender = gender
		self.mother = mother
		self.father = father

		self.generate_gender(gender)
		self.generate_age(age)
		self.generate_death_age()

	def generate_gender(self, gender):
		if gender is None:
			self.gender = choice(list(Gender))

	def generate_age(self, age):
		if age is None:
			self.age = choice(list(Gender))

	# self.race = self.__class__.__name__

	# def generate_race(self):
	# 	if self.mother is None and self.father is None:
	# 		pass
	# 	elif self.mother is None and self.father is not None:
	# 		pass
	# 	elif self.mother is not None and self.father is None:
	# 		pass
	# 	else:
	# 		pass


	def generate_surname(self):
		raise NotImplementedError("Last name generation not defined.")
		return None

	def generate_feminine(self):
		raise NotImplementedError("Feminine name generation not defined.")
		return None

	def generate_masculine(self):
		raise NotImplementedError("Masculine name generation not defined.")
		return None


class SimplePerson(Person):
	def generate_masculine(self):
		return choice(self.nm1)


class StandardPerson(Person):
	def generate_feminine(self):
		name_component = choice(self.nm3)
		name_component2 = choice(self.nm4)
		return name_component + name_component2

	def generate_masculine(self):
		name_component = choice(self.nm1)
		name_component2 = choice(self.nm2)
		return name_component + name_component2
