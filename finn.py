##########################################################
################# Plagiarism detection ###################
##########################################################

###Finn's plateu method
# Detects the duplicates based on number density in a text
# takes the list of preprocessed files (look preprocessing.py)
# outputs a list of possible duplicates 

import hashlib, os, preprocessing, near


 ## getting tags, numbers get no-tag, non-numbers get a tag
def tagging (text):
    tags = []
    for word in text:
        try:
            a = int(word)
            tags.append(0)
        except ValueError:
            tags.append(1)
    return tags


## o(n2 version)
# maximize a and b for
# sum(x)[from 1 to a-1] + sum c* sum(1-x)[from a to b] + sum (x)[from b+1 to n]
def tagPlateau (txt):
   
    tags = tagging(txt)

    best = 0
    besta = 0
    bestb = 0
    c = 100  # inverted slope parameter
    n = len(tags)

    L = 0
    for i in range(0,n-1):
        L += tags[i]
        M = 0
        R = sum(tags[i+1:])
        for j in range(i+1,n):
            R -= tags[j]
            M += (1 - tags[j])
            sum1 = L + c*M + R
            if (sum1 > best):
                    besta = i
                    bestb = j
                    best = sum1
    return (besta, bestb)

### hash the plateu
def hash_plateu (text):
    dic = {}
    for pair in text:
        (fileid, text) = pair
        words = text.split()
        (a, b) = tagPlateau(words)
        plat = words[a:b]
        if (len(plat) > 2):
            sH = near.simHash(plat)
            for i in range(0, len(sH), 64):
                h = sH[i:i+64]
                try:
                    txtlist = dic.get(h)
                    txtlist.append(fileid)
                    dic[h] = txtlist
                except:
                    dic[h] = [fileid]
    return dic

# get the near duplicates
# ie. at least two text hash to the same value
def compare (dic):
    same = []
    sameset = set () # gets rid of the same results, for nicer display
    for txtlist in dic.values():
        if (len(txtlist) >= 2):
            dup_pair = " - ". join(txtlist)
            sameset.add(dup_pair)
    return sameset

# main
def finn_duplicates(texts):
    hashdic = hash_plateu(texts)
    return compare(hashdic)

if __name__ == "__main__":
    print "You are executing finn.py"
    print "The candidates for duplicates using Finn's metod are as follows:"
    texts = preprocessing.prepare()
    output = finn_duplicates(texts)
    for item in output:
        print item
                          

