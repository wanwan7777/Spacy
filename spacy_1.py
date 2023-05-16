import spacy

nlp = spacy.load("en_core_web_sm")
doc = nlp("Apple is looking at buying U.K. startup for $1 billion")

for token in doc:
    print(token.text, token.pos_, token.dep_, token.lemma_, token.is_stop)

length =len(doc)
print(f'List No:{length}')

print(ent.text, ent.start_char, ent.end_char, ent.label_)