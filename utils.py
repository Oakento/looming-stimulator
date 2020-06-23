from math import tan, radians
from screeninfo import get_monitors

def degree_to_radius(angle, related):
    return related * tan(radians(angle))

def get_geometry():
    monitors = get_monitors()
    if len(monitors) > 1:
        monitor1 = monitors[0]
        monitor2 = monitors[-1]
        width = monitor2.width
        height = monitor2.height
        x = monitor2.x
        y = monitor2.y
    else:
        monitor = monitors[0]
        width = monitor.width
        height = monitor.height
        x = monitor.x
        y = monitor.y
    geometry = '{}x{}+{}+{}'.format(width, height, x, y)
    return geometry

def get_screen_height():
    monitor = get_monitors()[-1]
    return monitor.height_mm / 10.0
    