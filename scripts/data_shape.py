from statistics import median, mode, variance
import os
from collections import Counter
import math
import numpy as np
import seaborn as sns
import scipy.stats as stats

file = 'metrics.out'

text = open(file, 'r')
text = text.read()

num_lines = sum(1 for line in open(file))

tags = []
fields = []
measurements = []
for line in text.splitlines():
    if line.count(' ') == 2:
        line_tags, line_fields, time = line.split()
        line_tags = line_tags.split(',')
        measurement = line_tags.pop(0)
        measurements.append(measurement)
        line_fields = line_fields.split(',')
        tags.append(line_tags)
        fields.append(line_fields)

    elif line.count(' ') == 1:
        # counts fields if no tags in line (1 space in line indicates no tags)
        line_fields = line.split()

tags_dict = { f"Line{i+1} tags": len(elem) for i,elem in enumerate(tags)}
fields_dict = { f"Line{i+1} fields": len(elem) for i,elem in enumerate(fields)}

total_tags = sum(tags_dict.values())
total_fields = sum(fields_dict.values())

avg_fields_per_line = total_fields / num_lines
avg_tags_per_line = total_tags / num_lines

tags_mode = mode(tags_dict.values())
fields_mode = mode(fields_dict.values())

tags_median = median(tags_dict.values())
fields_median = median(fields_dict.values())

distinct_measurements = set(measurements)

tag_variance = variance(tags_dict.values())
tag_stddev = math.sqrt(tag_variance)

field_variance = variance(fields_dict.values())
field_stddev = math.sqrt(field_variance)

# print statements just to prove out the concept--will be moved into separate functions when I add complexity and better organization
print(avg_tags_per_line)
print(avg_fields_per_line)

print(f"Tags mode: {tags_mode}")
print(f"Fields mode: {fields_mode}")
print(f"Tags median: {tags_median}")
print(f"Fields median: {fields_median}")
print(f"Distinct measurements: {len(distinct_measurements)}")
print(f"Tag variance: {tag_variance}")
print(f"Tag stddev: {tag_stddev}")
print(f"Field variance: {field_variance}")
print(f"Field stddev: {field_stddev}")


'''
Add functions that allow for more exploration:
- # of occurrences of a mumber of fields/tags
- tag/field count bell-curve shape information
- determine how many congruent measurement, tag set combinations there are that can have fields merged (this would only really help for lines with one field)
'''
