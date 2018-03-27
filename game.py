import pygame

class Hero(object):
    def __init__(self, screen, img):

        self.image = img
        self.x = 100
        self.y = 100
        self.speed = 10
        self.screen = screen
    def render(self):
        self.screen.blit(self.image, [self.x, self.y])
class Goblin(object):
    def __init__(self, screen, img):
        self.image = img
        self.x = 300
        self.y = 300
        self.speed = 9
        self.screen = screen
    def render(self):
        self.screen.blit(self.image, [self.x, self.y])
    
class Monster(object):
    def __init__(self, screen, img):
        self.image = img
        self.x = 200
        self.y = 200
        self.speed = 9
        self.screen = screen
    def render(self):
        self.screen.blit(self.image, [self.x,self.y])

def main():
    width = 800
    height = 600
    blue_color = (97, 159, 182)

    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('My Game')
    clock = pygame.time.Clock()
    hero_img = pygame.image.load('images/hero.png')
    goblin_img = pygame.image.load('images/goblin.png')
    monster_img = pygame.image.load('images/monster.png')
    background_image = pygame.image.load('images/background.png')
    background_image = pygame.transform.scale(background_image,(800,600))
    music = pygame.mixer.music.load("sounds/music.wav")
    pygame.mixer.music.play(1, 0.0)
    hero = Hero(screen, hero_img)
    goblin = Goblin(screen, goblin_img)
    monster = Monster(screen, monster_img)
    

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
        hero.render()
        goblin.render()
        monster.render()
           
        
        pygame.display.update()
        clock.tick(60)

    pygame.quit()

if __name__ == '__main__':
    main()
