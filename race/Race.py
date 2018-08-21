import abc
from random import choice

from people.Gender import Gender


class Race(abc.ABC):
	# todo change this for each race
	# death_age_calculator = DeathAgeCalculator()

	def __str__(self):
		return self.__class__.__name__

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

	def generate_first_name(self, gender):
		if gender == Gender.female:
			return self.generate_feminine()
		elif gender == Gender.male:
			return self.generate_masculine()
		else:
			raise NotImplementedError("You have not provided a gender.")

	# endregion


class SimpleRace(Race, abc.ABC):
	def generate_masculine(self):
		return choice(self.nm1)


class StandardRace(Race, abc.ABC):
	def generate_feminine(self):
		name_component = choice(self.nm3)
		name_component2 = choice(self.nm4)
		return name_component + name_component2

	def generate_masculine(self):
		name_component = choice(self.nm1)
		name_component2 = choice(self.nm2)
		return name_component + name_component2