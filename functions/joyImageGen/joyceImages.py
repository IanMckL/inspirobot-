import os
import random
import textwrap

from PIL import Image, ImageDraw, ImageFont


def make_image(text):
    img = Image.open('assets/images/backgrounds/' + random.choice(os.listdir('assets/images/backgrounds')))
    accessory = Image.open('assets/images/lineArt/' + random.choice(os.listdir('assets/images/lineArt')))
    img.paste(accessory, (0, 0), accessory.convert("RGBA"))
    image_width, image_height = img.size
    print(image_width, image_height)
    quote = textwrap.wrap(text, width=25)
    largeFont = ImageFont.truetype('assets/fonts/Garamond.ttf', 77)
    smallFont = ImageFont.truetype('assets/fonts/Garamond.ttf', 65)

    rawImageEditable = ImageDraw.Draw(img)
    image_width, image_height = img.size

    text_top = image_height // 2 - ((len(quote) // 2) * 77)
    text_bottom = image_height // 2 + ((len(quote) // 2) * 77)

    for line in quote:
        width, height = largeFont.getsize(line)
        rawImageEditable.text(((image_width - width) / 2, text_top), line, font=largeFont, fill="black")
        text_top = text_top + 77

    rawImageEditable.text((image_width - image_width // 2.5, text_bottom + 140), '-C. Joybot C.', font=smallFont,
                          fill="black")
    img.show()
    img.save('generations/image.jpg')
