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
time.sleep(1)
with pyautogui.hold('winleft'):
    pyautogui.press('left')

time.sleep(2)
pyautogui.click()
time.sleep(2)
with pyautogui.hold('winleft'):
    pyautogui.press('rigth')