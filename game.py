import pygame, sys
from pygame.locals import *
import random
import time


class Character(object):
    def __init__(self):
        self.speed_x = 0
        self.speed_y = 0
    
    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

class Hero(Character):
    def __init__(self):
        super(Hero, self).__init__()
        self.image = pygame.image.load('images/hero.png')
        self.x = 240
        self.y = 224
        self.base_speed = 4

    def update(self):
        self.x += self.speed_x
        self.y += self.speed_y

class Monster(Character):
    def __init__(self):
        super(Monster, self).__init__()
        self.image = pygame.image.load('images/monster.png')
        self.x = 53
        self.y = 50
        self.base_speed = 2
        

def main():
    size = width, height = 512, 480   
    pygame.init()
    screen = pygame.display.set_mode(size)
    background_image = pygame.image.load('images/background.png').convert_alpha()
    pygame.display.set_caption('Monster Catch!')
    clock = pygame.time.Clock()
    win_sound = pygame.mixer.Sound('sounds/win.wav')
          
    # Music
    pygame.mixer.music.load('sounds/music.wav')
    pygame.mixer.music.play(-1)

    # Game initialization
    hero = Hero()    
    monster = Monster()
    stop_game = False
    timer_count = 119
    
    # When hero and monster collide
    def collide():
        # print "You caught the monster!"
        screen.blit(background_image, (0, 0))
        hero.draw(screen)
        pygame.mixer.Sound.play(win_sound)
        # pygame.mixer.music.stop()
        sys_font = pygame.font.SysFont('none', 40)
        rendered = sys_font.render('You caught the monster!',0,(80,200,80))
        screen.blit(rendered, (30,100))
        pygame.display.update()

    while not stop_game:
        for event in pygame.event.get():
            
            # Event handling

            if event.type == pygame.QUIT:
                stop_game = True

            # If no keys are pressed no movement by hero
            if event.type == pygame.KEYUP:

                if event.key == pygame.K_DOWN: #274
                    hero.speed_y = 0                
                elif event.key == pygame.K_UP: #273
                    hero.speed_y = 0                
                elif event.key == pygame.K_LEFT: #276
                    hero.speed_x = 0                
                elif event.key == pygame.K_RIGHT: #275
                    hero.speed_x = 0

            #Key held down moves hero
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_DOWN:
                    hero.speed_y = hero.base_speed
                elif event.key == pygame.K_UP:
                    hero.speed_y = -hero.base_speed
                elif event.key == pygame.K_LEFT:
                    hero.speed_x = -hero.base_speed
                elif event.key == pygame.K_RIGHT:
                    hero.speed_x = hero.base_speed

        # Boundary warping 
        if monster.x > 472:
            monster.x = 20
        if monster.x < 20:
            monster.x = 472
        if monster.y > 450:
            monster.y = 20
        if monster.y < 20:
            monster.y = 450
        
        if hero.x > 472:
            hero.x = 20
        if hero.x < 20:
            hero.x = 472
        if hero.y > 450:
            hero.y = 20
        if hero.y < 20:
            hero.y = 450
            
        # Update position of hero every loop
        hero.update()

        # Draw background
        screen.blit(background_image, [0,0])
        

        # Game display
        hero.draw(screen)        
        monster.draw(screen)       
        pygame.display.update()
        clock.tick(60)

        #Movement of monster
        clock.tick(60)
        timer_count = timer_count + 1
        monster.x += monster.speed_x
        monster.y += monster.speed_y

        #Changes monster direction randomly every 2 secs
        if timer_count >= 120:
            timer_count = 0
            random_direction = random.randint(0, 7)

            if random_direction == 0:
                monster.speed_x = -monster.base_speed
                monster.speed_y = 0

            elif random_direction == 1:
                monster.speed_x = monster.base_speed
                monster.speed_y = 0
            elif random_direction == 2:
                monster.speed_x = monster.base_speed
                monster.speed_y = 0
            elif random_direction == 3:
                monster.speed_x = monster.base_speed
                monster.speed_y = 0
            elif random_direction == 4:
                monster.speed_y = monster.base_speed
                monster.speed_x = monster.base_speed
            elif random_direction == 5:
                monster.speed_y = -monster.base_speed
                monster.speed_x = monster.base_speed
            elif random_direction == 6:
                monster.speed_y = -monster.base_speed
                monster.speed_x = monster.base_speed
            elif random_direction == 7:
                monster.speed_y = -monster.base_speed
                monster.speed_x = -monster.base_speed
            
        # Hero collision
        if hero.x + 20 < monster.x:
            pass
        elif monster.x + 20 < hero.x:
            pass
        elif hero.y + 20 < monster.y:
            pass
        elif monster.y + 20 < hero.y:
            pass
        else:
            collide()


    pygame.quit()

if __name__ == '__main__':
    main()
