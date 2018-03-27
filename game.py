import pygame
import random

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
        self.speed = 2

    def update(self):
        self.x += self.speed_x
        self.y += self.speed_y

class Monster(Character):
    def __init__(self):
        super(Monster, self).__init__()
        self.image = pygame.image.load('images/monster.png')
        self.x = 240
        self.y = 224
        self.speed = 2
        

def main():
    width = 800
    height = 600
    blue_color = (97, 159, 182)

    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('My Game')
    clock = pygame.time.Clock()
    hero_img = pygame.image.load('images/hero.png')
    
    monster_img = pygame.image.load('images/monster.png')
    background_image = pygame.image.load('images/background.png')
    background_image = pygame.transform.scale(background_image,(800,600))
    music = pygame.mixer.music.load("sounds/music.wav")
    pygame.mixer.music.play(1, 0.0)
    hero = Hero()
    
    monster = Monster()
    

    # Game initialization

    stop_game = False
    while not stop_game:
        for event in pygame.event.get():

            # Event handling

            if event.type == pygame.QUIT:
                stop_game = True


        # Game logic

        # Draw background
        screen.blit(background_image, [0,0])
        

        # Game display
        hero.draw(screen)        
        monster.draw(screen)       
        pygame.display.update()
        
        clock.tick(60)

    pygame.quit()

if __name__ == '__main__':
    main()
