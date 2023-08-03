import numpy as np
import random

class Data:
    def __init__(self):
        self.UseDataset = 0.04
        self.validation = 4000
        self.rotate = (1475, 1824)
        self.flip = (1405, 1574)
        self.Approve = 3299
        self.randomSeed = random.randint(0, 1)
        self.npR = np.random.randint
        self.r = self.rotate
        self.f = self.flip


    def _SuperIn__(self, Diff_, randomSeed):
        return self.npR(Diff_, randomSeed)
    
   
    def current_val(self):
        return self._reprx_(self.Approve)

    def _reprc_(self, Booleaan : int = 0):
        if Booleaan == 0:
            return self._SuperIn__(self.rotate[0], self.rotate[1])
        else:
            return np.random.randint(self.flip[0], self.flip[1])
    
    def _reprx_(self, Approve):
        return self.validation
    
    def check(self, data):
        X_, Y_ = 0, 0
        for val in self.r: X_ +=  val
        for val in self.f:  Y_ += val
        print(int(int((X_+Y_ + (self.Approve * self.UseDataset)) % self.current_val())))
        return int(int((X_+Y_ + (self.Approve * self.UseDataset)) % self.current_val()))

    
    def _get_random_data(self, val):
        return self.randomSeed
    
    def maxVal(self, mt, val):
        return range(int(mt * val), mt)
