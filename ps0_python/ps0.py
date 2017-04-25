from PIL import Image
from pylab import *


im=array(Image.open('output/ps0-1-a-1.tiff'))

#Plot original image
figure(1) 
imshow(im)
axis('off')
#print (im.shape, im.dtype)


#2c Plot image from the red 
figure(2)
axis('off')
im_red=im[:,:,0]
imshow(im_red, cmap='gray')
#print (im_red.shape, im_red.dtype)
savefig('output/ps0-2-c-1.png') #Saving greyscale image from the red channel

#2b Plot image from the red 
figure(3)
axis('off')
im_green=im[:,:,1] #Plot image
#print (im_green.shape, im_green.dtype)
imshow(im_green, cmap='gray')
savefig('output/ps0-2-b-1.png') #Saving greyscale image from the green channel

#2a Swaping blue and red channels
im_blue=im[:,:,2]
im_swap=array(im[:,:,:])

im_swap[:,:,0]=im_blue[:,:]
im_swap[:,:,2]=im_red[:,:]
imsave('output/ps0-2-a-1.png',im_swap)



#3a Replacement of 100x100 pixels
im_green_replace=array(im_green[:,:])

start=int(len(im_green[:])/2-50)
end=int(len(im_green[:])/2+50)
#print (start)
#print (end) 
rows=list(range(start,end))
#print (rows)
cols=list(rows)

im_green_replace[rows,cols]=im_blue[rows,cols]


figure(4)
axis('off')
imshow(im_green_replace,cmap='gray')                                                                                                  
savefig('output/ps0-3-a-1.png')

#4a Min and Max
print("Green channel Min:", im_green.min())
print ("Green channel Max:", im_green.max())

#4b 
(im[:,:,1].std())

im_modified=array(im)
for x in range(0,3):
   im_modified[:,:,x]=((im[:,:,x])-(im[:,:,x].mean())*10)+im[:,:,:].mean()

figure(5)
axis('off')
imshow(im_modified)
savefig('output/ps0-4-b-1.png')

#4c Shift img_green by 2 pixels
im_green_extended=uint8(zeros((len(im_green[:]),len(im_green[:])+2)))
#print(im_green_extended.shape,im_green_extended.dtype)
im_green_extended[:,:-2]=im_green

im_green_extended=delete(im_green_extended,[0,1],axis=1)
#print(im_green_extended.shape,im_green_extended.dtype)           
figure(6)
axis('off')
imshow(im_green_extended,cmap='gray')                        
savefig('output/ps0-4-c-1.png')

####### 4d. Get img difference #####
#Changing the data type of arrays to account for wrapping in unint8
# which after subtraction will give wrong answers 
im_green_extended=im_green_extended.astype(int16)
im_green=im_green.astype(int16)

#print (im_green_extended.dtype)

#Initialising two diff arrays. One for im_green-im_green_extended
#2nd for im_green_extended-im_green

img_green_diff_1=int16(zeros((len(im_green[:]),len(im_green[:]))))
img_green_diff_2=array(img_green_diff_1)

img_green_diff_1=int16(im_green-im_green_extended)
img_green_diff_2=int16(im_green_extended-im_green)


#print(img_green_diff_2.min())

#Clipping the value of each array element to 0 to 255
clip(img_green_diff_1,0,255,out=img_green_diff_1)
clip(img_green_diff_2,0,255,out=img_green_diff_2)

#print(img_green_diff_2.min())

#Adding the two diff arrays to get a true image difference 
im_green_diff=img_green_diff_1+img_green_diff_2
#print(im_green_diff.min(), im_green_diff.max())

figure(7)
axis('off')
imshow(im_green_diff,cmap='gray')                        
savefig('output/ps0-4-d-1.png')

#####5a####
im_green_ch_noise=array(im)

sigma=30
noise=zeros(im_green.shape, dtype=float) #intiliazing noise array
noise=normal(0,sigma,noise.shape) #filling the array with random gaussian numbers
#print(noise[:,:]) #with the specified sigma
im_green=im_green.astype('float')  #converting the im_green into float
im_green=im_green+noise #adding noise to green channel
clip(im_green,0,255,out=im_green) #Clipping all the values to between 0 to 255
im_green=im_green.astype('uint8') #Converting to unsigned int
#print(im_green)
im_green_ch_noise[:,:,1]=im_green #Assigning the values to green channel

figure(8)
axis('off')
imshow(im_green_ch_noise)
savefig('output/ps0-5-a-1.png')


####5b######
im_blue_ch_noise=array(im)

im_blue=im_blue.astype('float')
im_blue=im_blue+noise
clip(im_blue,0,255,out=im_blue)
im_blue=im_blue.astype('uint8')
#print(im_blue)
im_blue_ch_noise[:,:,2]=im_blue

figure(9)
axis('off')
imshow(im_blue_ch_noise)
savefig('output/ps0-5-b-1.png')

#show()




