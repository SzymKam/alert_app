from smtplib import SMTPException

from django.conf import settings
from django.core.mail import EmailMessage
from twilio.base.exceptions import TwilioException
from twilio.rest import Client

from .models import RescueContact


class SendingAlarmMessages:
    def __init__(self, ids, message) -> None:
        self.__ids = ids
        self.__message = message

    def main(self) -> dict:
        self.__get_contacts()
        email_result = self.__send_email()
        sms_result = self.__send_sms()

        return {"email": email_result, "sms": sms_result}

    def __get_contacts(self) -> None:
        self.contacts = RescueContact.objects.filter(id__in=self.__ids)

    def __send_email(self) -> dict:
        email_confirmation = dict()
        for contact in self.contacts:
            try:
                message = EmailMessage(
                    subject="Rescue Alert",
                    body=self.__message,
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    to=[contact.email],
                )
                message.send()
                email_confirmation.update({"user": contact.email, "info": "sent"})

            except SMTPException:
                email_confirmation.update({"user": contact.email, "info": "error"})
                continue

        return email_confirmation

    def __send_sms(self) -> dict:
        sms_confirmation = dict()
        client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)

        for contact in self.contacts:
            try:
                client.messages.create(to=contact.phone, from_=settings.TWILIO_PHONE_NUMBER, body=self.__message)
                sms_confirmation.update({"user": contact.phone, "info": "sent"})
            except TwilioException:
                sms_confirmation.update({"user": contact.phone, "info": "error"})
                continue

        return sms_confirmation
