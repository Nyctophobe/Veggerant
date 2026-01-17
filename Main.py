"""
Veggerant: My Game Design game
Will be a unique platformer designed to find ways to move the character.

Author: Simon Lopez-Trujillo
"""
#Imports
import os
import pygame
import numpy as np
import vector as vector

#____________________________________________________________Game Setup____________________________________________________________
def main():
#Initialize Pygame
    pygame.init()
    pygame.font.init()

#Set up display
    RESOLUTION = (400, 200)
    SCALE = 2
    UPSCALED = [int(x * SCALE) for x in RESOLUTION]
    
    screen = pygame.display.set_mode(list(UPSCALED))   
    drawSurface = pygame.Surface(list(RESOLUTION))

#Game Clock
    gameClock = pygame.time.Clock()
    seconds = gameClock.get_time() / 1000

#Game Run Control
    RUNNING = True

#Set up texts
    basicText = pygame.font.SysFont('Arial', 20)
    #Sample text
    """
        helloWorld = basicText.render("hello world", False, (255,0,0))
        drawSurface.blit(helloWorld, (0,0))"""
#---------------------------------------------------------------Objects----------------------------------------------------------------
#Egg 
    #Image
    egg = pygame.image.load(os.path.join("Game Sprites.png")).convert()
    egg.set_colorkey((0, 0, 0))
    #Movement
    eggVec = vector.vec(0, 0)
    eggPos = vector.vec(200, 100)



#____________________________________________________________Main Loop Start____________________________________________________________   
    while RUNNING:

#------------------------------------------------------------Display World------------------------------------------------------------
    #Fill Entire Screen to reset display
        drawSurface.fill((0, 50, 255))
        
    #Upscale Images
        pygame.transform.scale(drawSurface, list(UPSCALED), screen)

        
    #Draw Egg
        drawSurface.blit(egg, vector.pyVec(eggPos))

    #Update the display
        pygame.display.flip()
#------------------------------------------------------------Event Keys------------------------------------------------------------
        for event in pygame.event.get():
        #Quit Game
            if event.type == pygame.QUIT or \
               (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                RUNNING = False
        #Other Events
            else:
                """ #Future movement
                Egg movement will not be like this in the final game. The egg on its own will have very limited movement.
                The egg will be able to
                                - Jump (Cannot move while in the air)
                                - Roll (Each button press rolls a fixed distance)
                This movement may be altered by other abilities, such as chaning weight or cracking your shell,
                but all personal movement is tied to those two actions. Any additional movement is due to enviromental factors and how your 
                abilities interact with it

                Jumping on its own will need movement, gravity and collision
                Jumping will also be changed based on the weight of the egg, changing how effective gravity is on the egg.
                It will also be effected by if the egg is cracked or not, increacing gravity once it reaches its expected height.

                Rolling on its own will require movement, gravity and collision
                Rolling will also be changed based on the weight of the egg, changing how fast it can move.
                Rolling will also be effected by if the egg is cracked or not, preventing it from falling off edges and instead hang from the yoke

                Cracking will require movement, gravity and collision
                When the egg hits a surface fast enough, its shell will crack. The speed neede is based off the eggs weight.
                While the egg is cracked, all movement is altered.
                Yoke will stick to surfaces, allowing the egg to climb walls, hang under ledges, and prevent exterior methods of movement.

                Boiling will change the hardness & weight of the egg
                The egg starts out the level completely raw. It is at its lightest, frailest, and stickiest in this state. 
                The egg can boil itself twice, with its weight and strength increasing, but its stickiness decreasing.
                
                These will be my 4 main goals of movement, though they may not be fully implemented in all their interactions
                """
             #Egg Movement
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w:
                        eggVec[1] = -1
                    elif event.key == pygame.K_s:
                        eggVec[1] = 1
                    elif event.key == pygame.K_a:
                        eggVec[0] = -1
                    elif event.key == pygame.K_d:
                        eggVec[0] = 1
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_w:
                        eggVec[1] = 0
                    elif event.key == pygame.K_s:
                        eggVec[1] = 0
                    elif event.key == pygame.K_a:
                        eggVec[0] = 0
                    elif event.key == pygame.K_d:
                        eggVec[0] = 0
            #More Key Events
                if event.type == pygame.KEYUP:
                    pass

#------------------------------------------------------------Update Objects------------------------------------------------------------
        
    #Move Egg
        eggPos += eggVec * seconds * 100

    #Progresses & Tracks Clock
        gameClock.tick(60)
#____________________________________________________________Main Loop End____________________________________________________________
         


#Quit Pygame
    pygame.quit()

if __name__ == "__main__":
    main()
