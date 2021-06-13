import pygame
import os
import sys
import random
import threading
import discordsdk as sdk
import time

pygame.init()
pygame.font.init()
pygame.mixer.init()

taustakuva = pygame.image.load("bg.png")
ufo = pygame.transform.scale(pygame.image.load("ufo.png"),(100,100))
WIDTH, HEIGHT = 700, 700
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
spawnevent = pygame.USEREVENT + 1
clock = pygame.time.Clock()
pygame.display.set_caption("Testipeli")
miinat = []
app = sdk.Discord(853346441287041134, sdk.CreateFlags.default)
activity_manager = app.get_activity_manager()
osuma = pygame.mixer.Sound("hit.wav")


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
    activity = sdk.Activity()
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
                osuma.play()
                pelaaja1.health = pelaaja1.health - 5
                miinat.remove(miina)
    start = pygame.time.get_ticks()
    pygame.time.set_timer(spawnevent, 500)
    while run:
        #Peli rajoitetu 60fps
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == spawnevent:
                if len(miinat) > 0:
                    miinat.remove(miinat[0])
                randomWitdh = random.randint(0, WIDTH)
                randomHeight = random.randint(0, HEIGHT)
                miina = pygame.Rect(randomWitdh,randomHeight, 50,50)
                miinat.append(miina)
                pygame.time.set_timer(spawnevent, 500)

        txtHealth = font.render("HP: " + str(pelaaja1.health),True, (255,255,255))
        activity.state = "HP: " + str(pelaaja1.health)
        activity_manager.update_activity(activity, callback)
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
        app.run_callbacks()
def callback(result):
    if result != sdk.Result.ok:
        raise Exception(result)

main()