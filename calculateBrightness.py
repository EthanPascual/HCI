import math
from datetime import datetime

app_map = {
    "chrome.exe" : 0.8,
    "winword.exe" : 0.5,
    "notepad.exe" : 0.5,
    "vlc.exe" : 1.5,
    "game.exe" : 2,
    "code.exe": 0.9
}

def optimizeBrightness(ambientLight, current_hour, current_window, adjustor, min_brightness = 10, max_brightness = 100):
    if adjustor == 0:
        return "Keep Same"
    ambientLight /= 100
    base_brightness = 100 / (1+math.exp(-(ambientLight - 0.5) * 5))

    if not 6 <= current_hour <= 18:
        base_brightness *= 0.7
    if current_window in app_map:
        base_brightness *= app_map[current_window]

    modifier = float(adjustor) / 50.0
    base_brightness *= modifier

    brightness = max(min_brightness, min(max_brightness, base_brightness))
    return int(brightness)