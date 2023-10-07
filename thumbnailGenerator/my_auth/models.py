from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class User(AbstractUser):
    BASIC = "BA"
    PREMIUM = "PR"
    ENTERPRISE = "EN"
    TIER_CHOICES = [(BASIC, "Basic"),
                    (PREMIUM, "Premium"),
                    (ENTERPRISE, "Enterprise")]
    tier = models.CharField(max_length=16, choices=TIER_CHOICES)
