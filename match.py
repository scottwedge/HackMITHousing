"""
Toy algorithm for computing score between a landlord's request and a tenant's availability

Output: 

"""

from datetime import *


def calc_dist_diff(self, landlord_x, landlord_y, tenant_x, tenant_y):
  """
  method to return a score that represents difference in distance
  """
  pass 




def calc_diff(self, landlord, tenant):
  """
  Main algorithm to calculate the difference score for one pair of landlord and tenant
  """
  
  res = {}

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
  dist_diff = #??? use 
  
  res["hour_diff"] = hour_diff
  res["dist_diff"] = dist_diff

  
  
__main__():
  NUM_TAG = 9 #ie. length of each user's array

  #map each tag to its index in the array
  YEAR = 0
  MONTH_START = 1
  DATE_START = 2
  MONTH_END = 3
  DATE_END = 4
  WORK_TYPE = 5
  RATE = 6
  HOURS = 7
  LOC_X = 8
  LOC_Y = 9


  #Value for each work type
  KITCHEN = 0 #kitchen
  BATH = 1 #bathroom
  FURN = 2 #furniture
  ALL = 3 #entire apartment


  #landlord: list for curr landlord
  #tenants: list for all tenants

  landlord[2019, 5, 1, 5, 10, ALL, 10, 2, 


  for tenant in tenants:
  
  
  
  
