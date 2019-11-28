from statistics import median, mode, variance
import os
from collections import Counter
import math
import numpy as np
import seaborn as sns
import scipy.stats as stats
import re

file = 'metrics.out'

text = open(file, 'r')
text = text.read()

class Plotter:
    
    def __init__(self, text):
        #add error handling for not being passed text (or file if I go that route)
        self.measurements = []
        self.tags = [[]]
        self.fields = [[]] # in text with multiple lines, this is a list of lists
        self.timestamps = []
        self._parse(text)
        self.num_lines = sum(1 for line in open(file))
        self._tags_dict = { f"Line{i+1} tags": len(elem) for i,elem in enumerate(self.tags)}
        self._fields_dict = { f"Line{i+1} fields": len(elem) for i,elem in enumerate(self.fields)}

    def _parse(self,text):

        try:
            for line in text.splitlines():
                # if line.count(' ') == 2:
                line_tags, line_fields, timestamp = re.split('(?<!\\\\)\s', line)
                line_tags = line_tags.split(',')
                measurement = line_tags.pop(0)
                self.measurements.append(measurement)
                line_fields = line_fields.split(',')
                self.tags.append(line_tags)
                self.fields.append(line_fields)
                self.timestamps.append(timestamp)
        except ValueError:
            print(f"This line was disqualified due to formatting issues: {line}")

            # elif line.count(' ') < 2:
            #     other_lines = []
            #     other_lines.append(line)
        #     #     print(other_lines)
        #     else:
        #         other_lines = []
        #         other_lines.append(line)
        # print(other_lines[0])

            # elif line.count(' ') == 1:
            #     # counts fields if no tags in line (1 space in line indicates no tags)
            #     measurement = line.pop(0)
            #     line_fields, timestamp = line.split()
            #     line_fields = line_fields.split(',')


    def get_total_fields(self):
        _total_fields = sum(self._fields_dict.values())
        return _total_fields

    def get_total_tags(self):
        _total_tags = sum(self._tags_dict.values())
        return _total_tags

    def get_max_tags(self):
        _max_tag = max(self._tags_dict.values())
        return _max_tag

    def get_max_fields(self):
        _max_field = max(self._fields_dict.values())
        return _max_field

    def _average(self, _list):

        return len(_list) / self.num_lines

    def get_median():
        pass

    def describe(self):
        # To do: make this return dataframe
        print(f"Average tags per line: {avg_tags_per_line}")
        print(f"Average fields per line: {avg_fields_per_line}")
        print(f"Tags mode: {tags_mode}")
        print(f"Fields mode: {fields_mode}")
        print(f"Tags median: {tags_median}")
        print(f"Fields median: {fields_median}")
        print(f"Number of distinct measurements: {len(distinct_measurements)}")
        print(f"Tag variance: {tag_variance}")
        print(f"Tag stddev: {tag_stddev}")
        print(f"Field variance: {field_variance}")
        print(f"Field stddev: {field_stddev}")


