"""Visualize orbite of circles."""

import random

import pygame
from Mathy import Renderer


def main():
    """Run the Orbite viewer."""
    width, height = 800, 600
    renderer = Renderer(
        width, height,
        "Orbite Viewer",
        bg_color=(255, 255, 255)
    )
