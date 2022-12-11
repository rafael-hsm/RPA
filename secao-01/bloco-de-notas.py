import pyautogui as auto

#Aguarda um tempo para o computador processar informações
auto.sleep(1)

#Mesma coisa que pressionar as teclas do teclado
#Windows + R
auto.hotkey('win','r')

#Aguarda um tempo para o computador processar informações
auto.sleep(2)

#Digitando notepad na caixa de executar para
#abrir o bloco de notas
auto.typewrite('notepad')

#Aguarda um tempo para o computador processar informações
auto.sleep(2)

#Apertar a tecla enter para abrir o bloco de notas
auto.press('enter')

#Aguarda um tempo para o computador processar informações
auto.sleep(2)

#Estamos escrevendo dentro do bloco de notas
auto.typewrite('Abri o bloco de notas com o Python')

#Aguarda um tempo para o computador processar informações
auto.sleep(2)

#Permite pegar a janela que está ativa
fecharBlocoDeNotas = auto.getActiveWindow()

#Aguarda um tempo para o computador processar informações
auto.sleep(2)

#Aciona a opção para fechar a janela ativa
fecharBlocoDeNotas.close()

#Aguarda um tempo para o computador processar informações
auto.sleep(2)

#Pressionando a tecla tab para ir para o botão não salvar
auto.press('tab')

#Aguarda um tempo para o computador processar informações
auto.sleep(1)

#Apertamos a tecla enter para fechar sem salvar
auto.press('enter')

print("Automação executada com sucesso!")
