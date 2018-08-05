import numpy as np

from people.person import Person


class Community:
    def __init__(self, community_name):
        self.community_name = community_name
        self.people = list()

    def __str__(self):
        retter = "Name: " + self.community_name + "\n"
        retter += "Number of people: " + self.get_population()
        return retter

    def add_person(self, person):
        if type(person) is not Person:
            raise TypeError("You must add a person.")

        self.people.append(person)

    def remove_person(self, person):
        if person not in self.people:
            raise LookupError("That person is not in the community.")

        self.people.remove(person)

    def get_community_name(self):
        return self.community_name

    def get_community_level(self, alignment=None):

        if alignment is None:
            return sum([person.level for person in self.people])

        # TODO can change this to a filter look up in future
        retter = 0
        for person in self.people:
            if person.alignment == alignment:
                retter += person.level

        return retter

    def get_population(self):
        return len(self.people)


class Township(Community):
    POP_MU = 5.8
    POP_SIGMA = 2.4

    COMMUNITY_COUNT = 1000

    @staticmethod
    def generate_community():
        population = int(np.random.lognormal(Community.POP_MU, Community.POP_SIGMA, 1))

        return population


class Ethnicity(Community):
    pass


class Family(Community):
    pass
