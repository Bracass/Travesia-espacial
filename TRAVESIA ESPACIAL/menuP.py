import pygame,time
import random
import sys
from pygame.locals import *

# Definimos algunos colores
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
ROJO = (255, 0, 0)
AZUl = (0, 0, 255)
#Definimos mas colores
Azul=(0,0,250)
AzulClaro=(0,0,150)
Rojo=(250,0,0)
RojoClaro=(150,0,0)
Negro=(0,0,0)


def menuP ():
    
    def textoObjetos (texto, fuente,color):
        textSurface = fuente.render(texto,True,color)
        return textSurface,textSurface.get_rect()

    pygame.init()
    ventana= pygame.display.set_mode((640,480))
    pygame.display.set_caption("Juego Terminado")
    fondo= pygame.image.load("Imagenes/Juego/fondoMenu.jpg").convert()
    explosion= pygame.image.load("Imagenes/Juego/explosion.png")
    nave2= pygame.image.load("Imagenes/Juego/nave2.png")
    cont=0
    while True:
        ventana.blit(fondo, (0, 0))
        ventana.blit(nave2, (240, 230))
        if cont%7==0:
            ventana.blit(explosion, (250, 245))
            ventana.blit(explosion, (320, 280))
        if cont%5==0:
            ventana.blit(explosion, (270, 310))
        
        cont+=2
    
        fuente= pygame.font.Font(None,80)
        textSurfT, textRectT= textoObjetos("GAME OVER",fuente, BLANCO)
        textRectT.center=(320,150)
        ventana.blit(textSurfT,textRectT)

        mouse1=pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        #Boton regresar al menu
        if (5300+100>mouse1[0]>530 and 420+50>mouse1[1]>420):
            pygame.draw.rect(ventana,RojoClaro,(530,420,100,50))
            if  click [0]==1:
                return 0
        else:
            pygame.draw.rect(ventana,Rojo,(530,420,100,50))

        fuente2= pygame.font.Font(None,20)
        textSurf, textRect= textoObjetos("Regresar",fuente2,Negro)
        textRect.center=((530+(100/2)),(420+(50/2)))
        ventana.blit(textSurf,textRect)
        for evento in pygame.event.get():
            if evento.type==QUIT:
                pygame.quit()
                sys.exit()

        
        pygame.display.update();

def menuG ():
    
    def textoObjetos (texto, fuente,color):
        textSurface = fuente.render(texto,True,color)
        return textSurface,textSurface.get_rect()

    pygame.init()
    ventana= pygame.display.set_mode((640,480))
    pygame.display.set_caption("Felicidad, juego completado")
    fondo= pygame.image.load("Imagenes/Juego/fondoMenu.jpg").convert()
    explosion= pygame.image.load("Imagenes/Juego/explosion.png")
    ##remplazar por enemigo
    nave2= pygame.image.load("Imagenes/Juego/villanoG.png")
    cont=0
    while True:
        ventana.blit(fondo, (0, 0))
        ventana.blit(nave2, (240, 230))
        if cont%7==0:
            ventana.blit(explosion, (250, 245))
            ventana.blit(explosion, (320, 280))
        if cont%5==0:
            ventana.blit(explosion, (270, 310))
        
        cont+=2
    
        fuente= pygame.font.Font(None,50)
        textSurfT, textRectT= textoObjetos("FELICIDADES JUEGO COMPLETADO",fuente, BLANCO)
        textRectT.center=(320,150)
        ventana.blit(textSurfT,textRectT)

        mouse1=pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        #Boton regresar al menu
        if (5300+100>mouse1[0]>530 and 420+50>mouse1[1]>420):
            pygame.draw.rect(ventana,RojoClaro,(530,420,100,50))
            if  click [0]==1:
                return 0
        else:
            pygame.draw.rect(ventana,Rojo,(530,420,100,50))

        fuente2= pygame.font.Font(None,20)
        textSurf, textRect= textoObjetos("Regresar",fuente2,Negro)
        textRect.center=((530+(100/2)),(420+(50/2)))
        ventana.blit(textSurf,textRect)
        for evento in pygame.event.get():
            if evento.type==QUIT:
                pygame.quit()
                sys.exit()

        
        pygame.display.update();

