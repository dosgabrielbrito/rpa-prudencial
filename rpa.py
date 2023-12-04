import pyautogui
import time

# Vetor de Dados:

dados = [
    50137,
    68372,
    76138,
    107576,
    58038,
    65582,
    57051,
    77746,
    2046,
    4225,
    80702,
    107073,
    55062,
    75008,
    80787,
    88101,
    87706,
    70844,
    75243,
    69768,
    83152,
    85960,
    87476,
    48638,
    74024,
    97342,
    93525,
    72057,
    104816,
    89865,
    75829,
    103688,
    71655,
    97115,
    48029,
    90644,
    108680,
    109135,
    47536,
    108080,
    101173,
    107299,
    107987,
    104722,
    106348,
    108015,
    109408,
    102097,
    110336,
    107008,
    107506,
    70725,
]

# Informação sobre automação:
pyautogui.alert("Atenção, o código do RPA irá iniciar.")

# Delay entre execuções:
pyautogui.PAUSE = 0.10

# Abrir Google Chrome:
# pyautogui.press("winleft")
# pyautogui.write("chrome")
# pyautogui.press("enter")
# pyautogui.press("tab")
# pyautogui.press("enter")
# pyautogui.write("https://www.ccee.org.br/web/guest/fator-de-alavancagem")
# pyautogui.press("enter")

# Contador do Timer:
# print("Timer:")
# for i in range(5):
#     print(i)
#     time.sleep(1)

# Movimentação do Mouse:
# pyautogui.moveTo(2878, 393)
# pyautogui.click(button="left")
# pyautogui.scroll(-800)

# pyautogui.moveTo(2425, 255)
# pyautogui.click(button="left")
# pyautogui.moveTo(2425, 295)
# pyautogui.click(button="left")

# Contador do Timer:
print("Timer:")
for i in range(5):
    print(i)
    time.sleep(1)

# Movimentação do Mouse:
print("Iniciar Busca:")
count = 0
for i in dados:
    print("Preenchendo: " + str(i))
    pyautogui.moveTo(2317, 835)
    pyautogui.click(button="left")
    pyautogui.click(button="left")
    pyautogui.moveTo(2522, 835)
    pyautogui.click(button="left")
    pyautogui.write(str(i))
    pyautogui.moveTo(2829, 835)
    pyautogui.click(button="left")
    time.sleep(3)
    pyautogui.moveTo(2522, 865)
    pyautogui.click(button="left")
    pyautogui.moveTo(2881, 842)
    pyautogui.click(button="left")
    pyautogui.moveTo(3132, 835)
    pyautogui.click(button="left")
    pyautogui.moveTo(2456, 835)
    pyautogui.doubleClick(button="left")
    pyautogui.press("backspace")
    pyautogui.moveTo(3766, 1016)
    pyautogui.click(button="left")
    print("Total de : " + str(dados.index(i) + 1) + "/" + str(len(dados)))
    count = count + 1
    if count == 50:
        print("Salvando...")
        count = 0
        pyautogui.moveTo(2957, 1048)
        pyautogui.click(button="left")
        time.sleep(30)
