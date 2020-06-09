import json

# JSON parser class that parses JSON; initialized \
# with necessary information to parse the way user wants

class JSONparser:
    def __init__(self, batch_size=50):
        self.batch_size = batch_size

test_json = '''
{
    "fields": {
      "LogEndOffset": 0,
      "LogStartOffset": 0,
      "NumLogSegments": 1,
      "Size": 0,
      "UnderReplicatedPartitions": 0
    },
    "name": "partition",
    "tags": {
      "host": "CUD1-001560",
      "jolokia_agent_url": "http://localhost:7777/jolokia",
      "partition": "22",
      "topic": "qa-connect-offsets"
    },
    "timestamp": 1591124460
  }
'''

# function to normalize/clean loaded JSON

measurement = "partition"
tags = ["host","jolokia_agent_url","partition","topic"]
fields = ["LogEndOffset","LogStartOffset","NumLogSegments","Size","UnderReplicatedPartitions"]

def apply_schema(json, measurements, tags, fields):


def normalize(json):
    """ 
    Normalizes json into primitives to be more easily worked with
    :param obj: Any Python object
    :return:   normalized JSON
    """
  if is_json(json):

    json.loads(json)
    print(json)

# function to inspect anatomy of JSON
def inspect(json):
  pass



# function to take loaded JSON and parse into parts

# 



def is_json(obj: str) -> bool:
  """ 
  Checks if an object is a valid JSON string
  :param obj: Any Python object
  :return:    True if obj is a JSON object, else returns False
  """
  try:
    json_object = json.loads(obj)
  except ValueError as e:
    return False
  return True


def print_fields_and_vals(obj):
  if is_json(obj):
    orig = json.loads(obj)
    key_list = list(orig.keys())
    for key in key_list: 
      print(f"{key}: values: {orig[key]}") 
  else:
    return e

def one_level_keys(obj): 
  l1_keys = [] 
  for key in key_list:
    if type(orig[key]) in [int,bool,str,float]: 
      l1_keys.append(key) 
      key_list.remove(key) 
  return(l1_keys)

def get_level_keys(obj, lvl): 
  level_keys = {}
  for key in key_list:
    if type(orig[key]) in [int,bool,str,float]: 
      level_keys[lvl] = key
      key_list.remove(key) 
  return(level_keys)


# def get_level_keys(obj, lvl):
#   level_keys = {}     
#   level_key_name = f"{lvl}_level" 
#   level_keys[level_key_name] = [] 
#   for key in key_list: 
#     level_keys[level_key_name].append(key) 
#     rem_keys = key_list.remove(key)  
#   return(level_keys)

def get_level_keys(obj, lvl):
  key_list = list(obj.keys())
  print(f"key_list: {key_list}")
  level_keys = {}
  level_keys['one_level'] = []
  rem_keys = []

  for key in key_list:
    if type(orig[key]) in [int,bool,str,float]: 
      level_keys['one_level'].append(key)
    else:
      print(f"adding to rem_keys: {key}")
      rem_keys.append(key)
    level_keys['2_levels'] = []
    for key in rem_keys: 
      if type(orig[key]) == dict: 
        level_keys['2_levels'].append(key) 
        # rem_keys = key_list.remove(key)
  return(level_keys) 