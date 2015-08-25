__author__ = 'Administrator'
import random
import string
import Image
import ImageFont
import ImageDraw
import ImageFilter

lst = [random.choice(string.letters) for i in range(4)]

im = Image.new('RGB', (50*4, 50), (255, 255, 255))
draw = ImageDraw.Draw(im)
font = ImageFont.truetype('DejaVuSans.ttf', 24)

def randColor1():
    return (random.randit(64, 255), random.randint(64, 255), random.randint(64, 255))

def randColor2():
    return (random.randit(32, 127), random.randint(32, 127), random.randint(32, 127))

for x in range(50*4):
    for y in range(50):
        im.point((x, y), randColor1())

for i in range(4):
    draw.text((10+i*50, 10), lst[i], randColor2(), font=font)

im = im.filter(ImageFilter.BLUR)
im.save('result.jpg')
im.show()