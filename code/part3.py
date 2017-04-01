import nltk
import os

def tokens(directory,fileName):
    # tokenization each fileName
    text = str(open(directory + fileName).readlines())
    token = nltk.word_tokenize(text)
    return token


def frequency(tokens):
    tokenFreq = {}
    for token in tokens:
        if token in tokenFreq.keys():
            tokenFreq[token] += 1
        else:
            tokenFreq[token] = 1

    #print tokenFreq
    return tokenFreq


def sorting(freq):
    for key in freq.keys():
        if freq[key] > 10:
            print key + ": " + str(freq[key])
    return "done"

def readFiles(directory):
    token = []
    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            token += (tokens(directory,filename))
    #print token
    #print len(token)

    freq = frequency(token)
    out = open("/Users/kristen/Development/nlp_project/both_tokens.txt","w")
    out.write(str(freq))
    return freq





readFiles("/Users/kristen/Development/nlp_project/forums_v2/both/")
