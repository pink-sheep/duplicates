##########################################################
################# Plagiarism detection ###################
##########################################################

### Exact duplicates
# Detects the extact duplicates
# takes the list of preprocessed files (look preprocessing.py)
# outputs a list of exact copies

import os, hashlib, preprocessing

#for testing ONLY
path = "./test"
#path = "./0818591"
files = os.listdir(path)

# hashes files within the folder with md5 (message digest) algoritm
# creates dictionary {hash : [list of fileids]}
def hash_file (texts):
    dic = {}
    for pair in texts:
        (fileid, text) = pair
        h = hashlib.md5(text).digest()
        try:
            txtlist = dic.get(h)
            txtlist.append(fileid)
            dic[h] = txtlist
        except:
            dic[h] = [fileid]
    return dic

# get the exact duplicates
# ie. at least two text hash to the same value
def compare (dic):
    sameset = set()
    for txtlist in dic.values():
        if (len(txtlist) >= 2):
            dup_pair = " - ". join(txtlist)
            sameset.add(dup_pair)
    return sameset

# main
def exact_duplicates(texts):
    hashdic = hash_file(texts)
    return compare(hashdic)

if __name__ == "__main__":
    print "You are executing exact.py"
    print "It uses " + path + " as a path"
    print "The candidates for exact duplicates are as follows:"
    texts = preprocessing.prepare()
    output = exact_duplicates(texts)
    for item in output:
        print item
    
    
    
    

