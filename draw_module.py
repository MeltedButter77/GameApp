import pygame
import math
color_dict = {
    'black': (0, 0, 0),
    'white': (255, 255, 255),
    'red': (255, 0, 0),
    'green': (0, 255, 0),
    'blue': (0, 0, 255),
    'yellow': (255, 255, 0),
    'pink': (255, 192, 203),
    'cyan': (0, 255, 255),
    'magenta': (255, 0, 255),
    'orange': (255, 165, 0),
    'purple': (128, 0, 128),
    'brown': (165, 42, 42),
    'grey': (128, 128, 128),
    'lime': (50, 205, 50),
    'violet': (238, 130, 238),
    'indigo': (75, 0, 130),
    'gold': (255, 215, 0),
    'silver': (192, 192, 192),
    'beige': (245, 245, 220),
    'turquoise': (64, 224, 208),
    'olive': (128, 128, 0),
    'maroon': (128, 0, 0),
    'navy': (0, 0, 128),
}


def create_color_buttons(start_x, start_y, step_y, size_x, size_y, colors):
    buttons = []
    y = start_y
    for color_name in colors:
        clr = color_dict[color_name]
        buttons.append({'rect': pygame.Rect(start_x, y, size_x, size_y), 'info': {'color': clr}, 'color': clr})
        y += step_y
    return buttons


def draw_objects(surface, objects):
    surface.fill(color_dict['white'])
    print('drawing')
    # draw objects
    for object in objects:
        color = object['color']
        thickness = object['thickness']
        if object['shape'] == 'line':
            if len(object['points']) > 1:
                pygame.draw.lines(surface, color, False, object['points'], thickness)
            # for i in range(-1, len(object['points']) - 1):
            #     pygame.draw.circle(surface, color, (object['points'][i][0], object['points'][i][1]), (thickness / 2))
        if object['shape'] == 'straightLine':
            if len(object['points']) == 2:
                pygame.draw.line(surface, color, object['points'][0],
                                 object['points'][1], thickness)


def draw_buttons(buttons, hover_color, menu_surface):
    """
    Draws buttons on the provided surface, changes color on hover.

    :param buttons: List of dictionaries containing button information.
    :param hover_color: Color to be applied when mouse hovers over a button.
    :param menu_surface: Surface on which buttons are drawn.
    """

    # Get the mouse position only once to avoid multiple calls to pygame.mouse.get_pos()
    mouse_pos = pygame.mouse.get_pos()

    for button in buttons:
        color = button['color']

        # Change color on hover for buttons containing 'mode' in 'info' keys
        if 'mode' in button.get('info', {}).keys() and button['rect'].collidepoint(mouse_pos):
            color = hover_color

        # Draw buttons
        rect_to_draw = button.get('drawRect', button['rect'])
        pygame.draw.rect(menu_surface, color, rect_to_draw)
