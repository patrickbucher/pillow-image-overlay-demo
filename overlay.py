#!/usr/bin/env python3

from PIL import Image


def merge(image_paths):
    layers = iter(image_paths)
    with Image.open(next(layers)) as overlay:
        for image_source in layers:
            with Image.open(image_source) as image:
                overlay.paste(image, (0, 0), image)
    return overlay


if __name__ == '__main__':
    images = [
        '0-background.png',
        '1-sun.png',
        '2-clouds.png',
        '3-trees.png',
        '4-birds.png',
        '5-copyright.png']
    merged = merge(images)
    merged.show()
