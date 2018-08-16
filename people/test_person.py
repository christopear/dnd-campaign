from unittest import TestCase

from people.Person import Gender
from people.races.core.Races import *


class TestPerson(TestCase):
	def test_marry(self):
		p1 = Human()
		p2 = Human()

		p1.marry(p2)

		self.assertEqual(p1.partner, p2)
		self.assertEqual(p2.partner, p1)

	def gay_test_can_have_children(self):
		p1 = Chondathan(gender=Gender.male)
		p2 = Chondathan(gender=Gender.male)

		p1.marry(p2)

		self.assertFalse(p1.can_have_children())
		self.assertFalse(p2.can_have_children())

	def fem_gay_test_can_have_children(self):
		p1 = Chondathan(gender=Gender.female)
		p2 = Chondathan(gender=Gender.female)

		p1.marry(p2)

		self.assertFalse(p1.can_have_children())
		self.assertFalse(p2.can_have_children())

	def straight_test_can_have_children(self):
		p1 = Chondathan(gender=Gender.male)
		p2 = Chondathan(gender=Gender.female)

		p1.marry(p2)

		self.assertTrue(p1.can_have_children())
		self.assertTrue(p2.can_have_children())

	def test_add_child(self):
		p1 = Chondathan(gender=Gender.male)
		p2 = Chondathan(gender=Gender.female)

		p3 = Chondathan(father=p1, mother=p2)
		p1.add_child(p3)

		self.assertEqual(p3.father, p1)
		self.assertEqual(p3.mother, p2)

		self.assertIn(p3, p1.children)
		self.assertIn(p3, p2.children)

	def test_get_child_race(self):
		p1 = Chondathan(gender=Gender.male)
		p2 = Chondathan(gender=Gender.female)

		p1.marry(p2)

		self.assertEqual(p1.get_child_race(), Chondathan)

		p1 = Chondathan(gender=Gender.male)
		p2 = Illuskan(gender=Gender.female)

		p1.marry(p2)

		self.assertIn(p1.get_child_race(), [Chondathan, Illuskan])

	def test_create_child(self):
		p1 = Chondathan(gender=Gender.male)
		p2 = Chondathan(gender=Gender.female)

		p1.marry(p2)

		p3 = p1.create_child()

		self.assertEqual(p1.children[0], p3)
		self.assertEqual(p2.children[0], p3)

		self.assertEqual(p1, p3.father)
		self.assertEqual(p1, p3.mother)
