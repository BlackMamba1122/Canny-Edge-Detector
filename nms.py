import numpy as np

class NonMaxSuppression:

    def quantize(self, ang):
        q = np.zeros_like(ang, dtype=np.uint8)
        quadrant0 = ((ang>=0)&(ang<=22.5))|((ang>=157.5)&(ang<=202.5))|((ang>=337.5)&(ang<=360))
        quadrant1 = ((ang>22.5)&(ang<=67.5))|((ang>202.5)&(ang<=247.5))
        quadrant2 = ((ang>67.5)&(ang<=112.5))|((ang>247.5)&(ang<=292.5))
        quadrant3 = ((ang>112.5)&(ang<=157.5))|((ang>292.5)&(ang<=337.5))
        q[quadrant0]=0; q[quadrant1]=1; q[quadrant2]=2; q[quadrant3]=3
        return q

    def applynms(self, magnitude, quantize):
        x, y = magnitude.shape
        output = np.zeros_like(magnitude)
        for h in range(1,x-1):
            for w in range(1,y-1):
                mag, quadrant = magnitude[h,w], quantize[h,w]
                if quadrant==0: n1,n2=magnitude[h,w-1],magnitude[h,w+1]
                elif quadrant==1: n1,n2=magnitude[h-1,w+1],magnitude[h+1,w-1]
                elif quadrant==2: n1,n2=magnitude[h-1,w],magnitude[h+1,w]
                else: n1,n2=magnitude[h-1,w-1],magnitude[h+1,w+1]
                output[h,w]=mag if mag>=n1 and mag>=n2 else 0
        return output
    