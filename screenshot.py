import pyautogui
import time


import pyautogui
import time

try:
    # pyautogui.screenshot('exemplo.png')
    print("Movendo o cursor para (1751, 51)")
    pyautogui.moveTo(1751, 51, 1)
    print("Aguardando 1 segundo")
    time.sleep(1)
    print("Clicando")
    pyautogui.click()
    print("Aguardando 1 segundo")
    time.sleep(1)
    print("Tirando screenshot e salvando como 'exemplo2.png'")
    pyautogui.screenshot('exemplo2.png')
    print("Screenshot tirada e salva com sucesso")
except Exception as e:
    print(f"Ocorreu um erro: {e}")