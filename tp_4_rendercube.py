"""Render a cube using a simple rendering pipeline."""

from Mathy import (
    Cube,
    Camera,
    Vector3,
    Projection,
    Renderer
)


def main():
    """Render a cube on screen."""
    cube = Cube()
    cube_world = cube.renderer.convert_local_to_world(cube)
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
    cube_vertices_screen = cube.renderer.project_vertices(
        cube_world,
        camera,
        projection
    )
    renderer = Renderer(width=800, height=600)

    while renderer.running:
        renderer.handle_events()
        renderer.clear()
        for vertex in cube_vertices_screen:
            renderer.draw_point(vertex.x, vertex.y, color=(0, 0, 0))
        for i in range(0, len(cube.indices) - 1, 2):
            start = (cube_vertices_screen[cube.indices[i]].x,
                     cube_vertices_screen[cube.indices[i]].y)
            end = (cube_vertices_screen[cube.indices[i + 1]].x,
                   cube_vertices_screen[cube.indices[i + 1]].y)
            renderer.draw_segment(start, end, color=(0, 0, 0), width=2)

        renderer.update()
        renderer.clock.tick(60)


if __name__ == "__main__":
    main()
