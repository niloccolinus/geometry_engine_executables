import sys
import os
import math


from geometry_engine_librairie.Mathy.renderer import Renderer


# --- Utility functions ---
def distance(p1, p2):
    """Return the Euclidean distance between two 2D points."""
    dx = p1[0] - p2[0]
    dy = p1[1] - p2[1]
    return math.sqrt(dx**2 + dy**2)

def midpoint(p1, p2):
    """Return the midpoint between two 2D points."""
    return ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)

def main():
    # Define points
    A = (0, 0)
    B = (4, 0)
    C = (2, 2)

    # Compute circle of diameter AB
    D = midpoint(A, B)  # Midpoint of A and B (center of the circle)
    radius = distance(A, B) / 2  # Radius is half the distance between A and B
    dist_C = distance(D, C)  # Distance from D to C

    # Check if C lies on the circle
    on_circle = dist_C == radius
    print(f"1. C belongs to the circle of diameter AB: {on_circle}")

    # Display using Renderer
    width, height = 800, 600
    renderer = Renderer(width, height, "TP 2", bg_color=(255, 255, 255))

    scale = 60
    offset = (100, 400)

    def wp_to_screen(p):
        """Convert a 2D point (x, y) from world coordinates to screen coordinates."""
        return (int(p[0] * scale + offset[0]), int(-p[1] * scale + offset[1]))

    def wc_to_screen(x, y):
        """Convert x and y world coordinates to screen coordinates."""
        return (int(x * scale + offset[0]), int(-y * scale + offset[1]))

    while renderer.running:
        renderer.handle_events()
        renderer.clear((255, 255, 255))

        # Draw the grid with scaling and offset
        for x in range(-10, 11):  # Adjust the range for grid size
            for y in range(-10, 11):  # Adjust the range for grid size
                # Draw grid lines
                screen_pos = wc_to_screen(x, y)
                screen_x = screen_pos[0]
                screen_y = screen_pos[1]

                if x == 0 or y == 0:  # Draw the x and y axes in black
                    renderer.draw_point(screen_x, screen_y, color=(0, 0, 0), radius=2)
                else:
                    renderer.draw_point(screen_x, screen_y, color=(230, 230, 230), radius=2)

        # Draw the segment and circle
        renderer.draw_segment(wp_to_screen(A), wp_to_screen(B), color=(0, 0, 0), width=2)
        renderer.draw_circle(wp_to_screen(D), radius * scale, color=(0, 150, 255), width=2)

        # Draw points A, B, and C
        for label, pt in zip("ABC", [A, B, C]):  # Combine labels with points (A, B, C)
            x, y = wp_to_screen(pt)
            renderer.draw_point(x, y, color=(0, 0, 255), radius=4)
            renderer.draw_text(label, wp_to_screen(pt), font_size=24)

        renderer.update()
        renderer.clock.tick(60)

    renderer.quit()

if __name__ == "__main__":
    main()
