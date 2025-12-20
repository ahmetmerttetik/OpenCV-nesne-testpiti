import numpy as np
import cv2

def nothing(x):
    pass

class HSVDETECTOR:

    def __init__(self,hsv_lower,hsv_upper):

        self.hsv_lower = hsv_lower
        self.hsv_upper = hsv_upper

        # self.name_window = "Trackbar"
        
        # cv2.namedWindow(self.name_window)

        # cv2.createTrackbar("L-H", self.name_window, 0, 179, nothing)
        # cv2.createTrackbar("L-S", self.name_window, 0, 255, nothing)
        # cv2.createTrackbar("L-V", self.name_window, 0, 255, nothing)
        # cv2.createTrackbar("U-H", self.name_window, 0, 179, nothing)
        # cv2.createTrackbar("U-S", self.name_window, 0, 255, nothing)
        # cv2.createTrackbar("U-V", self.name_window, 0, 255, nothing)

    
    ## create hsv func

    ## get hsv func
    

    def detect(self,frame):
        
        img_blur = cv2.GaussianBlur(frame , (9 , 9) , 1)

        hsv = cv2.cvtColor(img_blur , cv2.COLOR_BGR2HSV)

        # lh = cv2.getTrackbarPos("L-H", self.name_window)
        # ls = cv2.getTrackbarPos("L-S", self.name_window)
        # lv = cv2.getTrackbarPos("L-V", self.name_window)
        # uh = cv2.getTrackbarPos("U-H", self.name_window)
        # us = cv2.getTrackbarPos("U-S", self.name_window)
        # uv = cv2.getTrackbarPos("U-V", self.name_window)

        # lower = np.array([lh,ls,lv])
        # upper = np.array([uh,us,uv])


        mask = cv2.inRange(hsv , self.hsv_lower , self.hsv_upper)

        structuring_element = cv2.getStructuringElement(cv2.MORPH_RECT , (3 , 3 ))

        mask = cv2.erode(mask,structuring_element)

        contours , hierarchy = cv2.findContours(mask,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

        center = None 
        
        if len(contours) > 0 :

            contour = max(contours,key = cv2.contourArea)

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

            # cv2.circle(frame,center,(0,0,255), -1)

            cv2.putText(frame , text , (50 , 50 ) , cv2.FONT_HERSHEY_COMPLEX_SMALL , 1 ,(0 , 0 , 0 ), 2)

            return frame
