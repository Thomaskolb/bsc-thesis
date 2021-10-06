# Thomas Kolb s1027332
# This program parses vtt files to something more useful

# Function that reads vtt file and returns a list of Caption objects
def read(path):
    with open(path, 'r') as vttfile:
        lines = vttfile.read().split('\n')
        times = [(l[:12], l[-12:]) for l in lines[2::3]]
        texts = lines[3::3]
        return [Caption(texts[i], times[i][0], times[i][1]) for i in range(min(len(times), len(texts)))]

# Caption object: text, start time, end time
class Caption:
    def __init__(self, text, start, end):
        self.text = text
        self.start = start
        self.end = end

    def __str__(self):
        return f"{self.text}, {self.start} -> {self.end}"
