import pyautogui
import time

# Wait for 5 seconds to give the user time to switch to the desired window
print("You have 5 seconds to switch to the window where you want to perform the clicks...")
time.sleep(5)

# Perform 10 clicks with an interval of 0.1 seconds between each click
for i in range(3000):
    pyautogui.click()
    time.sleep(0.1) # Sleep for 0.1 seconds between each click