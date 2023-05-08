import spacy

nlp = spacy.load("en_core_web_sm")
doc = nlp("Apple is looking at buying U.K. startup for $1 billion")

stopwords = 0
nonstopwords = 0
for token in doc:
    print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_, token.shape_, token.is_alpha, token.is_stop)
    if token.is_stop == False:
        nonstopwords += 1
    else:
        stopwords += 1

print(f"Number of stopwords:{stopwords}, Number of non-stopwords:{nonstopwords}")