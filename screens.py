import pygame
from pygame.locals import *
from widgets import *
import json



def init_screen(screen_name = None):
    
    with open("assets/"+str(screen_name)+".json") as json_file:
        data = json.load(jsonfile)
        for ele in data["Elements"]:
            print(ele)

    group = pygame.sprite.Group()
    

    return group