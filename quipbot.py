import tracery, json
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
print(grammar.flatten("#origin#"))


