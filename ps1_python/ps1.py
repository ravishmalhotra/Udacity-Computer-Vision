import cv2
from hough_lines import hough_lines_acc
from hough_lines import hough_peaks
from hough_lines import hough_lines_draw

from pylab import *
#import numpy as np


img=imread('input/ps1-input0.png', 0)
#img=imread('input/ps1-input1.png', 0)
#img=cv2.imread('input/test.tiff', 0)
#img=imread('input/ps1-input0-noise.png', 0)


edges=cv2.Canny(img,200,210)
theta_range=arange(-90,90,1).tolist()

[acc,theta,rho]=hough_lines_acc(edges, theta_range)
   
figure(1)
imshow(edges,cmap='gray')
savefig('output/ps1-1-a-1.png')

figure(2)
imshow(acc,cmap='gray', extent=(theta[0],theta[-1],rho[-1],rho[0]))


xlabel('Theta')
ylabel('Rho')
xticks([-90,-45, 0, 45,89])
savefig('output/ps1-2-a-1.png')

peaks_indices=hough_peaks(acc,6)
print (peaks_indices)
xlim(theta[0], theta[-1])
ylim(rho[0], rho[-1])
[rho_plot, theta_plot]=list(zip(*peaks_indices))
theta_plot=[ x-90 for x in theta_plot]
plot(theta_plot,rho_plot,'or')
savefig('output/ps1-2-b-1.png')


hough_lines_draw(img,'ps-1-2-c-1.png',peaks_indices, rho, theta)


show()
