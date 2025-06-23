"""Code used to verify questions 1-6 in math lab 2."""

from Mathy import Renderer, Triangle, Vector2


# --- Utility functions ---
def distance(p1, p2):
    """Return the Euclidean distance between two 2D points."""
    dx = p1[0] - p2[0]
    dy = p1[1] - p2[1]
    return (dx**2 + dy**2) ** 0.5


def midpoint(p1, p2):
    """Return the midpoint between two 2D points."""
    return ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)


def main():
    """Solve questions 1-6."""
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
    on_circle = abs(dist_C - radius) < 1e-9
    print(f"1. C belongs to the circle of diameter AB: {on_circle}")

    # --- Question 2 ---
    # Using the Pythagorean theorem to verify that triangle ABC is right-angled
    triangle = Triangle(A, B, C)
    is_right = triangle.right_angled()
    print(f"2. Triangle ABC is right: {is_right}")

    # --- Question 3 ---
    # Bisector of angle CDB
    vec_DC = Vector2(C[0] - D[0], C[1] - D[1]).normalize()
    vec_DB = Vector2(B[0] - D[0], B[1] - D[1]).normalize()
    bisector = vec_DC.add(vec_DB).normalize()

    # Point E lies along the bisector, at a distance equal to the radius
    E_vector = Vector2(D[0], D[1]).add(bisector.multiply_by_scalar(radius))
    E = (E_vector.x, E_vector.y)
    length_DE = distance(D, E)
    print(f"3. Length of segment DE: {length_DE:.2f}")

    # --- Question 4 ---
    # Point F is the second intersection of the circle C2 with the bisector
    F_vector = Vector2(D[0], D[1]).add(bisector.multiply_by_scalar(2 * radius))
    F = (F_vector.x, F_vector.y)
    length_DF = distance(D, F)
    print(f"4. Length of segment DF: {length_DF:.2f}")

    # --- Question 5 ---
    # Point G lies along the x axis, on the same axis as points A, D and B
    # Point G is such that line (FG) and line (BE) are parallel
    # Using Thales's theorem to find G's coordinates
    length_DB = distance(D, B)
    length_DG = (length_DF / length_DE) * length_DB
    length_AD = distance(A, D)
    length_AG = length_AD + length_DG
    G = (length_AG, 0)
    print(f"5. Coordinates of point G : {G}")

    # --- Question 6 ---
    # Display using Renderer
    width, height = 800, 600
    renderer = Renderer(
        width,
        height,
        "TP 2 - Visualization",
        bg_color=(255, 255, 255)
    )

    scale = 60
    offset = (100, 400)

    def wp_to_screen(p):
        """Convert a 2D point from world coordinates to screen coordinates."""
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

        # Draw segment AB
        renderer.draw_segment(
            wp_to_screen(A),
            wp_to_screen(B),
            color=(0, 0, 0),
            width=2
        )

        # Draw circle C1
        renderer.draw_circle(
            wp_to_screen(D),
            radius * scale,
            color=(0, 150, 255),
            width=2
        )
        # Label for circle C1
        d_x, d_y = wp_to_screen(D)
        renderer.draw_text(
            "C1",
            (d_x + 0.7 * radius * scale, d_y + 0.7 * radius * scale),
            font_size=18
        )

        # Draw circle C2
        renderer.draw_circle(
            wp_to_screen(E),
            radius * scale,
            color=(0, 150, 255),
            width=2
        )
        # Label for circle C2
        e_x, e_y = wp_to_screen(E)
        renderer.draw_text(
            "C2",
            (e_x + 0.7 * radius * scale, e_y + 0.7 * radius * scale + 5),
            font_size=18
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

        # Draw point F (green)
        f_x, f_y = wp_to_screen(F)
        renderer.draw_point(f_x, f_y, color=(0, 255, 0), radius=4)
        renderer.draw_text("F", (f_x + 5, f_y - 20), font_size=24)

        # Draw point G (magenta)
        g_x, g_y = wp_to_screen(G)
        renderer.draw_point(g_x, g_y, color=(255, 0, 255), radius=4)
        renderer.draw_text("G", (g_x + 5, g_y - 20), font_size=24)

        # Extend the bisector far enough in its direction
        long_vector = bisector.multiply_by_scalar(100)
        delta_end = Vector2(D[0], D[1]).add(long_vector)

        renderer.draw_segment(
            wp_to_screen(D),
            wp_to_screen((delta_end.x, delta_end.y)),
            color=(255, 0, 0),
            width=2
        )

        # Extend the axis generated by vector e1 = (1, 0)
        axis = Vector2(1, 0).multiply_by_scalar(100)
        axis_end = Vector2(A[0], A[1]).add(axis)
        renderer.draw_segment(
            wp_to_screen(B),
            wp_to_screen((axis_end.x, axis_end.y)),
            color=(230, 230, 230),
            width=2
        )

        # Draw line (d)
        vector_BE = Vector2(B[0] - E[0], B[1] - E[1]).normalize()
        line_d = vector_BE.multiply_by_scalar(100)
        line_end = Vector2(B[0], B[1]).add(line_d)
        line_end2 = Vector2(B[0], B[1]).subtract(line_d)

        renderer.draw_segment(
            wp_to_screen(B),
            wp_to_screen((line_end.x, line_end.y)),
            color=(255, 255, 0),
            width=2
        )
        renderer.draw_segment(
            wp_to_screen(B),
            wp_to_screen((line_end2.x, line_end2.y)),
            color=(255, 255, 0),
            width=2
        )

        # Label for line (d)
        b_x, b_y = wp_to_screen(B)
        renderer.draw_text("(d)", (b_x + 30, b_y + 50), font_size=24)

        # Draw line (d')
        vector_GF = Vector2(G[0] - F[0], G[1] - F[1]).normalize()
        parallel = vector_GF.multiply_by_scalar(50)
        parallel_end = Vector2(G[0], G[1]).add(parallel)
        parallel_end2 = Vector2(G[0], G[1]).subtract(parallel)

        renderer.draw_segment(
            wp_to_screen(G),
            wp_to_screen((parallel_end.x, parallel_end.y)),
            color=(255, 255, 0),
            width=2
        )
        renderer.draw_segment(
            wp_to_screen(G),
            wp_to_screen((parallel_end2.x, parallel_end2.y)),
            color=(255, 255, 0),
            width=2
        )

        # Label for line (d')
        renderer.draw_text("(d')", (g_x + 30, g_y + 50), font_size=24)

        renderer.update()
        renderer.clock.tick(60)

    renderer.quit()


if __name__ == "__main__":
    main()
