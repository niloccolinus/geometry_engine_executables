"""Visualize orbite of circles."""

import random

import pygame
from Mathy import (
        Renderer,
        Matrix3x3,
        TranslationMatrix3x3,
        RotationMatrix3x3,
        HomothetyMatrix3x3
)


def generate_random_circle() -> tuple[Matrix3x3, Matrix3x3]:
    """Generate a set of random circle."""
    dist = random.randfloat(10, 100)
    period = random.randfloat(50, 500)
    theta = float(360/period)
    pos = TranslationMatrix3x3(dist, 0)
    rota = RotationMatrix3x3(theta)
    return [pos, rota]


def main():
    """Run the Orbite viewer."""

    circles = [(generate_random_circle()) for _ in range(3)]

    # Display using Renderer
    width, height = 800, 600
    renderer = Renderer(
        width, height,
        "Orbite Viewer",
        bg_color=(255, 255, 255)
    )

    def do_render() -> None:

        renderer.update()

    while renderer.running:
        do_render()

        renderer.clock.tick(60)

    renderer.quit()
