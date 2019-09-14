"""
Toy algorithm for computing score between a landlord's request and a tenant's availability

Output: 
"""

NUM_TAG = 5 #ie. length of each user's array

#map each tag to its index in the array
WORK_TYPE = 0
HOURS = 1
DISTANCE = 2
NUM_WORKER = 3
PRICE = 4

#Value for each work type
KITCHEN = 0 #kitchen
BATH = 1 #bathroom
FURN = 2 #furniture
ALL = 3 #entire apartment




tenants = [] #list for all tenants
res = {}


landlord = [0 for i in range(NUM_TAG)] #curr landlord

for tenant in tenants:

  #work type doesn't match, return very high diff score
  if landlord[WORK_TYPE] != tenant[WORK_TYPE]:
    return #??
