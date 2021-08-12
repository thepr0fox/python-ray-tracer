#!/usr/bin/env python

from image import Image
from color import Color


def main():
    WIDTH = 320
    HEIGHT = 300
    im = Image(WIDTH, HEIGHT)
    col1 = Color(85.0 / 255, 88.0 / 255, 218.0 / 255)
    col2 = Color(209.0 / 255, 95.0 / 255, 200.0 / 255)

    for y in range(HEIGHT):
        t = y / HEIGHT
        col_one = col1 * (1.0 - t) + col2 * t
        col_two = col2 * (1.0 - t) + col1 * t
        for x in range(WIDTH):
            lightness = x / WIDTH
            col = col_one * (1.0 - lightness) + col_two * lightness
            im.set_pixel(x, y, col)

    with open("gradient.ppm","w") as img_file:
        im.write_ppm(img_file)


if __name__ == "__main__":
    main()
