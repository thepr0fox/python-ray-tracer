#!/usr/bin/env python

import argparse

from color import Color
from engine import RenderEngine
from light import Light
from material import Material
from point import Point
from scene import Scene
from sphere import Sphere
from vector import Vector


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("imageout", help="Path to rendered image")
    args = parser.parse_args()
    WIDTH = 1920
    HEIGHT = 1080
    camera = Vector(0, 0, -1.5)
    lights = [Light(Point(1.5, -1.0, -10.0), Color.from_hex("#FFFFFF"))]

    objects = [Sphere(Point(0, 0, -0.3), 0.2, Material(Color.from_hex("#FF1212"),0.05,0.8,1.65)), Sphere(Point(0.3, -0.2, -0.05), 0.2, Material(Color.from_hex("#11FF11"),0.05,0.9,1.7)), Sphere(Point(0.6, -0.35, -0.02 ), 0.2, Material(Color.from_hex("#1122FF"),0.05,0.65,1.65))]
    # Add spiky blob filaments


    scene = Scene(camera, objects, lights, WIDTH, HEIGHT)
    engine = RenderEngine()
    image = engine.render(scene)

    with open(args.imageout, "w") as img_file:
        image.write_ppm(img_file)


if __name__ == "__main__":
    main()
