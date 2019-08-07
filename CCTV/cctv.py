import cv2
import numpy as np
import datetime
import time

for i in range(1800):
    s = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    video = cv2.VideoCapture(0)
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    name = str(s) + '.avi'
    out = cv2.VideoWriter(name,fourcc, 20.0, (640,480))

    for _ in range(300):
        for z in range(300):
            ret, image = video.read()
            out.write(image)
        time.sleep(2)
            
    video.release()
    out.release()
