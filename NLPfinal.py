from tkinter import *
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
root=Tk()
def Token():
    IPdata=textBox.get("1.0","end-1c")
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
Label(root,text="Enter Paragraph to be Tokenied").pack(padx=50)
textBox=Text(root, height=8, width=50)
textBox.pack()
buttonCommit=Button(root, height=1, width=10, text="Tokenize",command=lambda: Token())
buttonCommit.pack()
mainloop()
