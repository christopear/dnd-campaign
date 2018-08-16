import abc
from enum import Enum
from random import choice

from tools.DeathAgeCalculator import DeathAgeCalculator


class Gender(Enum):
	female = 1
	male = 2


class Person(abc.ABC):
	# todo change this for each race
	death_age_calculator = DeathAgeCalculator()

	def __init__(self
				 , first_name=None
				 , surname=None
				 , mother=None
				 , father=None
				 , children=None
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
		self.children = children
		self.race = self.__class__.__name__

		self.check_gender()
		self.check_first_name()
		self.check_surname()
		self.check_children()

	def __str__(self):
		retter = "Race: " + self.race
		retter += ", Name: " + self.first_name + " " + self.surname
		retter += ", Gender: " + Gender(self.gender).name
		return retter

	# region abstract generators
	@abc.abstractmethod
	def generate_surname(self):
		pass

	@abc.abstractmethod
	def generate_feminine(self):
		pass

	@abc.abstractmethod
	def generate_masculine(self):
		pass

	# endregion

	# region checker functions
	def check_gender(self):
		if self.gender is None:
			self.gender = choice(list(Gender))

	def check_first_name(self):
		if self.first_name is None:
			if self.gender is Gender.male:
				self.first_name = self.generate_masculine()
			elif self.gender is Gender.female:
				self.first_name = self.generate_feminine()

	def check_surname(self):
		if self.surname is None:
			self.surname = self.generate_surname()

	def check_children(self):
		if self.children is None:
			self.children = list()

	# endregion

	# region actual functions

	def marry(self, other):
		self.partner = other
		other.partner = self

	def can_have_children(self):
		return (self.gender is Gender.male and self.partner.gender is Gender.female) or \
			   (self.gender is Gender.female and self.partner.gender is Gender.male)

	def add_child(self, child):
		if not self.can_have_children():
			raise ReferenceError(str(self) + " has no partner.")

		self.children.append(child)
		self.partner.children.append(child)

	def get_child_race(self):
		return choice([self.__class__, self.partner.__class__])

	def create_child(self, race=None):
		"""
		a function for creating a child with the person's partner
		:param race: force the race of the child
		:return: a child
		"""
		if not self.can_have_children():
			raise ReferenceError(str(self) + " has no partner.")

		if race is None:
			child_class = self.get_child_race()
		else:
			child_class = race

		if self.gender is Gender.female:
			child = child_class(father=self.partner, mother=self, age=0)
		else:
			child = child_class(father=self, mother=self.partner, age=0)

		self.add_child(child)

		return child

	# endregion


class SimplePerson(Person, abc.ABC):
	def generate_masculine(self):
		return choice(self.nm1)


class StandardPerson(Person, abc.ABC):
	def generate_feminine(self):
		name_component = choice(self.nm3)
		name_component2 = choice(self.nm4)
		return name_component + name_component2

	def generate_masculine(self):
		name_component = choice(self.nm1)
		name_component2 = choice(self.nm2)
		return name_component + name_component2
