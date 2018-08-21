import abc
from enum import Enum


class RelationshipTypes(Enum):
	father = 1
	mother = 2
	child = 3
	spouse = 4


class RelationshipChecker(abc.ABC):
	def __init__(self, owner):
		self.owner = owner
		self.relationships = {}

	def get_relationship(self, relationship_type):
		return {k: v for k, v in self.relationships.items() if v is relationship_type}

	def has_relationship(self, relationship_type):
		return len(self.get_relationship(relationship_type)) > 0

	def has_single(self, relationship_type):
		return len(self.get_relationship(relationship_type)) == 1

	def get_single(self, relationship_type):
		rel = self.get_relationship(relationship_type)
		if len(rel) == 1:
			return next(iter(rel.keys()))
		else:
			raise AssertionError("Does not have a single {}".format(relationship_type.name))


class Relationships(RelationshipChecker):
	def __init__(self, owner, mother=None, father=None, spouse=None, children=None):
		super().__init__(owner)

		if father is not None:
			self.add_father(father)

		if mother is not None:
			self.add_mother(mother)

		if spouse is not None:
			self.add_spouse(spouse)

		if children is not None:
			self.add_children(children)

	def add_father(self, father):
		# TODO add None checker here
		if not self.has_relationship(RelationshipTypes.father):
			self.relationships[father] = RelationshipTypes.father
		else:
			raise ValueError("This person already has a father.")

	def add_mother(self, mother):
		# TODO add None checker here
		if not self.has_relationship(RelationshipTypes.mother):
			self.relationships[mother] = RelationshipTypes.mother
		else:
			raise ValueError("This person already has a mother.")

	def add_child(self, child):
		# TODO add None checker here
		self.relationships[child] = RelationshipTypes.child

	def add_children(self, children):
		# TODO add None checker here
		for child in children:
			self.add_child(child)

	def add_spouse(self, spouse):
		if not self.has_relationship(RelationshipTypes.spouse):
			self.relationships[spouse] = RelationshipTypes.spouse
		else:
			raise ValueError("This person already has a spouse.")

	def get_spouse(self):
		return self.get_single(RelationshipTypes.spouse)

	def get_father(self):
		return self.get_single(RelationshipTypes.father)

	def get_mother(self):
		return self.get_single(RelationshipTypes.mother)

	def get_children(self):
		return self.get_relationship(RelationshipTypes.child)

	def has_spouse(self):
		return self.has_single(RelationshipTypes.spouse)

	def has_father(self):
		return self.has_single(RelationshipTypes.father)

	def has_mother(self):
		return self.has_single(RelationshipTypes.mother)

	def has_children(self):
		return self.has_relationship(RelationshipTypes.child)

		# def get_siblings(self):
		# 	siblings = []
		#
		# 	father_children = []
		# 	mother_children = []
		# 	if self.has_father():
		# 		father_children = self.father.get_children()
		#
		# 	if self.has_mother():
		# 		mother_children = self.mother.get_children()
		#
		# 	for child in father_children:
		# 		if child is not self and child in mother_children:
		# 			siblings.append(child)
		#
		# 	return siblings
		#
		# def get_parents(self):
		# 	parents = []
		#
		# 	if self.father is not None:
		# 		parents.append(self.father)
		#
		# 	if self.mother is not None:
		# 		parents.append(self.mother)
		#
		# 	return parents
		#
		# def get_uncles_and_aunts(self):
		# 	uncles_and_aunts = []
		#
		# 	parents = self.get_parents()
		#
		# 	for parent in parents:
		# 		for sibling in parent.get_siblings():
		# 			if sibling not in uncles_and_aunts:
		# 				uncles_and_aunts.append(sibling)
		#
		# 	return uncles_and_aunts
		#
		# def get_cousins(self):
		# 	cousins = []
		#
		# 	uncles_and_aunts = self.get_uncles_and_aunts()
		#
		# 	for uncle_or_aunt in uncles_and_aunts:
		# 		for child in uncle_or_aunt.get_children():
		# 			if child not in cousins:
		# 				cousins.append(child)
		#
		# 	return cousins
		#
		# def get_nephews_and_nieces(self):
		# 	nephews_and_nieces = []
		# 	siblings = self.get_siblings()
		#
		# 	for sibling in siblings:
		# 		for child in sibling.get_children():
		# 			if child not in nephews_and_nieces:
		# 				nephews_and_nieces.append(child)
		#
		# 	return nephews_and_nieces
		#
		# def get_grandparents(self):
		# 	grandparents = []
		#
		# 	for parent in self.get_parents():
		# 		for gp in parent.get_parents():
		# 			grandparents.append(gp)
		#
		# 	return grandparents
		#
		# def get_all_family(self):
		# 	family = []
		#
		# 	for p in self.get_children():
		# 		if p not in family:
		# 			family.append(p)
		#
		# 	for p in self.get_parents():
		# 		if p not in family:
		# 			family.append(p)
		#
		# 	for p in self.get_uncles_and_aunts():
		# 		if p not in family:
		# 			family.append(p)
		#
		# 	for p in self.get_cousins():
		# 		if p not in family:
		# 			family.append(p)
		#
		# 	for p in self.get_nephews_and_nieces():
		# 		if p not in family:
		# 			family.append(p)
		#
		# 	for p in self.get_grandparents():
		# 		if p not in family:
		# 			family.append(p)
		#
		# 	return family
