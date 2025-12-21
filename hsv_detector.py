import numpy as np
import cv2

def nothing(x):
    pass

class HSVDETECTOR:

    def __init__(self,hsv_lower,hsv_upper):

        
        self.hsv_lower = hsv_lower
        self.hsv_upper = hsv_upper

        self.create_trackbar()

    def create_trackbar(self):

        print("create_trackbar")

        cv2.namedWindow("Trackbar")

        cv2.createTrackbar("LH","Trackbar",0,179,nothing)
        cv2.createTrackbar("LS","Trackbar",0,255,nothing)
        cv2.createTrackbar("LV","Trackbar",0,255,nothing)
        cv2.createTrackbar("UH","Trackbar",0,179,nothing)
        cv2.createTrackbar("US","Trackbar",0,255,nothing)
        cv2.createTrackbar("UV","Trackbar",0,255,nothing)


    def get_trackbar(self):

        print("get_trackbar")

        lh = cv2.getTrackbarPos("LH","Trackbar")
        ls = cv2.getTrackbarPos("LS","Trackbar")
        lv = cv2.getTrackbarPos("LV","Trackbar")
        uh = cv2.getTrackbarPos("UH","Trackbar")
        us = cv2.getTrackbarPos("US","Trackbar")
        uv = cv2.getTrackbarPos("UV","Trackbar")

        lower = np.array([lh,ls,lv])
        upper = np.array([uh,us,uv])

        return lower , upper

    ## create hsv func

    ## get hsv func
    

    def detect(self,frame):
        
        print("detect_ilk")        

        imgBlur = cv2.GaussianBlur(frame,(9,9),1)

        hsv = cv2.cvtColor(imgBlur , cv2.COLOR_BGR2HSV)

        

        print("hsv")

        lower , upper = self.get_trackbar()

        
        mask = cv2.inRange(hsv , lower , upper)

        print("mask")

        cv2.imshow("mask",mask)

        structuring_element = cv2.getStructuringElement(cv2.MORPH_RECT , (3 , 3 ))

        mask = cv2.erode(mask,structuring_element)

        mask_copy = mask.copy()

        (contours,hierarchy) = cv2.findContours(mask_copy,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

        center = None 
        
        print("if_oncesi")
        
        if len(contours) > 0:

            print("if")

            for contour in contours:
                
                print("cnt")

                area = cv2.contourArea(contour)

                

                if area > 500:
                    
                    print("ikinci if")
                    
                    rect = cv2.minAreaRect(contour)

                    (x,y) , (width , height ) , rotation = rect

                    text = f"x : {np.around(x)} , y : {np.around(y)} , height : {np.around(height)} , width : {np.around(width)} ,rotation : {np.around(rotation)}"

                    # text = f"""

                    #     x : {np.around(x)} ,

                    #     y : {np.around(y)} ,

                    #     height : {np.around(height)} ,

                    #     width : {np.around(width)} ,

                    #     rotation : {np.around(rotation)}
                    
                    # """
                    
                    box = cv2.boxPoints(rect)

                    box = np.int64(box)

                    M = cv2.moments(contour)

                    center = (int(M['m10'] / M ['m00']), int(M['m01'] / M ['m00']))

                    cv2.drawContours(frame , [box] , 0 , (0 , 255 , 0) , 2)

                    cv2.putText(frame,"object",(int(x),int(y) - 10),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(0,0 , 0 ), 2)


        print("frame")    

        return frame
