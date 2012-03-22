##########################################################
################# Plagiarism detection ###################
##########################################################

#### Pre-processing
# Takes a path to a folder and prepares the files within
# that folder for a further steps.
# Ouputs list of pairs (fileid, clean_file)

import os, re


###for testing ONLY
##path = "./test"
###path = "./0818591"
##files = os.listdir(path)

# get a path
def get_path():
    try:
        path = input('Please enter the directory in " " : ')
    except NameError:
        print '\n It seems you forgot about " ". Try again'
        path = input('Please enter the directory in " " : ')
    try:
        files = os.listdir(path)
    except:
        print ("\nThis is not a valid directory\n" +
               "HINT: paths on Linux- based and Mac OS use ./" +
               " Windows uses .\\ instead.\n")
        path = input("Please enter the directory: ")
    return (path, files)

# reads a file in the folder
def read_file (path, filename):
    join = os.path.join(path, filename)
    read_filename = open(join).read()
    return read_filename

# removes punctuation and formatting noise, changes all to lower case
def remove (read_filename):
    regex = re.search("(?<=:\n\n).*", read_filename, re.DOTALL)
    match = regex.group()
    clean = match.replace("\r\n", "").replace(".", " ").replace(","," ").lower()
    return clean

# create fileid
def create_id (filename):
    fileid = filename.replace(".txt", "")
    return fileid

# Main
def prepare():
    texts = []
    (path, files) = get_path()
    for filename in files:
        read_filename = read_file(path, filename)
        clean_file = remove(read_filename)
        fileid = create_id(filename)
        texts.append((fileid, clean_file))
    return texts

if __name__ == "__main__":
    print "You are executing preprocessing.py"
    print "The output is saved in a list 'output'"
    output = prepare()

        
        
        
        
    

