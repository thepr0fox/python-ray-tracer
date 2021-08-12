class Scene:
    """This object has all the information needed for the ray tracer"""

    def __init__(self, camera, objects, WIDTH, HEIGHT):
        self.camera = camera
        self.objects = objects
        self.width = WIDTH
        self.height = HEIGHT