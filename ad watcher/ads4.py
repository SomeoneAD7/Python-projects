import time
import pyautogui

# Enable safety failsafe: moving mouse to any screen corner stops the script
pyautogui.FAILSAFE = True

# Define lists of all potential image variations
WATCH_AD_IMAGES = [
    'watch_ad.png', 
    'watch_ad1.png'
]
CLOSE_BUTTON_IMAGES = [
    'close_icon.png',
    'close_icon1.png',
    'close_icon2.png',
    'close_icon3.png',
    'close_icon4.png',
    'close_icon5.png',
    'close_button.jfif'
]

def locate_any(image_list, confidence=0.7):
    """Loops through a list of images and returns the first one found on screen."""
    for image_path in image_list:
        try:
            location = pyautogui.locateOnScreen(image_path, confidence=confidence)
            if location:
                return location
        except (pyautogui.ImageNotFoundException, OSError):
            continue
    return None

def run_ad_bot():
    print("Bot started. Press Ctrl+C in terminal or move mouse to corner to stop.")
    
    while True:
        # 1. Check for any 'Watch Ad' image
        watch_btn = locate_any(WATCH_AD_IMAGES, confidence=0.7)
        if watch_btn:
            center = pyautogui.center(watch_btn)
            pyautogui.click(center)
            print("Started ad. Waiting for completion...")
            time.sleep(30)  # Wait for ad duration
            continue

        # 2. Check for any 'Close' button image
        close_btn = locate_any(CLOSE_BUTTON_IMAGES, confidence=0.7)
        if close_btn:
            center = pyautogui.center(close_btn)
            pyautogui.click(center)
            print("Ad closed successfully.")
            time.sleep(3)  # Wait for main menu to reload
            continue
            
        time.sleep(1) # Polling interval

if __name__ == "__main__":
    run_ad_bot()