def pantallaInstrucciones ():
    
    def textoObjetos (texto, fuente,color):
        textSurface = fuente.render(texto,True,color)
        return textSurface,textSurface.get_rect()

    pygame.init()
    ventana= pygame.display.set_mode((640,480))
    pygame.display.set_caption("Instrucciones")
    fondo= pygame.image.load("Imagenes/Juego/fondoMenu.jpg").convert()
    
    tecladoEsp=pygame.image.load("Imagenes/Instrucciones/barra.png")
    disparo=pygame.image.load("Imagenes/Instrucciones/Disparo.png")
    tecladoFlechas=pygame.image.load("Imagenes/Instrucciones/Flechas.png")
    nave=pygame.image.load("Imagenes/Instrucciones/nave.png")

    while True:
        ventana.blit(fondo, (0, 0))
        ventana.blit(tecladoEsp, (10, 300))
        ventana.blit(disparo, (180, 300))
        ventana.blit(tecladoFlechas, (10, 150,))
        ventana.blit(nave, (200, 150,))
         
        fuente= pygame.font.Font(None,80)
        textSurfT, textRectT= textoObjetos("INSTRUCCIONES",fuente, BLANCO)
        textRectT.center=(320,80)
        ventana.blit(textSurfT,textRectT)

        fuente2= pygame.font.Font(None,20)
        textSurfT, textRectT= textoObjetos("MOVIMIENTO, EVADE LOS DISPAROS ENEMIGOS",fuente2, Negro)
        textRectT.center=(450,150)
        ventana.blit(textSurfT,textRectT)

        textSurfT, textRectT= textoObjetos("DISPARO, ELIMINA A LOS ENEMIGOS",fuente2, Negro)
        textRectT.center=(470,300)
        ventana.blit(textSurfT,textRectT)

        mouse1=pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        #Boton regresar al menu
        if (5300+100>mouse1[0]>530 and 420+50>mouse1[1]>420):
            pygame.draw.rect(ventana,RojoClaro,(530,420,100,50))
            if  click [0]==1:
                return 0
        else:
            pygame.draw.rect(ventana,Rojo,(530,420,100,50))

        fuente2= pygame.font.Font(None,20)
        textSurf, textRect= textoObjetos("Regresar",fuente2,Negro)
        textRect.center=((530+(100/2)),(420+(50/2)))
        ventana.blit(textSurf,textRect)
        for evento in pygame.event.get():
            if evento.type==QUIT:
                pygame.quit()
                sys.exit()


        pygame.display.update();

def pantallaDesarrolladores ():
    
    def textoObjetos (texto, fuente,color):
        textSurface = fuente.render(texto,True,color)
        return textSurface,textSurface.get_rect()

    pygame.init()
    ventana= pygame.display.set_mode((640,480))
    pygame.display.set_caption("Desarrolladores")
    fondo= pygame.image.load("Imagenes/Juego/fondoMenu.jpg").convert()

    imagEscu=pygame.image.load("Imagenes/Desarrolladores/LogoU.png")
    imagGrupo=pygame.image.load("Imagenes/Desarrolladores/LPygroup.png")
    nombres=pygame.image.load("Imagenes/Desarrolladores/nombres.png")
    while True:
        ventana.blit(fondo, (0, 0))
        ventana.blit(imagEscu,(324,10))
        ventana.blit(imagGrupo,(50,70))
        ventana.blit(nombres,(10,350))
        
        fuente= pygame.font.Font(None,50)
        textSurfT, textRectT= textoObjetos("DESARROLLADORES",fuente, BLANCO)
        textRectT.center=(310,330)
        ventana.blit(textSurfT,textRectT)

        mouse1=pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        #Boton regresar al menu
        if (5300+100>mouse1[0]>530 and 420+50>mouse1[1]>420):
            pygame.draw.rect(ventana,RojoClaro,(530,420,100,50))
            if  click [0]==1:
                return 0
        else:
            pygame.draw.rect(ventana,Rojo,(530,420,100,50))

        fuente2= pygame.font.Font(None,20)
        textSurf, textRect= textoObjetos("Regresar",fuente2,Negro)
        textRect.center=((530+(100/2)),(420+(50/2)))
        ventana.blit(textSurf,textRect)
        for evento in pygame.event.get():
            if evento.type==QUIT:
                pygame.quit()
                sys.exit()


        pygame.display.update();


