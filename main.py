from EnvCapture import *
from screenAdjustment import *
from calculateBrightness import optimizeBrightness
import cv2 as cv
import time
from datetime import datetime
import tkinter as tk

adjustor = 50

root = tk.Tk()
root.geometry("500x500")
root.title("Context-Aware Screen Brightness")

brightness_label = tk.Label(root, text="Brightness: Not Set", font=("Ariel", 18))
brightness_label.pack()

condition = False
def startLoop():
    global adjustor
    if condition:
        ambientLight = getEnv()
        current_hour = datetime.now().hour
        current_window = getTask()
        if ambientLight:
            screen_brightness = optimizeBrightness(ambientLight, current_hour, current_window, adjustor)
            if screen_brightness != "Keep Same":
                setBrightness(screen_brightness)
                brightness_label.config(text=f"Brightness: {screen_brightness}")

            print(f"Ambient Light: {ambientLight}, Screen Brightness set to {screen_brightness}")
    root.after(3000, startLoop)

def changeValue(value):
    global adjustor
    adjustor = value

def start():
    global condition
    condition = True

def stop():
    global condition
    condition = False


startButton = tk.Button(root, text="Start Dynamic Screen Adjustment!", command = start)
startButton.pack()
stopButton = tk.Button(root, text="Quit", command=stop)
stopButton.pack()
adjustLabel = tk.Label(root, text="Adjust optimization calculation: 50 = default")
adjustLabel.pack()
slider = tk.Scale(root, variable=adjustor, from_=0, to=100, orient="horizontal", command=changeValue )
slider.set(50)
slider.pack()

root.after(1000, startLoop)

root.mainloop()

