import pyautogui
import time

# Informação sobre automação:
pyautogui.alert("Atenção, o código do RPA irá iniciar.")

# Delay entre execuções:
pyautogui.PAUSE = 1

# Abrir Google Chrome:
pyautogui.press("winleft")
pyautogui.write("chrome")
pyautogui.press("enter")
pyautogui.press("tab")
pyautogui.press("enter")
pyautogui.write("https://www.ccee.org.br/web/guest/fator-de-alavancagem")
pyautogui.press("enter")
