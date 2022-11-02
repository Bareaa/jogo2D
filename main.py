import os
import time
import pygame
pygame.init()
os.system("cls")
print ("Inicio do jogo")

largura = 453
altura = 612
tamanho = (largura,altura)
display = pygame.display.set_mode(tamanho)
pygame.display.set_caption("Projeto Jogo.py")#Nome da aba que será aberto

fps = pygame.time.Clock() #fps
#cores rgb
azul = (42,45,255)

#variável para conseguir parar o while e printar a última msg
jogando = True
#looping para deixar a tela aberta 
while jogando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            jogando=False


    display.fill(azul)
    pygame.display.update()#atualiza a tela
    fps.tick(60) #determina os frames por segundo, para podermos interagir com a tela

print("Fim do jogo!")

#43:20