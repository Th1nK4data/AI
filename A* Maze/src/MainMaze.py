"""
 Pygame base template for opening a window
 
 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/
 
 Explanation video: http://youtu.be/vRB_983kUMc
"""
import numpy as np
import pygame

class Maze:
    def __init__(self, size):
        # Define some colors
        BLACK = (0, 0, 0)
        WHITE = (255, 255, 255)
        GREEN = (0, 255, 0)
        RED = (255, 0, 0)
        
        # Sets width and height of each grid block
        WIDTH = 20
        HEIGHT = 20
        
        # Sets margin between each cell block
        MARGIN = 5
        
        # Create grid
        grid = np.array([[np.random.randint(0,2) for i in range(size)] for i in range(size)])
        grid[0,0] = 0
        grid[size-1,size-1] = 0
        
        pygame.init()
         
        # Set the width and height of the screen [width, height]
        dimensions = (255, 255)
        screen = pygame.display.set_mode(dimensions)
        
        pygame.display.set_caption("My Maze")
         
        # Loop until the user clicks the close button.
        done = False
         
        # Used to manage how fast the screen updates
        clock = pygame.time.Clock()
         
        # -------- Main Program Loop -----------
        while not done:
            # --- Main event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
         
            # --- Game logic should go here
            
            # --- Screen-clearing code goes here
            
            # Here, we clear the screen to white. Don't put other drawing commands
            # above this, or they will be erased with this command.
         
            # If you want a background image, replace this clear with blit'ing the
            # background image.
            screen.fill(GREEN)
            
            # --- Drawing the grid
            for row in range(size):
                for column in range(size):
                    color = WHITE
                    if grid[row, column] == 1:
                        color = BLACK
                    if grid[row, column] == 2:
                        color = RED
                    pygame.draw.rect(screen,
                                     color,
                                     [(MARGIN + WIDTH) * column + MARGIN,
                                      (MARGIN + HEIGHT) * row + MARGIN,
                                      WIDTH,
                                      HEIGHT])

            
            # --- Go ahead and update the screen with what we've drawn.
            pygame.display.flip()
            
            # --- Limit to 60 frames per second
            clock.tick(60)
         
        # Close the window and quit.
        pygame.quit()
        
if __name__ == '__main__':
    Maze(10)
    