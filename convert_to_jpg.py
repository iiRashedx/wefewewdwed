from PIL import Image
from PIL import ImageFile


def convert(name):
    ImageFile.LOAD_TRUNCATED_IMAGES = True
    path = 'images/' + name
    if name.endswith(".png"):
        im = Image.open(path).convert('RGB')
        im.save(path, 'JPEG')
        return name
    return name
