from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ROLE_CHOICES = (
        ('super_admin', 'Super Admin'),
        ('csr', 'CSR'),
        ('client', 'Hatchery Client'),
        ('consultant', 'Hatchery Consultant'),
        ('staff', 'Hatchery Staff'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='client')