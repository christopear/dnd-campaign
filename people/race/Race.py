import abc
from random import choice

from people.race.UA.Races import Minotaur, Gith, Shifter, Warforged, Genasi, Changeling
from people.race.Volo.Races import Aarakocra, Aasimar, Goliath, Tabaxi, Triton, Kenku, Lizardfolk
from people.race.core.Races import HalfOrc, Turami, Shou, Rashemi, Mulan, Illuskan, Damaran, Chondathan, \
	Calashite, Tiefling, Dragonborn, Gnome, Halfelf, Halfling, Elf, Dwarf
from people.race.monsters.Races import YuanTi, Orcs, Kobolds, Hag, Gnoll, Beholder, MindFlayer


class Race(abc.ABC):
	# todo change this for each race
	# death_age_calculator = DeathAgeCalculator()

	CORE = [
		Dwarf,
		Elf,
		Halfling,
		Halfelf,
		Gnome,
		Dragonborn,
		HalfOrc,
		Tiefling
	]
	HUMANS = [
		Calashite,
		Chondathan,
		Damaran,
		Illuskan,
		Mulan,
		Rashemi,
		Shou,
		Turami
	]

	MONSTERS = [
		MindFlayer,
		Beholder,
		Gnoll,
		Hag,
		Kobolds,
		Orcs,
		YuanTi
	]

	UA = [
		Changeling,
		Genasi,
		Warforged,
		Shifter,
		Gith,
		Minotaur
	]

	VOLO = [
		Lizardfolk,
		Kenku,
		Triton,
		Tabaxi,
		Goliath,
		Aasimar,
		Aarakocra
	]

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
