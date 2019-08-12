import pygame
from pygame.locals import *
from widgets import *


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


def button_feedback(self, event, clock):
    print("button pressed")

def sprite_handle():
    for sprite in all_sprites_list:
        if hasattr(event, "pos"):
            focussed = sprite.rect.collidepoint(event.pos)
            if (focussed or sprite.focussed) and sprite.handle_event(event, pygame.time.Clock()):
                break


pygame.init()
screen = pygame.display.set_mode((750, 500), RESIZABLE)
pic=pygame.image.load("assets/dark_wood_seamless.jpg")

setup_background()

all_sprites_list = pygame.sprite.Group()

box = Block(Color(0,0,200), 100,100, 100, 100)
all_sprites_list.add(box)

button = Button(Color(0,0,200), 732,244, 10, 10, button_feedback, "welcome to the club now")
all_sprites_list.add(button)

text = Block_text("First text")
all_sprites_list.add(text)
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

        screen.blit(box.image, box.rect)
        all_sprites_list.update()
        sprite_handle()
        all_sprites_list.draw(screen)


        pygame.display.flip()


