
import pygame
import os
pygame.init()

FPS = 60

window_width = 600
window_height = 400

wnd = pygame.display.set_mode((window_width, window_height ))

clock = pygame.time.Clock()
pygame.display.update()

white = (255, 255, 255)
red   = (255, 0,   0)
green = (0,   255, 0)
blue  = (0,   0,   255)
black = (0,   0,   0)

enemy_images = [ pygame.image.load( './enemy/'  'enemy' + str(x) + '.png') for x in range(17)

 
  ]

hero_images = [ pygame.image.load( './hero/' 'hero' + str(x) + '.png') for x in range(13)
   
]

def get_size(image, width):
    image_size = image.get_rect().size
    return (width, int(image_size[1] * width / image_size[0]))


def resize_image(image):
    image_size = get_size(image, 100)
    return pygame.transform.scale(image, image_size)

hero_images = list(map(resize_image, hero_images))
enemy_images = list(map(resize_image, enemy_images))

class Base():
	def __init__(self, x, y, images):
		self.x = x
		self.y = y
		self.images = images

	def draw(self, frame):
		wnd.blit(self.images[frame], (self.x, self.y))

class Hero(Base):
    def __init__(self):
    	super().__init__(50,int(window_height / 2),hero_images)
      
    def move(self, x, y):
        self.x += x
        self.y += y
     
class  Enemy (Base):
	def __init__(self):
		super().__init__(
			int (window_width + 0.8),
			int (window_height / 2),
			enemy_images)
		

hero = Hero()

enemy = Enemy()

x = window_width /2
y = window_height /2



s = 3
s_x = 0
s_y = 0

hero_tick = 100
enemy_tick = 70
hero_frame = 0
enemy_frame = 0

while True:

    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                s_x += s
            elif event.key == pygame.K_a:
                s_x -= s
            elif event.key == pygame.K_w:
                s_y -= s
            elif event.key == pygame.K_s:
                s_y += s

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                s_x -= s
            elif event.key == pygame.K_a:
                s_x += s
            elif event.key == pygame.K_w:
                s_y += s
            elif event.key == pygame.K_s:
                s_y -= s


        if pygame.time.get_ticks() > hero_tick:
            if s_x > 0:
                hero_tick += 70
            elif s_x < 0:
                hero_tick += 100
            else:
                hero_tick += 85

        

        hero_frame = (hero_frame + 1) % 13

        if pygame.time.get_ticks() > enemy_tick:
            enemy_tick += 25

        enemy_frame = (enemy_frame + 1) % 17
		

    wnd.fill(green)
    hero.move(s_x,s_y)
    hero.draw(hero_frame)
    enemy.draw(enemy_frame)



    pygame.display.update()