from math import sqrt


class Sphere:
    """A 3D sphere, this has a center, radius and a material"""

    def __init__(self, center, radius, material):
        self.center = center
        self.radius = radius
        self.material = material

    def intersects(self, Ray):
        """Checks if a ray intersects this sphere. If a ray intersects then it will return the distance from the
        origin of the ray to the closest point of intersection, returns None if the ray does not intersects """

        sphere_to_ray = Ray.origin - self.center
        b = 2 * Ray.direction.dot_product(sphere_to_ray)
        c = sphere_to_ray.dot_product(sphere_to_ray) - self.radius * self.radius
        discriminant = b * b - 4 * c

        if discriminant >= 0:
            dist = -b - sqrt(discriminant) / 2
            if dist > 0:
                return dist
        return None
