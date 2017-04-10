import nltk
import os

def tokenize(directory,fileName):
    # tokenization each fileName
    text = str(open(directory + fileName).readlines())
    text = text.lower()
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


def readFiles(directory):
    token = []
    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            token += (tokens(directory,filename))
    #print token
    #print len(token)

    freq = frequency(token)
    #out = open("/Users/kristen/Development/nlp_project/both_tokens.txt","w")
    #out.write(str(freq))
    return freq


def sorting(freq):
    out = open("/Users/kristen/Development/nlp_project/removed-ascii/stemming/combined_dem_stem.txt","w")
    sortedList = []
    for i in range(0,len(freq.keys())):
        maxValue = 0
        maxToken = ""
        for token in freq:
            value = freq[token]
            if value > maxValue:
                maxToken = token
                maxValue = value
            else:
                continue
        out.write(str(maxToken) + ": " + str(maxValue) + "\n")
        del freq[maxToken]


    return "done"



from nltk.stem import PorterStemmer, WordNetLemmatizer
def stemLemi(token_input):
    stem_output = []
    lem_output = []
    stemmer = PorterStemmer()
    lemmatiser = WordNetLemmatizer()

    for token in token_input:
        word = stemmer.stem(token)
        stem_output.append(word)

        #print("Stem %s: %s" % ("studying", stemmer.stem("studying")))
        #print("Lemmatise %s: %s" % ("studying", lemmatiser.lemmatize("studying")))
        #print("Lemmatise %s: %s" % ("studying", lemmatiser.lemmatize("studying", pos="v")))
    freq = frequency(stem_output)
    output = sorting(freq)




token = tokenize("/Users/kristen/Development/nlp_project/removed-ascii/","combined-dem_v2.txt")
stemLemi(token)
#freq = frequency(token)
#sorting(freq)
