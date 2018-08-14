from random import choice

from constructs.DeathAgeCalculator import DeathAgeCalculator
from constructs.gender import Gender


class Person:
	# todo change this for each race
	death_age_calculator = DeathAgeCalculator()

	def __init__(self
				 , first_name=None
				 , surname=None
				 , mother=None
				 , father=None
				 , partner=None
				 , gender=None
				 , age=None
				 ):
		self.partner = partner
		self.surname = surname
		self.first_name = first_name
		self.age = age
		self.gender = gender
		self.mother = mother
		self.father = father
		self.race = self.__class__.__name__

		self.gender_check()
		self.race_check()
		self.first_name_check()
		self.surname_check()

	def __str__(self):
		return ("Race: " + self.race +
				", Name: " + self.first_name + " " + self.surname +
				", Gender: " + Gender(self.gender).name)

	def race_check(self):
		if self.race in ['Person', 'SimplePerson', 'StandardPerson']:
			raise NotImplementedError("Use a standard race.")

	def generate_surname(self):
		raise NotImplementedError("Last name generation not defined.")
		return None

	def generate_feminine(self):
		raise NotImplementedError("Feminine name generation not defined.")
		return None

	def generate_masculine(self):
		raise NotImplementedError("Masculine name generation not defined.")
		return None

	def gender_check(self):
		if self.gender is None:
			self.gender = choice(list(Gender))

	def first_name_check(self):
		if self.first_name is None:
			if self.gender is Gender.male:
				self.first_name = self.generate_masculine()
			elif self.gender is Gender.female:
				self.first_name = self.generate_feminine()

	def surname_check(self):
		if self.surname is None:
			self.surname = self.generate_surname()


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
