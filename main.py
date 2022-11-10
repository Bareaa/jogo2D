import pygame
import random
import time
pygame.init()
pygameDisplay = pygame.display
pygameDisplay.set_caption("teste de jogo")
altura = 612
largura = 453
tamanho = (largura, altura)
gameDisplay = pygame.display.set_mode(tamanho)
clock = pygame.time.Clock()
gameEvents = pygame.event
branco = (255,255,255)
vermelho = (255,0,0)

fundo = pygame.image.load("assets/fundo.jpg")
jogador = pygame.image.load("assets/clarencio.png")
bigorna = pygame.image.load("assets/bigorna.png")

bigorna = pygame.transform.scale(bigorna, (50, 60))
jogador = pygame.transform.scale(jogador, (100, 130))

pygame.mixer.music.load("assets/lo-fi.wav")
pygame.mixer.music.play(-1) #looping infinito (-1)
pygame.mixer.music.set_volume(0.3)




def escreverTexto (texto):
    fonte  = pygame.font.Font("freesansbold.ttf",15)
    textoDisplay = fonte.render(texto,True,branco)
    gameDisplay.blit(textoDisplay, (00,00))
    pygameDisplay.update()

def morreu():
    fonte  = pygame.font.Font("freesansbold.ttf",45)
    fonte2  = pygame.font.Font("freesansbold.ttf",30)
    textoDisplay = fonte.render("Fim de jogo",True,vermelho)
    textoDisplay2 = fonte2.render("press enter to continue !!!!",True,branco)
    gameDisplay.blit(textoDisplay, (100,150))
    gameDisplay.blit(textoDisplay2, (30,200))
    pygameDisplay.update()

def jogar():
    jogando = True
    ironX = 50
    ironY = 480
    movimentoIronX = 0
    larguraIron = 77
    alturaIron = 110
    alturabigorna = 70
    largurabigorna = 50
    posicaobigornaX = 400
    posicaobigornaY = -240
    velocidadebigorna = 10
    pontos = 0
    
    morte = pygame.mixer.Sound("assets/morte.mp3")
    morte.set_volume(1)
    # batida = pygame.mixer.Sound("assets/batida.wav")
    # batida.set_volume(0.8)
    queda = pygame.mixer.Sound("assets/queda.wav")
    queda.set_volume(0.1)


    while True:
        for event in gameEvents.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    movimentoIronX = -15
                elif event.key == pygame.K_d:
                    movimentoIronX = 15
                elif event.key == pygame.K_RETURN:
                    jogar()
            elif event.type == pygame.KEYUP:
                movimentoIronX = 0
            
        if jogando:
            if posicaobigornaY > altura:
                posicaobigornaY = -240
                posicaobigornaX = random.randint(0,largura)
                velocidadebigorna = velocidadebigorna + 1
                pygame.mixer.Sound.play(queda)
                pontos = pontos + 1
                
                
            else:
                posicaobigornaY =posicaobigornaY + velocidadebigorna

            if ironX + movimentoIronX >0 and ironX + movimentoIronX< largura-larguraIron:
                ironX = ironX + movimentoIronX
            gameDisplay.fill(branco)
            gameDisplay.blit(fundo,(0,0))
            gameDisplay.blit(jogador, (ironX,ironY))
            gameDisplay.blit(bigorna, (posicaobigornaX,posicaobigornaY))
            # escreverTexto("Pontos: "+str(pontos))

            pixelsXIron = list(range(ironX, ironX+larguraIron))
            pixelsYIron = list(range(ironY, ironY+alturaIron))

            pixelXbigorna = list(range(posicaobigornaX, posicaobigornaX+largurabigorna))
            pixelYbigorna = list(range(posicaobigornaY, posicaobigornaY+alturabigorna))

            colisaoY = len(list(set(pixelYbigorna) & set(pixelsYIron) ))
            if colisaoY > 0:
                colisaoX = len(list(set(pixelXbigorna) & set(pixelsXIron) ))
                print(colisaoX)
                if colisaoX > 39:
                    morreu()
                    jogando=False
                    # pygame.mixer.Sound.play(batida)
                    pygame.mixer.music.stop()                 
                    pygame.mixer.Sound.play(morte)


        pygameDisplay.update()
        clock.tick(60)

jogar()
