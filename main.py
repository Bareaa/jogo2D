def game():
    import pygame
    import random
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
    pirulito = pygame.image.load("assets/pirulito.png")
    tody = pygame.image.load("assets/toddynho.png")
    sopa = pygame.image.load("assets/sopa.png")

    bigorna = pygame.transform.scale(bigorna, (50, 60))
    jogador = pygame.transform.scale(jogador, (100, 130))
    pirulito = pygame.transform.scale(pirulito, (30, 50))
    tody = pygame.transform.scale(tody, (30, 60))
    sopa = pygame.transform.scale(sopa, (30, 50))

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
        jogadorX = 175 #posição do jogador na tela
        jogadorY = 480
        movimentojogadorX = 0
        largurajogador = 77
        alturajogador = 110

        alturabigorna = 70
        largurabigorna = 50
        posicaobigornaX = 400
        posicaobigornaY = -240
        velocidadebigorna = 1

        
        pirulitoY = -100
        pirulitoX = 300
        larguraPirulito = 30
        alturaPirulito = 50
        velocidadePirulito = 5

        todyY = -180
        todyX = 200
        larguraTody = 30
        alturaTody = 50
        velocidadeTody = 3

        sopaY = -230
        sopaX = 100
        larguraSopa = 30
        alturaSopa = 50
        velocidadeSopa = 4
        
        pontos = 0
        
        morte = pygame.mixer.Sound("assets/morte.mp3")
        morte.set_volume(1)
        batida = pygame.mixer.Sound("assets/batida.wav")
        batida.set_volume(0.8)
        queda = pygame.mixer.Sound("assets/queda.wav")
        queda.set_volume(0.1)


        while True:
            for event in gameEvents.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        movimentojogadorX = -15
                    elif event.key == pygame.K_d:
                        movimentojogadorX = 15
                    elif event.key == pygame.K_RETURN:
                        jogar()
                elif event.type == pygame.KEYUP:
                    movimentojogadorX = 0
            
            if jogando:
                if posicaobigornaY > altura:
                    posicaobigornaY = -240
                    posicaobigornaX = random.randint(0,largura)
                    velocidadebigorna = velocidadebigorna + 1
                    pygame.mixer.Sound.play(queda)
                    # pontos = pontos + 1
                    
                    
                else:
                    posicaobigornaY =posicaobigornaY + velocidadebigorna

            if jogando:
                if pirulitoY > altura:
                    pirulitoY = -240
                    pirulitoX = random.randint(0,largura)
                    velocidadePirulito = velocidadePirulito 
                    pygame.mixer.Sound.play(queda)
                    # pontos = pontos + 1
                else:
                    pirulitoY =pirulitoY + velocidadePirulito

            if jogando:
                if todyY > altura:
                    todyY = -240
                    todyX = random.randint(0,largura)
                    velocidadeTody = velocidadeTody 
                    pygame.mixer.Sound.play(queda)
                    # pontos = pontos + 1        
                else:
                    todyY =todyY + velocidadeTody
                    
            if jogando:
                if sopaY > altura:
                    sopaY = -240
                    sopaX = random.randint(0,largura)
                    velocidadeSopa = velocidadeSopa 
                    pygame.mixer.Sound.play(queda)
                    # pontos = pontos + 1        
                else:
                    sopaY =sopaY + velocidadeSopa

                if jogadorX + movimentojogadorX >0 and jogadorX + movimentojogadorX< largura-largurajogador:
                    jogadorX = jogadorX + movimentojogadorX
                gameDisplay.fill(branco)
                gameDisplay.blit(fundo,(0,0))
                gameDisplay.blit(jogador, (jogadorX,jogadorY))
                gameDisplay.blit(bigorna, (posicaobigornaX,posicaobigornaY))
                gameDisplay.blit(pirulito, (pirulitoX,pirulitoY))
                gameDisplay.blit(tody, (todyX, todyY))
                gameDisplay.blit(sopa, (sopaX, sopaY))
                

                pixelsXjogador = list(range(jogadorX, jogadorX+largurajogador))
                pixelsYjogador = list(range(jogadorY, jogadorY+alturajogador))

                pixelXbigorna = list(range(posicaobigornaX, posicaobigornaX+largurabigorna))
                pixelYbigorna = list(range(posicaobigornaY, posicaobigornaY+alturabigorna))

                colisaoY = len(list(set(pixelYbigorna) & set(pixelsYjogador) ))
                if colisaoY > 0:
                    colisaoX = len(list(set(pixelXbigorna) & set(pixelsXjogador) ))
                    print(colisaoX)
                    if colisaoX > 23:
                        morreu()
                        jogando=False
                        # pygame.mixer.Sound.play(batida)
                        pygame.mixer.music.stop()                 
                        pygame.mixer.Sound.play(morte)
    ##############################################################################################################################
                pixelXpirulito = list(range(pirulitoX, pirulitoX+larguraPirulito))
                pixelYpirulito = list(range(pirulitoY, pirulitoY+alturaPirulito))

                coletaYP = len(list(set(pixelYpirulito)& set(pixelsYjogador)))
                if coletaYP > 0:
                    coletaXP = len(list(set(pixelXpirulito) & set (pixelsXjogador)))
                    print (coletaXP)
                    if coletaXP >= 30:
                        pontos = pontos + 1
                        pirulitoY = -150
                
                pixelXsopa = list(range(sopaX, sopaX+larguraSopa))
                pixelYsopa = list(range(sopaY, sopaY+alturaSopa))

                coletaYS = len(list(set(pixelYsopa)& set(pixelsYjogador)))
                if coletaYS > 0:
                    coletaXS = len(list(set(pixelXsopa) & set (pixelsXjogador)))
                    print (coletaXS)
                    if coletaXS >= 30:
                        pontos = (pontos + 1)
                        sopaY = -230

                pixelXtody = list(range(todyX, todyX+larguraTody))
                pixelYtody = list(range(todyY, todyY+alturaTody))

                coletaYT = len(list(set(pixelYtody)& set(pixelsYjogador)))
                if coletaYT > 0:
                    coletaXT = len(list(set(pixelXtody) & set (pixelsXjogador)))
                    print (coletaXT)
                    if coletaXT >= 30:
                        pontos = pontos + 1
                        todyY = -180
                            
            escreverTexto("Pontos: "+str(pontos))
    #########################################################################################################################                    
            pygameDisplay.update()
            clock.tick(60)

    jogar()
