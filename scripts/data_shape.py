
import statistics
import os

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

print(avg_tags_per_line)
print(avg_fields_per_line)


'''Add mean, median, mode functionality here'''

