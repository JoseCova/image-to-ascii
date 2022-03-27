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


def get_scaled_image() -> Any:
    """Scale the loaded image."""

    image = pygame.image.load("image/amogus.jpg")
    img_width, img_height = image.get_width() * 0.7, image.get_height() * 0.7

    return pygame.transform.scale(image,(int(img_width), int(img_height)))



def main_game() -> None:
    """Execute the program logic."""

    screen, clock = setup_pygame()
    fps = 60

    IMAGE = get_scaled_image()


    screen.fill((0, 0, 0))
    screen.blit(IMAGE, (0,0))

    pygame.display.update()
    clock.tick(fps)

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()


main_game()
