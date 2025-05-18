from Mathy import (
    RotationMatrix3x3,
    TranslationMatrix3x3,
    Renderer,
    HomogeneousVector3
    )


def rotate_point(x, y, theta, origin=(0, 0)):
    """
    Rotate a point around another point in a 2D plane.

    x and y are the point's coordinates.
    The rotation angle theta should be expressed in degrees, not in radians.
    """
    # Express the point's coordinates as a vector3
    vector = HomogeneousVector3(x, y)
    # Define the local transform matrix
    translation = TranslationMatrix3x3(origin[0], origin[1])
    rotation = RotationMatrix3x3(theta)
    transform = translation.prod(rotation)
    # Apply the transform matrix to the point to be rotated
    new_vector = vector.multiply_by_matrix(transform)
    # Return the coordinates of the rotated point
    return new_vector


def rotate_circle(center_local, radius, screen_origin, angle, velocity, delta_time, renderer):

    # increment angle with each passing time unit
    angle += velocity * delta_time

    # generate rotation matrix
    rot = RotationMatrix3x3(angle)

    # update circle's center coordinates
    center_world = center_local.multiply_by_matrix(rot)
    center_screen = center_world.add(screen_origin)

    # draw circle
    renderer.draw_circle((int(center_screen.x), int(center_screen.y)), radius, color=(255, 0, 0))

    # return new angle, new center world coordinates, new center screen coordinates
    return angle, center_screen


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
    local_origin = M

    # Values to represent circle C1
    D1 = 10  # distance between center of circle and center of C
    r1 = 10  # radius of circle
    T1 = 20  # rotation period in seconds
    omega1 = 360 / T1  # angular velocity
    theta1 = 8  # rotation angle in degrees

    # Define the local translation matrix
    translation1 = TranslationMatrix3x3(D1, 0)
    # Deduce the local coordinates of circle C1's center
    M1 = HomogeneousVector3(M.x, M.y).multiply_by_matrix(translation1)

    # Values to represent circle C2
    D2 = 5  # distance between center of circle and center of C
    r2 = 5  # radius of circle
    T2 = 40  # rotation period in seconds
    omega2 = 360 / T2  # angular velocity
    theta2 = 8  # rotation angle in degrees

    # Define the local translation matrix
    translation2 = TranslationMatrix3x3(D2, 0)
    # Deduce the local coordinates of circle C2's center
    M2 = HomogeneousVector3(M.x, M.y).multiply_by_matrix(translation2)

    # Display using Renderer
    width, height = 600, 600
    renderer = Renderer(
        width,
        height,
        "TP 3 - Exercice 3",
        bg_color=(255, 255, 255)
    )

    while renderer.running:
        dt = renderer.clock.tick(60) / 1000  # milliseconds
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

        theta, local_origin = rotate_circle(M, r, screen_origin, theta, omega, dt, renderer)
        theta1 = rotate_circle(M1, r1, local_origin, theta1, omega1, dt, renderer)[0]
        theta2 = rotate_circle(M2, r2, local_origin, theta2, omega2, dt, renderer)[0]

        renderer.update()

    renderer.quit()


if __name__ == "__main__":
    main()
