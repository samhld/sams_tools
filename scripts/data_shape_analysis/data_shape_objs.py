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
    
    def __init__(self, text, flattened=False):
        #add error handling for not being passed text (or file if I go that route)
        self.flattened = flattened # determines whether self.tags/self.fields will be a list of lists; defaults to False so it's easier to work with a line at a time.
        self.measurements = []
        self.tags = []
        self.fields = [] # in text with multiple lines, this is a list of lists
        self.timestamps = []
        self._parse(text)
        self.num_lines = sum(1 for line in open(file))
        self._tags_dict = { f"Line{i+1} tags": len(elem) for i,elem in enumerate(self.tags)}
        self._fields_dict = { f"Line{i+1} fields": len(elem) for i,elem in enumerate(self.fields)}

    def _parse(self,text):
    
        if self.flattened:
            try:
                for line in text.splitlines():
                    line_tags, line_fields, timestamp = re.split('(?<!\\\\)\s', line)
                    line_tags = line_tags.split(',')
                    measurement = line_tags.pop(0)
                    self.measurements.append(measurement)
                    line_fields = line_fields.split(',')
                    self.tags.extend(line_tags)
                    self.fields.extend(line_fields)
                    self.timestamps.extend(timestamp)
            except ValueError:
                print(f"This line was disqualified due to formatting issues:\n{line}")
        
        else:
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
                print(f"This line was disqualified due to formatting issues:\n{line}")


    def total_fields(self):
        _total_fields = sum(self._fields_dict.values())
        return _total_fields

    def total_tags(self):
        _total_tags = sum(self._tags_dict.values())
        return _total_tags

    def max_tags(self):
        # returns the tag count of the line with the most tags
        _max_tags = max(self._tags_dict.values())
        return _max_tags

    def max_fields(self):
        # returns the field count of the line with the most fields
        _max_fields = max(self._fields_dict.values())
        return _max_fields

    def min_tags(self):
        # returns the tag count of the line with the fewest tags
        _min_tags = min(self._tags_dict.values())
        return _min_tags

    def min_fields(self):
         # returns the field count of the line with the fewest fields
        _min_fields = min(self._fields_dict.values())
        return _min_fields       

    def mean_fields(self):
        # per line
        return self.total_fields() / self.num_lines

    def mean_tags(self):
        # per line
        return self.total_tags() / self.num_lines

    def median_tags(self):
        _median_tags = median(self._tags_dict.values())
        return _median_tags

    def median_fields(self):
        _median_fields = median(self._fields_dict.values())
        return _median_fields

    def mode_tags(self):
        _mode_tags = mode(self._tags_dict.values())
        return _mode_tags

    def mode_fields(self):
        _mode_fields = mode(self._fields_dict.values())
        return _mode_fields

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


