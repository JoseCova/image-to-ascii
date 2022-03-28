#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import pygame
from typing import Tuple, Any


def setup_pygame() -> Tuple[Any, Any]:
    """Configure game window.

    Return the screen and clock to be used by the main game function
    """
    pygame.init()

    screen_width = 1280
    screen_height = 720

    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("IMAGE TO ASCII")

    clock = pygame.time.Clock()

    return screen, clock


def get_scaled_image() -> Any:
    """Scale the loaded image."""

    image = pygame.image.load("image/jg.jpg")
    img_width, img_height = image.get_width() * 0.08, image.get_height() * 0.08

    return pygame.transform.scale(image,(int(img_width), int(img_height)))

def map_to_range(value, from_x, from_y, to_x, to_y):
    """Map the given value.

        Given the mean value calculate the corresponding index
        in the ascii_chars
    """
    return value * (to_y - to_x ) / (from_y - from_x)


def text(msg, size=15):
    """Render text. """
    return pygame.font.SysFont("consolas", size).render(msg, True, (255,255,255))   


def image_to_ascii(image, screen):
    """Convert the image to ascii."""

    ascii_chars = "_.,-=+:;cba|?0123456789$W#@"

    # The rest of this comment is the video explanation

    image.lock()

    # iterate through image as a matrix
    for i in range(image.get_width()):
        for j in range(image.get_height()):
            r, g, b, _ = image.get_at([i,j])
            average = (r + g + b) // 3
            index = round(map_to_range(average, 0, 255, 0, len(ascii_chars) - 1))

            # Create text surface for the character
            ascii_char = text(ascii_chars[index])
            screen.blit(ascii_char, (i*15, j*15))

            #pdate screen everytime we blit
            pygame.display.update()


    image.unlock()


def main_game() -> None:
    """Execute the program logic."""

    screen, clock = setup_pygame()
    fps = 60

    IMAGE = get_scaled_image()

    screen.fill((0, 0, 0))

    image_to_ascii(IMAGE, screen)

    pygame.display.update()
    clock.tick(fps)

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()


main_game()
