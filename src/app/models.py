from mongoengine import BooleanField, Document, EmailField, StringField

from .constants import QUALIFICATIONS


class RescueContact(Document):
    first_name = StringField(max_length=50)
    last_name = StringField(max_length=50)
    medical_qualifications = StringField(
        max_length=50, choices=QUALIFICATIONS, default="Qualified first aid", help_text="Qualifications"
    )
    is_driver = BooleanField(default=False)
    has_vehicle_driving_privileges = BooleanField(default=False)
    is_navigator = BooleanField(default=False)
    is_planner = BooleanField(default=False)
    email = EmailField(max_length=254, unique=True)
    phone = StringField(max_length=12, unique=True)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name} - {self.medical_qualifications}"
