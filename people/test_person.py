from unittest import TestCase

from people.Gender import Gender
from people.Person import Person
from race.core.Races import Chondathan


class TestPerson(TestCase):
	def test_race(self):
		p1 = Person(race=Chondathan())
		self.assertIsInstance(p1.race, Chondathan)
		self.assertEqual(str(p1.race), "Chondathan")

	def test_gender(self):
		p1 = Person(gender=Gender.male)
		self.assertEqual(p1.gender, Gender.male)

		p2 = Person(gender=Gender.female)
		self.assertEqual(p2.gender, Gender.female)

	def test_first_name(self):
		p1 = Person(
			first_name="Olivia"
		)

		self.assertEqual(p1.first_name, "Olivia")

	def test_surname(self):
		p1 = Person(
			surname="Healey"
		)

		self.assertEqual(p1.surname, "Healey")

	def test_marry(self):
		# straight
		p1 = Person(gender=Gender.male)
		p2 = Person(gender=Gender.female)

		p1.marry(p2)

		self.assertEqual(p1.partner, p2)
		self.assertEqual(p2.partner, p1)

		# gay
		p1 = Person(gender=Gender.male)
		p2 = Person(gender=Gender.male)

		p1.marry(p2)

		self.assertEqual(p1.partner, p2)
		self.assertEqual(p2.partner, p1)

		# gay 2
		p1 = Person(gender=Gender.female)
		p2 = Person(gender=Gender.female)

		p1.marry(p2)

		self.assertEqual(p1.partner, p2)
		self.assertEqual(p2.partner, p1)

	def test_can_have_children(self):
		# male
		p1 = Person(gender=Gender.male)
		p2 = Person(gender=Gender.male)

		p1.marry(p2)

		self.assertFalse(p1.can_have_children())
		self.assertFalse(p2.can_have_children())

		# female
		p1 = Person(gender=Gender.female)
		p2 = Person(gender=Gender.female)

		p1.marry(p2)

		self.assertFalse(p1.can_have_children())
		self.assertFalse(p2.can_have_children())

		# straight
		p1 = Person(gender=Gender.male)
		p2 = Person(gender=Gender.female)

		p1.marry(p2)

		self.assertTrue(p1.can_have_children())
		self.assertTrue(p2.can_have_children())

	def test_add_child(self):
		p1 = Person(gender=Gender.male)
		p2 = Person(gender=Gender.female)

		p3 = Person(father=p1, mother=p2)
		p1.marry(p2)
		p1.add_child(p3)

		self.assertEqual(p3.father, p1)
		self.assertEqual(p3.mother, p2)

		self.assertIn(p3, p1.children)
		self.assertIn(p3, p2.children)

	def test_get_child_race(self):
		p1 = Person(gender=Gender.male)
		p2 = Person(gender=Gender.female)

		p1.marry(p2)

		self.assertEqual(p1.get_child_race(), Person)

		p1 = Person(gender=Gender.male)
		p2 = Person(gender=Gender.female)

		p1.marry(p2)

		self.assertIn(p1.get_child_race(), [Person, Person])

	def test_create_child(self):
		p1 = Person(gender=Gender.male)
		p2 = Person(gender=Gender.female)

		p1.marry(p2)

		p3 = p1.create_child()

		self.assertEqual(p1.children[0], p3)
		self.assertEqual(p2.children[0], p3)

		self.assertEqual(p1, p3.father)
		self.assertEqual(p2, p3.mother)

	def test_get_is_childs_parents(self):
		p1 = Person(gender=Gender.male)
		p2 = Person(gender=Gender.female)

		p1.marry(p2)

		p3 = p1.create_child()

		self.assertEqual(p1, p3.father)
		self.assertEqual(p2, p3.mother)
		self.assertTrue(p1.get_is_childs_parents(p3))
		self.assertTrue(p2.get_is_childs_parents(p3))

		p4 = Person()

		self.assertNotEqual(p1, p4.father)
		self.assertNotEqual(p2, p4.mother)
		self.assertFalse(p1.get_is_childs_parents(p4))
		self.assertFalse(p2.get_is_childs_parents(p4))

	def test_has_both_parents(self):
		p1 = Person(gender=Gender.male)
		p2 = Person(gender=Gender.female)

		p1.marry(p2)

		p3 = p1.create_child()

		self.assertTrue(p3.has_father())
		self.assertTrue(p3.has_mother())
		self.assertTrue(p3.has_both_parents())

	def test_siblings(self):
		p1 = Person(gender=Gender.male)
		p2 = Person(gender=Gender.female)

		p1.marry(p2)

		c1 = p1.create_child()
		c2 = p1.create_child()
		c3 = p1.create_child()

		self.assertIn(c1, c2.get_siblings())
		self.assertIn(c1, c3.get_siblings())
		self.assertNotIn(c1, c1.get_siblings())

		self.assertEqual(c1.father, c2.father, c3.father)

		self.assertIn(c1, c2.father.children)
		self.assertIn(c1, c3.mother.children)
