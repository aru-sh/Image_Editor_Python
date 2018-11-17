import cv2
import numpy as np

name=input("Enter the name of image you want to edit: ")
#print(name)
image=cv2.imread(name)
image=np.array(image)

print(np.shape(image))
option=0

channels=0
height, width, channels=np.shape(image)

print(channels)

def menu():
    global option
    print("1. Change Brightness")
    print("2. Change Contrast")
    print("3. Change Scale of Image")
    print("4. Convert to B/W")
    option=input("Enter the option number: ")
    

   
def brightness():
    global image
    global height
    global width
    global channels

    value=int(input("Enter the absolute amount by which you want to increase brightness: "))
    blue=image[:,:,0]
    green=image[:,:,1]
    red=image[:,:,2]

    if(channels==3):    
        blue=np.where((255-blue)<value,255,blue+value)
        green=np.where((255-green)<value,255,green+value)
        red=np.where((255-red)<value,255,red+value)
        

    blue=np.expand_dims(blue, axis=2)
    red=np.expand_dims(red, axis=2)
    green=np.expand_dims(green, axis=2)
    image=np.concatenate([blue, green, red], axis=2)
    
    cv2.namedWindow('image', cv2.WINDOW_NORMAL)
    cv2.imshow('image',image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

 
    
#brightness2()

def contrast():
    global image
    global height
    global width
    global channels

    factor=float(input("Enter the factor by which you want to increase contrast: "))
    blue=image[:,:,0]
    green=image[:,:,1]
    red=image[:,:,2]

    if(channels==3):    
        blue=np.where((255/blue)< factor ,255,blue*factor)
        green=np.where((255/green)< factor,255,green*factor)
        red=np.where((255/red)< factor,255,red*factor)
        

    blue=np.expand_dims(blue, axis=2)
    red=np.expand_dims(red, axis=2)
    green=np.expand_dims(green, axis=2)
    image=np.concatenate([blue, green, red], axis=2)
    image=image.astype('uint8')
    
    cv2.imshow('image',image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
        
#contrast()
    
    
def greyscale():#0.21 R + 0.72 G + 0.07 B.
    global image
    global height
    global width
    global channels

    if(channels==0):
        print("Already in greyscale format")
    else:
        greyimage=image[:,:,0]*0.07+image[:,:,1]*0.72+image[:,:,2]*0.21
        greyimage=greyimage.astype('uint8')
        cv2.imshow('image',greyimage)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        
#greyscale()
                    
def fusion():
    global image
    global height
    global width
    global channels
    name=input("Enter the name of second image you want to fuse first image ")
    image2=cv2.imread(name)

    factor=float(input("Enter the fusion factor 0<factor<1(which will tell about dominance of second image over first image: "))

    while(factor<0 or factor>1):
        print("Invalid factor")
        factor=input("Enter the fusion factor 0<factor<1(which will tell about dominance of second image over first image: ")
        
    blue1=(1-factor)*image[:,:,0]
    green1=(1-factor)*image[:,:,1]
    red1=(1-factor)*image[:,:,2]

    blue2=factor*image2[:,:,0]
    green2=factor*image2[:,:,1]
    red2=factor*image2[:,:,2]


    blue1=np.where((255-blue1)<blue2,255,blue1+blue2)
    green1=np.where((255-green1)<green2,255,green1+green2)
    red1=np.where((255-red1)<red2,255,red1+red2)
    
    blue1=np.expand_dims(blue1, axis=2)
    red1=np.expand_dims(red1, axis=2)
    green1=np.expand_dims(green1, axis=2)
    image=np.concatenate([blue1, green1, red1], axis=2)
    image=image.astype('uint8')
    
    cv2.imshow('image',image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    



#fusion()


def histogram():
    global image
    global channels
    global height
    global width

    
    if(channels==3):
        image=image[:,:,0]*0.07+image[:,:,1]*0.72+image[:,:,2]*0.21
        image=image.astype('uint8')

    range1=int(input("Enter the range: "))
    array=np.reshape(image,(height*width))
    dictionary={}
    dictionary2={}
    
    unique, counts = np.unique(array, return_counts=True)
    dictionary=dict(zip(unique, counts))
    cumulative=0
    for key, value in dictionary.items():
        dictionary2[key]=value+cumulative
        cumulative+=value

    firstitem=int(dictionary2[next(iter(dictionary2))])
    print(firstitem)
    for key, value in dictionary2.items():
        dictionary2[key]=round((int(dictionary2[key])-firstitem)*(range1-1)/((height*width)-firstitem))
        #print(int(dictionary2[key])-firstitem)
        
    for i in range(height):
        for j in range(width):
            image[i,j]=dictionary2[image[i,j]]
        

    cv2.imshow('image',image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

        

histogram()




'''def meanblur():
    global image
    global height
    global width
    global channels

    kernel=int(input("Enter the kernel size: ")
    if(kernel%2==0):
        print("Kernel size must be in odd!")
        kernel=int(input("Enter the kernel size: "))

    kernelstart=int((kernel-1)/2)
    
    for start in range(kernel, width-kernel):
        for i in range(start,start+kernel):
            for j in range(start, start+kernel):
               value+=image[i,j]
               image[i+kernestart,j+kernelstart]
                
'''





















def brightness():
    global image
    global height
    global width
    global channels

    increase=int(input("Enter the absolute amount by which you want to increase brightness: "))

    for i in range(height):
        for j in range(width):
            if(channels==0):
                if((image[i, j]+increase)>255):
                    image[i,j]=255
                else:
                    image[i,j]+=increase
            else:
                for k in range(channels):
                    value=image[i,j,k]
                    
                    if((value+increase)>255):
                        image[i,j,k]=255
                    else:
                        image[i,j,k]+=value+increase
            
    cv2.namedWindow('image', cv2.WINDOW_NORMAL)
    cv2.imshow('image',image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

#brightness()
