import numpy as np

class Astar:
    def __init__(self, size):
        self.size = size
        self.grid = np.array([[0 for i in range(self.size)] for i in range(self.size)])
        self.H = np.array([[0 for i in range(self.size)] for i in range(self.size)])
        self.G = 10
        self.queue = []
        self.initialize()
        
    def solve(self):
        pass
    def initialize(self):
        # finalize grid
        # calculate H values based on finalized grid
        pass