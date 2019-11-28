

class Plotter:
    
    def __init__(self, text):
        self.measurements = []
        self.tags = []
        self.fields = []
        self.time = []
        self._parse(text)

    def _parse(self,text):

        for line in text.splitlines():
            if line.count(' ') == 2:
                line_tags, line_fields, self.time = line.split()
                line_tags = line_tags.split(',')
                measurement = line_tags.pop(0)
                self.measurements.append(measurement)
                line_fields = line_fields.split(',')
                self.tags.append(line_tags)
                self.fields.append(line_fields)

            elif line.count(' ') == 1:
                # counts fields if no tags in line (1 space in line indicates no tags)
                line_fields = line.split()

    def _average(self, arr):
        return len(arr) / self.num_lines