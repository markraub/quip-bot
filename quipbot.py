from PIL import Image, ImageDraw, ImageFont
import tracery, json, os
from tracery.modifiers import base_english
import spacy

def buildGrammar(data_list):
    grammar_in = ""
    for each in data_list:
        grammar_in += open(each).read()
    grammar_out = open("static/grammar.json", "w")
    grammar_out.write(grammar_in)
    grammar_out.close()
    return json.load(open("static/grammar.json"))



def GenerateImage():
    nlp = spacy.load("en_core_web_md")
    grammar_in = ""
    rules = buildGrammar(["static/head.json", "static/prompt.json", "static/noun.json", "static/verb.json", "static/tail.json"])
    grammar = tracery.Grammar(rules)
    grammar.add_modifiers(base_english)
    prompt_pre = grammar.flatten("#prompt#")
    prompt_break = nlp(prompt_pre)
    print("Nouns: ", [chunk.text for chunk in prompt_break.noun_chunks])
    print("Verbs: ", [token.lemma_ for token in prompt_break if token.pos_ == "VERB"])
    for entity in prompt_break.ents:
        print(entity.text, entity.label_)


    quip = prompt_pre
    img = Image.open("static/bg.png")
    fnt = ImageFont.truetype('static/Georgia.ttf', 100)
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
    new_quip = str.join("", quip_l)
    x = x - d.textsize(new_quip, font=fnt)[0] / 2 
    y = y - d.textsize(new_quip, font=fnt)[1] / 2

    d.multiline_text((x+3, y+3), new_quip, font=fnt, fill=shadowcolor, align="center")
    d.multiline_text((x, y), new_quip, font=fnt, fill="purple", align="center")
    img.save('static/out.png')
    os.popen("rm -f static/grammar.json")


if __name__ == "__main__":
    GenerateImage()
