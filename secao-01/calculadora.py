import pyautogui as auto

#Tempo de espera para que o computador possa pensar
auto.sleep(2)

#Movendo o mouse até o botão iniciar
auto.moveTo(36, 1056)

#Tempo de espera para que o computador possa pensar
auto.sleep(2)

#Clicando na posição
auto.click(36, 1056)

#Tempo de espera para que o computador possa pensar
auto.sleep(2)

#Escrevenda a palavra calc / calculadora
auto.typewrite('calc')

#Tempo de espera para que o computador possa pensar
auto.sleep(1)

#Movendo o mouse até o aplicativo da calculadora
auto.press('enter')

#Tempo de espera para que o computador possa pensar
auto.sleep(2)

#Clico na calculadora
auto.typewrite("35", interval=0.25)
auto.press('+')

auto.typewrite("3", interval=0.25)
auto.press('enter')

#Tempo de espera para que o computador possa pensar
auto.sleep(2)

calc_ = auto.getActiveWindow()
auto.sleep(2)

calc_.close()

print("Automação finalizada com sucesso!")

#print(auto.position())
