"""
Toy algorithm for computing score between a landlord's request and a tenant's availability

Output: 

"""

from datetime import *


def calc_dist_diff(self, landlord_x, landlord_y, tenant_x, tenant_y):
  """
  method to return a score that represents difference in distance
  """
  
  #to d0
  
  
  return 2.0 #needs to be changed 



def calc_diff(self, landlord, tenant):
  """
  Main algorithm to calculate the difference score for one pair of landlord and tenant
  output: diff score ---???
  """


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
  dist_diff = self.calc_dist_diff(landlord[LOC_X], landlord[LOC_Y], tenant[LOC_X], tenant[LOC_Y])

  
  #the following needs to be changed
  res = []
  res.append(hour_diff)
  res.append(dist_diff)
  
  return res
  
  
def main(self, landlord, tenants):
  """
  output: dictioanry "res" that has every tenant's score
  """

  res = {}

  for tenant in tenants:
    
    diff = self.calc_diff(landlord, tenant)
    res.append(diff)

  return res

if __name__ == '__main__':
  
  NUM_TAG = 9 #ie. length of each user's array

  #map each tag to its index in the array
  YEAR = 0
  MONTH_START = 1
  DATE_START = 2
  MONTH_END = 3
  DATE_END = 4
  WORK_TYPE = 5
  RATE = 6 #rating
  HOURS = 7
  LOC_X = 8
  LOC_Y = 9


  #Value for each work type
  KITCHEN = 0 #kitchen
  BATH = 1 #bathroom
  FURN = 2 #furniture
  ALL = 3 #entire apartment
           
  
  landlord = [2018, 5, 1, 5, 10, ALL, 3, 2, 0, 0]
  tenants = [[2018, 4, 1, 6, 1, ALL, 3, 4, 0, 0]]
  
  res = self.main(landlord, tenants)
           
  print(res)
  
