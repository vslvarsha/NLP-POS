# -*- coding: utf-8 -*-
sentences = open("kannada_corpus_train_tagged1.txt","r")
out = open("25ktrain_crf.txt","w")

def convert():
    str = ''
    for sentence in sentences:
        sentence = sentence.split()
        for word in sentence:
            word = word.split("/")
            if len(word)!=1:
                str +=  word[0] +" "+ word [1] + "\n"
        str+="\n"
    out.write(str)

convert()