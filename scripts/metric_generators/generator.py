from generator_funcs import *
import argparse
import socket

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
parser.add_argument("--protocol",
                                help="Can be 'http' or 'udp'--> Default='http'",
                                type=str,
                                default='http')

args = parser.parse_args()

bucket = "default"
org = "influxdata"
token = os.environ['INFLUX_TOKEN']
addr = "http://localhost"
port = 9999

url = addr+':'+str(port)
client = InfluxDBClient(url=url, token=token, org=org, debug=True)

'''
-This will generate and write metrics to either Influx1.X or Influx2.X in any of the below formats:
--Influx, Graphite, Prometheus, JSON
-It will write over HTTP or UDP (no UDP for 2.X yet)
-It allows for determing number of batches, size of batches, and the sampling interval you want to test
'''

def generate():

    write_api = client.write_api(write_options=SYNCHRONOUS)

    if args.format == 'influx':
        points = influx_metric_gen(batch_size=args.batch_size, num_batches=args.num_batches, interval=args.interval, use_case=args.use_case)

        if args.protocol == 'udp':
            #note: no udp support for 2.0 yet so, when using port 9999, don't use udp for now
            addr = '127.0.0.1'
            port = 8089
            server = (addr,port)
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(server)
            #s.sendto(line.encode('utf-8'), server)
            for point in points:
                s.send(point.encode('utf-8'))
            #sleep(cfg.settings['interval'])
            s.close()

        elif args.protocol == 'http':
            write_api.write(bucket=bucket, org=org, record=points)

    if args.format == 'graphite':
        points = graphite_metric_gen(batch_size=args.batch_size, num_batches=args.num_batches, interval=args.interval, use_case=args.use_case)

        if args.protocol == 'udp':
            #note: no udp support for 2.0 yet so, when using port 9999, don't use udp for now
            addr = '127.0.0.1'
            port = 8089
            server = (addr,port)
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(server)
            #s.sendto(line.encode('utf-8'), server)
            for point in points:
                s.send(point.encode('utf-8'))
            #sleep(cfg.settings['interval'])
            s.close()
        
        if args.protocol == 'http':
            write_api.write(bucket=bucket, org=org, record=points)

    if args.format == 'prometheus':
        points = prom_metric_gen(batch_size=args.batch_size, num_batches=args.num_batches, interval=args.interval, use_case=args.use_case)

        if args.protocol == 'udp':
            #note: no udp support for 2.0 yet so, when using port 9999, don't use udp for now
            addr = '127.0.0.1'
            port = 8089
            server = (addr,port)
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(server)
            #s.sendto(line.encode('utf-8'), server)
            for point in points:
                s.send(point.encode('utf-8'))
            #sleep(cfg.settings['interval'])
            s.close()

        elif args.protocol == 'http':
            write_api.write(bucket=bucket, org=org, record=points)
generate()

# elif args.format == 'graphite':


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