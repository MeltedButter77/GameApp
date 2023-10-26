import pygame
from draw_module import color_dict  # Assuming draw_module is correctly imported

clock = pygame.time.Clock()
fps = 100


class Menu1Mode:
    def __init__(self, display):
        self.display = display

    def run(self):
        hover_color = color_dict['green']
        buttons = [
            {'rect': pygame.Rect(10, 10, 10, 10), 'info': {'mode': "draw"}, 'text': "Drawing Pad",
             'color': color_dict['blue']},
            {'rect': pygame.Rect(30, 10, 10, 10), 'info': {'mode': "draw"}, 'text': "Drawing Pad",
             'color': color_dict['blue']},
            {'rect': pygame.Rect(50, 10, 10, 10), 'info': {'mode': "draw"}, 'text': "Drawing Pad",
             'color': color_dict['blue']},
            {'rect': pygame.Rect(70, 10, 10, 10), 'info': {'mode': "quit"}, 'text': "Drawing Pad",
             'color': color_dict['red']}
        ]
        self.display.fill(color_dict['white'])
        while True:
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.MOUSEBUTTONUP:
                    for button in buttons:
                        if button['rect'].collidepoint(pygame.mouse.get_pos()):
                            return button['info']['mode']
            for button in buttons:
                if button['rect'].collidepoint(pygame.mouse.get_pos()):
                    pygame.draw.rect(self.display, hover_color, button['rect'])
                else:
                    pygame.draw.rect(self.display, button['color'], button['rect'])
            clock.tick(fps)
            real_fps = clock.get_fps()
            pygame.display.set_caption(f'FPS: {real_fps:.2f}')