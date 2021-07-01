class Stats:
    def __init__(self, values):
        self.cumulative = [0] * len(values)
        self.cumulative[0] = values[0]
        for index, c in enumerate(values[1:], 1):
            self.cumulative[index] = self.cumulative[index-1] + c
        self.total = sum(values)


    def less(self, value):
        return self.cumulative[value - 1] if value > 0 else 0

    def greater(self, value):
        return self.total - self.less(value + 1)

    def between(self, value_from, value_to):
        return self.less(value_to + 1) - self.less(value_from - 1)



class DataCapture:
    def __init__(self, n=1000):
        self.values = [0] * n


    def add(self, value):
        self.values[value] += 1

    def build_stats(self):
        return Stats(self.values)



capture = DataCapture()

capture.add(3)
capture.add(9)
capture.add(3)
capture.add(6)
capture.add(4)


stats = capture.build_stats()

print(stats.less(4))

print(stats.between(3, 6))

print(stats.greater(4))