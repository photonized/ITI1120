def indexes(word, character):
    b=[]
    for i in range(len(word)):
        if character in word[i]:
            b+=[i]
    return b

def betterindexes(word, character):
    return [i for i,char in enumerate(word) if char==character]
