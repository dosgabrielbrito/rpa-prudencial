import pyautogui
import time

### FUNÇÃO DE DETECÇÃO DE MOUSE ###
for i in range(3):
    print(i)
    time.sleep(1)

print(pyautogui.position())

# ### FUNÇÃO DE DETECÇÃO DE IMAGEM - SÓ FUNCIONA EM TELA ÚNICA ###
# try:
#     pyautogui.locateCenterOnScreen("button.png")
#     print("Precisão Encontrada!")
#     buttonx, buttony = pyautogui.locateCenterOnScreen("button.png")
#     pyautogui.moveTo(buttonx, buttony)

# except pyautogui.ImageNotFoundException:
#     print("O índice de confiança não é o suficiente.")
