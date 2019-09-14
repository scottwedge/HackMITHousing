from django.db import models

import datetime 

GENDERS = [('male', 'MALE'), ('female', 'FEMALE')]
WORK_TYPES = [('kitchen', 'KITCHEN'), ('bathroom', 'BATHROOM'), ('furniture', 'FURNITURE'), ('all', 'ALL')]

class Employee(models.Model):
  name = models.CharField(max_length=200)
  gender = models.ChoiceField(choices=GENDERS)
  
  #calendar mode??
  start_year = models.IntegerField(min_value = datetime.now().year, 
                                   max_value = datetime.now().year + 1)
  start_month = models.IntegerField(min_value=1, max_value=12)
  #start_date = 
  
  
  work_type = models.ChoiceField(choices=WORK_TYPES)
  max_hours = models.IntegerField(min_value=1, max_value=24)
