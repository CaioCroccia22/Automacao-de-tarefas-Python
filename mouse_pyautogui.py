import pyautogui
import time
#  1 - Obtendo o tamanho da tela
print(pyautogui.size())

# 2 - Pegar a posição atual do cursor
print(pyautogui.position())
time.sleep(1.5)
# 3 - Movendo o cursor do mouse
pyautogui.moveTo(1751, 33, duration=0.6)
pyautogui.click()

# 4 - Realizando o scroll
time.sleep(1.5)
pyautogui.moveTo(1060,461)
pyautogui.click()
time.sleep(1.5)
pyautogui.scroll(900)