from django.db import models

GENDERS = [('male', 'MALE'), ('female', 'FEMALE')]

class Employee(models.Model):
  name = models.CharField(max_length=200)
  gender = models.ChoiceField(choices=GENDERS)
