from people.Person import Race


class Community:
	ID = 0

	def __init__(self, community_name):
		self.id = Community.ID
		Community.ID += 1

		self.community_name = community_name
		self.people = list()

	def __str__(self):
		retter = "Name: " + self.community_name + "\n"
		retter += "Number of people: " + str(self.get_population())
		return retter

	def add_person(self, person):
		if type(person) is not Race:
			raise TypeError("You must add a person.")

		self.people.append(person)

	def remove_person(self, person):
		if person not in self.people:
			raise LookupError("That person is not in the community.")

		self.people.remove(person)

	def get_community_name(self):
		return self.community_name

	def get_community_level(self):
		pass

	def get_population(self):
		return len(self.people)
