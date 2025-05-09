import colorsys  # To use HSV colors
import pygame
from Mathy import Renderer


def julia(c: complex, z: complex, max_iter: int) -> int:
    """
    Return the number of iterations before divergence, or max_iter if bounded.
    A point is considered bounded if |zn| <= 2 after max_iter iterations.
    """
    for i in range(max_iter):
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
    t = iteration / max_iter  # Normalized index to range [0, 1]
    # Hue from 0 to 1, full saturation and brightness
    hue = t % 1.0  # wrap around
    r, g, b = colorsys.hsv_to_rgb(hue, 1.0, 1.0)
    return (int(r * 255), int(g * 255), int(b * 255))


def render_julia(renderer: Renderer,
                 c: complex,
                 max_iter=100,
                 zoom=1.0,
                 offset=(0.0, 0.0)):
    """
    Renders the Julia set, black if bounded, colored otherwise.
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

    # Draw c info
    c_text = f"c = {c.real:.5f} + {c.imag:.5f}i"
    renderer.draw_text(c_text, (10, 10), font_size=20, color=(0, 0, 0))
    renderer.update()


def main():
    width, height = 800, 600
    renderer = Renderer(
        width, height,
        "Julia Set Viewer",
        bg_color=(255, 255, 255)
    )

    # List of complex numbers for different Julia sets
    c_list = [
        complex(-0.7, 0.27015),
        complex(-0.123, 0.745),
        complex(0.355, 0.355),
        complex(-0.70176, -0.3842),
        complex(-0.4, 0.6),
    ]

    c_index = 0
    c = c_list[c_index]
    max_iter = 30
    zoom = 1.0
    offset = (0.0, 0.0)

    render_julia(renderer, c, max_iter, zoom, offset)

    while renderer.running:
        # Event loop to handle window events and key presses
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                renderer.running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                # Switch to next complex number c when SPACE is pressed
                c_index = (c_index + 1) % len(c_list)
                c = c_list[c_index]
                renderer.clear()
                render_julia(renderer, c, max_iter, zoom, offset)

        renderer.clock.tick(60)

    renderer.quit()


if __name__ == "__main__":
    main()
