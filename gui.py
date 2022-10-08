# import pygame, arrow, graphing, math
from widgets import *
from gui_settings import *
from graphing import *

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
pygame.init()

# Functions


def extract(lst):
    return [item[0] for item in lst]


# Object initialization
app = WidgetManager(screen)
# TODO
# old_graph = Graph()
new_graph = nx.MultiDiGraph()
app.graph = new_graph


if __name__ == '__main__':
    # Main Loop
    running = True
    while running:
        # Initialize
        dt = clock.tick(FPS) / 1000  # Returns milliseconds between each call to 'tick'. The convert time to seconds.

        # Background drawing
        screen.fill(COLOR_SCREEN)  # Fill the screen with background color.
        # backdrop.draw(screen)

        # Updates before pygame events
        app.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Left clicking
                if event.button == LMB:
                    app.left_click()
                if event.button == RMB:
                    app.test()
            if event.type == pygame.MOUSEBUTTONUP:
                # Left click release
                if event.button == LMB:
                    app.left_click_release()
            if event.type == pygame.KEYDOWN:
                app.keydown(event)

                # Replaced by Buttons
                # match event.key:
                #     case pygame.K_n:
                #         App.change_mode("create node")
                #     case pygame.K_e:
                #         App.change_mode("create edge")
                #     case pygame.K_m:
                #         App.change_mode("move")
                #     case pygame.K_d:
                #         App.change_mode("delete")
                #     case pygame.K_x:
                #         App.change_mode("edit")

        # Updates after pygame events
        app.draw()

        pygame.display.update()  # Or pygame.display.flip()

    print("Exited the game loop. Game will quit...")
