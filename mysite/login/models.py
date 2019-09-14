from django.db import models


# can only assume one role

# user = models.OneToOneField(User, on_delete=models.CASCADE)
first_name = models.CharField(max_length=50, null=True, blank=True, default=None)
last_name = models.CharField(max_length=50, null=True, blank=True, default=None)
gender = models.CharField(max_length=30, null=True, blank=True, default=None)
phone = models.CharField(max_length=50, unique=True, null=True, blank=True, default=None)
address = models.CharField(max_length=50, unique=True, null=True, blank=True, default=None)
