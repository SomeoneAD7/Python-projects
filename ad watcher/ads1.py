import time
import pyautogui

# Failsafe: Moving mouse to top-left corner immediately stops script
pyautogui.FAILSAFE = True

print("Starting in 5 seconds. Switch to your Telegram window...")
time.sleep(5)

# Replace with the exact screen coordinates of the bot's button/tap zone on your monitor
TARGET_X = 960  
TARGET_Y = 540  

# Delay between actions in seconds (e.g., 35 seconds for ad completion)
ACTION_DELAY = 35  

try:
    while True:
        print(f"Clicking at ({TARGET_X}, {TARGET_Y})...")
        pyautogui.click(x=TARGET_X, y=TARGET_Y)
        
        # Wait for the ad or action timer to complete
        time.sleep(ACTION_DELAY)
        
except KeyboardInterrupt:
    print("Script stopped by user.")
