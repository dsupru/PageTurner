import numpy as np
import cv2 as cv
import pyautogui
from recognizer import Recognizer
from time import time, sleep

def print_result(result, output_image, timestamp_ms: int):
    if result != None and result.gestures != []:
        print('hand landmarker result: {}'.format(result.gestures[0][0].category_name))
        if (result.gestures[0][0].category_name) == 'Thumb_Up':
            pyautogui.press('right')
        elif (result.gestures[0][0].category_name) == 'Pointing_Up':
            pyautogui.press('left')

def main():
    cap = cv.VideoCapture(0)
    if not cap.isOpened():
        print("Cannot open camera")
        exit()
    recognizer = Recognizer(print_result)
    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()
        # if frame is read correctly ret is True
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break
        # Our operations on the frame come here
        image = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
        recognizer.recognize(image, time()*1000)
        sleep(0.7)
        print('ran loop')
        if cv.waitKey(1) == ord('q'):
            break

main()
