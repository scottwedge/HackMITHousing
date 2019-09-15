"""
Algorithm for computing score between a landlord's request and a tenant's availability
"""

import datetime

import requests

def geocode_request(landlord_address, tenant_address):
  """
  NOT BEING USED
  """
  # api-endpoint 
  URL = "https://maps.googleapis.com/maps/api/geocode/json"

  # location given here 
  #location = "Massachusetts Institute of Technology"
  key = "AIzaSyC6_cXqg7wSDJMhx9Z19VV3AdgH5ZqXMnI" #this is our personal key for the Google Maps API
  
  # defining a params dict for the parameters to be sent to the API 
  params_landlord = {'address':landlord_address, 'key':key} 
  params_tenant = {'address':tenant_address, 'key':key}

  # sending get request and saving the response as response object 
  response_landlord = requests.get(url = URL, params = params_landlord) 
  response_tenant = requests.get(url = URL, params = params_tenant)

  # extracting data in json format 
  data_l = response_landlord.json() 
  data_t = response_tenant.json()

  # extracting latitude, longitude and formatted address  
  # of the first matching location 
  latitude_l = data_l['results'][0]['geometry']['location']['lat'] 
  longitude_l = data_l['results'][0]['geometry']['location']['lng'] 
  formatted_address_l = data_l['results'][0]['formatted_address'] 
  
  latitude_t = data_t['results'][0]['geometry']['location']['lat'] 
  longitude_t = data_t['results'][0]['geometry']['location']['lng'] 
  formatted_address_t = data_t['results'][0]['formatted_address']

  # printing the output 
  #print("Latitude:%s\nLongitude:%s\nFormatted Address:%s" %(latitude, longitude,formatted_address))


def calc_dist_diff(landlord_loc, tenant_loc):
  """
  method to return walking distance in minutes
  """  
  URL = "https://maps.googleapis.com/maps/api/distancematrix/json"

  key = "AIzaSyC6_Bj65KjeNOmigkezVM3RI5sfI8K-TmA" #this is our personal key for the Distance Matrix API

  #loc1 = "Massachusetts Institute of Technology"
  #loc2 = "Harvard University"

  PARAMS = {'origins': landlord_loc, 'destinations': tenant_loc, 'key': key, 'mode': "walking"}

  r = requests.get(url=URL, params = PARAMS)

  data = r.json()

  res = data['rows'][0]['elements'][0]['duration']['text'].split(" ") 
  
  #hack to parse the result into int that represents the minute
  final_res = 0
  
  i = 1
  while i < len(res):
    if res[i] == 'days' or res[i] == 'day':
      final_res += 1440 * int(res[i-1])
    elif res[i] == 'hours' or res[i] == 'hour':
      final_res += 60 * int(res[i-1])
    else:
      final_res += int(res[i-1])

    i += 2

  
  return float(final_res)



def calc_diff(landlord, tenant):
  """
  Algorithm to calculate the difference score for one pair of landlord and tenant
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
  dist_diff = calc_dist_diff(landlord[LOCATION], tenant[LOCATION])

  
  #the following needs to be changed
  res = []
  res.append(hour_diff)
  res.append(dist_diff)
  
  #print(res)
  return sum(res)


def print_info(tenants, idx):
  """
  inputs: tenants: list of tenant arrays; idx
  """

  print("Name: {}, {}".format(tenants[idx][NAME_LAST], tenants[idx][NAME_FIRST]))
  print("Age: {}".format(tenants[idx][AGE]))
  print("Start Date (MM/DD/YYYY): {} / {}, {}".format(tenants[idx][MONTH_START], tenants[idx][DATE_START], tenants[idx][YEAR]))
  print("Hours: {}".format(tenants[idx][HOURS]))
  print("Location: {}".format(tenants[idx][LOCATION]))
  print("——————")
  
  
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
  LOCATION = 8 #type should be string
  NAME_LAST = 9 #type: str
  NAME_FIRST = 10 #type: str
  AGE = 11 #type: int


  #Value for each work type
  KITCHEN = 0 #kitchen
  BATH = 1 #bathroom
  FURN = 2 #furniture
  ALL = 3 #entire apartment
  
  loc1 = "Massachusetts Institute of Technology"
  loc2 = "Harvard University"
  loc3 = "Tufts University"
  loc4 = "700 Boylston Street, MA" #Boston Public Library
  
  landlord = [2018, 5, 1, 5, 10, ALL, 3, 2, loc1]
  tenants = [[2018, 4, 2, 6, 5, ALL, 3, 4, loc2, "Smith", "John", 40],
              [2018,5, 2, 5, 20, BATH, 4, 3, loc4, "Fish", "Jane", 46],
              [2018, 4, 2, 6, 30, ALL, 3, 1, loc3, "Last Name", "First Name", 48]]
  
  res = main(landlord, tenants)

  sorted_res = sorted(res.items(), key=lambda kv: kv[1])
  
  print("The sorted recommendations are [tenant id, diff score]")
  print(sorted_res)
  

  for idx, score in sorted_res:
      print_info(tenants, idx)
