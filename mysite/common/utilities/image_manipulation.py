# rotates an image to match it's exif information
# https://medium.com/@giovanni_cortes/rotate-image-in-django-when-saved-in-a-model-8fd98aac8f2a

from PIL import Image, ExifTags
from mysite.settings import MEDIA_ROOT
import os

def rotate_image(filepath):
  try:
    image = Image.open(filepath)
    for orientation in ExifTags.TAGS.keys():
      if ExifTags.TAGS[orientation] == 'Orientation':
            break
    exif = dict(image._getexif().items())

    if exif[orientation] == 3:
        image = image.rotate(180, expand=True)
    elif exif[orientation] == 6:
        image = image.rotate(270, expand=True)
    elif exif[orientation] == 8:
        image = image.rotate(90, expand=True)
    image.save(filepath)
    image.close()
  except (AttributeError, KeyError, IndexError):
    # cases: image don't have getexif
    pass


def create_responsive_images(filepath, url):
    try:
        srcset = ""
        widths = [100,500,1000]
        # url = url
        image = Image.open(filepath)
        longest_side = max(image.height, image.width)
        file, ext = os.path.splitext(filepath)
        # print(longest_side)
        
        for width in widths:
            if longest_side > width:
                size = (width, width)
                image_copy = image.copy()
                image_copy.thumbnail(size)
                image_copy.save(f'{file}_{image_copy.width}_{image_copy.height}{ext}')
                srcset += f"{url.split('.')[0]}_{image_copy.width}_{image_copy.height}{ext} {image_copy.width}w, "
        srcset += f"{url} {image.width}w"
        return srcset

        # if longest_side > 1000:
        #     size = (1000,1000)
        #     copy_1000 = image.copy()
        #     copy_1000.thumbnail(size)
        #     copy_1000.save(file + '_1000'+ ext)
        # if longest_side > 500:
        #     size = (500,500)
        #     copy_500 = image.copy()
        #     copy_500.thumbnail(size)
        #     copy_500.save(file + '_500'+ ext)
        # if longest_side > 100:
        #     size = (100,100)
        #     copy_100 = image.copy()
        #     copy_100.thumbnail(size)
        #     copy_100.save(file + '_100'+ ext)

    except (AttributeError, KeyError, IndexError):
        # cases: image don't have getexif
        pass
