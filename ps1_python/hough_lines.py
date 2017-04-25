#import cv2
import numpy as np
from math import pi
from math import sqrt
from numpy import zeros
from math import cos
from math import sin
import matplotlib.pyplot as plt


#img=cv2.imread('input/ps1-input0.png', 0)
#img=cv2.imread('input/test.tiff', 0)

#edges=cv2.Canny(img,100,255)

def hough_lines_acc(edge_img, theta_range=[i for i in range(-90,90)]):

    x=len(edge_img)
    y=len(edge_img[0])
    max_rho=round(sqrt((x*x)+(y*y)))

    acc=zeros((max_rho,len(theta_range)));

    rho_range=[i for i in range(0,max_rho+1)]
            
    theta_interval=theta_range[1]-theta_range[0]
               

    #For every x and y pixel, if the thresholded value is 0
    # then, calculate all possible intercepts (rho values)
    # when slope changes 0 to 180.
    # If the value of rho is within the defined limits
    #then add 1 to the accumulator for the current pho and theta
    #Since there will be multiple intersections in the (rho,theta)
    # space for colinear points. the accumulator for that particular
    # value of rho, theta will get more votes, leading to identification
    # of straight lines
            
    for y in range(0,len(edge_img)):  ##Important. Y are all the rows
        for x in range(0,len(edge_img[0])): ##Important. X are the columns
            if edge_img[y,x]==255:
               for theta in theta_range:
                  rho=abs(round((y*sin(theta*pi/180))+(x*cos(theta*pi/180))))
                  acc[rho,int((theta+90)/theta_interval)]=acc[rho,int((theta+90)/theta_interval)]+1
                     
         

    acc=(acc/acc.max())*255 #Normalising the array to max output of acc to 255 

    acc=acc.astype('uint8')
    return (acc,theta_range,rho_range)

def hough_peaks(hough_acc,N):

    acc_1d=hough_acc.flatten() #Flatten the rho, theta matrix to find out 
    idx_1d=acc_1d.argsort()[::-1][:N] #the maximum values  

    [rho_idx, theta_idx]=np.unravel_index(idx_1d, hough_acc.shape) #Figure out 
    peaks=[peak for peak in zip(rho_idx,theta_idx)] #the actual index of the 2-d matrix where these maximum values exist

    return (peaks)

def hough_lines_draw(img,img_with_lines,peaks,rho,theta):
    
    [rho_index,theta_index]=list(zip(*peaks))
    rho_max=[rho[i] for i in rho_index]
    theta_max=[ (i*(theta[1]-theta[0]))-90 for i in theta_index]
    #a=len(img)+100
    #b=len(img[0])+100
    a=3000
    b=3000
    plt.figure(10)
    for i in range(0,len(peaks)):

        #x0=abs(rho_max[i]*cos(theta_max[i]*pi/180))
        x0=0;
        y0=(rho_max[i]/sin(theta_max[i]*pi/180))
     
        x1=int(x0+a*sin(theta_max[i]*pi/180))
        y1=int(y0-b*cos(theta_max[i]*pi/180))

        x2=int(x0-a*sin(theta_max[i]*pi/180))
        y2=int(y0+b*cos(theta_max[i]*pi/180))
        

        plt.plot([x1,x2],[y1,y2],'r-',linewidth=3)

    
    plt.imshow(img,cmap='gray')
    
    plt.savefig('output/'+img_with_lines)
    
    

    
    
