import json

from graphene_django.utils.testing import GraphQLTestCase
from mongoengine.connection import connect, disconnect
from pymongo import MongoClient

from core.alert_app_env import env

from ..models import RescueContact
from .rescue_contact_factory import RescueContactFactory


class RescueContactTestCase(GraphQLTestCase):
    GRAPHQL_URL = "/api"

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

    # @tag('x')
    def test_query_return_all_contacts(self):
        response = self.query(
            """query MyQuery {
                listRescueContacts {
                    id
                    firstName
                    lastName
                    phone
                    email
                    medicalQualifications
                    driver
                    drivingPrivileges
                    navigator
                    planner
        }
        }
        """
        )

        content = json.loads(response.content)

        self.assertResponseNoErrors(response)

        self.assertEqual(content["data"]["listRescueContacts"][0]["firstName"], self.contact1.first_name)
        self.assertEqual(content["data"]["listRescueContacts"][0]["lastName"], self.contact1.last_name)
        self.assertEqual(content["data"]["listRescueContacts"][0]["phone"], self.contact1.phone)
        self.assertEqual(content["data"]["listRescueContacts"][0]["email"], self.contact1.email)
        self.assertEqual(
            content["data"]["listRescueContacts"][0]["medicalQualifications"], self.contact1.medical_qualifications
        )
        self.assertEqual(content["data"]["listRescueContacts"][0]["driver"], self.contact1.driver)
        self.assertEqual(
            content["data"]["listRescueContacts"][0]["drivingPrivileges"], self.contact1.driving_privileges
        )
        self.assertEqual(content["data"]["listRescueContacts"][0]["navigator"], self.contact1.navigator)
        self.assertEqual(content["data"]["listRescueContacts"][0]["planner"], self.contact1.planner)

        self.assertEqual(content["data"]["listRescueContacts"][1]["firstName"], self.contact2.first_name)
        self.assertEqual(content["data"]["listRescueContacts"][1]["lastName"], self.contact2.last_name)
        self.assertEqual(content["data"]["listRescueContacts"][1]["phone"], self.contact2.phone)
        self.assertEqual(content["data"]["listRescueContacts"][1]["email"], self.contact2.email)
        self.assertEqual(
            content["data"]["listRescueContacts"][1]["medicalQualifications"], self.contact2.medical_qualifications
        )
        self.assertEqual(content["data"]["listRescueContacts"][1]["driver"], self.contact2.driver)
        self.assertEqual(
            content["data"]["listRescueContacts"][1]["drivingPrivileges"], self.contact2.driving_privileges
        )
        self.assertEqual(content["data"]["listRescueContacts"][1]["navigator"], self.contact2.navigator)
        self.assertEqual(content["data"]["listRescueContacts"][1]["planner"], self.contact2.planner)

        self.assertEqual(content["data"]["listRescueContacts"][2]["firstName"], self.contact3.first_name)
        self.assertEqual(content["data"]["listRescueContacts"][2]["lastName"], self.contact3.last_name)
        self.assertEqual(content["data"]["listRescueContacts"][2]["phone"], self.contact3.phone)
        self.assertEqual(content["data"]["listRescueContacts"][2]["email"], self.contact3.email)
        self.assertEqual(
            content["data"]["listRescueContacts"][2]["medicalQualifications"], self.contact3.medical_qualifications
        )
        self.assertEqual(content["data"]["listRescueContacts"][2]["driver"], self.contact3.driver)
        self.assertEqual(
            content["data"]["listRescueContacts"][2]["drivingPrivileges"], self.contact3.driving_privileges
        )
        self.assertEqual(content["data"]["listRescueContacts"][2]["navigator"], self.contact3.navigator)
        self.assertEqual(content["data"]["listRescueContacts"][2]["planner"], self.contact3.planner)

    # @tag('x')
    def test_query_return_one_contact(self):
        contact = RescueContact.objects.get(phone=self.contact1.phone)

        response = self.query(
            """query MyQuery {{
                getRescueContacts (id: "{0}") {{
                    id
                    firstName
                    lastName
                    phone
                    email
                    medicalQualifications
                    driver
                    drivingPrivileges
                    navigator
                    planner
        }}
        }}
        """.format(
                contact.id
            )
        )

        content = json.loads(response.content)

        self.assertResponseNoErrors(response)
        self.assertEqual(content["data"]["getRescueContacts"]["firstName"], self.contact1.first_name)
        self.assertEqual(content["data"]["getRescueContacts"]["lastName"], self.contact1.last_name)
        self.assertEqual(content["data"]["getRescueContacts"]["phone"], self.contact1.phone)
        self.assertEqual(content["data"]["getRescueContacts"]["email"], self.contact1.email)
        self.assertEqual(
            content["data"]["getRescueContacts"]["medicalQualifications"], self.contact1.medical_qualifications
        )
        self.assertEqual(content["data"]["getRescueContacts"]["driver"], self.contact1.driver)
        self.assertEqual(content["data"]["getRescueContacts"]["drivingPrivileges"], self.contact1.driving_privileges)
        self.assertEqual(content["data"]["getRescueContacts"]["navigator"], self.contact1.navigator)
        self.assertEqual(content["data"]["getRescueContacts"]["planner"], self.contact1.planner)

    # # @tag('x')
    # def test_mutation_create_contact(self):
    #     response = self.query(
    #         """mutation MyMutation {
    #         createRescueContact(
    #         firstName: "API_test_create"
    #         lastName: "API_test_create"
    #         phone: "+48111222333"
    #         email: "fakeemail@gmail.com"
    #         medicalQualifications: "Nurse"
    #         driver: true
    #         drivingPrivileges: true
    #         navigator: true
    #         planner: true
    #         ) {
    #         rescueContact {
    #         id
    #         firstName
    #         lastName
    #         phone
    #         email
    #         medicalQualifications
    #         driver
    #         drivingPrivileges
    #         navigator
    #         planner
    #         }
    #         }
    #         }
    #         """)
    #
    #     content = json.loads(response.content)
    #     contact = RescueContact.objects.get(phone='+48111222333')
    #
    #     self.assertResponseNoErrors(response)
    #     self.assertEqual(content['data']['createRescueContact']['rescueContact']['firstName'], 'API_test_create')
    #     self.assertEqual(content['data']['createRescueContact']['rescueContact']['firstName'], contact.first_name)
    #
    #     self.assertEqual(content['data']['createRescueContact']['rescueContact']['lastName'], 'API_test_create')
    #     self.assertEqual(content['data']['createRescueContact']['rescueContact']['lastName'], contact.last_name)
    #
    #     self.assertEqual(content['data']['createRescueContact']['rescueContact']['phone'], '+48111222333')
    #     self.assertEqual(content['data']['createRescueContact']['rescueContact']['phone'], contact.phone)
    #
    #     self.assertEqual(content['data']['createRescueContact']['rescueContact']['email'], 'fakeemail@gmail.com')
    #     self.assertEqual(content['data']['createRescueContact']['rescueContact']['email'], contact.email)
    #
    #     self.assertEqual(content['data']['createRescueContact']['rescueContact']['medicalQualifications'], 'Nurse')
    #     self.assertEqual(content['data']['createRescueContact']['rescueContact']['medicalQualifications'], contact.medical_qualifications)
    #
    # # @tag('x')
    # def test_mutation_update_contact(self):
    #     to_update = RescueContact.objects.get(phone=self.contact1.phone)
    #
    #     response = self.query(
    #         """mutation MyMutation {{
    #                 updateRescueContact(
    #                     firstName: "updated"
    #                     lastName: "updated"
    #                     phone: "+48999888777"
    #                     email: "updated@gmail.com"
    #                     medicalQualifications: "Paramedic"
    #                     driver: false
    #                     drivingPrivileges: false
    #                     navigator: false
    #                     planner: false
    #                     id: "{0}"
    #                     ) {{
    #                     ok
    #                     rescueContact {{
    #                       firstName
    #                       lastName
    #                       phone
    #                       email
    #                       medicalQualifications
    #                       driver
    #                       drivingPrivileges
    #                       navigator
    #                       planner
    #                       id
    #                     }}
    #                     }}
    #                     }}""".format(to_update.id))
    #
    #     content = json.loads(response.content)
    #
    #     self.assertResponseNoErrors(response)
    #     self.assertEqual(content['data']['updateRescueContact']['ok'], True)
    #     self.assertEqual(content['data']['updateRescueContact']['rescueContact']['firstName'], "updated")
    #     self.assertEqual(content['data']['updateRescueContact']['rescueContact']['lastName'], "updated")
    #     self.assertEqual(content['data']['updateRescueContact']['rescueContact']['phone'], "+48999888777")
    #     self.assertEqual(content['data']['updateRescueContact']['rescueContact']['email'], "updated@gmail.com")
    #     self.assertEqual(content['data']['updateRescueContact']['rescueContact']['medicalQualifications'], "Paramedic")
    #     self.assertEqual(content['data']['updateRescueContact']['rescueContact']['driver'], False)
    #     self.assertEqual(content['data']['updateRescueContact']['rescueContact']['drivingPrivileges'], False)
    #     self.assertEqual(content['data']['updateRescueContact']['rescueContact']['navigator'], False)
    #     self.assertEqual(content['data']['updateRescueContact']['rescueContact']['planner'], False)
    #
    # # @tag('x')
    # def test_mutation_delete_contact(self):
    #     to_delete = RescueContact.objects.get(phone=self.contact3.phone)
    #
    #     response = self.query(
    #         """mutation MyMutation {{
    #         deleteRescueContact(id: "{0}") {{
    #         ok
    #         }}
    #         }}
    #         """.format(to_delete.id))
    #
    #     content = json.loads(response.content)
    #     contacts = RescueContact.objects.all()
    #
    #     self.assertResponseNoErrors(response)
    #     self.assertEqual(content['data']['deleteRescueContact']['ok'], True)
    #     self.assertEqual(len(contacts), 2)

    # @tag('x')
    # def test_mutation_send_rescue_message(self):
    #     contacts = RescueContact.objects.all()
    #
    #     response = self.query(
    #         """mutation MyMutation {{
    #         sendAlarm(ids: "{}", message: "test_message") {{
    #         confirmation
    #         }}
    #         }}""".format(contacts[0].id))
    #
    #     result = json.loads(response.content)
    #     print(result['data']['sendAlarm']['confirmation'])
    #
    #     # self.assertEqual()
