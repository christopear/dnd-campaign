from unittest import TestCase

from people.Person import Gender
from people.races.core.Races import *


class TestPerson(TestCase):
	def test_gender(self):
		p1 = Chondathan(gender=Gender.male)
		self.assertEqual(p1.gender, Gender.male)

		p2 = Chondathan(gender=Gender.female)
		self.assertEqual(p2.gender, Gender.female)

	def test_first_name(self):
		p1 = Chondathan(
			first_name="Olivia"
		)

		self.assertEqual(p1.first_name, "Olivia")

	def test_surname(self):
		p1 = Chondathan(
			surname="Healey"
		)

		self.assertEqual(p1.surname, "Healey")

	def test_marry(self):
		# straight
		p1 = Human(gender=Gender.male)
		p2 = Human(gender=Gender.female)

		p1.marry(p2)

		self.assertEqual(p1.partner, p2)
		self.assertEqual(p2.partner, p1)

		# gay
		p1 = Human(gender=Gender.male)
		p2 = Human(gender=Gender.male)

		p1.marry(p2)

		self.assertEqual(p1.partner, p2)
		self.assertEqual(p2.partner, p1)

		# gay 2
		p1 = Human(gender=Gender.female)
		p2 = Human(gender=Gender.female)

		p1.marry(p2)

		self.assertEqual(p1.partner, p2)
		self.assertEqual(p2.partner, p1)

	def test_can_have_children(self):
		# male
		p1 = Chondathan(gender=Gender.male)
		p2 = Chondathan(gender=Gender.male)

		p1.marry(p2)

		self.assertFalse(p1.can_have_children())
		self.assertFalse(p2.can_have_children())

		# female
		p1 = Chondathan(gender=Gender.female)
		p2 = Chondathan(gender=Gender.female)

		p1.marry(p2)

		self.assertFalse(p1.can_have_children())
		self.assertFalse(p2.can_have_children())

		# straight
		p1 = Chondathan(gender=Gender.male)
		p2 = Chondathan(gender=Gender.female)

		p1.marry(p2)

		self.assertTrue(p1.can_have_children())
		self.assertTrue(p2.can_have_children())

	def test_add_child(self):
		p1 = Chondathan(gender=Gender.male)
		p2 = Chondathan(gender=Gender.female)

		p3 = Chondathan(father=p1, mother=p2)
		p1.marry(p2)
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
		self.assertEqual(p2, p3.mother)

	def test_get_is_childs_parents(self):
		p1 = Chondathan(gender=Gender.male)
		p2 = Chondathan(gender=Gender.female)

		p1.marry(p2)

		p3 = p1.create_child()

		self.assertEqual(p1, p3.father)
		self.assertEqual(p2, p3.mother)
		self.assertTrue(p1.get_is_childs_parents(p3))
		self.assertTrue(p2.get_is_childs_parents(p3))

		p4 = Illuskan()

		self.assertNotEqual(p1, p4.father)
		self.assertNotEqual(p2, p4.mother)
		self.assertFalse(p1.get_is_childs_parents(p4))
		self.assertFalse(p2.get_is_childs_parents(p4))

	def test_has_both_parents(self):
		p1 = Chondathan(gender=Gender.male)
		p2 = Chondathan(gender=Gender.female)

		p1.marry(p2)

		p3 = p1.create_child()

		self.assertTrue(p3.has_father())
		self.assertTrue(p3.has_mother())
		self.assertTrue(p3.has_both_parents())
