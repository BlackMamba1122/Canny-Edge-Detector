# bscs23169
# Muhammad Ahmad
# Assignment 2

from Mask import Mask
from convolution import Convolution
from Image import ImageOperations
import os
from gradient import Gradient
from nms import NonMaxSuppression
import numpy as np
from Hystherises import Hysteresis
import argparse

def main(args):
    output_folder=args.output_folder
    name = args.save_name
    scale=255.0
    sigmas = [0.5,1,2]
    img = ImageOperations(args.input_file)
    image = img.load_image()
    for sigma in sigmas:

        mask=Mask(sigma,0.3,scale)
        filter_size=mask.filter_size()
        Gx,GY=mask.generate(filter_size)

        conv =Convolution()
        fx=conv.apply(image,Gx)
        fy=conv.apply(image,GY)
        img.save_image(np.abs(fx),os.path.join(output_folder, f"{name}_fx_{sigma}.png"))
        img.save_image(np.abs(fy),os.path.join(output_folder, f"{name}_fy_{sigma}.png"))

        gradient = Gradient(scale)
        magnitude = gradient.magnitude(fx,fy)
        img.save_image(magnitude,os.path.join(output_folder, f"{name}_magnitude_{sigma}.png"))
        
        direction= gradient.direction(fx,fy)

        nms = NonMaxSuppression()
        quantize = nms.quantize(direction)
        q_vis = (quantize.astype(np.float32) * 85)
        img.save_image(q_vis,os.path.join(output_folder, f"{name}_quantize_{sigma}.png"))
        nmss = nms.applynms(magnitude, quantize)
        img.save_image(nmss,os.path.join(output_folder, f"{name}_nms_{sigma}.png"))

        mmax = nmss.max()
        hys = Hysteresis()
        thres1, thres2 = 0.2, 0.6
        thresholds = [(thres1, thres1/2), (thres2, thres2/2)]

        for Th_ratio, Tl_ratio in thresholds:
            Th, Tl = Th_ratio * mmax, Tl_ratio * mmax
            edges = hys.apply(nmss, Th, Tl)
            img.save_image(edges,os.path.join(output_folder, f"{name}_canny_{sigma}_T{int(Th_ratio*100)}_{int(Tl_ratio*100)}.png"))

        
def parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input_file', default='Input/circle.jpg')
    parser.add_argument('--output_folder', default='Output/circle')
    parser.add_argument('--save_name', default='circle')
    args = parser.parse_args()
    return args

if __name__ == "__main__":
    args=parser()
    main(args)