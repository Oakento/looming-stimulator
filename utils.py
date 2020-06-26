from math import tan, radians
from screeninfo import get_monitors


def degree_to_radius(angle, related):
    return related * tan(radians(angle))

def get_stimulator_geometry():
    monitors = get_monitors()
    monitor = monitors[0] if (monitors[0].x + monitors[0].y != 0) else monitors[-1]
    width = monitor.width
    height = monitor.height
    x = monitor.x
    y = monitor.y
    geometry = '{}x{}+{}+{}'.format(width, height, x, y)
    return width, height, x, y


# def get_panel_geometry():
#     monitors = get_monitors()
#     monitor = monitors[0] if (monitors[0].x + monitors[0].y == 0) else monitors[-1]
#     print(monitor)
#     width = int(monitor.width * 0.15)
#     height = int(monitor.height * 0.22)
#     geometry = '{}x{}'.format(width, height)
#     return geometry


def get_screen_height():
    monitors = get_monitors()
    monitor = monitors[0] if (monitors[0].x + monitors[0].y != 0) else monitors[-1]
    return monitor.height_mm / 10.0
    