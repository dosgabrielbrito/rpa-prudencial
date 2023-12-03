import pyautogui
import time

# Vetor de Dados:
dados = [
    "2B ENERGIA",
    "2W COMERCIALIZADORA",
    "2W VAREJISTA",
    "2WENERGIA",
    "3G ENERGIA",
    "00_VPCOM",
    "88 ENERGIA",
    "ABC BRASIL",
    "ABENGOA AGROIN",
    "ABM MATRIZ",
    "ABM TRADING",
    "ABRANJO I",
    "ACAI TAPAJOS CONSUMO",
    "ACANTHUS",
    "ACAUÃ I",
    "ACAUÃ II",
    "ACAUÃ III",
    "ACE",
    "ACL ENERGIA",
    "ADECO IMPORT EXPORT",
    "ADM",
    "ADM BRASIL",
    "ADN ENERGIA",
    "AEROPORTO SALVADOR",
    "AES BRASIL OPERACOES",
    "AES COMERCIALIZADORA",
    "AES TIETE INTEGRA",
    "AFLUENTE",
    "AG ENERGY",
    "AGE ENERGIA",
    "AGORA ENERGIA",
    "AGRARIA ENERGIA",
    "AGRESTE",
    "AGRO NOVO MILENIO",
    "AGROENERGIA",
    "AGUA CLARA",
    "ÁGUAS DA SERRA",
    "AGV IV",
    "AGV V",
]

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

# Contador do Timer:
print("Timer:")
for i in range(5):
    print(i)
    time.sleep(1)

# Movimentação do Mouse:
pyautogui.moveTo(2878, 393)
pyautogui.click(button="left")
pyautogui.scroll(-800)

pyautogui.moveTo(2425, 255)
pyautogui.click(button="left")
pyautogui.moveTo(2425, 295)
pyautogui.click(button="left")

# Contador do Timer:
print("Timer:")
for i in range(5):
    print(i)
    time.sleep(1)

# Movimentação do Mouse:
print("Iniciar Busca:")
for i in dados:
    print("Pesquisando: " + i)
    pyautogui.moveTo(2650, 255)
    pyautogui.click(button="left")
    pyautogui.write(i)
    time.sleep(2)
    pyautogui.moveTo(2650, 300)
    pyautogui.click(button="left")
    time.sleep(2)
