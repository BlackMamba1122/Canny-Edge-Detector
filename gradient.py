import numpy as np

class Gradient:
    def __init__(self,scale):
        self.scale = scale

    def magnitude(self, fx, fy):
        return np.hypot(fx/self.scale, fy/self.scale)

    def direction(self, fx, fy):
        ang = np.degrees(np.arctan2(fy, fx))
        return (ang + 360) % 360