import pygame
from pygame.locals import *
from pygame.font import Font
import json
from handlers import handler_dict

def init_sprite_group(screen_name = None):
    
    group = pygame.sprite.Group()

    with open("assets/"+str(screen_name)+".json") as json_file:
        data = json.load(json_file)
        for ele in data["Elements"]:
            create_sprite(ele, group)

    
    

    return group



def create_sprite(properties, group):
    if properties["Type"] == "TextBox":
        item = Block_text(properties=properties)
    elif properties["Type"] == "Button":
        item = Button(properties=properties)
    group.add(item)


class Block(pygame.sprite.DirtySprite):

    # Constructor. Pass in the color of the block,
    # and its x and y position
    def __init__(self, color=None, width=None, height=None, x=None, y=None, handler=None, properties=None):
       # Call the parent class (Sprite) constructor

       if properties:
           color = properties["Color"]
           width = properties["Width"]
           height = properties["Height"]
           x = properties["X"]
           y = properties["Y"]
           handler = properties["Handler"]
       
       pygame.sprite.DirtySprite.__init__(self)

       
       size = (width, height)

       try:
           if self.image:
               pass
       except:
           self.image = pygame.Surface(size).convert()
           self.image.fill(color)



       self.rect = self.image.get_rect()
       self.rect.top = y
       self.rect.left = x
       self.size = (self.rect.width, self.rect.height)
       self.background = self.image.copy()

       self.focussed = False

       if handler != None and handler != 'None':
           self.handler = handler_dict[handler]


       self.pressed_time = 0 
       self.long_pressed = False
      



    def handle_event(self, event, clock):
        handled = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            self.pressed_time = pygame.time.get_ticks()
            self.focussed = True

        if (event.type == pygame.MOUSEBUTTONUP):
            if self.handler and self.focussed:
                self.handler(self, event, clock)
                handled = True

            self.pressed_time = 0
            self.long_pressed = False
            self.focussed = False

        return handled


class Block_text(Block):

    def __init__(self, text=None, color=Color(255,255,255), width=100, height=100, x=50, y=50, handler=None, properties=None):
        
        if properties:
            text = properties["Text"]


        Block.__init__(self,color, width,height, x, y, properties=properties)
        if text:
           self.render_text(text)

    def render_text(self, text):
        image = self.image
        font = Font("assets/swiss2.ttf", 30)
        textImage = font.render(text, False, Color(0,0,200))


        self.image.blit(textImage, (image.get_rect().width/2 - textImage.get_rect().width/2 - 10, image.get_rect().height/2 - textImage.get_rect().height/2 - 5))
        self.text = text

    def clear_text(self):
        self.image.blit(self.background, (0,0))

    def get_text(self):
        return self.text

    def set_text(self, new_text):
        self.clear_text()
        self.render_text(new_text)

class Button(Block):

    def __init__(self, color=None, width=None, height=None, x=None, y=None, handler=None, text=None, properties=None):

        if properties:
            text = properties["Text"]



        self.image_file = pygame.image.load("assets/wooden-sign.png").convert_alpha()
        self.image = self.image_file
        Block.__init__(self, color, width, height, x, y, handler, properties)

        if text:
           self.render_text(text)

    def render_text(self, text):
        image = self.image
        font = Font("assets/swiss2.ttf", 30)
        textImage = font.render(text, False, Color(0,0,200))


        self.image.blit(textImage, (image.get_rect().width/2 - textImage.get_rect().width/2 - 10, image.get_rect().height/2 - textImage.get_rect().height/2 - 5))
    
    def clear_text(self):
        self.image.blit(self.background, (0,0))

    def get_text(self):
        return self.text

    def set_text(self, new_text):
        self.clear_text()
        self.render_text(new_text)

    def handle_event(self, event, clock):
        return Block.handle_event(self, event, clock)





    