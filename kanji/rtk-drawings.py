# coding:utf8
from PIL import Image, ImageDraw, ImageFont
import pandas as pd


def draw_text_centered(draw, text, color, font, bounds):
    w, h = draw.textsize(text, font=font)
    draw.text(((bounds.W - w) / 2, (bounds.H - h) / 2), text, fill=color, font=font)


font_small = ImageFont.truetype('../assets/font/MSMINCHO.TTF', 12)
font_large = ImageFont.truetype('../assets/font/MSMINCHO.TTF', 32)

col_list = ['kanji', 'id_6th_ed', 'keyword_6th_ed']
df = pd.read_csv("kanji-index.csv", usecols=col_list)

# config
draw_lines = True
padding = 2
template_color = 'black'


def generate_rtk_template(num):
    img = Image.new('RGBA', (1280, 1280), (255, 255, 255, 0))
    draw = ImageDraw.Draw(img)
    draw.fontmode = "1"  # remove antialias
    for i in range(0, 100):
        origin = ((i % 10) * 128 + padding, i // 10 * 128 + padding)
        number = num + i
        draw.text(origin, f"{number}", template_color, font=font_small)
        kanji = df.loc[number, 'kanji']
        draw.text((origin[0] - padding, origin[1] + 15), kanji, template_color, font=font_large)
        meaning = df.loc[number, 'keyword_6th_ed']
        draw.text((origin[0], origin[1] + 112), meaning, template_color, font=font_small)
    if draw_lines:
        for i in range(0, 10):
            draw.line((0, 128 * i, img.size[0], 128 * i), template_color)
            draw.line((128 * i, 0, 128 * i, img.size[1]), template_color)

    img.save(f'../assets/output/rtk_{num}s.png', 'PNG')


for n in range(0, 2000, 100):
    generate_rtk_template(n)
