"""Render a 3D model of an airplane."""

from Mathy import (
    Airplane,
    GameObject,
    Camera,
    Vector3,
    Projection,
    Renderer,
    Quaternion,
    deg_to_rad,
    RotationMatrix4x4_x,
    RotationMatrix4x4_y,
    RotationMatrix4x4_z,
    TotalRotationMatrix4x4,
)


def render_object(game_object: GameObject,
                  camera: Camera,
                  projection: Projection,
                  renderer: Renderer,
                  angle_deg: float,
                  mode: str = "SLERP"):
    """Apply successive operations to render a 3D object on a 2D screen."""
    game_object.transform = game_object.transform.__class__()

    # Apply rotation on y axis
    angle_rad = deg_to_rad(angle_deg)
    if mode == "SLERP":
        q = Quaternion.euler_to_quaternion(0, angle_rad, 0)
        # game_object.transform.rotate_quaternion(q)
        q.slerp(Quaternion(0, 0, 270, 0), 0.5)
        game_object.transform.rotate_quaternion(q)
    else:
        game_object.transform.lerp(
            TotalRotationMatrix4x4(
            RotationMatrix4x4_x(0),
            RotationMatrix4x4_y(angle_deg),
            RotationMatrix4x4_z(0)
            ),
            t=0.5        
        )

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
    """Render two airplanes on screen with different local coordinates."""
    airplane1 = Airplane()
    airplane2 = Airplane()

    # Set different local positions for each airplane
    airplane1.transform.position = Vector3(0, 0, 0)
    airplane2.transform.position = Vector3(5, 0, 0)
    
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

    airplane1.renderer.set_mesh_data(airplane1)
    airplane2.renderer.set_mesh_data(airplane2)
    
    while renderer.running:
        renderer.handle_events()
        renderer.clear()
        airplane1.renderer.clear_z_buffer()
        airplane2.renderer.clear_z_buffer()

        render_object(airplane1, camera, projection, renderer, angle_deg, mode="SLERP")
        render_object(airplane2, camera, projection, renderer, angle_deg, mode="LERP")

        renderer.update()
        renderer.clock.tick(60)

        # Increment angle
        angle_deg = (angle_deg + 1) % 360


if __name__ == "__main__":
    main()
