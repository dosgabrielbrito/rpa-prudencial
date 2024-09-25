import pyautogui
import time

### FUNÇÃO PARA DETECÇÃO DE MOUSE ###
for i in range(3):
    print(i)
    time.sleep(1)

print(pyautogui.position())

# ### FUNÇÃO DE DETECÇÃO DE IMAGEM - SÓ FUNCIONA EM TELA ÚNICA ###
# try:
#     pyautogui.locateCenterOnScreen("botao.png")
#     print("Precisão Encontrada!")
#     buttonx, buttony = pyautogui.locateCenterOnScreen("botao.png")
#     pyautogui.moveTo(buttonx, buttony)

# except pyautogui.ImageNotFoundException:
#     print("O índice de confiança não é o suficiente.")
