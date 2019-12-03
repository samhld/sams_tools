from influxdb import InfluxDBClient

host = "localhost"
port = 8086
db = "telegraf"

client = InfluxDBClient(host=host, port=port, database=db)

measurements = client.get_list_measurements()

m_list = [measurements[i]["name"] for i in range(0,len(measurements))]  

def get_tags(m_list, response='keys'):
    _tags = []
    for i in range(len(m_list)):
        query = f'''SHOW TAG KEYS FROM "{m_list[i]}"'''
        _tags.extend(client.query(query))
    tags = []
    for i in _tags:
        for j in i:
            tags.append(j['tagKey']) 
    # print(tags)
    # print(len(tags))

get_tags(m_list)

'''
1) add caching because this is going to run the same series of meta queries over and over
2) add a client writer function that writes the tag values count per tag AND overall cardinality per measurement to Influx--
--this will provide monitoring for tag cardinality
'''
    

