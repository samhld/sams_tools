from influxdb_client import InfluxDBClient, Point, WriteOptions
from influxdb_client.client.write_api import SYNCHRONOUS
import os
import random
from time import sleep
import time
import pysnooper

bucket = "default"
org = "influxdata"
token = os.environ['INFLUX_TOKEN']

url = "http://localhost:9999"

regions = ['us-west-1','us-west2','us-east-1','us-east-2','ap-southeast-2','eu-west-1']
apps = ['checkout','shoes','payment','frontend',]
user_sessions = range(5,2000,45)
num_xactions = range(0,11)

client = InfluxDBClient(url=url, token=token, org=org)

write_api = client.write_api(write_options=SYNCHRONOUS)

#with pysnooper.snoop():
for i in range(0,100):
    points = []
    #local = time.localtime()
    for x in range(0,5):
        points.append(f"biz_intel.{random.choice(regions)}.{random.choice(apps)}.user_sessions {random.choice(user_sessions)} {time.time_ns()}")
        points.append(f"biz_intel.{random.choice(regions)}.{random.choice(apps)}.num_transactions {random.choice(num_xactions)} {time.time_ns()}")
    print(points)
    write_api.write(bucket=bucket, org=org, record=points)
    sleep(5)
