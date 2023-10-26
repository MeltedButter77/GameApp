import pygame
from draw_module import draw_buttons, draw_objects, color_dict, create_color_buttons  # Assuming draw_module is correctly imported

clock = pygame.time.Clock()
fps = 60


class DrawMode:
    def __init__(self, display, window_size):
        self.display = display
        self.windowSize = window_size

    def run(self):
        buttons = create_color_buttons(5, 10, 15, 10, 10, list(color_dict.keys()))

        tool_buttons_x = 40
        thickness_buttons_x = 40
        more_buttons_data = [
            # Tools
            {'rect': pygame.Rect(tool_buttons_x - 5, 70, 20, 20), 'info': {'type': 'pen'}, 'color': 'black'},
            {'rect': pygame.Rect(tool_buttons_x, 100, 10, 10), 'info': {'type': 'straightLine'}, 'color': 'green'},
            {'rect': pygame.Rect(tool_buttons_x, 120, 10, 10),
             'info': {'type': 'eraser', 'color': color_dict['white'], 'thickness': 40}, 'color': 'pink'},

            # thickness
            {'rect': pygame.Rect(thickness_buttons_x, 10, 10, 10), 'drawRect': pygame.Rect(thickness_buttons_x, 10, 2, 2),
             'info': {'thickness': 2}, 'color': 'white'},
            {'rect': pygame.Rect(thickness_buttons_x, 20, 10, 10), 'drawRect': pygame.Rect(thickness_buttons_x, 20, 4, 4),
             'info': {'thickness': 4}, 'color': 'white'},
            {'rect': pygame.Rect(thickness_buttons_x, 30, 10, 10), 'drawRect': pygame.Rect(thickness_buttons_x, 30, 6, 6),
             'info': {'thickness': 6}, 'color': 'white'},
            {'rect': pygame.Rect(thickness_buttons_x, 40, 10, 10), 'drawRect': pygame.Rect(thickness_buttons_x, 40, 8, 8),
             'info': {'thickness': 8}, 'color': 'white'},
            {'rect': pygame.Rect(thickness_buttons_x, 50, 10, 10),
             'drawRect': pygame.Rect(thickness_buttons_x, 50, 10, 10), 'info': {'thickness': 10}, 'color': 'white'},

            # Exit
            {'rect': pygame.Rect(20, self.windowSize[1] - 40, 20, 20), 'info': {'mode': "menu1"}, 'color': 'red'},
        ]
        buttons.extend(list(more_buttons_data))

        menu_surface_size = (80, self.windowSize[1])
        menu_surface_location = (0, 0)
        menu_surface = pygame.Surface(menu_surface_size)

        board_surface_size = (self.windowSize[0] - 80, self.windowSize[1])
        board_surface_location = (menu_surface_size[0], 0)
        draw_surface = pygame.Surface(board_surface_size)

        menu_surface.fill(color_dict['grey'])
        draw_surface.fill(color_dict['white'])

        draw_surface_mouse_pos = (0, 0)

        hover_color = color_dict['green']
        pen_type = None

        pen_settings = {
            'pen': {'color': color_dict['blue'], 'thickness': 5, },
            'eraser': {'color': color_dict['white'], 'thickness': 20, },
            'straightLine': {'color': color_dict['blue'], 'thickness': 5, }
        }
        layers = [[]]
        objects = []
        draw_buttons(buttons, hover_color, menu_surface)
        mouse_down = False

        while True:
            menu_surface_rect = self.display.blit(menu_surface, menu_surface_location)
            draw_surface_rect = self.display.blit(draw_surface, board_surface_location)

            pygame.display.update([menu_surface_rect, draw_surface_rect])

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.MOUSEMOTION:
                    draw_surface_mouse_pos = (pygame.mouse.get_pos()[0] - menu_surface_size[0], pygame.mouse.get_pos()[1])
                    if draw_surface_rect.collidepoint(pygame.mouse.get_pos()):
                        if mouse_down and pen_type in ['pen', 'eraser']:
                            if draw_surface_mouse_pos not in objects[len(objects) - 1]['points']:
                                objects[len(objects) - 1]['points'].append((draw_surface_mouse_pos[0]-1, draw_surface_mouse_pos[1]-1))
                            if pen_type != 'eraser':
                                draw_objects(draw_surface, objects)
                        if pen_type == 'eraser':
                            draw_objects(draw_surface, objects)
                            color = (240, 240, 240) if mouse_down else (200, 200, 200)
                            pygame.draw.circle(draw_surface, color, draw_surface_mouse_pos, pen_settings['eraser']['thickness'] / 2)
                        if mouse_down and pen_type == 'straightLine':
                            draw_objects(draw_surface, objects)
                            pygame.draw.line(draw_surface, pen_settings['straightLine']['color'], objects[-1]['points'][0], draw_surface_mouse_pos, pen_settings['straightLine']['thickness'])
                    if menu_surface_rect.collidepoint(pygame.mouse.get_pos()):
                        draw_buttons(buttons, hover_color, menu_surface)

                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_down = True
                    if pen_type == 'pen' or pen_type == 'eraser':
                        objects.append(
                            {'shape': 'line', 'points': [draw_surface_mouse_pos], 'color': pen_settings[pen_type]['color'],
                             'thickness': pen_settings[pen_type]['thickness']})
                    if pen_type == 'straightLine':
                        objects.append({'shape': 'straightLine', 'points': [draw_surface_mouse_pos],
                                        'color': pen_settings[pen_type]['color'],
                                        'thickness': pen_settings[pen_type]['thickness']})
                    draw_objects(draw_surface, objects)

                if event.type == pygame.MOUSEBUTTONUP:
                    mouse_down = False
                    if pen_type == 'straightLine':
                        objects[-1]['points'].append(draw_surface_mouse_pos)
                    for button in buttons:
                        if not button['rect'].collidepoint(pygame.mouse.get_pos()):
                            continue
                        for setting in button['info'].keys():
                            if setting == 'mode':
                                return button['info'][setting]
                            if setting == 'type':
                                pen_type = button['info'][setting]
                            if pen_type:
                                pen_settings[pen_type][setting] = button['info'][setting]
            clock.tick(fps)
            real_fps = clock.get_fps()
            pygame.display.set_caption(f'FPS: {real_fps:.2f}')