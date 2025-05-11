import random
from collections import Counter
import pygame

from Mathy import Renderer, Triangle, Vector2

# --- Algorithm functions ---
def create_super_triangle(points) -> Triangle:
    """Create a super triangle that encompasses all points."""
    x_coords = [p[0] for p in points]
    y_coords = [p[1] for p in points]
    return Triangle(
        (0, 0),
        (max(x_coords) * 2, 0),
        (0, max(y_coords) * 2)
    )


def delaunay_triangulation(points) -> list[Triangle]:
    """Perform Delaunay triangulation on a set of points."""
    super_triangle = create_super_triangle(points)
    # Initialize the triangulation with the super triangle
    triangulation = {super_triangle}
    for p in points:
        # Find the triangles for which the circumcircle contains point p
        # Those are to be removed later on
        bad_triangles = []
        for triangle in triangulation:
            if triangle.is_point_in_circumcircle(p):
                bad_triangles.append(triangle)

        # Determine the boundary of the cavity formed by bad_triangles
        boundary_edges = []
        edge_counter = Counter()

        for triangle in bad_triangles:
            for edge in triangle.get_edges():
                # The sorted method is used to handle edges in both directions
                # e.g. (A, B) and (B, A) are the same edge
                edge_counter[tuple(sorted(edge))] += 1

        # Edges that appear in the counter only once
        boundary_edges = [
            edge for edge, 
            count in edge_counter.items() if count == 1
        ]

        # Remove bad triangles from the triangulation
        for triangle in bad_triangles:
            triangulation.remove(triangle)

        # Connect p and the boundary edges to form a new triangle
        for edge in boundary_edges:
            new_triangle = Triangle(p, edge[0], edge[1])
            triangulation.add(new_triangle)

    # Remove triangles that share vertices with the super triangle
    super_triangle_vertices = {
        super_triangle.p1, 
        super_triangle.p2, 
        super_triangle.p3
    }
    for triangle in list(triangulation):
        if (triangle.p1 in super_triangle_vertices or
                triangle.p2 in super_triangle_vertices or
                triangle.p3 in super_triangle_vertices):
            triangulation.remove(triangle)

    return list(triangulation)

def generate_random_points(num_points: int) -> list[tuple]:
    points = [(random.randint(50, 750), random.randint(50, 550)) for _ in range(num_points)]
    return points

# --- Code execution ---
def main():
    # Defining random points
    num_points = 10
    points = generate_random_points(num_points)
    render_circles = False # Set to True to render circumcircles
    key_to_randomize = pygame.K_SPACE

    # Display using Renderer
    width, height = 800, 600
    renderer = Renderer(
        width, 
        height, 
        "TP 2 - Delaunay Triangulation", 
        bg_color=(255, 255, 255)
    )
    action_text = f"Press {pygame.key.name(key_to_randomize)} to randomize points"

    def draw_triangulation(renderer, triangulation) -> None:
        """Draw the given triangulation on the renderer screen."""
        for triangle in triangulation:
            renderer.draw_triangle(
                triangle.p1,
                triangle.p2,
                triangle.p3,
                color=(0, 0, 255),  # Blue triangle
                width=1
            )
            draw_circumcircle(renderer, triangle)

    def draw_circumcircle(renderer, triangle) -> None:
        """Draw the circumcircle of a triangle."""
        if not render_circles:
            return
        circumcenter, radius = triangle.circumcircle()
        renderer.draw_circle(
            circumcenter,
            radius,
            color=(255, 0, 0),  # Red circle
            width=1
        )

    def do_render() -> None:
        # Perform triangulation and draw it
        triangulation = delaunay_triangulation(points)
        draw_triangulation(renderer, triangulation)

        # Draw points
        for point in points:
            renderer.draw_point(
                point[0],
                point[1],
                color=(0, 255, 0),  # Green point
                radius=4
            )
        
        # Draw action text
        renderer.draw_text(action_text, (10, 10), font_size=20, color=(0, 0, 0))
        renderer.update()


    while renderer.running:
        do_render()

        # Event loop to handle window events and key presses
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                renderer.running = False
            elif event.type == pygame.KEYDOWN and event.key == key_to_randomize:
                # Randomize points when the key is pressed
                renderer.clear()
                points = generate_random_points(num_points)
                do_render()
                continue

        renderer.update()
        renderer.clock.tick(60)

    renderer.quit()


if __name__ == "__main__":
    main()
