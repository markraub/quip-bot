import tracery, json
from tracery.modifiers import base_english

rules = json.load(open("grammar.json"))


grammar = tracery.Grammar(rules)
grammar.add_modifiers(base_english)
print(grammar.flatten("#origin#"))


