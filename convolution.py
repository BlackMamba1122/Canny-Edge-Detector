import numpy as np

class Convolution:
    def apply(self,image,kernel):
        image_height,image_width=image.shape
        kernel_height,kernel_width=kernel.shape
        ah , aw = kernel_height//2 , kernel_width//2
        padded = np.pad(image, ((ah, ah), (aw, aw)), mode="constant")
        output = np.zeros_like(image,dtype=float)
        # kflip = np.flipud(np.fliplr(kernel))
        for h in range(image_height):
            for w in range(image_width):
                region = padded[h:h+kernel_height,w:w+kernel_width]
                output[h,w] = np.sum(region*kernel)
        return output