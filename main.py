import pygame
import gui
from gui_settings import *


class GameManager(object):
    def __init__(self, fps=60):
        self.running = True
        self.fps = fps
        self.clock = pygame.time.Clock()
        self.dt = 0

    def event_handling(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Closing Window
                self.running = False

            if event.type == pygame.MOUSEBUTTONDOWN:  # clicking Mouse
                if event.button == LMB:
                    gui.app.left_click()
                if event.button == RMB:
                    gui.app.test()

            if event.type == pygame.MOUSEBUTTONUP:  # release Mouse
                if event.button == LMB:
                    gui.app.left_click_release()
                if event.button == RMB:
                    pass

            if event.type == pygame.KEYDOWN:
                gui.app.keydown(event)


if __name__ == '__main__':

    game = GameManager(FPS)

    # Main Loop
    game.running = True
    while game.running:
        # Initialize
        game.dt = game.clock.tick(game.fps)

        # Drawing Layer 0 (Background)
        gui.screen.fill(COLOR_SCREEN)
        # Pre-Event
        gui.app.update()

        # Pygame Events
        game.event_handling()

        # Post-Events

        # Drawing Layer 1
        gui.app.draw()

        # Final
        pygame.display.update()

    print("Main Loop closed.")



