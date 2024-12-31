import pyautogui
import time
import keyboard

# Set the coordinates of the click
x = int(input('enter the x coordinate:'))
y = int(input('enter the y coordinate:'))

#interval in seconds
interval = int(input('enter the interval in seconds:'))
try:
    while True:
        if keyboard.is_pressed('q'):
            print('Exiting...')
            break
        pyautogui.click(x, y)
        time.sleep(interval)
except Exception as e:
    print(f"Keyboard input detected. Exiting... {e}")