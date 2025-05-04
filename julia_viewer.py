import pygame
import sys
import os

# Add the parent directory to the path to avoid ModuleNotFoundError
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(project_root)

from geometry_engine_librairie.Mathy.renderer import Renderer

def julia(c: complex, z: complex, max_iter: int) -> bool:
    """
    Returns True if the sequence zn remains bounded (|zn| <= 2 after max_iter iterations).
    """
    for _ in range(max_iter):
        if abs(z) > 2:  # abs() is used to calculate the module
            return False  # The sequence diverges
        z = z * z + c
    return True  # The sequence remains bounded


def map_pixel_to_complex(x, y, width, height, zoom=1.0, offset=(0.0, 0.0)) -> complex:
    """
    Maps a pixel (x, y) to a point in the complex plane.
    """
    # Center and scale pixel (x, y)
    re = (x - width / 2) / (0.5 * zoom * width) + offset[0]
    im = (y - height / 2) / (0.5 * zoom * height) + offset[1]
    return complex(re, im)


def render_julia(renderer: Renderer, c: complex, max_iter=100, zoom=1.0, offset=(0.0, 0.0)):
    """
    Renders the Julia set, black if bounded, white otherwise.
    """
    width, height = renderer.width, renderer.height
    for x in range(width):
        for y in range(height):
            z = map_pixel_to_complex(x, y, width, height, zoom, offset)
            is_bounded = julia(c, z, max_iter)
            color = (0, 0, 0) if is_bounded else (255, 255, 255)
            renderer.draw_point(x, y, color=color)
    renderer.update()


def main():
    width, height = 800, 600
    renderer = Renderer(width, height, "Julia Set Viewer", bg_color=(255, 255, 255))

    c = complex(-0.7, 0.27015)  # A classic value for a nice Julia set
    max_iter = 100
    zoom = 1.0
    offset = (0.0, 0.0)

    render_julia(renderer, c, max_iter, zoom, offset)

    while renderer.running:
        renderer.handle_events()
        renderer.clock.tick(60)

    renderer.quit()


if __name__ == "__main__":
    main()
