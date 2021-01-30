#! python3
#  customSeatingCards.py - Create custom seating cards from a guest list with a flowery decoration.

import os
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

def create_card(name):
    card = Image.new('RGBA', (288, 360), 'white')
    flower = Image.open('flower.png')
    card.paste(flower, (124, 20), flower)
    draw_obj = ImageDraw.Draw(card)
    draw_obj.line([(0,0), (288, 0), (288, 360), (0, 360), (0,0)], fill='black', width=2)
    fonts_folder = '/System/Library/Fonts/Supplemental'
    custom_font = ImageFont.truetype(os.path.join(fonts_folder, 'Verdana.ttf'), 32)
    draw_obj.text((20, 100), name, fill='black', font=custom_font)

    card.save(f'{name}-invite.png')

guests = open('guests.txt').readlines()

for guest in guests:
    guest = guest.strip()
    create_card(guest)

print('All seating cards have been personalised and saved to the CWD - enjoy the dinner.')
