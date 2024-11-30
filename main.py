from EnvCapture import getEnv
from screenAdjustment import setBrightness
from calculateBrightness import optimizeBrightness
import cv2 as cv
import time

while True:
    ambientLight = getEnv()
    if ambientLight:
        screen_brightness = optimizeBrightness(ambientLight)
        setBrightness(screen_brightness)
        print(f"Ambient Light: {ambientLight}, Screen Brightness set to {screen_brightness}")

    time.sleep(5)

    if cv.waitKey(0) == ord('q'):
        break