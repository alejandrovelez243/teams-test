


class Stats:
    ordered_array = None
    def __init__(self, orderd_array):
        """
        Get the ordered array.
        """
        print('This is the processed array: ', orderd_array)
        self.ordered_array = orderd_array

    def less(self, value: int):
        """
        Search the value on the array, and if it don't find it, it raise and error
        if it find it, return the values less of it
        """
        if value in self.ordered_array:
            index = self.ordered_array.index(value)
            return len(self.ordered_array[0:index])
        else:
            raise Exception("To works the value to search, should be inside of the array.")


    def greater(self, value: int):
        """
        Search the value on the array, and if it don't find it, it raise and error
        if it find it, return the values greater of it
        """
        if value in self.ordered_array:
            index = self.ordered_array.index(value)
            return len(self.ordered_array[index+1::])
        else:
            raise Exception("To works the value to search, should be inside of the array.")


    def between(self, value_from: int, value_to: int):
        """
        Search the values on the array, and if it don't find it, it raise and error
        if it find it, return the values between bot of then
        """
        if value_from in self.ordered_array and value_to in self.ordered_array:
            index_from = self.ordered_array.index(value_from)
            index_to = self.ordered_array.index(value_to)
            return len(self.ordered_array[index_from:index_to+1])
        else:
            raise Exception("To works the value to search, should be inside of the array.")