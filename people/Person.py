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

		self.gender_check()
		self.first_name_check()
		self.surname_check()
		self.children_check()

	def __str__(self):
		retter = "Race: " + self.race
		retter += ", Name: " + self.first_name + " " + self.surname
		retter += ", Gender: " + Gender(self.gender).name
		return retter

	@abc.abstractmethod
	def generate_surname(self):
		pass

	@abc.abstractmethod
	def generate_feminine(self):
		pass

	@abc.abstractmethod
	def generate_masculine(self):
		pass

	# region checker functions
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

	def children_check(self):
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

	def create_child(self, race=None):
		"""
		a function for creating a child with the person's partner. the child is always "created" by the female, but can
		be called by both the father and the mother
		:param race: force the race of the child
		:return: a child
		"""
		if not self.can_have_children():
			raise ReferenceError(str(self) + " has no partner.")

		if self.gender is Gender.female:
			if race is None:
				child_class = choice([self.__class__, self.partner.__class__])
			else:
				child_class = race
			return child_class(father=self.partner, mother=self)
		else:
			return self.partner.create_child()

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
