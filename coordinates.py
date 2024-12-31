import pyautogui
import time

def get_coordinates():
    x, y = pyautogui.position()
    return x, y

try:
    while True:
        x, y = get_coordinates()
        screen_width, screen_height = pyautogui.size()
        print(f"Raw Coordinates: ({x}, {y}), Screen size: ({screen_width}x{screen_height})", end="\r")
        time.sleep(0.1)
except KeyboardInterrupt:
    print("\nExiting...")