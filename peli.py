import pygame
import os
import sys

taustakuva = pygame.image.load("bg.png")
ufo = pygame.transform.scale(pygame.image.load("ufo.png"),(100,100))
WIDTH, HEIGHT = 700, 700
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption("Testipeli")
ammukset = []

class Pelaaja:
    def __init__(self, x, y, health=100):
        self.x = x
        self.y = y
        self.health = health
    def draw(self):
        #Piirretään ufo koordinaateilla
        WIN.blit(ufo,(self.x,self.y))
def main():
    run = True
    pelaaja1 = Pelaaja(1,1,100)
    def drawbg():
        WIN.blit(taustakuva,(0,0))
    while run:
        #Peli rajoitetu 60fps
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        keys = pygame.key.get_pressed()
        drawbg()
        # Liikkuminen
        if keys[pygame.K_RIGHT] and pelaaja1.x + ufo.get_width() < WIDTH:
            pelaaja1.x = pelaaja1.x + 3
        if keys[pygame.K_LEFT] and pelaaja1.x > 0:
            pelaaja1.x = pelaaja1.x - 3
        if keys[pygame.K_UP] and pelaaja1.y > 0:
            pelaaja1.y = pelaaja1.y - 3
        if keys[pygame.K_DOWN] and pelaaja1.y + ufo.get_height() < HEIGHT:
            pelaaja1.y = pelaaja1.y + 3
        pelaaja1.draw()
        pygame.display.update()


main()