#cs3130 Assignment 2
#Janelle Montgomery
#Reading from a file and counting the word(string) frequency
#Printing out the word frequency table

from collections import Counter

def table(file):
    print("Word Frequency Table\n")
    print("---------------------------------------")
    #checking for punctuation
    file = file.replace("'", " ")
    file = file.replace("-"," ")
    file = file.replace("."," ")
    freqs = file
    freqs = freqs.lower()
    freqs = Counter(freqs.split())
    for word, count in freqs.most_common():
        if len(word) > 10:
           word = word[:9]
        print("{0:10} {1}".format(word,count))

        
    print("\n")
    print("HISTOGRAM")
    print("\n")
    for word,count in freqs.most_common():
        if len(word) > 10:
           word = word[:9]
        if count > 10:
            print("{0:10}".format(word) +"|"+ "X"*10 + " ({0})".format(count))

        else:
            multiply = int(count)
            print("{0:10}".format(word) + "|"+ "X"*count)
    
          
