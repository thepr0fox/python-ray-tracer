#!/usr/bin/env python
from color import Color
from vector import Vector
from point import Point
from sphere import Sphere
from scene import Scene
from engine import RenderEngine


def main():
    WIDTH = 320
    HEIGHT = 200

    camera = Vector(0,0,-1)
    objects = [Sphere(Point(0,-0.3,0),0.1, Color(1,0,0)), Sphere(Point(0,0,0),0.1, Color(1,1,0)), Sphere(Point(0,0.3,0),0.1, Color(0,1,0))]
    scene = Scene(camera, objects, WIDTH, HEIGHT)
    engine = RenderEngine()
    image = engine.render(scene)

    with open("trafic_light.ppm","w") as img_file:
        image.write_ppm(img_file)


if __name__ == "__main__":
    main()
