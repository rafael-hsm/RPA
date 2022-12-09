import pyautogui as posicao_mouse
import pyautogui as tempo_espera


# Tempo de espera para que o computador possa processar
tempo_espera.sleep(1)

# Movendo o mouse ate o botao iniciar
posicao_mouse.moveTo(x=35, y=1040)
tempo_espera.sleep(1)

# Clicando na posicao
posicao_mouse.click(35, 1040)

# Escrevendo a palavra
posicao_mouse.typewrite('calc')
tempo_espera.sleep(1)
# print(posicao_mouse.position())

posicao_mouse.click(x=709, y=530)
