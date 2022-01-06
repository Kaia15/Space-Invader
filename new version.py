import pygame
import random
import time 
import os
from pygame import mixer
from pygame.locals import *
clock  = pygame.time.Clock()
fps = 60

scrwidth = 600
scrheight = 600

screen = pygame.display.set_mode((scrwidth,scrheight))
pygame.display.set_caption("Space Invader version 2")

BG = pygame.image.load("./background_black.png")

def draw_bg():
    screen.blit(BG,(0,0))


run = True
while run:

    #draw the background
    draw_bg()

    #event handlers
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    pygame.display.update()

    
            