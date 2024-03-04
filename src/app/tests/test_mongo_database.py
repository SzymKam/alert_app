from django.test import TestCase
from mongoengine.connection import connect, disconnect
from pymongo import MongoClient

from core.alert_app_env import env

from ..models import RescueContact
from .rescue_contact_factory import RescueContactFactory


class RescueContactTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        disconnect(alias="default")
        connect(db="alert_app_db_mongo_test", host=env("MONGODB_HOST"), port=int(env("MONGODB_PORT")), alias="default")

    def setUp(self):
        self.contact1 = RescueContactFactory()
        self.contact1.phone = "+48" + str(self.contact1.phone)
        self.contact1.save()

        self.contact2 = RescueContactFactory()
        self.contact2.phone = "+48" + str(self.contact2.phone)
        self.contact2.save()

        self.contact3 = RescueContactFactory()
        self.contact3.phone = "+48" + str(self.contact3.phone)
        self.contact3.save()

    def tearDown(self):
        RescueContact.objects.all().delete()

    @classmethod
    def tearDownClass(cls):
        disconnect(alias="default")
        connection = MongoClient(env("MONGODB_HOST"), int(env("MONGODB_PORT")))
        connection.drop_database("alert_app_db_mongo_test")

    # def test_database_return_rescue_contacts(self):
    #     contacts = RescueContact.objects.all()
    #     self.assertEqual(len(contacts), 3)
    #     self.assertEqual(contacts[0].phone, self.contact1.phone)
    #     self.assertEqual(contacts[1].first_name, self.contact2.first_name)
    #     self.assertEqual(contacts[2].last_name, self.contact3.last_name)
    #
    # def test_database_return_one_rescue_contact(self):
    #     contact = RescueContact.objects.filter(phone=self.contact1.phone)
    #     self.assertEqual(len(contact), 1)
    #     self.assertEqual(contact[0].first_name, self.contact1.first_name)
    #     self.assertEqual(contact[0].last_name, self.contact1.last_name)
    #     self.assertEqual(contact[0].email, self.contact1.email)
    #
    # def test_database_create_object(self):
    #     new_contact = RescueContactFactory()
    #     new_contact.phone = "+48" + str(new_contact.phone)
    #     new_contact.save()
    #
    #     contacts = RescueContact.objects.all()
    #     self.assertEqual(len(contacts), 4)
    #     self.assertEqual(contacts[3].phone, new_contact.phone)
    #     self.assertEqual(contacts[3].email, new_contact.email)
    #     self.assertEqual(contacts[3].first_name, new_contact.first_name)
    #     self.assertEqual(contacts[3].last_name, new_contact.last_name)
    #
    # def test_database_update_object(self):
    #     old_contact = RescueContact.objects.get(phone=self.contact2.phone)
    #     print(old_contact)
    #
    #     old_contact.first_name = "John"
    #     old_contact.last_name = "Wick"
    #     old_contact.email = "john@wick.com"
    #     old_contact.save()
    #
    #     self.assertEqual(old_contact.first_name, "John")
    #     self.assertEqual(old_contact.last_name, "Wick")
    #     self.assertEqual(old_contact.email, "john@wick.com")
    #
    # def test_database_delete_object(self):
    #     RescueContact.objects.get(phone=self.contact3.phone).delete()
    #     result = RescueContact.objects.all()
    #
    #     self.assertEqual(len(result), 2)
    #     self.assertEqual(result[0].phone, self.contact1.phone)
    #     self.assertEqual(result[1].phone, self.contact2.phone)
