import math

from Mathy import Renderer, Triangle, Vector2


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

    # --- Question 1 ---
    # Check if C lies on the circle
    on_circle = dist_C == radius
    print(f"1. C belongs to the circle of diameter AB: {on_circle}")

    # --- Question 2 ---
    # Using the Pythagorean theorem to verify that triangle ABC is right-angled
    triangle = Triangle(A, B, C)
    is_right = triangle.right_angled()
    print(f"2. Triangle ABC is right: {is_right}")

    # Question 3
    # Bisector of angle CDB
    vec_DC = Vector2(C[0] - D[0], C[1] - D[1]).normalize()
    vec_DB = Vector2(B[0] - D[0], B[1] - D[1]).normalize()
    bisector = vec_DC.add(vec_DB).normalize()

    # Point E lies along the bisector, at a distance equal to the radius
    E_vector = Vector2(D[0], D[1]).add(bisector.multiply_by_scalar(radius))
    E = (E_vector.x, E_vector.y)
    length_DE = distance(D, E)
    print(f"3. Length of segment DE: {length_DE:.2f}")

    # Display using Renderer
    width, height = 800, 600
    renderer = Renderer(width, height, "TP 2", bg_color=(255, 255, 255))

    scale = 60
    offset = (100, 400)

    def wp_to_screen(p):
        """
        Convert a 2D point (x, y) from world coordinates to screen coordinates.
        """
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
                    renderer.draw_point(
                        screen_x,
                        screen_y,
                        color=(0, 0, 0),
                        radius=2
                    )
                else:
                    renderer.draw_point(
                        screen_x,
                        screen_y,
                        color=(230, 230, 230),
                        radius=2
                    )

        # Draw the segment and circle
        renderer.draw_segment(
            wp_to_screen(A),
            wp_to_screen(B),
            color=(0, 0, 0),
            width=2
        )
        renderer.draw_circle(
            wp_to_screen(D),
            radius * scale,
            color=(0, 150, 255),
            width=2
        )

        # Draw triangle ABC
        renderer.draw_triangle(
            wp_to_screen(A),
            wp_to_screen(B),
            wp_to_screen(C),
            color=(0, 0, 0),
            width=2
        )

        # Draw points A, B, C and D (blue)
        for label, pt in zip("ABCD", [A, B, C, D]):
            x, y = wp_to_screen(pt)
            renderer.draw_point(x, y, color=(0, 0, 255), radius=4)
            renderer.draw_text(label, (x + 5, y - 20), font_size=24)

        # Draw point E (red)
        e_x, e_y = wp_to_screen(E)
        renderer.draw_point(e_x, e_y, color=(255, 0, 0), radius=4)
        renderer.draw_text("E", (e_x + 5, e_y - 20), font_size=24)

        # Draw segment DE (red)
        renderer.draw_segment(
            wp_to_screen(D),
            wp_to_screen(E),
            color=(255, 0, 0),
            width=2
        )

        renderer.update()
        renderer.clock.tick(60)

    renderer.quit()


if __name__ == "__main__":
    main()
