import spacy

nlp = spacy.load("en_core_web_sm")
doc = nlp("Apple is looking at buying U.K. startup for $1 billion")
stopwords = 0
nonstopwords = 0
for token in doc:
    print(token.text, token.pos_, token.dep_, token.lemma_, token.is_stop)

length =len(doc)
print(f'List No:{length}')

if token.is_stop == False:
    stopwords += 1
else:
    nonstopwords += 1

print(f"Number of stopwords:{stopwords}, Number of non-stopwords:{nonstopwords}")
