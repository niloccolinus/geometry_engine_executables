"""Solve problem 3 of math lab no 3 by representing orbiting circles."""

from Mathy import (
    RotationMatrix3x3,
    TranslationMatrix3x3,
    Renderer,
    HomogeneousVector3
    )


# --- Helper functions ---
def wp_to_screen(x, y, scale, offset):
    """Convert a 2D point from world coordinates to screen coordinates."""
    a, b = offset
    screen_point = HomogeneousVector3(int(x * scale + a), int(-y * scale + b))
    return screen_point


def wc_to_screen(x, y, scale, offset):
    """Convert x and y world coordinates to screen coordinates."""
    a, b = offset
    world_point = HomogeneousVector3(int(x * scale + a), int(-y * scale + b))
    return world_point


def rotate_point(point, theta, origin):
    """
    Rotate a point around a local or global origin in a 2D plane.

    Variables point and origin are of type HomogeneousVector3.
    The rotation angle theta should be expressed in degrees, not in radians.
    """
    # Define the local transform matrix
    translation = TranslationMatrix3x3(origin.x, origin.y)
    rotation = RotationMatrix3x3(theta)
    transform = translation.prod(rotation)
    # Apply the transform matrix to the point to be rotated
    rotated_point = point.multiply_by_matrix(transform)
    # Return the coordinates of the rotated point
    return rotated_point


# --- Problem 3 solution ---
def main():
    """Simulate 2 circles orbiting around another circle."""
    # Define initial values

    # Values to represent the frame
    scale = 60
    offset = (300, 300)
    # Frame origin in world and on screen
    origin = HomogeneousVector3(0, 0)
    screen_origin = wc_to_screen(origin.x, origin.y, scale, offset)

    # Values to represent circle C
    D = 80  # distance between center of circle and origin
    M = HomogeneousVector3(D, 0)  # center of circle
    r = 20  # radius of circle
    T = 8  # rotation period in seconds
    omega = 360 / T  # angular velocity
    theta = 8  # rotation angle in degrees

    # Values to represent circle C1
    D1 = 10  # distance between center of circle and center of C
    r1 = 10  # radius of circle
    T1 = 4  # rotation period in seconds
    omega1 = 360 / T1  # angular velocity
    theta1 = 8  # rotation angle in degrees
    # Define the local translation matrix
    translation1 = TranslationMatrix3x3(D1, 0)
    # Deduce the local coordinates of circle C1's center with M as the origin
    M1 = M.multiply_by_matrix(translation1)

    # Values to represent circle C2
    D2 = 5  # distance between center of circle and center of C
    r2 = 5  # radius of circle
    T2 = 2  # rotation period in seconds
    omega2 = 360 / T2  # angular velocity
    theta2 = 8  # rotation angle in degrees
    # Define the local translation matrix
    translation2 = TranslationMatrix3x3(D2, 0)
    # Deduce the local coordinates of circle C2's center with M as the origin
    M2 = M.multiply_by_matrix(translation2)

    # Display using Renderer
    width, height = 600, 600
    renderer = Renderer(
        width,
        height,
        "TP 3 - Exercice 3",
        bg_color=(255, 255, 255)
    )

    while renderer.running:
        dt = renderer.clock.tick(60) / 1000  # delta time in milliseconds

        renderer.handle_events()
        renderer.clear()

        # Draw the grid with scaling and offset
        for x in range(-10, 11):  # Adjust the range for grid size
            for y in range(-10, 11):  # Adjust the range for grid size
                # Draw grid lines
                screen_pos = wc_to_screen(x, y, scale, offset)
                screen_x = screen_pos.x
                screen_y = screen_pos.y
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

        # Draw circle C
        # Calculate the rotation angle
        theta += omega * dt
        # Rotate the circle's center
        m_world = rotate_point(M, theta, origin)  # world coordinates
        m_screen = m_world.add(screen_origin)  # screen coordinates
        # Render the circle on-screen
        renderer.draw_circle((int(m_screen.x), int(m_screen.y)), r,
                             color=(255, 0, 0))

        # Draw circle C1
        theta1 += omega1 * dt
        m1_world = rotate_point(M1, theta1, m_world)
        m1_screen = m1_world.add(screen_origin)
        renderer.draw_circle((int(m1_screen.x), int(m1_screen.y)), r1,
                             color=(0, 255, 0))

        # Draw circle C2
        theta2 += omega2 * dt
        m2_world = rotate_point(M2, theta2, m_world)
        m2_screen = m2_world.add(screen_origin)
        renderer.draw_circle((int(m2_screen.x), int(m2_screen.y)), r2,
                             color=(0, 0, 255))

        # Caption for circle C
        renderer.draw_text(
            "C: red circle",
            (screen_origin.x + 100, screen_origin.y + 200),
            font_size=18
        )
        # Caption for circle C1
        renderer.draw_text(
            "C1: green circle",
            (screen_origin.x + 100, screen_origin.y + 225),
            font_size=18
        )
        # Caption for circle C2
        renderer.draw_text(
            "C2: blue circle",
            (screen_origin.x + 100, screen_origin.y + 250),
            font_size=18
        )

        renderer.update()

    renderer.quit()


if __name__ == "__main__":
    main()
