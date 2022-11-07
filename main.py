import os
import pygame
import random
pygame.init()
os.system("cls")
print("Inicio do jogo!")
largura = 470
altura = 612
tamanho = (largura,altura) #tupla - imutável -> não pode alterar os valores
display = pygame.display.set_mode( tamanho )
fps = pygame.time.Clock()
pygame.display.set_caption("gamePygame")
tamanhoXjogador = 50
tamanhoYjogador = 50
posicaojogadorX = 202
posicaojogadorY = 455
movimentojogadorX = 0
movimentojogadorY = 0
velocidade = 3.5
posicaoX=433 #X vai crescendo da esquerda para direita 0 --> 470
posicaoY=00 #Y vai crescendo de baixo para cima 0 --> 612
velocidadequeda = 4.56
branco = (255,255,255)

rodando = True  # looping para ficar rodando o jogo

sopa = pygame.image.load("assets/macarrao.png")
pirulito = pygame.image.load("assets/pirulito.png")
toddynho = pygame.image.load("assets/toddynho.png")

fundo = pygame.image.load("assets/fundo.jpg")
jogador = pygame.image.load("assets/clarencio.png")
jogador = pygame.transform.scale(jogador, (155, 155)) #redimensionar uma imagem
sopa = pygame.transform.scale(sopa, (40, 60))
pirulito = pygame.transform.scale(pirulito, (40, 60))
toddynho = pygame.transform.scale(toddynho, (40, 50))

# pontuacao = falta fazer o esquema de pontuação
pontuacao = 0


def escreverTexto (texto):
    fonte  = pygame.font.Font("freesansbold.ttf",15)
    textoDisplay = fonte.render(texto,True,branco)
    display.blit(textoDisplay, (5,5))

def alimentos (posicaoalimentoX, posicaoalimentoY):
    display.blit(sopa, (random.randint(posicaoalimentoX, posicaoalimentoY)))
    

pygame.mixer.music.load("assets/lo-fi.mp3")
pygame.mixer.music.play(-1) #looping infinito (-1)
pygame.mixer.music.set_volume(0.35)



while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_a:
                movimentojogadorX = velocidade * -1
            elif evento.key == pygame.K_d:
                movimentojogadorX = velocidade
        elif evento.type == pygame.KEYUP:
            movimentojogadorX = 0
    
    #FAZER UM BLOCO COM COLISÃO DO LADO DIREITO DA TELA PARA O CLARENCIO NÃO SE ESCONDER NELA
    #pra não sair da tela (antigo - limite de bordas)
    if posicaojogadorX + movimentojogadorX < largura and posicaojogadorX + movimentojogadorX > 0:
        posicaojogadorX = posicaojogadorX + movimentojogadorX
    
    posicaoY += velocidadequeda
    if (posicaoY >= -200):
            posicaoY = 433 
    display.blit(fundo , (0,0) )
    posicao = (posicaojogadorX,posicaojogadorY) 
    display.blit(jogador , (posicaojogadorX,posicaojogadorY) )
    display.blit(sopa, (posicaoX,posicaoY))
    display.blit(pirulito, (300,posicaoY))
    display.blit(toddynho, (120,posicaoY))
    parede = pygame.draw.rect(display, (0,0,0), (468,00,10,800))#parede, precisamos por comando de colisão!

    # if parede.colliderect(jogador): 
    #     velocidade=0


    pygame.display.update()
    fps.tick(60)


print("Volte Sempre!")