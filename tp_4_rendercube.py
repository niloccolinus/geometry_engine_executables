"""Render a cube using a simple rendering pipeline with rotation."""

from Mathy import (
    Cube,
    Camera,
    gengar_tex,
    Vector3,
    Projection,
    Renderer,
    Quaternion,
    deg_to_rad,
    barycentric_coordinates
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
    cube.renderer.set_mesh_data(cube)

    while renderer.running:
        renderer.handle_events()
        renderer.clear()
        cube.renderer.clear_z_buffer()

        cube.transform = cube.transform.__class__()

        # Apply rotation on y axis
        angle_rad = deg_to_rad(angle_deg)
        q = Quaternion.euler_to_quaternion(0, angle_rad, 0)
        cube.transform.rotate_quaternion(q)

        # Apply new transform
        triangles_world = cube.renderer.convert_local_to_world(cube)

        # Draw triangles
        for triangle in triangles_world:
            cube.renderer.draw_2d_triangle(
                triangle,
                camera,
                projection,
                renderer
            )
        # # Display points
        # for i, vertex in enumerate(cube_vertices_screen, start=1):
        #     renderer.draw_point(vertex.x, vertex.y, color=(0, 0, 0))

        renderer.update()
        renderer.clock.tick(60)

        # Increment angle
        angle_deg = (angle_deg + 1) % 360


if __name__ == "__main__":
    main()
