import pygame
from pygame.locals import *
from widgets import *
import json



def init_screen(screen_name = None):
    
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


