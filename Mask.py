import math
import numpy as np

class Mask:
    def __init__(self,sigma:float,T:float,scale:float):
        self.sigma = sigma
        self.T = T
        self.scale=scale

    def filter_size(self):
        sHalf = int(round(math.sqrt(- math.log(self.T)*2*(self.sigma**2))))  
        return sHalf
     
    def generate(self,filter_size: int):
        sHalf = self.filter_size()
        xs = np.arange(-sHalf, sHalf + 1)
        ys = np.arange(-sHalf, sHalf + 1)
        X, Y = np.meshgrid(xs, ys)
        G = np.exp(-(X**2 + Y**2)/(2*self.sigma**2))
        Gx = -(X/(self.sigma**2)) * G
        Gy = -(Y/(self.sigma**2)) * G
        return np.round(Gx*self.scale).astype(np.int32), np.round(Gy*self.scale).astype(np.int32)