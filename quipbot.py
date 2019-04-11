from PIL import Image, ImageDraw, ImageFont
import tracery, json, string
from tracery.modifiers import base_english

grammar_in = ""
for each in ["head.json", "prompt.json", "noun.json", "verb.json", "tail.json"]:
    grammar_in += open(each).read()
grammar_out = open("grammar.json", "w")
grammar_out.write(grammar_in)
grammar_out.close()

rules = json.load(open("grammar.json")) 


grammar = tracery.Grammar(rules)
grammar.add_modifiers(base_english)
quip = grammar.flatten("#origin#")

img = Image.open("bg.png")
fnt = ImageFont.truetype('/Lirary/Fonts/Georgia.ttf', 80)
d = ImageDraw.Draw(img)
x = 1280 
y = 720
shadowcolor = (0, 0, 0, 25)
quip_l = list(str(quip))
if d.textsize(quip, font=fnt)[0] > 2160:
    for i in range(0, len(quip_l)):
        if i > len(quip)/2:
            if quip_l[i] == " ":
                quip_l[i] = "\n"
                break
new_quip = string.join(quip_l, "")
x = x - d.textsize(new_quip, font=fnt)[0] / 2 
y = y - d.textsize(new_quip, font=fnt)[1] / 2

d.multiline_text((x+2, y+2), new_quip, font=fnt, fill=shadowcolor, align="center")
d.multiline_text((x, y), new_quip, font=fnt, fill="purple", align="center")
img.save('out.png')
print(new_quip)
print(d.textsize(new_quip, font=fnt))

