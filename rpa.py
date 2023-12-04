import pyautogui
import time

# Vetor de Dados:

dados = [
    4,
    9,
    102,
    126,
    134,
    151,
    182,
    195,
    1292,
    1337,
    1585,
    1589,
    1869,
    1901,
    2104,
    2164,
    2581,
    2726,
    2740,
    2747,
    2847,
    2874,
    3092,
    3502,
    3504,
    3505,
    3638,
    3652,
    3658,
    3675,
    4046,
    4075,
    4165,
    4175,
    4539,
    5004,
    5005,
    5006,
    5007,
    5028,
    5195,
    6758,
    7521,
    7868,
    8080,
    9289,
    9290,
    9291,
    9949,
    11289,
    11729,
    14975,
    15035,
    15377,
    15636,
    15758,
    16525,
    17238,
    17324,
    17356,
    17405,
    48151,
    49644,
    49993,
    50096,
    50763,
    51367,
    52090,
    52400,
    52747,
    52763,
    52784,
    52964,
    52991,
    52992,
    52994,
    56082,
    56170,
    56301,
    56832,
    57917,
    58102,
    58810,
    59231,
    60443,
    60752,
    61810,
    63552,
    64453,
    64733,
    65065,
    65554,
    65872,
    67938,
    68053,
    68278,
    69678,
    69692,
    69694,
    69738,
    69808,
    69999,
    70397,
    70469,
    70477,
    70579,
    70596,
    70641,
    70781,
    71084,
    71181,
    73364,
    74547,
    75239,
    75702,
    77671,
    78929,
    79489,
    79492,
    82283,
    82461,
    83887,
    87005,
    87470,
    88436,
    88542,
    91463,
    92192,
    92425,
    92687,
    93279,
    93699,
    95260,
    95298,
    95465,
    97772,
    100944,
    101020,
    101723,
    101954,
    102857,
    102969,
    103502,
]

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
        pyautogui.press("f5")
        time.sleep(15)
