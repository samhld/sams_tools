from influxdb_client import InfluxDBClient, Point, WriteOptions
from influxdb_client.client.write_api import SYNCHRONOUS
import os
import random
import pysnooper
from time import sleep
import time

# bucket = "sam+20191104's Bucket"
# org = "sam+20191104@influxdata.com"
# token = os.environ['INFLUX_TOKEN']

bucket = "default"
org = "influxdata"
token = os.environ['INFLUX_TOKEN']

url = "http://localhost:9999"

regions = ['us-west-1','us-west2','us-east-1','us-east-2','ap-southeast-2','eu-west-1']
apps = ['checkout','shoes','payment','frontend',]
user_sessions = range(5,2000,45)
num_xactions = range(0,11)
# host_prefixes = ['a','b','c','d','e','f']
# host_suffixes = range(0,5)

# host = random.choice(host_prefixes) + str(random.choice(host_suffixes))

client = InfluxDBClient(url=url, token=token, org=org, debug=True)


# with pysnooper.snoop():
write_api = client.write_api(write_options=SYNCHRONOUS)


for i in range(0,100):
    points = []
    local = time.localtime()
    for x in range(0,5):
        points.append(Point("biz_intel").tag("region", random.choice(regions)) \
                            .tag("app",random.choice(apps)) \
                            # .tag("host",host) \
                            .field("user_sessions", random.choice(user_sessions)) \
                            .field("num_transactions",random.choice(num_xactions)) \
                            .time(int(time.mktime(local))))
        write_api.write(bucket=bucket, org=org, record=points)
        # print(points[0].time())
        sleep(5)

p_alt = f"biz_intel,region={random.choice(regions)},app={random.choice(apps)},host={host} user_sessions={random.choice(user_sessions)},num_transactions={random.choice(num_xactions)} "


point = Point("biz_intel").tag("region", random.choice(regions)) \
                            .tag("app",random.choice(apps)) \
                            .tag("host",host) \
                            .field("user_sessions", random.choice(user_sessions)) \
                            .field("num_transactions",random.choice(num_xactions)) \

print(point.time())
# client.__del__()