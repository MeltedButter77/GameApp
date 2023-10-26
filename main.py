import pygame
from draw_mode import DrawMode
from menu1_mode import Menu1Mode

pygame.init()

window_size = (1000, 800)
display = pygame.display.set_mode(window_size)

clock = pygame.time.Clock()
fps = 60

mode = "menu1"
while True:
    if mode == "quit":
        pygame.quit()
        quit()
    elif mode == "menu1":
        mode = Menu1Mode(display).run()
    elif mode == "draw":
        mode = DrawMode(display, window_size).run()
    clock.tick(fps)