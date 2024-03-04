import random

from factory import Factory, Faker

from ..constants import QUALIFICATIONS
from ..models import RescueContact


class RescueContactFactory(Factory):
    class Meta:
        model = RescueContact

    first_name = Faker("first_name")
    last_name = Faker("last_name")
    email = Faker("email")
    phone = Faker("pyint", min_value=100000000, max_value=999999999)
    medical_qualifications = random.choice(QUALIFICATIONS)[0]
    driver = Faker("boolean")
    driving_privileges = Faker("boolean")
    navigator = Faker("boolean")
    planner = Faker("boolean")
