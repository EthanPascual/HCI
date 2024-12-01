from EnvCapture import *
from screenAdjustment import *
from calculateBrightness import optimizeBrightness
import cv2 as cv
import time
from datetime import datetime

while True:
    ambientLight = getEnv()
    current_hour = datetime.now().hour
    current_window = getTask()
    if ambientLight:
        screen_brightness = optimizeBrightness(ambientLight, current_hour, current_window)
        setBrightness(screen_brightness)
        print(f"Ambient Light: {ambientLight}, Screen Brightness set to {screen_brightness}")

    

    time.sleep(5)