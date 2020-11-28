from PIL import Image
import glob, os

'''
The following script creates nice thumbnails of all JPEG images in the current directory 
preserving aspect ratios with 128x128 max resolution.
'''
def create_thumbs(folder="*.jpg", size = (128, 128)):
    for infile in glob.glob("*.jpg"):
        file, ext = os.path.splitext(infile)
        im = Image.open(infile)
        im.thumbnail(size)
        im.save(file + ".thumbnail", "JPEG")