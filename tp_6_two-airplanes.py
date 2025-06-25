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
    RotationMatrix4x4_z
)


def render_object_quaternion(game_object: GameObject,
                  camera: Camera,
                  projection: Projection,
                  renderer: Renderer,
                  angle_deg: float):
    """Apply successive operations to render a 3D object on a 2D screen."""
    

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
        
def render_object_euler(game_object: GameObject,
                  camera: Camera,
                  projection: Projection,
                  renderer: Renderer,
                  angle_deg: float):
    """Apply successive operations to render a 3D object on a 2D screen."""
    

    # Apply rotation on y axis
    game_object.transform.rotate(0, angle_deg, 0)

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
    airplane1 = Airplane()
    airplane2 = Airplane()
    airplane1.transform.translate(0,0,-10)
    airplane2.transform.translate(0,0,10)

    camera = Camera(
        position=Vector3(15, 2, 0),
        target=Vector3(0, 0, 0),
        up=Vector3(0, 1, 0)
    )

    projection = Projection(
        width=1200,
        height=720,
        fov=90,
        near_plane=0.1,
        far_plane=1000
    )

    renderer = Renderer(width=1200, height=720)
    angle_deg = 0

    airplane1.renderer.set_mesh_data(airplane1)
    airplane2.renderer.set_mesh_data(airplane2)
    
    while renderer.running:
        renderer.handle_events()
        renderer.clear()
        airplane1.renderer.clear_z_buffer()
        airplane2.renderer.clear_z_buffer()

        render_object_quaternion(airplane1, camera, projection, renderer, angle_deg)
        render_object_quaternion(airplane2, camera, projection, renderer, angle_deg)

        renderer.update()
        renderer.clock.tick(60)

        # Increment angle
        angle_deg = 1 


if __name__ == "__main__":
    main()
