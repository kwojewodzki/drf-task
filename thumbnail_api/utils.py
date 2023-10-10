from imagekit import ImageSpec
from imagekit.processors import ResizeToFill


class Thumbnail(ImageSpec):
    processors = [ResizeToFill(400, 200)]
    format = 'JPEG'
    options = {'quality': 60}
