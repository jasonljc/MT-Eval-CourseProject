import config
import word_match


def get_chunk_num(h, ref):
    '''Get number of matching chunks.
    '''
    rdict = {}
    for i, w in enumerate(ref):
        if w not in rdict:
            rdict[w] = []
        rdict[w].append(i)
        
    l = len(h)

    memoize = [-1]*(l+1)
    def dfs(ind, cur, prev_match):
        ''' A simple recursion to find the best chunk matching.
            Need to memoize for large input.
        '''
        memoize[ind] = min(memoize[ind], cur) if memoize[ind] != -1 else cur
        if ind == l:
            return
        if h[ind] in rdict:
            for i in rdict[h[ind]]:
                if i==prev_match+1:
                    dfs(ind+1, cur, i)
                else:
                    dfs(ind+1, cur+1, i)
        else:
            if memoize[ind+1] != -1:
                return
            dfs(ind+1, cur, -1)
    dfs(0, 0, -2)
    return memoize[-1]
        
 
def meteor(h, ref, a, unigram_match=None):
    if not h or not ref:
        print h, ref
        return 0
    matches = word_match.word_matches(h, set(ref)) if not unigram_match else unigram_match
    recall = float(matches)/len(ref)
    precision = float(matches)/len(h)
    f_score = precision*recall/((1.0-a)*recall+a*precision) if matches!=0 else 0
    penalty = 0.5*(float(get_chunk_num(h, ref))/matches) if matches!=0 else 0
    return f_score*(1-penalty)
