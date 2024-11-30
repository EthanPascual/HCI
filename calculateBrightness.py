import math
from datetime import datetime

def optimizeBrightness(ambientLight, min_brightness = 10, max_brightness = 100, k = 0.1):
    ambientLight /= 100
    base_brightness = 100 / (1+math.exp(-(ambientLight - 0.5) * 10))

    current_hour = datetime.now().hour
    if not 6 <= current_hour <= 18:
        base_brightness *= 0.7

    brightness = max(min_brightness, min(max_brightness, base_brightness))
    return int(brightness)