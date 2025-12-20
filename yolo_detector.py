from ultralytics import YOLO


class YOLODETECTOR:

    def __init__(self,model_path,conf = 0.5):

        self.model = YOLO(model_path)
        self.conf = conf

    # otomatik pt dosyası bulan bir find_pt adında bir kod yaz

    def detect(self,frame):

        results = self.model(frame,conf = self.conf)

        annotated_frame = results[0].plot()

        return annotated_frame
        