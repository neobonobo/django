from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # Remove the user_type field, keeping it minimal
    pass
