import pygame
import gui
from gui_settings import *

if __name__ == '__main__':

    # Main Loop
    running = True
    while running:
        # Initialize
        dt = gui.clock.tick(FPS)

        # Drawing Layer 0 (Background)
        gui.screen.fill(COLOR_SCREEN)
        # Pre-Event
        # App.update()

        # Pygame Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Closing Window
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:  # clicking Mouse
                if event.button == LMB:
                    pass
                if event.button == RMB:
                    pass

            if event.type == pygame.MOUSEBUTTONUP:  # release Mouse
                if event.button == LMB:
                    pass
                if event.button == RMB:
                    pass

            if event.type == pygame.KEYDOWN:  # Keyboard pressed
                pass

        # Post-Events

        # Drawing Layer 1
        # App.draw()

        # Final
        pygame.display.update()

    print("Main Loop closed.")



