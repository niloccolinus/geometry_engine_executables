"""Render a cube using a simple rendering pipeline with rotation."""

from Mathy import (
    Cube,
    Camera,
    Vector3,
    Projection,
    Renderer,
    Quaternion,
    deg_to_rad
)


def main():
    """Render a rotating cube on screen."""
    cube = Cube()

    camera = Camera(
        position=Vector3(3, 0, 5),
        target=Vector3(0, 0, 0),
        up=Vector3(0, 1, 0)
    )

    projection = Projection(
        width=800,
        height=600,
        fov=90,
        near_plane=0.1,
        far_plane=1000
    )

    renderer = Renderer(width=800, height=600)
    angle_deg = 0

    while renderer.running:
        renderer.handle_events()
        renderer.clear()

        cube.transform = cube.transform.__class__()

        # Apply rotation on y axis
        angle_rad = deg_to_rad(angle_deg)
        q = Quaternion.euler_to_quaternion(0, angle_rad, 0)
        cube.transform.rotate_quaternion(q)

        # Apply new transform
        cube_world, triangles_world = cube.renderer.convert_local_to_world(cube)

        # Project to screen
        cube_vertices_screen = cube.renderer.project_vertices(
            cube_world,
            camera,
            projection
        )

        # Draw triangles
        for triangle in triangles_world:
            p1 = cube.renderer.project_vertices(
                [triangle.pa],
                camera,
                projection
            )[0]
            p2 = cube.renderer.project_vertices(
                [triangle.pb],
                camera,
                projection
            )[0]
            p3 = cube.renderer.project_vertices(
                [triangle.pc],
                camera,
                projection
            )[0]
            renderer.draw_triangle(
                (p1.x, p1.y),
                (p2.x, p2.y),
                (p3.x, p3.y),
                color=(0.5, 0.5, 0.5)
            ) # todo : z-buffering

        # Display points and labels
        for i, vertex in enumerate(cube_vertices_screen, start=1):
            alphabet = ["", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P"]  # noqa: E501
            renderer.draw_text(
                f"{alphabet[i]}",
                (vertex.x + 5, vertex.y + 5),
                font_size=14
            )
            renderer.draw_point(vertex.x, vertex.y, color=(0, 0, 0))

        renderer.update()
        renderer.clock.tick(60)

        # Increment angle
        angle_deg = (angle_deg + 1) % 360


if __name__ == "__main__":
    main()
