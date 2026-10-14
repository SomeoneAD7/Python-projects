import time
import pyautogui

# Enable safety failsafe: moving mouse to any screen corner stops the script
pyautogui.FAILSAFE = True

def run_ad_bot():
    print("Bot started. Press Ctrl+C in terminal or move mouse to corner to stop.")
    
    while True:
        # 1. Look for 'Watch Ad' button
        try:
            watch_btn = pyautogui.locateOnScreen('watch_ad.png', confidence=0.8)
            if watch_btn:
                center = pyautogui.center(watch_btn)
                pyautogui.click(center)
                print("Started ad. Waiting for completion...")
                time.sleep(30)  # Minimum ad playback wait
        except pyautogui.ImageNotFoundException:
            pass # Button not on screen right now, do nothing

        # 2. Scan for the close ('X') button dynamically
        try:
            close_btn = pyautogui.locateOnScreen('close_icon.png', confidence=0.7)
            if close_btn:
                center = pyautogui.center(close_btn)
                pyautogui.click(center)
                print("Ad closed successfully.")
                time.sleep(3)  # Wait for main menu to reload
        except pyautogui.ImageNotFoundException:
            pass # Button not on screen right now, do nothing
            
        time.sleep(1) # Polling interval

if __name__ == "__main__":
    run_ad_bot()