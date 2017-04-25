import cv2
from hough_lines import hough_lines_acc
from hough_lines import hough_peaks
from hough_lines import hough_lines_draw

from pylab import *

sigma=4
low_threshold=140
#low_threshold=170

figure(1)
#img=cv2.imread('input/ps1-input0-noise.png', 0)

img=cv2.imread('input/ps1-input1.png', 0)
#img=cv2.imread('input/test_img_2.jpg', 0)
#img=img[:,:,2]

print (img.shape)
imshow(img,cmap='gray')

#for sigma in range(1,10,2):
blur = cv2.GaussianBlur(img,(9,9),sigma) #Gaussian blur
figure(2)
imshow(blur, cmap='gray')
savefig('output/ps1-4-a-1.png')

edges=cv2.Canny(blur,low_threshold,low_threshold*1.2) #Canny edge detection of blurred image
figure(3)
imshow(edges, cmap='gray')
savefig('output/ps1-4-b-1.png')

theta_range=arange(-90,90,2).tolist() #Change the spacing of theta

[acc,theta,rho]=hough_lines_acc(edges, theta_range) #Calculate the accumulator
   

figure(5)
imshow(acc,cmap='gray', extent=(theta[0],theta[-1],rho[-1],rho[0]))


xlabel('Theta')
ylabel('Rho')
xticks([-90,-45, 0, 45,89])

#peaks_indices=hough_peaks(acc,int(25/(theta[1]-theta[0])))
peaks_indices=hough_peaks(acc,4)
print (peaks_indices)
xlim(theta[0], theta[-1])
ylim(rho[0], rho[-1])
[rho_plot, theta_plot]=list(zip(*peaks_indices))
theta_plot=[ (x*(theta[1]-theta[0]))-90 for x in theta_plot]
plot(theta_plot,rho_plot,'or')
savefig('output/ps1-4-c-1.png')


hough_lines_draw(img,'ps1-4-c-2.png',peaks_indices, rho, theta)


show()
