import sys
from Mathy import Renderer


def julia(c: complex, z: complex, max_iter: int) -> int:
    """
    Returns True if the sequence zn remains bounded.
    |zn| <= 2 after max_iter iterations.
    """
    for _, i in enumerate(range(max_iter)):
        if abs(z) > 2:  # abs() is used to calculate the module
            return i  # The sequence diverges
        z = z * z + c
    return max_iter  # The sequence is bounded


def map_pixel_to_complex(x, y, width, height,
                         zoom=1.0, offset=(0.0, 0.0)) -> complex:
    """
    Maps a pixel (x, y) to a point in the complex plane.
    """
    # Center and scale pixel (x, y)
    re = (x - width / 2) / (0.5 * zoom * width) + offset[0]
    im = (y - height / 2) / (0.5 * zoom * height) + offset[1]
    return complex(re, im)


def get_color(iteration: int, max_iter: int) -> tuple:
    """
    Returns a color based on the number of iterations.
    """
    # Normalized index to range [0, 1]
    t = iteration / max_iter
    # Calculate the RGB values
    red = int(255 * (1 - t))
    green = int(255 * t)
    blue = int(255 * (0.5 - abs(t - 0.5)))
    # Return the color as an RGB tuple
    return (red, green, blue)


def render_julia(renderer: Renderer,
                 c: complex,
                 max_iter=100,
                 zoom=1.0,
                 offset=(0.0, 0.0)):
    """
    Renders the Julia set, black if bounded, white otherwise.
    """
    width, height = renderer.width, renderer.height
    for x in range(width):
        for y in range(height):
            z = map_pixel_to_complex(x, y, width, height, zoom, offset)
            iterations = julia(c, z, max_iter)
            is_bounded = iterations == max_iter
            # Get the color based on the number of iterations
            if not is_bounded:
                color = get_color(iterations, max_iter)
            else:
                color = (0, 0, 0)
            renderer.draw_point(x, y, color=color)
    renderer.update()


def main():
    width, height = 800, 600
    renderer = Renderer(width, height,
                        "Julia Set Viewer", bg_color=(255, 255, 255))

    c_list = [  # List of complex numbers for different Julia sets
        complex(-0.7, 0.27015),  # This is the default value
        complex(-0.123, 0.745),
        complex(0.355, 0.355),
        complex(-0.70176, -0.3842),
        complex(-0.4, 0.6)
    ]

    c = c_list[int(sys.argv[1])] if len(sys.argv) > 1 else c_list[0]

    max_iter = 30
    zoom = 1.0
    offset = (0.0, 0.0)

    render_julia(renderer, c, max_iter, zoom, offset)

    while renderer.running:
        renderer.handle_events()
        renderer.clock.tick(60)

    renderer.quit()


if __name__ == "__main__":
    main()
