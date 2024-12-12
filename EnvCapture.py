import numpy as np
import cv2 as cv
import win32gui
import win32process
import psutil


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

        norm = (avg_brightness / 255) * 100

        cap.release()
        return norm

def getTask():
    window = win32gui.GetForegroundWindow()
    _, pid = win32process.GetWindowThreadProcessId(window)
    if pid <= 0:
        return "none"
    process = psutil.Process(pid)
    print(f"Process: {process.name().lower()}")
    return process.name().lower()
