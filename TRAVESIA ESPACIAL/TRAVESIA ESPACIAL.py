import pygame,sys
import random
from pygame.locals import *
from Niveluno import lvl1
from Niveldos import lvl2
from Niveltres import lvl3
from menuP import *


def menuPrincipal ():
        #Definimos colores
    Azul=(0,0,250)
    AzulClaro=(0,0,150)
    Rojo=(250,0,0)
    RojoClaro=(150,0,0)
    Negro=(0,0,0)
    BLANCO = (255, 255, 255)
    verde=(0,255,0)
    verdeClaro=(0,150,0)

    

    def textoObjetos (texto, fuente,color):
        textSurface = fuente.render(texto,True,color)
        return textSurface,textSurface.get_rect()


    pygame.init()
    ventana= pygame.display.set_mode((640,480))
    pygame.display.set_caption("Menu")
    fondo= pygame.image.load("Imagenes/Juego/fondoMenu.jpg").convert()

    imagNave=pygame.image.load("Imagenes/Juego/nave.png")

    posX=265
    posY=400
    velocidadY=1
    velocidadX=100
    superior=False
    derecha=False
    while True:
        ventana.blit(fondo, (0, 0))
        ventana.blit(imagNave,(posX,posY))
        
        fuente= pygame.font.Font(None,60)
        textSurfT, textRectT= textoObjetos("TRAVESIA ESPACIAL",fuente, BLANCO)
        textRectT.center=(350,150)
        ventana.blit(textSurfT,textRectT)

        if superior==True:
            posY=480
            if posX>500:
                posX=0
            else:
                posX+=velocidadX

            superior=False
        else:
            posY-=velocidadY
            if posY==-70:
                superior=True
                
            
        mouse1=pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        #Boton jugar
        if (150+100>mouse1[0]>150 and 250+50>mouse1[1]>250):
            pygame.draw.rect(ventana,AzulClaro,(150,250,100,50))
            if  click [0]==1:
                ## Empieza Nivel 1
                confirmacion=lvl1()

                    ### Si pierde 
                if confirmacion==0:
                    reinicio=menuP()
                    if reinicio==0:
                        menuPrincipal()

                ## Empieza Nivel 2
                confirmacion2=0
                if confirmacion==1:
                    confirmacion2=lvl2()

                    ### Si pierde
                if confirmacion2==0:
                    reinicio=menuP()
                    if reinicio==0:
                        menuPrincipal()

                ## Empieza Nivel 3
                confirmacion3=0
                if confirmacion2==1:
                    confirmacion3=lvl3()

                    ## Si pierde
                if confirmacion3==0:
                    reinicio=menuP()
                    if reinicio==0:
                        menuPrincipal

                ## Si completa los 3 niveles
                if confirmacion3==1:
                    reinicioVictoria=menuG()
                    if reinicioVictoria==0:
                        menuPrincipal()

                pygame.quit()
                sys.exit()
        else:
            pygame.draw.rect(ventana,Azul,(150,250,100,50))

        fuente2= pygame.font.Font(None,20)
        textSurf, textRect= textoObjetos("Jugar",fuente2,Negro)
        textRect.center=((150+(100/2)),(250+(50/2)))
        ventana.blit(textSurf,textRect)

        #Boton salir    
        if (350+100> mouse1[0]> 350 and 250+50> mouse1[1]>250):
            pygame.draw.rect(ventana,RojoClaro,(350,250,100,50))
            if  click [0]==1:
                pygame.quit()
                sys.exit()
        else:
            pygame.draw.rect(ventana,Rojo,(350,250,100,50))

        textSurf2, textRect2= textoObjetos("Salir!",fuente2,Negro)
        textRect2.center=((350+(100/2)),(250+(50/2)))
        ventana.blit(textSurf2,textRect2)

        #Boton Instrucciones 
        if (250+100> mouse1[0]> 250 and 350+30> mouse1[1]>350):
            pygame.draw.rect(ventana,verdeClaro,(250,350,100,30))
            if  click [0]==1:
                confirmacion=pantallaInstrucciones () ()
                if confirmacion==0:
                    menuPrincipal()
                pygame.quit()
                sys.exit()
        else:
            pygame.draw.rect(ventana,verde,(250,350,100,30))

        textSurf2, textRect2= textoObjetos("Instrucciones",fuente2,Negro)
        textRect2.center=((250+(100/2)),(350+(30/2)))
        ventana.blit(textSurf2,textRect2)

        #Boton Desarrolladores
        if (250+100> mouse1[0]> 250 and 400+30> mouse1[1]>400):
            pygame.draw.rect(ventana,verdeClaro,(250,400,100,30))
            if  click [0]==1:
                confirmacion=pantallaDesarrolladores()
                if confirmacion==0:
                    menuPrincipal()
                pygame.quit()
                sys.exit()
        else:
            pygame.draw.rect(ventana,verde,(250,400,100,30))

        textSurf2, textRect2= textoObjetos("Desarrolladores",fuente2,Negro)
        textRect2.center=((250+(100/2)),(400+(30/2)))
        ventana.blit(textSurf2,textRect2)
       
       

        for evento in pygame.event.get():
            if evento.type== QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update();

menuPrincipal ()


