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

# Current state of this function returns a dict of the keys per level
# Next iteration of this function should associate values with each at each level
# ^^ that iteration could potentially be a separate function
def get_level_keys(obj, level_count=0, level_keys={}): 
     level_key = f"{level_count}_level" 
    
     if level_key not in level_keys: 
         level_keys[level_key] = [] 
        
     for key, val in obj.items(): 
         if isinstance(val, (int,float,complex,str,bool)): 
             level_keys[level_key].append(key) 
        
             if key not in level_keys[level_key]: 
                 level_keys[level_key].append(key) 
        
         else: 
             level_keys.update(get_level_keys(obj[key], level_count + 1, level_keys)) 
     return(level_keys) 