import pygame
from pygame.locals import *
from pygame.font import Font

class Block(pygame.sprite.DirtySprite):

    # Constructor. Pass in the color of the block,
    # and its x and y position
    def __init__(self, color, width, height, x, y, handler=None):
       # Call the parent class (Sprite) constructor
       pygame.sprite.DirtySprite.__init__(self)

       self.image = pygame.Surface(width, height).convert()
       self.image.fill(color)

       self.rect = self.image.get_rect()
       self.rect.top = pos[0]
       self.rect.left = pos[1]
       self.size = (self.rect.width, self.rect.height)
       
       self.focussed = False
       self.handler = handler
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

    def __init__(self, text):
        
        Block.__init__(self,Color(255,255,255), 100,100, 50, 50)
        if text:
           self.render_text(text)


    def render_text(self, text):
        image = self.image
        font = Font("assets/swiss2.ttf", 30)
        textImage = font.render(text, False, Color(0,0,200))


        self.image.blit(textImage, (image.get_rect().width/2 - textImage.get_rect().width/2 - 10, image.get_rect().height/2 - textImage.get_rect().height/2 - 5))


class Button(Block):

    def __init__(self, color, width, height, x, y, handler=None, text=None):

        self.image = pygame.image.load("assets/wooden-sign.png").convert_alpha()
        Block.__init__(self, color, width, height, x, y, handler)

        if text:
           self.render_text(text)

    def render_text(self, text):
        image = self.image
        print("fonting")
        font = Font("assets/swiss2.ttf", 30)
        textImage = font.render(text, False, Color(0,0,200))


        self.image.blit(textImage, (image.get_rect().width/2 - textImage.get_rect().width/2 - 10, image.get_rect().height/2 - textImage.get_rect().height/2 - 5))
    
    def set_text(new_text):
        render_text(new_text)

    def handle_event(self, event, clock):
        return Block.handle_event(self, event, clock)





    