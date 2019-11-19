from generator_funcs import *
import argparse
import pysnooper

bucket = "default"
org = "influxdata"
token = os.environ['INFLUX_TOKEN']
url = "http://localhost:9999"

parser = argparse.ArgumentParser()
parser.add_argument("--format", 
                            help="Can be 'influx', 'graphite', ('prometheus', 'json' coming soon)--> Default='influx'",
                            type=str,
                            default='influx')
parser.add_argument("--batch_size", 
                                help="Determines how many points are written per batch--> Default=5",
                                type=int, 
                                default=5)
parser.add_argument("--num_batches", 
                                help="Determines number of batches to write in a single run--> Default=1",
                                type=int, 
                                default=1)
parser.add_argument("--interval", 
                                help="Determines sampling rate in seconds--> Default=5",
                                type=int, 
                                default=5)
parser.add_argument("--use_case", 
                                help="Can be 'biz_intel', 'devops', ('financial','app' coming soon)--> Default='biz_intel'",
                                type=str, 
                                default='biz_intel')

args = parser.parse_args()


client = InfluxDBClient(url=url, token=token, org=org)
write_api = client.write_api(write_options=SYNCHRONOUS)

'''
-This will generate and write metrics to either Influx1.X or Influx2.X in any of the below formats:
--Influx, Graphite, Prometheus, JSON
-It will write over HTTP or UDP (no UDP for 2.X yet)
-It allows for determing number of batches, size of batches, and the sampling interval you want to test
'''
# with pysnooper.snoop():

if args.format == 'influx':
    points = influx_metric_gen(batch_size=args.batch_size, num_batches=args.num_batches, interval=args.interval, use_case=args.use_case)

    # print(args.num_batches)
    # print(args.interval)
    # print(args.batch_size)
    print(f"Points: {points}")
    #print(f"Points from client: {points}")
    write_api.write(bucket=bucket, org=org, record=points)


'''
The below `write_influx_metrics()` function is the start of an example of how I might use the client library Point class to write points.
    This requires generating them in the function with Point() in `generator_funcs.py`.  For now, I'm sticking with
    generating strings.  Generating with `Point()` looks like:
    ```
           for i in range(0,num_batches):
            points = []
            #local = time.localtime()
            for x in range(0,batch_size):
                points.append(Point("biz_intel").tag("region", random.choice(regions)) \
                                    .tag("app",random.choice(apps)) \
                                    .field("user_sessions", random.choice(user_sessions)) \
                                    .field("num_transactions",random.choice(num_xactions)) \
                                    .time(time.time_ns()))
                                    ```
```                                  
def write_influx_metrics():
    if args.format == 'influx':
        points = influx_metric_gen(batch_size=args.batch_size, num_batches=args.num_batches, interval=args.interval, use_case=args.use_case)

        for point in points:
            for field in point:
                point[field]._fields
```
'''