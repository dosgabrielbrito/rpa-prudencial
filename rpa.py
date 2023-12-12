import pyautogui
import time

# Vetor de Dados:

dados = []

# Informação sobre automação:
pyautogui.alert("Atenção, o código do RPA irá iniciar.")

# Delay entre execuções:
pyautogui.PAUSE = 0.10

# Contador do Timer:
print("Timer:")
for i in range(6):
    print(i)
    time.sleep(1)

# Movimentação do Mouse:
print("Iniciar Busca:")
count = 0
countTot = 0

for i in dados:
    print("Preenchendo: " + str(i))

    # ### Função de Exclusão de Linha: FIREFOX ###
    # pyautogui.moveTo(2380, 1050)
    # pyautogui.click(button="left")
    # pyautogui.press("home")
    # pyautogui.hotkey("ctrl", "f")
    # pyautogui.write(str(i))
    # time.sleep(1)
    # pyautogui.press("enter")
    # pyautogui.moveTo(3818, 1057)
    # pyautogui.click(button="left")
    # pyautogui.moveTo(3425, 577)
    # pyautogui.click(button="left")  # Clique de Exclusão

    ### Função de Inclusão de Linha: CHROME ###
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
    pyautogui.moveTo(2881, 842)  # Incluir
    # pyautogui.moveTo(2976, 842)  # Excluir
    pyautogui.click(button="left")
    pyautogui.moveTo(3132, 835)
    pyautogui.click(button="left")
    pyautogui.moveTo(2456, 835)
    pyautogui.doubleClick(button="left")
    pyautogui.press("backspace")
    pyautogui.moveTo(3766, 1016)
    pyautogui.click(button="left")

    countTot = countTot + 1
    count = count + 1

    print("Total de : " + str(dados.index(i) + 1) + "/" + str(len(dados)))

    if count == 50:
        print("Salvando...")
        count = 0
        pyautogui.moveTo(2957, 1048)
        pyautogui.click(button="left")
        time.sleep(30)
        pyautogui.press("f5")
        time.sleep(15)
