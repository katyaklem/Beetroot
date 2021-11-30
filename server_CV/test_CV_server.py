import unittest

from CV_server import Skill, Contact

class TestSkill(unittest.TestCase):
	def test_add_skill(self):
		new_skill = Skill('languages', 'eng', 15, 'expert')
		self.assertEqual(new_skill.category, 'languages')
		self.assertEqual(new_skill.name, 'eng')
		self.assertEqual(new_skill.experience, 15)
		self.assertEqual(new_skill.level, 'expert')

	def test_add_skill_mistake(self):
		new_skill = Skill('programmist', 'py', 'ten years', 'guru')
		self.assertEqual(new_skill.category, None)
		self.assertEqual(new_skill.name, 'py')
		self.assertEqual(new_skill.experience, None)
		self.assertEqual(new_skill.level, None)

	def test_add_contact_phone(self):
		new_contact = Contact('phone', 380)
		self.assertEqual(new_contact.contact_type, 'phone')
		self.assertEqual(new_contact.value, 380)

	def test_add_contact_email(self):
		new_contact = Contact('email', 'some@some.com')
		self.assertEqual(new_contact.contact_type, 'email')
		self.assertEqual(new_contact.value, 'some@some.com')

	def test_add_contact_phone_mistake(self):
		new_contact = Contact('phone', '234567')
		self.assertEqual(new_contact.contact_type, 'phone')
		self.assertEqual(new_contact.value, None)

	def test_add_contact_email_mistake(self):
		new_contact = Contact('email', 'somesome.com')
		self.assertEqual(new_contact.contact_type, 'email')
		self.assertEqual(new_contact.value, None)
'''
	def test_add_contact_mistake(self):
		new_contact = Contact('some', 'some@some.com')
		self.assertEqual(new_contact.contact_type, None)
		self.assertEqual(new_contact.value, None)

'''

