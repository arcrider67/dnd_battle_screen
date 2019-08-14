import pygame
from pygame.locals import *
from widgets import *
from screens import *

def setup_background():

    pic_width, pic_height = pic.get_width(), pic.get_height()
    w, h = screen.get_size()
    size = (w,h)
    background =  pygame.Surface(size).convert()

    y = 0
    x = 0
    print(str(w) +" "+ str(h))
    while (x <= w+1):
        while (y <= h+1):

            # print(x,y)
            background.blit(pic, (x, y))
            y = y + pic_height
        y = 0
        x = x + pic_width
    return background


def button_feedback(self, event, clock):
    count = text.get_text()
    count = count.split()
    count[1] = int(count[1])+1
    
    new_text = count[0]+" "+str(count[1])
    text.set_text(new_text)
    set_screen()
    

def set_screen(new_screen=None):
    global screen
    global current_sprites
    current_sprites.clear(screen, background)
    current_sprites.remove(current_sprites)
    current_sprites.add(battle_screen)



def sprite_handle():
    for sprite in current_sprites:
        if hasattr(event, "pos"):
            focussed = sprite.rect.collidepoint(event.pos)
            if (focussed or sprite.focussed) and sprite.handle_event(event, pygame.time.Clock()):
                break


pygame.init()
screen = pygame.display.set_mode((750, 500), RESIZABLE)
pic=pygame.image.load("assets/dark_wood_seamless.jpg")

background = setup_background()
screen.blit(background,(0,0))

all_sprites_list = pygame.sprite.Group()
start_screen = pygame.sprite.Group()
battle_screen = pygame.sprite.Group()
current_sprites = pygame.sprite.Group()

box = Block(Color(0,0,200), width=100,height=100, x=100, y=100)
all_sprites_list.add(box)

start_button = Button(Color(0,0,200), 732,244, 10, 10, button_feedback, "Start Battle")
all_sprites_list.add(start_button)
start_screen.add(start_button)

text = Block_text("First text")
all_sprites_list.add(text)

text = Block_text("Counter: 0", x=650, y=0)
all_sprites_list.add(text)
battle_screen.add(text)

battle_screen = init_screen("battle_screen")

current_sprites.add(start_screen)

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

        current_sprites.update()
        sprite_handle()
        current_sprites.draw(screen)


        pygame.display.flip()