from django.db import models

import datetime 
from calendar immport monthrange

GENDERS = [('male', 'MALE'), ('female', 'FEMALE')]
WORK_TYPES = [('kitchen', 'KITCHEN'), ('bathroom', 'BATHROOM'), ('furniture', 'FURNITURE'), ('all', 'ALL')]


class Employer(models.Model):
  
  employer_id = models.AutoField(primary_key=True)
  name = models.CharField(max_length=200)
  gender = models.ChoiceField(choices=GENDERS)
  age = models.IntegerField(max_value=90)
  
  start_date = models.DateField(input_format='%Y-%m-%d', initial=datetime.date.today)
  end_date = models.DateField(input_format='%Y-%m-%d', initial=datetime.date.today)
  
  work_type = models.ChoiceField(choices=WORK_TYPES)
  min_hours = models.IntegerField(min_value=1, max_value=24)
  street_address = models.CharField(max_length=500)
  city = models.CharField(max_length=100)
  state = models.CharField(max_length=100)
