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
    triangles_world = game_object.renderer.convert_local_to_world(game_object)  # noqa: E501

    # Draw triangles in world space
    for triangle in triangles_world:
        game_object.renderer.draw_2d_triangle(
                triangle,
                camera,
                projection,
                renderer
        )
        
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

    airplane.renderer.set_mesh_data(airplane)
    
    while renderer.running:
        renderer.handle_events()
        renderer.clear()
        airplane.renderer.clear_z_buffer()

        render_object(airplane, camera, projection, renderer, angle_deg)

        renderer.update()
        renderer.clock.tick(60)

        # Increment angle
        angle_deg = (angle_deg + 1) % 360


if __name__ == "__main__":
    main()
