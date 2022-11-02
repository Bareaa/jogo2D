import os
import pygame
import time
pygame.init()
os.system("cls")
print("Inicio do jogo!")
largura = 453
altura = 612
tamanho = (largura,altura) #tupla - imutável -> não pode alterar os valores
display = pygame.display.set_mode( tamanho )
fps = pygame.time.Clock()
pygame.display.set_caption("gamePygame")
#   RGB   Red Green Blue
branco = (255,255,255)
preto = (0,0,0)
cor = (170,50,8) 
# looping para ficar rodando o jogo

rodando = True

fundo = pygame.image.load("assets/fundo.jpg")
jogador = pygame.image.load("assets/clarencio.png")
jogador = pygame.transform.scale(jogador, (155, 155)) #redimensionar uma imagem

tamanhoXjogador = 50
tamanhoYjogador = 50
posicaojogadorX = 202
posicaojogadorY = 455
movimentojogadorX = 0
movimentojogadorY = 0
velocidade = 10

# pontuacao = falta fazer o esquema de pontuação
pontuacao = 0


def escreverTexto (texto):
    fonte  = pygame.font.Font("freesansbold.ttf",15)
    textoDisplay = fonte.render(texto,True,branco)
    display.blit(textoDisplay, (5,5))

pygame.mixer.music.load("assets/lo-fi.mp3")
pygame.mixer.music.play(-1) #looping infinito (-1)
pygame.mixer.music.set_volume(0.35)



while rodando:
    # Mapeamento
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                movimentojogadorX = velocidade * -1
            elif evento.key == pygame.K_RIGHT:
                movimentojogadorX = velocidade
            elif evento.key == pygame.K_UP:
                movimentojogadorY = velocidade * -1
            elif evento.key == pygame.K_DOWN:
                movimentojogadorY = velocidade
        elif evento.type == pygame.KEYUP:
            movimentojogadorX = 0
            movimentojogadorY = 0
    
    #pra não sair da tela (antigo - limite de bordas)
    # if posicaojogadorX + movimentojogadorX + tamanhoXjogador < largura and posicaojogadorX + movimentojogadorX > 0:
    #     posicaojogadorX = posicaojogadorX + movimentojogadorX
    if posicaojogadorX + movimentojogadorX < largura and posicaojogadorX + movimentojogadorX > 0:
        posicaojogadorX += movimentojogadorX
    elif posicaojogadorX + movimentojogadorX == largura:
        posicaojogadorX = 0
    else:
        posicaojogadorX = largura

   
    display.fill(branco)
    display.blit(fundo , (0,0) )
    posicao = (posicaojogadorX,posicaojogadorY) # tupla 
    #pygame.draw.circle(display, cor ,posicao, 10)
    display.blit(jogador , (posicaojogadorX,posicaojogadorY) )


    pygame.display.update()
    fps.tick(60)


print("Volte Sempre!")
