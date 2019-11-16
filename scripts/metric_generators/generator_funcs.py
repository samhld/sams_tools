from influxdb_client import InfluxDBClient, Point, WriteOptions
from influxdb_client.client.write_api import SYNCHRONOUS
import random
from time import sleep
import time
import os
import pysnooper

bucket = "default"
org = "influxdata"
token = os.environ['INFLUX_TOKEN']

regions = ['us-west-1','us-west2','us-east-1','us-east-2','ap-southeast-2','eu-west-1']
apps = ['checkout','shoes','payment','frontend',]
user_sessions = range(5,2000,45)
num_xactions = range(0,11)

'''
All metric generators will take a parameters 'batch_size', 'num_batches',
'interval', 'use_case', and 'write_once' to determine how and what to write to Influx.

Params:
-batch_size: how many lines/points are written in a single batch
-num_batches: how many batches will be written in a run of this function
-interval: sample rate; how often a request is made (in seconds)
-use_case: what metrics to write {biz_metrics, devops, appmetrics (coming), logs (coming), stocks (coming)}
-write_once: if set to True, generator will write one batch only
''' 


def influx_metric_gen(batch_size=5, num_batches=100, interval=5, use_case='biz_intel', write_once=False): 

    url = "http://localhost:9999"
    client = InfluxDBClient(url=url, token=token, org=org, debug=True)
    write_api = client.write_api(write_options=SYNCHRONOUS)

    if use_case == 'biz_intel':
        # write biz_intel metrics
        apps = ['checkout','shoes','payment','frontend']
        user_sessions = range(5,2000,45)
        num_xactions = range(0,11)
        
        if write_once:
            # writes one batch
            points = []
            for x in range(0,batch_size):
                points.append(Point("biz_intel").tag("region", random.choice(regions)) \
                                    .tag("app",random.choice(apps)) \
                                    .field("user_sessions", random.choice(user_sessions)) \
                                    .field("num_transactions",random.choice(num_xactions)) \
                                    .time(time.time_ns()))
            write_api.write(bucket=bucket, org=org, record=points)
        else:
            # generates num_batches of batches   
            for i in range(0,num_batches):
                points = []
                #local = time.localtime()
                for x in range(0,batch_size):
                    points.append(Point("biz_intel").tag("region", random.choice(regions)) \
                                        .tag("app",random.choice(apps)) \
                                        .field("user_sessions", random.choice(user_sessions)) \
                                        .field("num_transactions",random.choice(num_xactions)) \
                                        .time(time.time_ns()))
                write_api.write(bucket=bucket, org=org, record=points)
                sleep(interval)


    elif use_case == 'devops':
        # write devops metrics
        host_prefixes = ['a','b','c','d']
        host_suffixes = range(0,5)
        host = random.choice(host_prefixes) + str(random.choice(host_suffixes))
    



def graphite_metric_gen(batch_size=5, num_batches=100, interval=5, use_case='biz_intel', write_once=False): 

    if use_case == 'biz_intel':

        apps = ['checkout','shoes','payment','frontend']
        user_sessions = range(5,2000,45)
        num_xactions = range(0,11)       

        if write_once:
            for x in range(0,batch_size):
                points.append(f"biz_intel.{random.choice(regions)}.{random.choice(apps)}.user_sessions {random.choice(user_sessions)} {time.time_ns()}")
                points.append(f"biz_intel.{random.choice(regions)}.{random.choice(apps)}.num_transactions {random.choice(num_xactions)} {time.time_ns()}")
            write_api.write(bucket=bucket, org=org, record=points)
        else:       
            for i in range(0,num_batches):
                points = []
                #local = time.localtime()
                for x in range(0,batch_size):
                    points.append(f"biz_intel.{random.choice(regions)}.{random.choice(apps)}.user_sessions {random.choice(user_sessions)} {time.time_ns()}")
                    points.append(f"biz_intel.{random.choice(regions)}.{random.choice(apps)}.num_transactions {random.choice(num_xactions)} {time.time_ns()}")
                write_api.write(bucket=bucket, org=org, record=points)
                sleep(interval)

