import pyautogui
import time

pyautogui.press('winleft')
time.sleep(1)
pyautogui.write('chrome')
time.sleep(1)
pyautogui.press('enter')
pyautogui.click(1380,161,duration=1)
pyautogui.click(250,66,duration=1)
pyautogui.write('ibovespa hoje')
pyautogui.press('enter')
time.sleep(1)
pyautogui.screenshot('exemplo.png')
print('Tirei o print')