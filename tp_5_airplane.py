"""Render a 3D model of an airplane."""

from Mathy import (
    Airplane,
    GameObject,
    Camera,
    Vector3,
    Projection,
    Renderer,
    Quaternion,
    deg_to_rad
)


def render_object(game_object: GameObject,
                  camera: Camera,
                  projection: Projection,
                  renderer: Renderer,
                  angle_deg: float):
    """Apply successive operations to render a 3D object on a 2D screen."""
    game_object.transform = game_object.transform.__class__()

    # Apply rotation on y axis
    angle_rad = deg_to_rad(angle_deg)
    q = Quaternion.euler_to_quaternion(0, angle_rad, 0)
    game_object.transform.rotate_quaternion(q)

    # Apply new transform
    game_object_world, triangles_world = game_object.renderer.convert_local_to_world(game_object)  # noqa: E501

    # Project to screen
    game_object_vertices_screen = game_object.renderer.project_vertices(
        game_object_world,
        camera,
        projection
    )

    # Display vertices
    for vertex in game_object_vertices_screen:
        renderer.draw_point(vertex.x, vertex.y, (0, 0, 0))

    # Draw triangles
    for triangle in triangles_world:
        p1 = game_object.renderer.project_vertices(
            [triangle.pa],
            camera,
            projection
        )[0]
        p2 = game_object.renderer.project_vertices(
            [triangle.pb],
            camera,
            projection
        )[0]
        p3 = game_object.renderer.project_vertices(
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

def main():
    """Render an airplane on screen."""
    airplane = Airplane()

    camera = Camera(
        position=Vector3(10, 2, -5),
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

        render_object(airplane, camera, projection, renderer, angle_deg)

        renderer.update()
        renderer.clock.tick(60)

        # Increment angle
        angle_deg = (angle_deg + 1) % 360


if __name__ == "__main__":
    main()
