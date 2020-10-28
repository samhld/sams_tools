# from influxdb_client import InfluxDBClient, Point, WriteOptions
# from influxdb_client.client.write_api import SYNCHRONOUS
import random
from time import sleep
import time
import os
from enum import Enum
import string

bucket = "default"
org = "influxdata"
token = os.environ['INFLUX_TOKEN']

regions = ['us-west-1','us-west2','us-east-1','us-east-2','ap-southeast-2','eu-west-1']
apps = ['checkout','shoes','payment','frontend',]
user_sessions = range(5,2000,45)
num_xactions = range(0,11)

'''
All metric generators will take a parameters 'batch_size', 'num_batches',
'interval', and 'use_case' to determine how and what to write to Influx.

Params:
-batch_size: how many lines/points are written in a single batch
-num_batches: how many batches will be written in a run of this function
-interval: sample rate; how often a request is made (in seconds)
-use_case: what metrics to write {biz_metrics, devops, appmetrics (coming), logs (coming), stocks (coming)}
-write_once: if set to True, generator will write one batch only
''' 

url = "http://localhost:9999"
# client = InfluxDBClient(url=url, token=token, org=org, debug=True)
# write_api = client.write_api(write_options=SYNCHRONOUS)


def generate_point():
    # create an instance of LineLP
    pass

def generate_batch():
    # Function should return a list of instances of LineLP shaped according to how they're initialized
    pass

def write_batch(num_batches=1, batch_size=100):
    # Write batch after generating with generate_batch()
    pass

class LineLP:
    '''
    Class instances are a single line of Line Protocol shaped according to the following parameters:
        - number of int Fields (int_fields)        --> int
        - number of string Fields (str_fields)  --> int
        - number of float Fields (float_fields)    --> int
        - number of Tags (num_tags)                --> int
        - approx field key size (field_key_size)   --> int
        - approx tag key size (tag_key_size)       --> int
        - measurement size                         --> int
        - timestamp precision (precision)          --> str

    '''
    def __init__(self, measurement="measurement", 
                        int_fields=1, 
                        str_fields=0, 
                        float_fields=0,    
                        num_tags=2,    
                        field_key_size=10, 
                        tag_key_size=10,    
                        tag_value_size=10, 
                        int_value_size=4, 
                        float_value_size=4, 
                        str_value_size=10, 
                        measurement_size=10):
        self.int_fields = int_fields
        self.str_fields = str_fields
        self.float_fields = float_fields
        self.num_tags = num_tags
        self.field_key_size = field_key_size
        self.tag_key_size = tag_key_size
        self.field_value_size = field_value_size
        self.tag_value_size = tag_value_size
        self.measurement_size = measurement_size
        self.measurement = measurement
        # Create structures necessary for creating line
        self.tag_keys = [_gen_string(range(tag_key_size) for tag_key in range(num_tags)]


        point = f"{measurement}""

        return(point)

    # Generate random string of length equal to `num`
    def _gen_string(num):
        letters = string.ascii_lowercase
        result_str = ''.join(random.choice(letters) for i in range(num))
        return(result_str)

# class webAppMetricGenerator:
    
#     def __init__(self, batch_size=5, num_batches=1, interval=5, apps=['checkout','shoes','payment','frontend'], user_sessions=range(5,2000,45), num_xactions=range(0,11)):
#         self.batch_size = batch_size
#         self.num_batches = num_batches
#         self.interval = interval
#         self.apps = apps
#         self.user_sessions = user_sessions
#         self.num_xactions = num_xactions
    
#     def influx_metric_gen(self.batch_size, self.num_batches, self.interval): 

#         for i in range(0,num_batches):
#             points = []
#             #local = time.localtime()
#             for x in range(0,batch_size):
#                 points.append(f"biz_intel,region={random.choice(regions)},app={random.choice(apps)} user_sessions={random.choice(user_sessions)}i,num_transactions={random.choice(num_xactions)}i {time.time_ns()}")
#                 # points.append(Point("biz_intel").tag("region", random.choice(regions)) \
#                 #                     .tag("app",random.choice(apps)) \
#                 #                     .field("user_sessions", random.choice(user_sessions)) \
#                 #                     .field("num_transactions",random.choice(num_xactions)) \
#                 #                     .time(time.time_ns()))
#             sleep(interval)
        
#         return(points)


#     def graphite_metric_gen(self.batch_size, self.num_batches, self.interval)
    
#         for i in range(0,num_batches):
#             points = []
#             for x in range(0,batch_size):
#                 points.append(f"biz_intel.{random.choice(regions)}.{random.choice(apps)}.user_sessions value={random.choice(user_sessions)} {time.time_ns()}")
#                 points.append(f"biz_intel.{random.choice(regions)}.{random.choice(apps)}.num_transactions value={random.choice(num_xactions)} {time.time_ns()}")
#             sleep(interval)
        
#         return(points)

#     def prom_metric_gen(self.batch_size, self.num_batches, self.interval):

#         host_prefixes = ['a','b','c','d']
#         host_suffixes = range(0,5)
#         host = random.choice(host_prefixes) + str(random.choice(host_suffixes))

#         for i in range(0,num_batches):
#             points = []
#             for x in range(0,batch_size):
#                 points.append(f"user_sessions{{region={region}, host={host}, app={app}}}")
#                 points.append(f"user_sessions{{region={region}, host={host}, app={app}}}")
#             sleep(interval)
        
#         return(points)


# class devopsMetricGenerator:

#     def __init__(self, batch_size=5, num_batches=1, interval=5):
#         self.batch_size = batch_size
#         self.num_batches = num_batches
#         self.interval = interval
        
        
#         host_prefixes = ['a','b','c','d']
#         host_suffixes = range(0,5)
#         host = random.choice(host_prefixes) + str(random.choice(host_suffixes))

#     def prom_metric_gen(self.batch_size, self.num_batches, self.interval):

#         apps = ['checkout','shoes','payment','frontend']
#         user_sessions = range(5,2000,45)
#         num_xactions = range(0,11)       

#         for i in range(0,num_batches):
#             points = []
#             #local = time.localtime()
#             for x in range(0,batch_size):
#                 # Prometheus doesn't support writing multiple Fields (metrics) per line, so a "batch" will consist of more than 1 line to write all Fields in the batch
#                 app = random.choice(apps)
#                 region = random.choice(regions)
#                 points.append(f"user_sessions{{region={region},app={app}}} value={random.choice(user_sessions)} {time.time_ns()}")
#                 points.append(f"num_xactions{{region={region},app={app}}} value={random.choice(num_xactions)} {time.time_ns()}")
#             sleep(interval)
        
#         return(points)