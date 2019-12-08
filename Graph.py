import numpy
import sys

MAX_NUM = sys.maxsize


class Graph:
    cost_matrix = [int, int]

    def __init__(self, count=0):
        self.city_count = count

    def make_empty_matrix(self):
        self.cost_matrix = numpy.zeros((self.city_count, self.city_count), dtype=int)

    def fix_diagonal(self):
        for i in range(self.city_count):
            self.cost_matrix[i, i] = MAX_NUM
