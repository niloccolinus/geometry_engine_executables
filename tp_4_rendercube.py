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

        # Initialize z-buffer and framebuffer for the whole frame
        width, height = renderer.width, renderer.height
        z_buffer = []
        framebuffer_color = []
        for x in range(width):
            z_buffer.append([float('inf')] * height)
            framebuffer_color.append([(0, 0, 0)] * height)

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
            )
            # Bounding box of our triangle:
            xmin = min(p1.x, p2.x, p3.x)
            xmax = max(p1.x, p2.x, p3.x)
            ymin = min(p1.y, p2.y, p3.y)
            ymax = max(p1.y, p2.y, p3.y)
            # Cicle through each pixel in the bounding box
            for x in range(int(xmin), int(xmax) + 1):
                for y in range(int(ymin), int(ymax) + 1):
                    # Compute the pixel's center
                    center_x = x + 0.5
                    center_y = y + 0.5
                    # Determine if the pixel is inside the triangle using barycentric coordinates
                    p = Vector3(center_x, center_y, 0)
                    lambda_A, lambda_B, lambda_C = barycentric_coordinates(p, p1, p2, p3)
                    if (
                        0 <= lambda_A <= 1 and
                        0 <= lambda_B <= 1 and
                        0 <= lambda_C <= 1 and
                        # Due to floating point precision issues,
                        # we allow a small tolerance for values extremely close to 1
                        abs(lambda_A + lambda_B + lambda_C - 1) < 1e-8
                    ):
                        # The pixel is inside the triangle, draw it based on its depth
                        z_pixel = lambda_A * p1.z + lambda_B * p2.z + lambda_C * p3.z
                        if z_pixel < z_buffer[x][y]:
                            # Our triangle at this pixel is closer to the camera than the previous one
                            z_buffer[x][y] = z_pixel
                            i1 = triangle.indices["pa"]
                            i2 = triangle.indices["pb"]
                            i3 = triangle.indices["pc"]
                            ## Compute the color using barycentric coordinates
                            # c_p1 = (100, 200, 100)  # Color for vertex A
                            # c_p2 = (200, 100, 100)  # Color for vertex B
                            # c_p3 = (100, 100, 200)  # Color for vertex C
                            # color_pixel = (
                            #     c_p1[0] * lambda_A + c_p2[0] * lambda_B + c_p3[0] * lambda_C,
                            #     c_p1[1] * lambda_A + c_p2[1] * lambda_B + c_p3[1] * lambda_C,
                            #     c_p1[2] * lambda_A + c_p2[2] * lambda_B + c_p3[2] * lambda_C
                            # )
                            u_pixel = (
                                cube.uvs[i1].x * lambda_A +
                                cube.uvs[i2].x * lambda_B +
                                cube.uvs[i3].x * lambda_C
                            )
                            v_pixel = (
                                cube.uvs[i1].y * lambda_A +
                                cube.uvs[i2].y * lambda_B +
                                cube.uvs[i3].y * lambda_C
                            )
                            # Clamp UVs to [0, 1] to avoid out-of-bounds
                            u_pixel = max(0, min(1, u_pixel))
                            v_pixel = max(0, min(1, v_pixel))
                            # Assuming a 150x150 image
                            x_tex = int(u_pixel * (150 - 1))
                            y_tex = int(v_pixel * (150 - 1))
                            tex_index = y_tex * 150 + x_tex
                            framebuffer_color[x][y] = (gengar_tex[tex_index])
                        renderer.draw_point(center_x, center_y, framebuffer_color[x][y], radius=2)

        # # Display points
        # for i, vertex in enumerate(cube_vertices_screen, start=1):
        #     renderer.draw_point(vertex.x, vertex.y, color=(0, 0, 0))

        renderer.update()
        renderer.clock.tick(60)

        # Increment angle
        angle_deg = (angle_deg + 1) % 360


if __name__ == "__main__":
    main()
