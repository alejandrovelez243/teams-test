from Stats import Stats
import sys

class DataCapture:
    values = []

    def add(self, value: int):
        """
        Add a value to the array values.
        """
        if value < 0:
            raise Exception("The value have to be a positive integer.")
        print("Added ", value)
        self.values.append(value)
        return True

    def build_stats(self):
        """
        Orders the array and then send it to a new class, called Stats.
        """
        print("Processing....")
        self.values.sort()
        stats = Stats(self.values)
        return stats