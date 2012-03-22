##########################################################
################# Plagiarism detection ###################
##########################################################

#### Main - user interation
# manages the plagiarism detection program, introduces
# human-computer interaction

import os, preprocessing, near, exact, finn


def choice(texts):
    print (" For exact duplicates press - 1 \n" +
           " For near duplicates press - 2 \n" +
           " For Finn's plateu method press - 3\n" +
           " To exit press Enter\n")
    num = input("Enter your choice ")
    print "\n"
    try:
        if (num == 1):
            print "The candidates for exact duplicates are as follows:"
            de = exact.exact_duplicates(texts)
            for item in de:
                print item
            print "\n"
            choice(texts)     
        elif (num == 2):
            print "The candidates for near duplicates are as follows:"
            dn = near.near_duplicates(texts)
            for item in dn:
                print item
            print "\n"
            choice(texts)
        elif (num == 3):
            print "The candidates for duplicates using Finn's metod are as follows:"
            df = finn.finn_duplicates(texts)
            for item in df:
                print item
            print "\n"
            choice(texts)
    except:
        print "\nGood-bye"

if __name__ == "__main__":
    print "Welcome to Plagiarism Detection program\n"
    texts = preprocessing.prepare()
    choice(texts)



    
        
    
        
    

