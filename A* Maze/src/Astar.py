import numpy as np

class Astar:
    def __init__(self, size):
        self.size = size
        self.grid = np.array([[0 for i in range(self.size)] for i in range(self.size)])
        
    def solve(self):
        