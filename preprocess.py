from nltk.corpus import wordnet as wn

def is_punctuation(c):
    return c == ',' or c == '.' or c == ':' or c == '*'

def morphy_stem(word):
    """
    Simple stemmer
    """
    
    def strip_punctuation(word):
        while word and is_punctuation(word[-1]):
            word = word[:-1]
        return word
        
    word = strip_punctuation(word)
    stem = wn.morphy(word)
    if stem:
        return stem.lower()
    else:
        return word.lower()

def remove_punctuations(list_):
    ret = []
    for w in list_:
        try:
            nw = morphy_stem(w)
            if nw:
                ret.append(nw)
        except e:
            print list_
            raise e
    return ret