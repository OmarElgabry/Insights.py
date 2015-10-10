'''

@author: Omar
'''

class Stats():
    """
    Stats class for performing some simple statistics on a list of values. 
    """
    
    def __init__(self):
        """
        Constructor method.
        """
        pass
    
    @staticmethod
    def average(lst):
        """
        Computes the average.
        """
        return __class__.sum(lst) / __class__.length(lst)
    
    @staticmethod
    def meanDeviation(lst):
        """
        Computes the mean deviation.
        Mean Deviation is average of distance of each value from that mean(average).
        """
        average  = __class__.average(lst)
        mean_deviation = 0
        for v in lst:
            mean_deviation += abs(average - v)
        return mean_deviation / __class__.length(lst)
    
    @staticmethod
    def count(lst, value):
        """
        Counts the occurrence of a value in a list of values.
        """
        return lst.count(value)
    
    @staticmethod
    def variance(lst):
        """
        Computes the variance.
        Variance is useful to see how the list of values varied against the average.
        """
        average  = __class__.average(lst)
        variance = 0
        for v in lst:
            variance += ((average - v) ** 2)
        return variance / __class__.length(lst)
    
    @staticmethod
    def standardDeviation(lst):
        """
        Computes the standard deviation.
        Standard Deviation is useful to give an idea about range of normal values(i.e. location of most of values). 
        """
        return __class__.variance(lst) ** 0.5
    
    @staticmethod
    def median(lst):
        """
        Computes the median.
        Median is the middle value in a sorted list of values.
        """
        lst    = __class__.sort(lst)
        length = __class__.length(lst)
        mid    = int(length / 2)
        
        if length % 2 == 0:
            return (lst[mid] + lst[mid - 1]) / 2
        return lst[mid]
        
    @staticmethod
    def max(lst):
        """
        Returns the max value.
        """
        return max(lst)
    
    @staticmethod
    def min(lst):
        """
        Returns the min value.
        """
        return min(lst)
    
    @staticmethod
    def range(lst):
        """
        Returns the difference between max and min values.
        """
        return __class__.max(lst) - __class__.min(lst)
    
    @staticmethod
    def sum(lst):
        """
        Returns summation of all values in a list.
        """
        return sum(lst)
    
    @staticmethod
    def length(lst):
        """
        Returns the length of list.
        """
        return len(lst)
    
    @staticmethod
    def sort(lst):
        """
        Sorts the list.
        """
        return sorted(lst)
    
