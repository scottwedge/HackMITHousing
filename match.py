"""
Toy algorithm for computing score between a landlord's request and a tenant's availability

Output: 

"""

from datetime import *

NUM_TAG =  #ie. length of each user's array

#map each tag to its index in the array
WORK_TYPE = 
YEAR = 
MONTH_START = 
DATE_START = 
MONTH_END = 
DATE_END = 
HOURS = 
DISTANCE = 
PRICE = 
RATE = 

#Value for each work type
KITCHEN = 0 #kitchen
BATH = 1 #bathroom
FURN = 2 #furniture
ALL = 3 #entire apartment


#landlord: list for curr landlord
#tenants: list for all tenants

res = {}


for tenant in tenants:

  #work type doesn't match, return very high diff score
  if landlord[WORK_TYPE] != tenant[WORK_TYPE]:
    return #??
  
  #Check for overlap in date
  l_date_start = datetime.datetime(landlord[YEAR], landlord[MONTH_START], landlord[DATE_START])
  l_date_end = datetime.datetime(landlord[YEAR], landlord[MONTH_END], landlord[DATE_END])
  t_date_start = datetime.datetime(tenant[YEAR], tenant[MONTH_START], tenant[DATE_START])
  t_date_end = datetime.datetime(tenant[YEAR], tenant[MONTH_END], tenant[DATE_END])
  
  if not (t_date_start >= l_date_start or t_date_end <= l_date_end): #no overlap front or back
    return #??
  
  
  #check for rating expectation
  if tenant[RATE] < landlord[RATE]:
    return #??
  
  #diff in expectation of hours
  hour_diff = abs(landlord[HOURS] - tenant[HOURS]) 
  
  #diff in location distance
  dist_diff = abs(landlord[DIST] - tenant[DIST])
  
  
  
