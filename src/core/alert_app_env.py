from django.core.management.utils import get_random_secret_key
from environ import Env

env = Env(
    DEBUG=(bool, False),
    SECRET_KEY=(str, get_random_secret_key()),
    EMAIL_HOST_PASSWORD=(str, "your_email_host_user_password"),
    EMAIL_HOST_USER=(str, "your_email_host_user"),
    DEFAULT_FROM_EMAIL=(str, "default_email_address"),
    TWILIO_ACCOUNT_SID=(str, "your_twilio_account_sid"),
    TWILIO_AUTH_TOKEN=(str, "your_twilio_auth_token"),
    TWILIO_PHONE_NUMBER=(str, "your_twilio_phone_number"),
    MONGODB_NAME=(str, "your_mongodb_database_name"),
    MONGODB_HOST=(str, "your_mongodb_database_host"),
    MONGODB_PORT=(int, "default=27017"),
)
