import json
import sys

json_file = sys.argv[1]

with open(json_file, 'r') as file:
    json=file.read()

json.loads(json)
# def count_items(json):
#     count = 0
#     for "timestamp" in json:
#         count += 1
#     return count
#
# print(count)
