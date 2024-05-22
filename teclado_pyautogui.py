import pyautogui
import time


# Abrindo a calculadora
pyautogui.press('winleft')
time.sleep(1)
pyautogui.write('calculadora')
pyautogui.press('enter')
time.sleep(1)
pyautogui.hotkey('crtl', 'shift', 'esc')

# Utilizando o teclado virtual