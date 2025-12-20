import yolo_detector
import hsv_detector
import camera


if __name__ == "__main__":

    # yolo = yolo_detector.YOLODETECTOR("/home/mert/Desktop/renk_nesne_tespiti/best.pt",0.6)

    green_lower = (45 , 107 , 93)
    green_upper = (98 , 233 , 227)  

    hsv = hsv_detector.HSVDETECTOR(green_lower,green_upper)

    cap = camera.Camera(0,hsv)

    cap.start()

    cap.stop()
