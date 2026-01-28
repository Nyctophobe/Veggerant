"""
Veggerant: My Game Design game
Will be a unique platformer designed to find ways to move the character.

Author: Simon Lopez-Trujillo
"""
#Imports
import pygame
from GameEngine import GameEngine
from vector import vec, pyVec
RESOLUTION = vec(400, 200)
SCALE = 2
UPSCALED = RESOLUTION * SCALE

#____________________________________________________________Game Setup____________________________________________________________
def main():

    pygame.init()
    pygame.font.init()

    screen = pygame.display.set_mode(pyVec(UPSCALED))   
    drawSurface = pygame.Surface(pyVec(RESOLUTION))

    game = GameEngine()
    
    gameClock = pygame.time.Clock()


    RUNNING = True
    
#____________________________________________________________Main Loop Start____________________________________________________________   
    while RUNNING:
    
#------------------------------------------------------------Display World------------------------------------------------------------           
        game.draw(drawSurface)
    
        pygame.transform.scale(drawSurface, pyVec(UPSCALED), screen)

        pygame.display.flip()
#------------------------------------------------------------Event Keys------------------------------------------------------------
        for event in pygame.event.get():
        #Quit Game
            if event.type == pygame.QUIT or \
               (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                RUNNING = False
        #Other Events
            else:
                game.handleEvent(event)

    #Progresses & Tracks Clock
        seconds = gameClock.get_time() / 1000
        gameClock.tick(60)

        game.update(seconds)

#____________________________________________________________Main Loop End____________________________________________________________
         


#Quit Pygame
    pygame.quit()

if __name__ == "__main__":
    main()
