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
        try:
            message = EmailMessage(
                subject="Rescue Alert",
                body=self.__message,
                from_email=settings.DEFAULT_FROM_EMAIL,
                to=[contact.email for contact in self.contacts],
            )
            message.send()
            return {"email_sent": "sent successfully"}

        except SMTPException as error:
            return {"email_sent": error}

    def __send_sms(self) -> dict:
        confirmation = dict()
        client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)

        for contact in self.contacts:
            try:
                client.messages.create(to=contact.phone, from_=settings.TWILIO_PHONE_NUMBER, body=self.__message)
                confirmation.update({"sent": contact.phone})
            except TwilioException as error:
                confirmation.update({"not sent": contact.phone, "error": error})
                continue

        confirmation = {"sms_sent": confirmation}
        return confirmation
