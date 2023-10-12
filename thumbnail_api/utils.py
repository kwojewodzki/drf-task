import os
from io import BytesIO
from PIL import Image as PILImage
from django.core.files.uploadedfile import SimpleUploadedFile
from .models import Image


def convert_to_thumbnails(pk):
    instance = Image.objects.get(id=pk)

    user_tier = instance.owner.tier
    tier_thumbnails = user_tier.get_thumbnail_size()
    filename, extension = os.path.splitext(os.path.basename(instance.image_url.name))
    image_name = filename.split("/")[-1]
    print(filename)
    for size in tier_thumbnails:
        width, height = 200, int(size)

        img_file = BytesIO(instance.image_url.read())
        image = PILImage.open(img_file)

        thumb = image.resize((width, height))
        thumbnail_io = BytesIO()

        thumb.save(
            thumbnail_io,
            format='JPEG' if extension.lower() == 'jpg' else 'PNG',
            quality=100)
        thumbnail_name = f'{image_name}_thumb{width}x{height}{extension.lower()}'
        print(thumbnail_name)
        thumb_file = SimpleUploadedFile(
            thumbnail_name,
            thumbnail_io.getvalue(),
            content_type="image/jpg" if extension.lower() == 'jpg' else 'image/png')
        instance.image_url.save(thumbnail_name, thumb_file, save=False)
