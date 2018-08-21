from enum import Enum


class RelationshipTypes(Enum):
	father = 1
	mother = 2
	child = 3


class Relationships:
	def __init__(self
				 , owner):
		self.owner = owner
		self.relationships = {}

	def add_father(self, father):
		if RelationshipTypes.father not in self.relationships.values():
			self.relationships[father] = RelationshipTypes.father

	def add_mother(self, mother):
		if RelationshipTypes.mother not in self.relationships.values():
			self.relationships[mother] = RelationshipTypes.mother

	def add_child(self, child):
		self.relationships[child] = RelationshipTypes.child
