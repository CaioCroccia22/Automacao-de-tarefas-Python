import pyautogui
import time

pyautogui.press('winleft')
time.sleep(1)
pyautogui.write('chrome')
time.sleep(1)
pyautogui.press('enter')
time.sleep(1)
pyautogui.click(1510,189, duration=1)
pyautogui.write('youtube.com')
time.sleep(1)
pyautogui.press('enter')