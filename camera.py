import cv2
import time
import threading

class Camera:

    def __init__(self,source_id = 0, detector = None):
        
        self.frame = None

        self.cap = cv2.VideoCapture(source_id)

        if not self.cap.isOpened():
            print("kamera acilmadi")

        # self.running = True

        # self.thread = threading.Thread(target=self.thread_frame)
        # self.thread.daemon = True
        # self.thread.start()


        self.detector = detector

        self.prev_time = time.time()

        self.curr_time = 0 

    # def thread_frame(self):
        
    #     while self.running:
    #         ret , frame = self.cap.read()
            
    #         if ret:
    #             self.frame = frame
            
    # def get_frame(self):

    #     return self.frame
            



    def start(self):

        if self.cap.isOpened():
            
            

            while True:

                ret,frame = self.cap.read()

                

                # if not ret:
                #     print("ret is False")
                
                if self.detector:
                    
                    frame = self.detector.detect(frame)


                self.curr_time = time.time()
                fps = int(1/(self.curr_time-self.prev_time))
                self.prev_time=self.curr_time
                
                cv2.putText(frame,f"fps: {fps}",(50,50),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,0),2)

                cv2.imshow("frame",frame)

                if cv2.waitKey(1) == ord('q'):
                    break
        else: 
            print("kamera acilmadi")


    def stop(self):

        self.running = False
        self.thread.join()

        self.cap.release()
        cv2.destroyAllWindows()


    