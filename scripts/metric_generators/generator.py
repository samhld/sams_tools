from generator_funcs import *

bucket = "default"
org = "influxdata"
token = os.environ['INFLUX_TOKEN']
url = "http://localhost:9999"

client = InfluxDBClient(url=url, token=token, org=org, debug=True)
write_api = client.write_api(write_options=SYNCHRONOUS)

'''
-This will generate and write metrics to either Influx1.X or Influx2.X in any of the below formats:
--Influx, Graphite, Prometheus, JSON
-It will write over HTTP or UDP (no UDP for 2.X yet)
-It allows for determing number of batches, size of batches, and the sampling interval you want to test
'''

influx_metric_gen()