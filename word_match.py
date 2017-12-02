import config
from nltk.corpus import wordnet as wn

def get_synonyms(word):
	synonyms = set()
	syns = wn.synsets(word)
	for syn in syns:
		lemmas = syn.lemmas()
		for lemma in lemmas:
			synonyms.add(lemma.name())
	synonyms = list(synonyms)
	return synonyms
	
	
def word_matches(h, ref):
    if config.synonym == True:
        rset = set()
        rset.update(ref)
        for w in ref:
            rset.update(get_synonyms(w))
        print rset
        return sum(1 for w in h if w in rset)
    return sum(1 for w in h if w in ref)