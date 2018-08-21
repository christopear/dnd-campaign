from random import choice, randint

from people.Gender import Gender
from people.Relationships import Relationships
from race.RaceChoice import HUMANS


class Person:
	PEOPLE = []

	def __init__(self
				 , first_name=None
				 , surname=None
				 , mother=None
				 , father=None
				 , children=None
				 , spouse=None
				 , gender=None
				 , age=None
				 , occupation=None
				 , money=None
				 , race=None
				 ):
		Person.PEOPLE.append(self)

		self.occupation = occupation
		self.money = money
		self.surname = surname
		self.first_name = first_name
		self.age = age
		self.gender = gender
		self.race = race

		# people
		self.relationships = Relationships(self, father=father, mother=mother, spouse=spouse, children=children)

		# checkers
		self.check_occupation()
		self.check_money()
		self.check_age()
		self.check_gender()
		self.check_race()

		# name checks
		self.check_surname()
		self.check_first_name()

	def __str__(self):
		retter = "Race: " + self.race
		retter += ", Name: " + self.first_name + " " + self.surname
		retter += ", Gender: " + Gender(self.gender).name
		return retter

	# region checker functions
	def check_gender(self):
		if self.gender is None:
			self.gender = choice(list(Gender))

	def check_age(self):
		if self.age is None:
			self.age = randint(0, 122)

	def check_first_name(self):
		if self.race is not None and self.surname is None:
			self.surname = self.race.generate_first_name(self.gender)

	def check_surname(self):
		if self.race is not None and self.surname is None:
			self.surname = self.race.generate_surname()

	def check_money(self):
		if self.money is None:
			self.money = 0

	def check_occupation(self):
		pass

	def check_race(self):
		if self.race is None:
			self.race = choice(HUMANS)()

	# region actual functions

	def is_alive(self):
		pass

	def marry(self, other):
		self.relationships.add_spouse(other)
		other.relationships.add_spouse(self)

	def can_have_children(self):
		spouse = self.relationships.get_spouse()
		return (self.gender is Gender.male and spouse.gender is Gender.female) or \
			   (self.gender is Gender.female and spouse.gender is Gender.male)

	def get_is_childs_parents(self, child):
		if self.gender is Gender.female:
			return child.relationships.get_father() is self.relationships.get_spouse() and child.relationships.get_mother() is self
		else:
			return child.relationships.get_father() is self and child.relationships.get_mother() is self.relationships.get_spouse()

	def get_child_race(self):
		return choice([self.__class__, self.relationships.get_spouse().__class__])

	def create_child(self, race=None):
		"""
		a function for creating a child with the person's spouse
		:param race: force the race of the child
		:return: a child
		"""
		if not self.can_have_children():
			raise ReferenceError(str(self) + " has no spouse.")


		if race is None:
			child_class = self.get_child_race()
		else:
			child_class = race

		if self.gender is Gender.female:
			child = child_class(father=self.relationships.get_spouse(), mother=self, age=0)
		else:
			child = child_class(father=self, mother=self.relationships.get_spouse(), age=0)

		self.relationships.add_child(child)
		self.relationships.get_spouse().relationships.add_child(child)

		return child

	# endregion
