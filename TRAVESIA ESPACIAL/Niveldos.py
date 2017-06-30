import pygame
import random
import sys
from menuP import menuP

from pygame import *
# Definimos algunos colores
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
ROJO = (255, 0, 0)
AZUL     = (   0,   0, 255)
Verde = (50,240,22)
Morado = (100, 0, 200)
Amarillo = (200,200,000)
MARLO = (0, 250, 154)

def lvl2 ():
    class Bloque(pygame.sprite.Sprite):
        """
        Esta clase representa la pelota
        Deriva de la clase "Sprite" en Pygame
        """
        
        def __init__(self):

            super().__init__()
            self.image= pygame.image.load("Imagenes/Juego/villanoInferior.png")
            #self.image = pygame.Surface([20, 15])
            #self.image.fill(Amarillo)

            self.rect = self.image.get_rect()
        def update(self):               # direccion de los bloques
            #self.rect.x +=1
            self.rect.y +=1
            if self.rect.x> largo_pantalla:
                self.rect.x=0
            if self.rect.y>400:
                self.rect.y=0

                
    class Blo(pygame.sprite.Sprite):
       
        
        def __init__(self):
            
            super().__init__()
            self.image= pygame.image.load("Imagenes/Juego/villanoSuperior.png")
            #self.image = pygame.Surface([20, 14])
            #Eself.image.fill(ROJO)

            self.rect = self.image.get_rect()
        def update(self):               # direccion de los bloques
            self.rect.y -=3
            
            
            if self.rect.y==3:
                self.rect.y=480        

    class Jugador(pygame.sprite.Sprite):
        def __init__(self):
            

            # Llama al constructor de la clase padre (Sprite)
            super().__init__()

            self.image = pygame.image.load("Imagenes/Juego/nave.png")

            self.rect = self.image.get_rect()
        def update(self):               #direccion del jugador
                teclas= pygame.key.get_pressed()
                if teclas[K_LEFT]:
                    self.rect.x -= 2
                if teclas[K_RIGHT]:
                    self.rect.x +=2
                if teclas[K_UP]:
                    self.rect.y -=2
                if teclas[K_DOWN]:
                    self.rect.y +=2

                if self.rect.x== 0:
                    self.rect.x= 420
                if self.rect.x == 490:
                  self.rect.x = 20

                if self.rect.y== -50:
                    self.rect.y= 480
                if self.rect.y == 510:
                  self.rect.y = 10

    class Proyectil(pygame.sprite.Sprite):
        """ Esta clase representa al proyectil . """
        def __init__(self):
            #  Llama al constructor de la clase padre (Sprite)
            super().__init__()

            self.image = pygame.Surface([4, 10])
            self.image.fill(MARLO)

            self.rect = self.image.get_rect()

        def update(self):
            """ Desplaza al proyectil. """
            self.rect.y -= 3
            
    class Muerte(pygame.sprite.Sprite):                                  ###################
        """ Esta clase representa al proyectil . """
        def __init__(self):
            #  Llama al constructor de la clase padre (Sprite)
            super().__init__()

            self.image = pygame.Surface([4, 10])
            self.image.fill(ROJO)

            self.rect = self.image.get_rect()

        def update(self):
            """ Desplaza al proyectil. """
            self.rect.y += 1
            
    class Balavil(pygame.sprite.Sprite):
        """ Esta clase representa al proyectil . """
        def __init__(self):
            #  Llama al constructor de la clase padre (Sprite)
            super().__init__()

            self.image = pygame.Surface([4, 10])
            self.image.fill(AZUL)

            self.rect = self.image.get_rect()

        def update(self):
            """ Desplaza al proyectil. """
            self.rect.x -= 3



    # Iniciamos Pygame
    pygame.init()

    # Establecemos las dimensiones de la pantalla
    largo_pantalla = 640
    alto_pantalla = 480
    pantalla = pygame.display.set_mode([largo_pantalla, alto_pantalla])

    fondo= pygame.image.load("Imagenes/Juego/fondolvl2.jpg").convert()

    # --- Lista de sprites

    # Esta es una lista de cada sprite, así como de todos los bloques y del protagonista.
    lista_de_todos_los_sprites = pygame.sprite.Group()

    # Lista de cada bloque en el juego
    lista_bloques = pygame.sprite.Group()
    lista= pygame.sprite.Group()                        ##########
    # Lista de cada proyectil
    lista_proyectiles = pygame.sprite.Group()

     # LISTA DEL PROYECTIL DEL VILLANO
    lista_proyevil= pygame.sprite.Group()

    
    # --- Creamos los sprites

    for i in range(20):
        # Esto representa un bloque
        bloque = Bloque()

        # Configuramos una ubicación aleatoria para el bloque
        bloque.rect.x = random.randrange(450)
        bloque.rect.y = random.randrange(350)

        # Añadimos el bloque a la lista de objetos
        lista_bloques.add(bloque)

        lista_de_todos_los_sprites.add(bloque)

    # Creamos un bloque protagonista ROJO
    protagonista = Jugador()
    lista.add(protagonista)
    lista_de_todos_los_sprites.add(protagonista)
    villano = Blo()
    lista_de_todos_los_sprites.add(villano)
    
    villano.rect.y = 450
    villano.rect.x = 600
    # Iteramos hasta que el usuario presione el botón de salir.
    hecho = False

    # Para controlar la tasa de refresco de la pantalla
    reloj = pygame.time.Clock()

    puntuacion = 0
    vidas=3
    protagonista.rect.y = 370
    protagonista.rect.x= 300


    fuente = pygame.font.Font(None, 30)                             ######

    print(i)



    while not hecho:
        # --- Procesamiento de Eventos
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                hecho = True

            elif evento.type == pygame.KEYDOWN:  # OJO DISPARO
                if evento.key == K_SPACE:
                    bala = Proyectil()
                    bala.rect.x= protagonista.rect.x
                    bala.rect.y= protagonista.rect.y
                    lista_de_todos_los_sprites.add(bala)
                    lista_proyectiles.add(bala)

        lista_de_todos_los_sprites.update()

        if puntuacion == 10 or puntuacion == 17:
            balas = Muerte()
            balas.rect.x= bloque.rect.x
            balas.rect.y= bloque.rect.y
            lista_de_todos_los_sprites.add(balas)
            lista_proyevil.add(balas)
            
            if balas.rect.y > 450:
                lista_proyevil.remove(balas)
                lista_de_todos_los_sprites.remove(balas)
    
            
        pro= Balavil()
        villano.rect.y
        pro.rect.x = villano.rect.x
        pro.rect.y = villano.rect.y
        superior=False
        vlVillano=1
        if superior==True:
            pro.rect.y=380
            superior=False
        else:
            pro.rect.y -=vlVillano
            if pro.rect.y ==0:
                superior=True
        
        locY=pro.rect.y
        
        if locY%34==0:                  ## Disparo del villano
            lista_de_todos_los_sprites.add(pro)
        lista_proyevil.add(pro)
        
        texto1 = fuente.render("Puntaje: "+ str(puntuacion), 0, (255, 255, 255))   ###
        
        texto2= fuente.render("Vidas: "+str(vidas), 0, (255, 255, 255)) 

        for proyectil in lista_proyectiles:

           
            lista_bloques_alcanzados = pygame.sprite.spritecollide(proyectil,lista_bloques, True)
            

            for bloque in lista_bloques_alcanzados:
                lista_proyectiles.remove(proyectil)
                lista_de_todos_los_sprites.remove(proyectil)
                puntuacion += 1 
                i = i-1
              #  print( puntuacion )


            

            # Eliminamos el proyectil si vuela fuera de la pantalla
            if proyectil.rect.y < -10:
                lista_proyectiles.remove(proyectil)
                lista_de_todos_los_sprites.remove(proyectil)

        for proyevil in lista_proyevil:                     ##DISPARO MORTAL
            lista_impacto = pygame.sprite.spritecollide(proyevil, lista, True)
            
            for pro in lista_impacto:
                lista_proyevil.remove(pro)
                lista_de_todos_los_sprites.remove(pro)
                vidas -= 1
                if vidas==0:
                    return 0
                   
                protagonista = Jugador()
                lista.add(protagonista)
                lista_de_todos_los_sprites.add(protagonista)
                protagonista.rect.y = 370
                protagonista.rect.x= 300
                
               
        pantalla.blit(fondo, (0, 0))
        # Dibujamos todos los sprites
        lista_de_todos_los_sprites.draw(pantalla)
        pantalla.blit(texto1, (100,400))      #####
        pantalla.blit(texto2, (400,400)) 

        
        # Avanzamos y actualizamos la pantalla con todo lo que hemos dibujado.
        pygame.display.flip()

        reloj.tick(60)

        if puntuacion==20:
            return 1

    pygame.quit()



    
