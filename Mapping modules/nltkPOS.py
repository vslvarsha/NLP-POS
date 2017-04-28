#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import nltk
from nltk.corpus import indian
from nltk.tag import tnt

#POS tagging using NLTK inbuilt package
#NLTK indian language package not available for Kannada
def main():
    fin = open('clean_ajji_kathe.txt','r')
    fout = open('ajji_kathe_tagged.txt','w')
    data = fin.readlines()
    for line in data:
        tokens = nltk.word_tokenize(line.decode('utf-8'))
        tagged = nltk.pos_tag(tokens)
        for word in tagged:
            fout.write(word[0].encode('utf-8')+"/"+word[1]+ " ")
        fout.write("\n")
    fout.close()
    fin.close()

if __name__ == '__main__':
    main()
