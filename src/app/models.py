from django.db import models

from .constants import QUALIFICATIONS


class RescueContact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    medical_qualifications = models.CharField(
        max_length=50, choices=QUALIFICATIONS, default="Qualified first aid", help_text="Qualifications"
    )
    is_driver = models.BooleanField(default=False)
    has_vehicle_driving_privileges = models.BooleanField(default=False)
    is_navigator = models.BooleanField(default=False)
    is_planner = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.medical_qualifications}"
