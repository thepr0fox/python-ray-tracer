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
    WIDTH = 320
    HEIGHT = 200
    camera = Vector(0, 0, -1.5)
    lights = [Light(Point(1.5, -1.0, -10.0), Color.from_hex("#FFFFFF"))]

    objects = [Sphere(Point(0, 0, 0), 0.5, Material(Color.from_hex("#FF0000"),0.05,1.0,1.0))]
    # Add spiky blob filaments


    scene = Scene(camera, objects, lights, WIDTH, HEIGHT)
    engine = RenderEngine()
    image = engine.render(scene)

    with open(args.imageout, "w") as img_file:
        image.write_ppm(img_file)


if __name__ == "__main__":
    main()
