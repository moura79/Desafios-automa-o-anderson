# Como pegar e arrastar algo de um lugar para outro

import pyautogui

for i in range(18):
    # mover ate uma coordenada
    pyautogui.moveTo(962,238,duration=0.5)
    # clicar arraste ate um ponto, arrastar ate um ponto
    pyautogui.dragTo(1116,691,button='left',duration=0.5)
    # repetir  tanto de vezes necessario
