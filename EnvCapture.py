import numpy as np
import cv2 as cv


def getEnv():
    cap = cv.VideoCapture(0)
    if not cap.isOpened():
        print("Could not open camera")
        return
    ret, frame = cap.read()
    if ret:
        lab = cv.cvtColor(frame, cv.COLOR_BGR2LAB)
        light_channel = lab[:,:,0]
        avg_brightness = np.mean(light_channel)
        cap.release()
        return avg_brightness


print("Average Brightness: " + str(getEnv()))