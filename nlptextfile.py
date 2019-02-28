import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
tf='textfile.txt'
f=open(tf)
IPdata=f.read()
SentenceTokens=sent_tokenize(IPdata)
WordTokens = word_tokenize(IPdata)
POSTAG=nltk.pos_tag(WordTokens)
print("Sentence tokens are:")
print (SentenceTokens)
print("word tokens are:")
print (WordTokens)
print ("Pos Tagging is:")
print (POSTAG)
nouns={}
NounTags=['NN','NNS','NNP','NNPS']
for word, pos in POSTAG:
    if pos in NounTags:
        if word not in nouns:
            nouns[word]=1
        else:
            nouns[word]+=1    
sorted_nouns=sorted(nouns,key=nouns.get, reverse=True)
print("Frequently used nouns")
print(sorted_nouns[:5])
