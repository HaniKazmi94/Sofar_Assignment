#importing Modules

import cv2
import numpy as np
import time
#Capturing Video through webcam.
#cap = cv2.VideoCapture(0)
while(1):
        y1=0
        object_found=False
        print("Press 1 for MIRO")
        x = int(input("Please Enter any Number from above "))
        if(x==1):
                print("Miro is in Active state")
                print("press 2 for Search yellow Ball")
                print("press 3 for Back")
                x = int(input("Please Enter any Number from above "))
                if(x==2):
                        while(1):
                        #        _, img = cap.read()
                                img = cv2.imread("/home/zaid/hanisofar/yellow.jpeg")
                                print("Miro Searching")

                                #converting frame(img) from BGR (Blue-Green-Red) to HSV (hue-saturation-value)

                                hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
                                
                                #defining the range of Yellow color
                                yellow_lower = np.array([22,60,200],np.uint8)
                                yellow_upper = np.array([60,255,255],np.uint8)

                                #finding the range yellow colour in the image
                                yellow = cv2.inRange(hsv, yellow_lower, yellow_upper)

                                #Morphological transformation, Dilation         
                                kernal = np.ones((5 ,5), "uint8")

                                blue=cv2.dilate(yellow, kernal)

                                res=cv2.bitwise_and(img, img, mask = yellow)

                                #Tracking Colour (Yellow) 
                                (_,contours,hierarchy)=cv2.findContours(yellow,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
                                
                                for pic, contour in enumerate(contours):
                                        area = cv2.contourArea(contour)
                                        print(area)
                                        if(area>1):
                                                print("MIRO is in Happy state")
                                                object_found=True
                                                x,y,w,h = cv2.boundingRect(contour)     
                                                img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),3)
               
                                cv2.imshow("Color Tracking",img)
                                img = cv2.flip(img,1)
                                cv2.imshow("Yellow",res)                                                
                                if cv2.waitKey(10) & 0xFF == 27:
                                        cap.release()
                                        cv2.destroyAllWindows()
                                        break
                                if (y1==5 ):
                                        y1=0       #increase this number to increase timer
                                        if(object_found==False):
                                                y1=0
                                                print("MIRO is SAD STATE")
                                                cap.release()
                                                cv2.destroyAllWindows()
                                                break
                                time.sleep(1)                                       
                                y1=y1+1
                                print(y1)
                                if(object_found==False):
                                        y1=0
                                        print("MIRO is SAD STATE")
                elif(x==3):
                        print("Thank You!")
