from math import tan, radians

def degree_to_radius(angle, related):
    return related * tan(radians(angle))