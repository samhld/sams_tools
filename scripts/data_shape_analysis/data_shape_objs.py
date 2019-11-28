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

class Plotter:
    
    def __init__(self, text):
        self.measurements = []
        self.tags = []
        self.fields = []
        self.timestamps = []
        self._parse(text)

    def _parse(self,text):

        for line in text.splitlines():
            if line.count(' ') == 2:
                line_tags, line_fields, timestamp = line.split()
                line_tags = line_tags.split(',')
                measurement = line_tags.pop(0)
                self.measurements.append(measurement)
                line_fields = line_fields.split(',')
                self.tags.append(line_tags)
                self.fields.append(line_fields)

            elif line.count(' ') == 1:
                # counts fields if no tags in line (1 space in line indicates no tags)
                measurement = line.pop(0)
                line_fields, timestamp = line.split()
                line_fields = line_fields.split(',')

    def _average(self, arr):
        return len(arr) / self.num_lines
