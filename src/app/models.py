from mongoengine import BooleanField, Document, EmailField, StringField

from .constants import QUALIFICATIONS


class RescueContact(Document):
    first_name = StringField(max_length=50)
    last_name = StringField(max_length=50)
    medical_qualifications = StringField(
        max_length=50, choices=QUALIFICATIONS, default="Qualified first aid", help_text="Qualifications"
    )
    driver = BooleanField(default=False)
    driving_privileges = BooleanField(default=False)
    navigator = BooleanField(default=False)
    planner = BooleanField(default=False)
    email = EmailField(max_length=254, unique=True)
    phone = StringField(max_length=12, unique=True)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name} - {self.medical_qualifications}"
