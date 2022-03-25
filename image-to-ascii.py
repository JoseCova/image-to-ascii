#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import pygame
from typing import Tuple, Any


def setup_pygame() -> Tuple[Any, Any]:
    """Configure game window.

    Return the screen and clock to be used by the main game function
    """

    screen_width = 1280
    screen_height = 720

    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("IMAGE TO ASCII")

    clock = pygame.time.Clock()

    return screen, clock


def main_game() -> None:
    """Execute the program logic."""

    screen, clock = setup_pygame()
    fps = 60

    screen.fill(0, 0, 0)
    pygame.display.update()
    clock.tick(fps)

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()


main_game()
