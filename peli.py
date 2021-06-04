import pygame
import os
import sys
import random
import threading

pygame.font.init()
taustakuva = pygame.image.load("bg.png")
ufo = pygame.transform.scale(pygame.image.load("ufo.png"),(100,100))
WIDTH, HEIGHT = 700, 700
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption("Testipeli")
miinat = []


class Pelaaja:
    def __init__(self, x, y, health=100):
        self.x = x
        self.y = y
        self.health = health
    def draw(self):
        #Piirretään ufo koordinaateilla
        WIN.blit(ufo,(self.x,self.y))
class Miina:
    def __init__(self, x, y):
        self.x = x
        self.y = y
def main():
    run = True
    pelaaja1 = Pelaaja(1,1,100)
    font = pygame.font.SysFont("comicsans",30)
    txtHealth = font.render("HP: " + str(pelaaja1.health),True, (255,255,255))
    def draw(txthp):
        WIN.blit(taustakuva,(0,0))
        pelaaja1.draw()
        WIN.blit(txthp,(10,10))
        for miina in miinat:
            pygame.draw.rect(WIN,(255,0,0),miina)
    def handle(pelaaja):
        for miina in miinat:
            if pelaaja.colliderect(miina):                                                               
                pelaaja1.health = pelaaja1.health - 5
                miinat.remove(miina)
                print(pelaaja1.health)
    def uusimiina():
            miina = pygame.Rect(randomWitdh,randomHeight, 50,50)
            miinat.append(miina)
    while run:
        #Peli rajoitetu 60fps
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        randomWitdh = random.randint(50, WIDTH - 50)
        randomHeight = random.randint(50, HEIGHT - 50)
        txtHealth = font.render("HP: " + str(pelaaja1.health),True, (255,255,255))
        if run and len(miinat) == 0:
            lisays = threading.Thread(target=uusimiina())
            lisays.start()
            
        pelaajarect = pygame.Rect(pelaaja1.x,pelaaja1.y, ufo.get_width(),ufo.get_height())
        handle(pelaajarect)
        draw(txtHealth)

        if pelaaja1.health <= 0:
            run = False
        keys = pygame.key.get_pressed()
        # Liikkuminen
        if keys[pygame.K_RIGHT] and pelaaja1.x + ufo.get_width() < WIDTH:
            pelaaja1.x = pelaaja1.x + 3
        if keys[pygame.K_LEFT] and pelaaja1.x > 0:
            pelaaja1.x = pelaaja1.x - 3
        if keys[pygame.K_UP] and pelaaja1.y > 0:
            pelaaja1.y = pelaaja1.y - 3
        if keys[pygame.K_DOWN] and pelaaja1.y + ufo.get_height() < HEIGHT:
            pelaaja1.y = pelaaja1.y + 3
        pygame.display.update()


main()