from vector import Vector


class Color(Vector):
    """Stores color as red green and blue values. This is a sub class of vector"""

    def __init__(self, red, green, blue):
        self.x = red
        self.y = green
        self.z = blue

    @classmethod
    def from_hex(cls, hex_color="#000000"):
        red = int(hex_color[1:3], 16) / 255.0
        green = int(hex_color[3:5], 16) / 255.0
        blue = int(hex_color[5:7], 16) / 255.0
        return cls(red, green, blue)


