# What is pyGame? 
    # 'A game library', a collection of tools to help in making games
    # Graphics/Animations, Sound, Control

# The most important piece: The Game Loop
 # PROCESS INPUT ---> UPDATE GAME ---> RENDER and return back to beg. of loop
 # You also have to control how fast this happens.
            # - how fast this loop happens... 
    # PROCESS INPUT: The key getting pressed, mouse clicked, etc.

    # UPDATE GAME: Changing anything that needs to change.
        # - If a character needs to move, we need to figure out where to move to
        # - If two things collide, what was supposed to happen
        # - Anything that has happened since the last time it was updated.

    # RENDER: Drawing everything to the screen
        # - something changed, now we have to draw that
        # - Character moves 'x' places to right, draw that number to the right

import pygame
import random

# tell pyGame to create a window.
WIDTH = 480 
HEIGHT = 640
FPS = 30    # how fast our screen will be updated

# List of colors I could use often, quicker to refer to later
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)



pygame.init() # initilizies pygame and gets it ready to go. 
pygame.mixer.init() # the mixer handles all the music, sound fx in game

# Create our window:
screen = pygame.display.set_mode((WIDTH, HEIGHT))
# Create what our window header displays
screen = pygame.display.set_caption("It's PyGame by your very own...")
# Create the clock: handles the speed & how fast we're going to make sure we are running the rt FPS
clock = pygame.time.Clock()

# THE GAME LOOP: our core 
    # we need a while loop but we also need a way to stop it by creating running = true
running = True  #if running is ever set to false, the loop will end and the game is over
while running:
    # first want to make sure our game runs at the right speed.
    clock.tick(FPS) # however long it took to process invent, update, draw, etc, pause just long
                    # enough to make it under 30FPS
    # PROCESS INPUT (events) 
            # events can happen anytime, if player presses button to jump, we need it addressed
            # right then and not after the loop.
                
    for event in pygame.event.get(): # # python keeps track of any events since the last time asked
 
        # Check for closing the window
        if event.type == pygame.QUIT:
            running = False


    # UPDATE - don't bog down and create too much or you will create L-A-G

    # DRAW / RENDER
screen.fill((0,0,0)) # much easier to define as a constant at top to use multipe times
    
    # now **AFTER** drawing everything, flip the display; neeeds to be last because if you 
    # flipped the display & then you 'drew on your white board', nobody would see it.
pygame.display.flip() # flip that imaginary white board over, draw, flip and repeat.
        # also referred to as 'Double Buffering'
    


# Double Buffering: your white board with two sides. We draw on the back, flip over
# draw on the back side for the next animation and then flip over and repeat over and over.


#  -----     PROBLEM(s)     ---------
# Traceback (most recent call last):
#   File "myPyGameTemplete.py", line 67, in <module>
#     screen.fill(0,0,0) # much easier to define as a constant at top to use multipe times
# AttributeError: 'NoneType' object has no attribute 'fill'
# ----- INDENT ERROR IF I INDENT SCREEN.FILL ------#