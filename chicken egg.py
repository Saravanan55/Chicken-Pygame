import pygame
import time
import random


pygame.init()


screenwidth = 960
screenheigth = 640
screen = pygame.display.set_mode((screenwidth,screenheigth))


white = (255,255,255)
black = (0,0,0)
gold = (255,215,0)
green = (0,255,0)

chickenwidth = 50
chickenheigth = 100
chicken = pygame.image.load("chicken.jpg")
chicken = pygame.transform.scale(chicken, (chickenwidth, chickenheigth))


eggwidth = 50
eggheigth = 50
egg = pygame.image.load("egg.jpg")
egg = pygame.transform.scale(egg, (eggwidth, eggheigth))


egg2width = 50
egg2heigth = 50
egg2 = pygame.image.load("egg.jpg")
egg2 = pygame.transform.scale(egg2, (egg2width, egg2heigth))

pygame.display.set_caption("Chicken Vs Egg")


clock = pygame.time.Clock()



def chickenplace(chickenx, chickeny):
    screen.blit(chicken, (chickenx, chickeny))


def eggplace(eggx, eggy):
    screen.blit(egg, (eggx, eggy))

def egg2place(egg2x, egg2y):
    screen.blit(egg2, (egg2x, egg2y))



def gameloop():

    
    time.sleep(2)

    dead = False

    
    eggcounter = 0


    chickenx = (screenwidth * 0.5)
    chickeny = (screenheigth * 0.8)
    chickenxchange = 0


    eggx = random.randint(0,910)
    eggy = -200
    eggspeed = 7

    
    egg2x = random.randint(0,910)
    egg2y = -200
    egg2speed = 14

    while not dead:

        for event in pygame.event.get():

            
            if event.type == pygame.QUIT:
                dead = True

            
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_LEFT:
                    chickenxchange = -10
                elif event.key == pygame.K_RIGHT:
                    chickenxchange = 10
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    chickenxchange = 0

        
        chickenx += chickenxchange
        eggy += eggspeed

        
        screen.fill(white)

        
        chickenplace(chickenx, chickeny)
        eggplace(eggx, eggy)
        egg2place(egg2x, egg2y)

        
        if chickenx > screenwidth - chickenwidth:
            chickenx = screenwidth - chickenwidth
            chickenplace(chickenx, chickeny)
        if chickenx < 0:
            chickenx = 0
            chickenplace(chickenx, chickeny)

        
        if eggy > screenheigth:
                 eggy = -200
                 eggx = random.randint(0,910)

        
        if egg2y > screenheigth:
            egg2y = -200
            egg2x = random.randint(0,910)

        
        if eggy == chickeny + 2:
            if eggx > chickenx + 50 or eggx < chickenx - 50:
                eggcounter += 1
            else:
                eggcounter = 0
                time.sleep(2)
                gameloop()

        
        if egg2y == chickeny + 2:
            if egg2x > chickenx + 50 or egg2x < chickenx - 50:
                eggcounter = eggcounter
            else:
                eggcounter = 0
                time.sleep(2)
                gameloop()

        
        countertext = pygame.font.SysFont(None, 40)
        counterlabel = countertext.render("Counter:" + str(eggcounter), True, black)
        screen.blit(counterlabel, (20, 20))

        lvltxt = pygame.font.SysFont(None,40)
        
        
        if eggcounter < 5:
            eggspeed = 7
            lvllable = lvltxt.render("Level:1",True,gold)
            screen.blit(lvllable,(40,40))
        else:
            lvllable = lvltxt.render("Level:",True,gold)
            screen.blit(lvllable,(40,40))
        if eggcounter >=5 :
            eggspeed = 14
            lvllable = lvltxt.render("Level:2",True,gold)
            screen.blit(lvllable,(40,40))
        else:
            lvllable = lvltxt.render("Level:",True,gold)
            screen.blit(lvllable,(40,40))
        if eggcounter > 15:
            egg2y += egg2speed
            egg2place(egg2x, egg2y)
            lvllable = lvltxt.render("Level:3",True,gold)
            screen.blit(lvllable,(40,40))
        if eggcounter == 30:
            wintext = pygame.font.SysFont(None, 60)
            winlabel = wintext.render("You won!", True, green)
            screen.blit(winlabel, (200, 200))
            time.sleep(1)
            dead = True


        pygame.display.update()
        clock.tick(60)


gameloop()
pygame.quit()
quit()