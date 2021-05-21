#!/usr/bin/env python3

from tempfile import NamedTemporaryFile

from PIL import Image
from reportlab.lib.pagesizes import A2
from reportlab.lib.pagesizes import landscape
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Image as PDFImage


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
    doc = SimpleDocTemplate('landscape.pdf', pagesize=landscape(A2))
    with NamedTemporaryFile(suffix='.png') as f:
        merged.save(f.name)
        image = PDFImage(f.name, 1024, 768)
        doc.build([image])
