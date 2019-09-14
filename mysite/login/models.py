from django.db import models


# can only assume one role

class Profile(models.Model):
  TYPE_CHOICES = (
      (1, 'employer'),
      (2, 'employee'),
      (3, 'landlord'),
      (4, 'tenant'),
  )

type = models.CharField(max_length=3, choices=TYPE_CHOICES, unique=True, null=True, blank=True, default=None)
user = models.OneToOneField(User, on_delete=models.CASCADE)
first_name = models.CharField(max_length=50, null=True, blank=True, default=None)
last_name = models.CharField(max_length=50, null=True, blank=True, default=None)
gender = models.CharField(max_length=30, null=True, blank=True, default=None)
phone = models.CharField(max_length=50, unique=True, null=True, blank=True, default=None)
address = models.CharField(max_length=50, unique=True, null=True, blank=True, default=None)
