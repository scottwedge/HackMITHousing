"""
Toy algorithm for computing score between a landlord's request and a tenant's availability
TODO:
  calc_dist_diff
  get tenant id
"""

import datetime

import requests

def geocode_request(landlord_address, tenant_address):
  # api-endpoint 
  URL = "https://maps.googleapis.com/maps/api/geocode/json"

  # location given here 
  landlord_address = "Massachusetts Institute of Technology"
  key = "AIzaSyC6_cXqg7wSDJMhx9Z19VV3AdgH5ZqXMnI" #this is our personal key for the Google Maps API

  # defining a params dict for the parameters to be sent to the API 
  params_landlord = {'address':landlord_address, 'key':key} 

  # sending get request and saving the response as response object 
  response_landlord = requests.get(url = URL, params = params_landlord) 

  # extracting data in json format 
  data_landlord = response_landlord.json() 


  # extracting latitude, longitude and formatted address  
  # of the first matching location 
  latitude_l = data['results'][0]['geometry']['location']['lat'] 
  longitude_l = data['results'][0]['geometry']['location']['lng'] 
  formatted_address_l = data['results'][0]['formatted_address'] 

  # printing the output 
  #print("Latitude:%s\nLongitude:%s\nFormatted Address:%s" %(latitude, longitude,formatted_address))


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
    return float("inf")
  
  #Check for overlap in date
  l_date_start = datetime.datetime(landlord[YEAR], landlord[MONTH_START], landlord[DATE_START])
  l_date_end = datetime.datetime(landlord[YEAR], landlord[MONTH_END], landlord[DATE_END])
  t_date_start = datetime.datetime(tenant[YEAR], tenant[MONTH_START], tenant[DATE_START])
  t_date_end = datetime.datetime(tenant[YEAR], tenant[MONTH_END], tenant[DATE_END])
  
  if not (t_date_start <= l_date_start or t_date_end >= l_date_end): #no overlap front or back
    #print("no overlap in time")
    return float("inf")
  
  
  #check for rating expectation
  if tenant[RATE] < landlord[RATE]:
    return float("inf")
  
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
  tenant_id = 0

  for tenant in tenants:
    
    diff = calc_diff(landlord, tenant)

    res[tenant_id] = diff
    tenant_id += 1
  
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
  tenants = [[2018, 4, 2, 6, 5, ALL, 3, 4, 0, 0],
              [2018,5, 2, 5, 20, BATH, 4, 3, 0, 0],
              [2018, 4, 2, 6, 30, ALL, 3, 1, 0, 0]]
  
  res = main(landlord, tenants)

  sorted_res = sorted(res.items(), key=lambda kv: kv[1])
          
  print(sorted_res)
  
