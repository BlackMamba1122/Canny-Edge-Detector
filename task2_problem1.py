import numpy as np
import matplotlib.pyplot as plt

def gaussian(x, y, sigma):
    return np.exp(-(x**2 + y**2) / (2 * sigma**2))

def gaussian_derivatives(sigma=1.0, size=5):
    ax = np.linspace(-size, size, 100)  # create a 1-D array of size 100 from -5 to 5 with (5-(-5))/100-1  difference at each step
    X, Y = np.meshgrid(ax, ax) # create a grid of 100*100 array of X and Y direction respectively   
    G = gaussian(X, Y, sigma) # takes gausian on x y array
    Gx = -X / (sigma**2) * G # first derivative of X
    Gy = -Y / (sigma**2) * G # first derivative of Y
    Gxx = (X**2 - sigma**2) / (sigma**4) * G # second derivative of X
    Gyy = (Y**2 - sigma**2) / (sigma**4) * G # second derivative of Y
    return X, Y, G, Gx, Gy, Gxx, Gyy

X, Y, G, Gx, Gy, Gxx, Gyy = gaussian_derivatives(sigma=1.0, size=5)
fig = plt.figure(figsize=(12, 8))

ax1 = fig.add_subplot(231, projection='3d')
ax1.plot_surface(X, Y, G, cmap='plasma')
ax1.set_title("Gaussian G(x,y)")

ax2 = fig.add_subplot(232, projection='3d')
ax2.plot_surface(X, Y, Gx, cmap='plasma')
ax2.set_title("First Derivative of Gx")

ax3 = fig.add_subplot(233, projection='3d')
ax3.plot_surface(X, Y, Gy, cmap='plasma')
ax3.set_title("First Derivative of Gy")

ax4 = fig.add_subplot(234, projection='3d')
ax4.plot_surface(X, Y, Gxx, cmap='plasma')
ax4.set_title("Second Derivative of Gx")

ax5 = fig.add_subplot(235, projection='3d')
ax5.plot_surface(X, Y, Gyy, cmap='plasma')
ax5.set_title("Second Derivative of Gy")

plt.tight_layout()
plt.savefig("Problem 1.pdf", format="pdf")
plt.show()
 