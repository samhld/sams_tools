from influxdb import InfluxDBClient

host = "localhost"
port = 8086
db = "telegraf"

client = InfluxDBClient(host=host, port=port, database=db)

def get_measurements():
    m_dict = client.get_list_measurements()
    measurements = [m_dict[i]["name"] for i in range(0,len(m_dict))]  
    return measurements

class Measurement:
    def __init__(self):
        self.measurements = get_measurements()
        self.tags = get_tags(self.measurements)

def get_tags(measurements):
    _tags = []
    for i in measurements:
        # print(i)
        query = f'''SHOW TAG KEYS FROM "{i}"'''
        _tags.extend(client.query(query))
    # print(f"_tags: {_tags}")
    tags = []
    for i in _tags:
        for j in i:
            tags.append(j['tagKey']) 
    return tags

def measurement_tag_map(tags, measurements):
    tags = {}
    for i,elem in enumerate(measurements): 
        query = f'''SHOW TAG KEYS FROM "{elem}"''' 
        rs = client.query(query) 
        rs = rs.raw 
        tags.update({elem: [tag for tag in rs['series'][0]['values']]})
    print(tags)
    return tags

def tag_key_value_map():
    pass

# def get_tag_values(tags, measurements):
#     for 



'''
1) add caching because this is going to run the same series of meta queries over and over
2) add a client writer function that writes the tag values count per tag AND overall cardinality per measurement to Influx--
--this will provide monitoring for tag cardinality
'''
    



