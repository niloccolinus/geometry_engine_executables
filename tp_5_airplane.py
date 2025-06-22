"""Render an airplane 3D model."""

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
    """Apply successive operations to render a 3D cube on a 2D screen."""
    game_object.transform = game_object.transform.__class__()

    # Apply rotation on y axis
    angle_rad = deg_to_rad(angle_deg)
    q = Quaternion.euler_to_quaternion(0, angle_rad, 0)
    game_object.transform.rotate_quaternion(q)

    # Apply new transform
    game_object_world = game_object.renderer.convert_local_to_world(game_object)  # noqa: E501

    # Project to screen
    game_object_vertices_screen = game_object.renderer.project_vertices(
        game_object_world,
        camera,
        projection
    )

    # Display points and labels
    for i, vertex in enumerate(game_object_vertices_screen, start=1):
        renderer.draw_point(vertex.x, vertex.y, (0, 0, 0))

    # Display edges
    for i in range(0, len(game_object.indices) - 1, 3):
        p1 = (game_object_vertices_screen[game_object.indices[i]].x,
              game_object_vertices_screen[game_object.indices[i]].y)
        p2 = (game_object_vertices_screen[game_object.indices[i + 1]].x,
              game_object_vertices_screen[game_object.indices[i + 1]].y)
        p3 = (game_object_vertices_screen[game_object.indices[i + 2]].x,
              game_object_vertices_screen[game_object.indices[i + 2]].y)
        renderer.draw_triangle(p1, p2, p3, (0, 0, 0), width=2)


def main():
    """Render an airplane on screen."""
    airplane = Airplane()

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

        render_object(airplane, camera, projection, renderer, angle_deg)

        renderer.update()
        renderer.clock.tick(60)

        # Increment angle
        angle_deg = (angle_deg + 1) % 360


if __name__ == "__main__":
    main()
