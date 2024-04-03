# Know image size
from PIL import Image

im = Image.open('./experiment/test/results-DIV2K/00001_x4_SR.png')
width, height = im.size
print(width, height)