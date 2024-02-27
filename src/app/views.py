from smtplib import SMTPException

from django.conf import settings
from django.core.mail import EmailMessage
from twilio.base.exceptions import TwilioException
from twilio.rest import Client

from .models import RescueContact


class SendingAlarmMessages:
    def __init__(self, ids, message):
        self.__ids = ids
        self.__message = message

    def main(self):
        self.__get_contacts()
        self.__get_email_phone_lists()
        self.__send_email()
        self.__send_sms()

        return self.contacts

    def __get_contacts(self):
        self.contacts = RescueContact.objects.filter(id__in=self.__ids)

    def __get_email_phone_lists(self):
        self.__email_list = [contact.email for contact in self.contacts]
        self.__phone_list = [contact.phone for contact in self.contacts]

    #
    # def __send_email(self):
    #     try:
    #         message = EmailMessage(
    #             subject='Rescue Alert',
    #             body=self.__message,
    #             from_email=settings.DEFAULT_FROM_EMAIL,
    #             to=self.__email_list,
    #         )
    #         message.send()
    #         return True
    #
    #     except SMTPException as e:
    #         print(f"SMTPException: {e}")
    #         return False
    #
    #
    # def __send_sms(self):
    #     client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
    #     for phone in self.__phone_list:
    #         try:
    #             client.messages.create(
    #                 to=phone,
    #                 from_=settings.TWILIO_PHONE_NUMBER,
    #                 body=self.__message
    #             )
    #
    #         except TwilioException as e:
    #             print(f"TwilioException: {e}")
    #             continue
