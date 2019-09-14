from django.db import models

import datetime 
from calendar immport monthrange

GENDERS = [('male', 'MALE'), ('female', 'FEMALE')]
WORK_TYPES = [('kitchen', 'KITCHEN'), ('bathroom', 'BATHROOM'), ('furniture', 'FURNITURE'), ('all', 'ALL')]

class Employee(models.Model):
  
  employee_id = models.AutoField(primary_key=True)
  name = models.CharField(max_length=200)
  gender = models.ChoiceField(choices=GENDERS)
  
  
  #How to parse date format into a uniform one??
  start_year = models.IntegerField(min_value = datetime.now().year, 
                                   max_value = datetime.now().year + 1)
  start_month = models.IntegerField(min_value=1, max_value=12)
  start_date = models.IntegerField(min_value=1, max_value=monthrange(datetime.now().year, start_month)[1])
  
  
  end_year = models.IntegerField(min_value = datetime.now().year, 
                                   max_value = datetime.now().year + 1)
  end_month = models.IntegerField(min_value=1, max_value=12)
  end_date = models.IntegerField(min_value=1, max_value=monthrange(datetime.now().year, end_month)[1])
  
  
  
  work_type = models.ChoiceField(choices=WORK_TYPES)
  max_hours = models.IntegerField(min_value=1, max_value=24)
  city = models.CharField(max_length=100)
  state = models.CharField(max_length=100)
