import pygame
import os

class drawable(object):

    def __init__(self):
        #The image to draw on screenDisplay
        self.image = image
        #Where to draw the image
        self.position = position

    def draw(position, image):
        pygame.image.load(os.path.join(image)).convert()
        
    def update(self, seconds):
        pass
