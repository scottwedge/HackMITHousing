"""
Toy algorithm for computing score between a landlord's request and a tenant's availability
Output: 
"""

import datetime



def calc_dist_diff(landlord_x, landlord_y, tenant_x, tenant_y):
  """
  method to return a score that represents difference in distance
  """
  
  #to d0
  
  
  return 2.0 #needs to be changed 



def calc_diff(landlord, tenant):
  """
  Main algorithm to calculate the difference score for one pair of landlord and tenant
  output: diff score ---???
  """


  #work type doesn't match, return very high diff score
  if landlord[WORK_TYPE] != tenant[WORK_TYPE]:
    return [-1]
  
  #Check for overlap in date
  l_date_start = datetime.datetime(landlord[YEAR], landlord[MONTH_START], landlord[DATE_START])
  l_date_end = datetime.datetime(landlord[YEAR], landlord[MONTH_END], landlord[DATE_END])
  t_date_start = datetime.datetime(tenant[YEAR], tenant[MONTH_START], tenant[DATE_START])
  t_date_end = datetime.datetime(tenant[YEAR], tenant[MONTH_END], tenant[DATE_END])
  
  if not (t_date_start <= l_date_start or t_date_end >= l_date_end): #no overlap front or back
    #print("no overlap in time")
    return [-1]
  
  
  #check for rating expectation
  if tenant[RATE] < landlord[RATE]:
    return [-1]
  
  #diff in expectation of hours
  hour_diff = float(abs(landlord[HOURS] - tenant[HOURS])) 
  
  #diff in location distance
  dist_diff = calc_dist_diff(landlord[LOC_X], landlord[LOC_Y], tenant[LOC_X], tenant[LOC_Y])

  
  #the following needs to be changed
  res = []
  res.append(hour_diff)
  res.append(dist_diff)
  
  #print(res)
  return sum(res)
  
  
def main(landlord, tenants):
  """
  output: dictioanry "res" that has every tenant's score
  """

  res = {}

  for tenant in tenants:
    
    diff = calc_diff(landlord, tenant)

    tenant_id = 0
    res[tenant_id] = diff
  
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
  tenants = [[2018, 4, 2, 6, 5, ALL, 3, 4, 0, 0]]
  
  res = main(landlord, tenants)
          
  print(res)
  
