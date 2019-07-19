import pygame
from pygame.locals import *
from widgets import Block


def setup_background():

    pic_width, pic_height = pic.get_width(), pic.get_height()
    w, h = screen.get_size()
    y = 0
    x = 0
    print(str(w) +" "+ str(h))
    while (x <= w+1):
        while (y <= h+1):

            # print(x,y)
            screen.blit(pic, (x, y))
            y = y + pic_height
        y = 0
        x = x + pic_width
    pygame.display.flip()


pygame.init()
screen = pygame.display.set_mode((750, 500), RESIZABLE)
pic=pygame.image.load("dark_wood_seamless.jpg")

setup_background()

all_sprites_list = pygame.sprite.Group()

box = Block(Color(0,0,200), 100,100)
all_sprites_list.add(box)
all_sprites_list.draw(screen)

#screen.blit(box, (0,0))


done = False

while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
                if event.type == pygame.VIDEORESIZE:
                    #resize the screen canvas
                    screen=pygame.display.set_mode(event.dict['size'],RESIZABLE)
                    #redraw images
                    setup_background()

        all_sprites_list.update()
        all_sprites_list.draw(screen)


        pygame.display.flip()