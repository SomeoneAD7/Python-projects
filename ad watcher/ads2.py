import time
import pyautogui

def run_ad_bot():
    while True:
        watch_btn = pyautogui.locateOnScreen('watch_ad.png', confidence=0.8)
        if watch_btn:
            pyautogui.click(pyautogui.center(watch_btn))
            time.sleep(30)
            
        close_btn = pyautogui.locateOnScreen('close_icon.png', confidence=0.7)
        if close_btn:
            pyautogui.click(pyautogui.center(close_btn))
            time.sleep(3)