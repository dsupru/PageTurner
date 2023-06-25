import numpy as np
import cv2 as cv
from recognizers import build_recognizer
from gesture_handlers import build_gesture_handler
from time import time, sleep

def main():
    cap = cv.VideoCapture(0)
    if not cap.isOpened():
        print("Cannot open camera")
        exit()

    gestureHandler = build_gesture_handler('arrows', 2)
    recognizer = build_recognizer('hand_gesture', gestureHandler.event_callback)

    while True:
        print('processing frame')
        # Capture frame-by-frame
        ret, frame = cap.read()
        # if frame is read correctly ret is True
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break

        image = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
        recognizer.recognize(image, time()*1000)
        sleep(0.7)
        if cv.waitKey(1) == ord('q'):
            break

main()
