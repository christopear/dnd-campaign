from enum import Enum
from random import choice, randint


class Gender(Enum):
	female = 1
	male = 2


class Person:
	PEOPLE = []

	def __init__(self
				 , first_name=None
				 , surname=None
				 , mother=None
				 , father=None
				 , children=None
				 , partner=None
				 , gender=None
				 , age=None
				 , occupation=None
				 , money=None
				 , race=None
				 ):
		Person.PEOPLE.append(self)

		self.occupation = occupation
		self.money = money
		self.partner = partner
		self.surname = surname
		self.first_name = first_name
		self.age = age
		self.gender = gender
		self.mother = mother
		self.father = father
		self.children = children
		self.race = race

		self.check_race()
		self.check_gender()
		# self.check_first_name()
		# self.check_surname()
		self.check_children()
		self.check_money()
		self.check_occupation()
		self.check_age()

	def __str__(self):
		retter = "Race: " + self.race
		retter += ", Name: " + self.first_name + " " + self.surname
		retter += ", Gender: " + Gender(self.gender).name
		return retter

	def description(self):
		retter = "{} {} is a {} year old {}.".format(
			self.first_name,
			self.surname,
			self.age,
			self.gender.name
		)
		return retter

	# region checker functions
	def check_gender(self):
		if self.gender is None:
			self.gender = choice(list(Gender))

	def check_age(self):
		if self.age is None:
			self.age = randint(0, 122)

	def check_first_name(self):
		pass

	def check_surname(self):
		pass

	def check_children(self):
		if self.children is None:
			self.children = list()

	def check_money(self):
		if self.money is None:
			self.money = 0

	def check_occupation(self):
		pass

	def check_race(self):
		pass

	# endregion

	# region actual functions

	def has_father(self):
		return self.father is not None

	def has_mother(self):
		return self.mother is not None

	def has_both_parents(self):
		return self.has_father() and self.has_mother()

	def is_alive(self):
		pass

	def marry(self, other):
		self.partner = other
		other.partner = self

	def can_have_children(self):
		return (self.gender is Gender.male and self.partner.gender is Gender.female) or \
			   (self.gender is Gender.female and self.partner.gender is Gender.male)

	def get_is_childs_parents(self, child):
		if self.gender is Gender.female:
			return child.father is self.partner and child.mother is self
		else:
			return child.father is self and child.mother is self.partner

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
