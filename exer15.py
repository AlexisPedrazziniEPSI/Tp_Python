import statistics

class Statistics:
    def __init__(self, data):
        self.data = data

    def mean(self):
        return statistics.mean(self.data)

    def median(self):
        return statistics.median(self.data)

    def variance(self):
        return statistics.variance(self.data)

data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
stats = Statistics(data)

print("Mean:", stats.mean())        # Outputs: Mean: 5.5
print("Median:", stats.median())    # Outputs: Median: 5.5
print("Variance:", stats.variance()) # Outputs: Variance: 9.166666666666666