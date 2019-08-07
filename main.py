import numpy as np
import cv2 as cv
import random
import string
from PIL import ImageFont, ImageDraw, Image
from skimage.util import random_noise
import json

padding = 20
spacing = 40
width = 300
height = 100

minY, maxY = 10, 50
minFontSize, maxFontSize = 45, 60

textLength = 7
lineNumber = 5


def randomString(stringLength=6):
    """Generate a random string of letters and digits """
    lettersAndDigits = 'abcdefghkmnpqrstvwxyzABCDEFGHKLMNPRSTUVWXYZ'
    return ''.join(random.choice(lettersAndDigits) for i in range(stringLength))

def randomStringDigit(stringLength=6):
    """Generate a random string of letters and digits """
    lettersAndDigits = string.ascii_letters+string.digits
    return ''.join(random.choice(lettersAndDigits) for i in range(stringLength))


def randomDigits(stringLength=6):
    """Generate a random string of letters and digits """
    digits = '12345678'
    return ''.join(random.choice(digits) for i in range(stringLength))

# Init image



#  List font

fontpaths = [
    # Chu nhoe dam
    "./fonts/font1.ttf",
    # Chu nhoe thanh
    "./fonts/font2.ttf",
    "./fonts/font2.ttf",
# Chu + ky hieu la 1
    "./fonts/font_4_hard.ttf",
# Chu + ky hieu la 2
    "./fonts/font_5_hard.ttf",
    "./fonts/font_5_hard.ttf",
#Bang so dien tu
    # "./fonts/font_6_hard.ttf",
# Hoa la canh
#     "./fonts/font_7_hard.ttf",
#     Chu bi nhoe
    "./fonts/font3.ttf",
]
data = []
for j in range(1000):
    img = np.ones((height, width, 3), np.uint8) * 255

    # Add noise

    img = random_noise(img, mode='gaussian', var=0.1 ** 2)
    img = (255 * img).astype(np.uint8)

    # Draw line
    for i in range(lineNumber):
        r = int(random.uniform(0, 255))
        g = int(random.uniform(0, 255))
        b = int(random.uniform(0, 255))
        cv.line(img,
                (random.randrange(0, width, 1), random.randrange(0, height, 1)),
                (random.randrange(0, width, 1), random.randrange(0, height, 1)),
                (r, g, b),
                1)

    text = ''
    img_pil = Image.fromarray(img)
    draw = ImageDraw.Draw(img_pil)


    for i in range(textLength):
        x = padding + spacing * i
        y = random.randrange(minY, maxY, 1)
        # font = random.choice(fonts)
        fontSize = random.randrange(minFontSize, maxFontSize, 1)
        # font = ImageFont.truetype(random.choice(fontpaths), fontSize)
        font = ImageFont.truetype(fontpaths[i], fontSize)


        characters = [
            randomString(1),
            randomDigits(1),
            randomString(1),
            randomString(1),
            randomDigits(1),
            randomString(1),
            randomString(1),
        ]
        character = characters[i]
        text += character
        # scale = random.uniform(2, 3)
        # cv.putText(img, character, (x, y), font, scale, (random.uniform(0, 255), random.uniform(0, 255), random.uniform(0, 255)), 2, cv.LINE_AA)
        r = int(random.uniform(0, 205))
        g = int(random.uniform(0, 205))
        b = int(random.uniform(0, 205))
        draw.text((x, y), character, font=font,
                  fill=(r, g, b))

        # img_pil = Image.fromarray(img)
        # draw = ImageDraw.Draw(img_pil)
        # b,g,r = 0,255,0
        # draw.text((50, 50),  text, font = font, fill = (b, g, r))

    img = np.array(img_pil)


    print text
    file_name =  randomString(1) + randomStringDigit(16)
    cv.imwrite('./images/'+file_name+'.jpg', img)
    data.append({
        'name': file_name,
        'code': text,
    })


with open('./decode/data.txt', 'w') as outfile:
    json.dump(data, outfile)


