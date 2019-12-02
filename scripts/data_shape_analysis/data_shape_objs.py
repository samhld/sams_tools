from statistics import median, variance
import os
from collections import Counter
import math
import matplotlib.pyplot as plt
import re
import numpy as np
import pysnooper


file = 'metrics.out'

text = open(file, 'r')
text = text.read()

class Plotter:
    # @pysnooper.snoop()
    def __init__(self, text, flattened=False, no_timestamps=False):
        #add error handling for not being passed text (or file if I go that route)
        self.flattened = flattened # determines whether self.tags/self.fields will be a list of lists; defaults to False so it's easier to work with a line at a time.
        self.num_lines = len(text.splitlines())
        self.measurements = []
        self.tags = []
        self.fields = [] # in text with multiple lines, this is a list of lists
        self.timestamps = []
        self._parse(text)
        self._tags_dict = { f"Line{i+1} tags": len(elem) for i,elem in enumerate(self.tags)}
        self._fields_dict = { f"Line{i+1} fields": len(elem) for i,elem in enumerate(self.fields)}
        self.no_timestamps = no_timestamps
        # if text is str:
        #     self.num_lines = sum(1 for line in text.splitlines())
        # if text is list:
        #     self.num_lines = sum(1 for line in text)



    # @pysnooper.snoop()
    def _parse(self,text):
    
        if self.flattened:
            try:
                self.bad_lines = {}
                for i,line in enumerate(text.splitlines()):
                    if len(re.split('(?<!\\\\)\s', line)) == 3:
                        line_tags, line_fields, timestamp = re.split('(?<!\\\\)\s', line)
                        line_tags = line_tags.split(',')
                        measurement = line_tags.pop(0)
                        self.measurements.append(measurement)
                        line_fields = line_fields.split(',')
                        self.tags.extend(line_tags)
                        self.fields.extend(line_fields)
                        self.timestamps.extend(timestamp)

                    elif len(re.split('(?<!\\\\)\s', line)) == 2 and self.no_timestamps == True:
                        print(f"This line was disqualified due to formatting issues:\n{line}")
                        self.bad_lines[f'{i}'] = line
                        line_tags, line_fields = re.split('(?<!\\\\)\s', line)
                        line_tags = line_tags.split(',')
                        measurement = line_tags.pop(0)
                        self.measurements.append(measurement)
                        line_fields = line_fields.split(',')
                        self.tags.extend(line_tags)
                        self.fields.extend(line_fields)
                        
            except ValueError:
                print(f"This line was disqualified due to formatting issues:\n{line}")
        
        else:
            try:
                self.bad_lines = {}
                for i,line in enumerate(text.splitlines()):
                    if len(re.split('(?<!\\\\)\s', line)) == 3:
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
        self._total_fields = sum(self._fields_dict.values())
        return self._total_fields

    def total_tags(self):
        self._total_tags = sum(self._tags_dict.values())
        return self._total_tags

    def max_tags(self):
        # returns the tag count of the line with the most tags
        self._max_tags = max(self._tags_dict.values())
        return self._max_tags

    def max_fields(self):
        # returns the field count of the line with the most fields
        self._max_fields = max(self._fields_dict.values())
        return self._max_fields

    def min_tags(self):
        # returns the tag count of the line with the fewest tags
        self._min_tags = min(self._tags_dict.values())
        return self._min_tags

    def min_fields(self):
         # returns the field count of the line with the fewest fields
        self._min_fields = min(self._fields_dict.values())
        return self._min_fields       

    def mean_fields(self):
        # per line
        return self.total_fields() / self.num_lines

    def mean_tags(self):
        # per line
        return self.total_tags() / self.num_lines

    def median_tags(self):
        self._median_tags = median(self._tags_dict.values())
        return self._median_tags

    def median_fields(self):
        self._median_fields = median(self._fields_dict.values())
        return self._median_fields

    # def mode_tags(self):
    #     self._mode_tags = Counter(self._tags_dict.values()).most_common(1)[0][0]
    #     return self._mode_tags

    # def mode_fields(self):
    #     self._mode_fields = Counter(self._fields_dict.values()).most_common(1)[0][0]
    #     return self._mode_fields

    def mode_tags(self, value='mode'):
        if value == 'mode':
            # mode is the number of tags that occurred most often
            self._mode_tags = Counter(self._tags_dict.values()).most_common(1)[0][0]
            return self._mode_tags
        if value == 'occurrences':
            # number of times the mode occurred
            self._mode_tag_occurrences = Counter(self._tags_dict.values()).most_common(1)[0][1]
            return self._mode_tag_occurrences

    def mode_fields(self, value='mode'):
        if value == 'mode':
            # mode is the number of tags that occurred most often
            self._mode_fields = Counter(self._fields_dict.values()).most_common(1)[0][0]
            return self._mode_fields
        if value == 'occurrences':
            # number of times the mode occurred
            self._mode_field_occurrences = Counter(self._fields_dict.values()).most_common(1)[0][1]
            return self._mode_field_occurrences

    def distinct_measurements(self):
        self._distinct_measurements = len(set(self.measurements))
        return self._distinct_measurements

    def tag_variance(self):
        self._tag_variance = variance(self._tags_dict.values())
        return self._tag_variance

    def field_variance(self):
        self._field_variance = variance(self._fields_dict.values())
        return self._field_variance

    def tag_stddev(self):
        self.tag_variance()
        self._tag_stddev = math.sqrt(self._tag_variance)
        return self._tag_stddev

    def field_stddev(self):
        self.field_variance()
        self._field_stddev = math.sqrt(self._field_variance)
        return self._field_stddev

    def tag_counts(self):
        self._tag_counts = Counter(self._tags_dict.values())
        return dict(self._tag_counts)

    def field_counts(self):
        self._field_counts = Counter(self._fields_dict.values())
        return self._field_counts

    def tag_bar_plot(self):
        self.tag_counts()
        self._counts_dict = dict(self._tag_counts)
        plt.bar(range(len(self._counts_dict)), list(self._counts_dict.values()))
        plt.xticks(range(len(self._counts_dict)), list(self._counts_dict.keys()))
        plt.ylabel('Tag Counts')
        plt.title('Count of Occurrences of Tags Per Line')
        plt.show()

    def field_bar_plot(self):
        self.field_counts()
        self._counts_dict = dict(self._field_counts)
        plt.bar(range(len(self._counts_dict)), list(self._counts_dict.values()))
        plt.xticks(range(len(self._counts_dict)), list(self._counts_dict.keys()))
        plt.ylabel('Tag Counts')
        plt.title('Count of Occurrences of Tags Per Line')
        plt.show()
        

    def describe(self, t='dict'):
        # 't' is return type-->can be 'dict' or 'dataframe'
        description = {
            'Mean tags per line': self.mean_tags(),
            'Average fields per line': self.mean_fields(),
            'Tags mode': self.mode_tags(),
            'Fields mode': self.mode_fields(),
            'Tags median': self.median_tags(),
            'Fields median': self.median_fields(),
            'Count distinct measurements': self.distinct_measurements(),
            'Tag variance': self.tag_variance(),
            'Field variance': self.field_variance(),
            'Tag stddev': self.tag_stddev(),
            'Field stddev': self.field_stddev()
        }
        if  t == 'dict':
            return description
        elif t  == 'dataframe':
            try:
                import pandas as pd
                return pd.DataFrame(description, np.array([description.keys()]))
            except ModuleNotFoundError:
                print("Please install pandas module to use Dataframes")
