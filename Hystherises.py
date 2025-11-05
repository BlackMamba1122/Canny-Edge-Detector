import numpy as np
from collections import deque


class Hysteresis:
    def apply(self, img, Th, Tl):
        h, w = img.shape
        strong, weak = 255, 100
        result = np.zeros_like(img, dtype=np.uint8)
        strong_x,strong_y=np.where(img>=Th)
        weak_x,weak_y=np.where((img>=Tl)&(img<Th))
        result[strong_x,strong_y]=strong
        result[weak_x,weak_y]=weak
        q=deque([(i,j) for i,j in zip(strong_x,strong_y)])
        while q:
            i,j=q.popleft()
            for di in (-1,0,1):
                for dj in (-1,0,1):
                    if di==0 and dj==0:
                        continue
                    ni,nj=i+di,j+dj
                    if 0<=ni<h and 0<=nj<w and result[ni,nj]==weak:
                        result[ni,nj]=strong
                        q.append((ni,nj))
        result[result!=strong]=0
        return result