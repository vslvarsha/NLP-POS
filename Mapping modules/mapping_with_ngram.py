# -*- coding: utf-8 -*-
import unidecode
import ngram
import unicodelist
import codecs
import time


def main():
    # tagdict = {}
    # telugumap = {}
    # tel = []

    start = time.clock()

    uniword = ""
    # tagfile = open("/Users/varsha/Downloads/telugu_clean_tagged.txt","r")
    kan = open("Kantext.txt", "r")
    out = open("Kantext_tagged.txt", "w")
    print time.clock() - start
    # a = "శ్యామలదేవి"
    # p = unicode(a,"utf-8")
    # print p
    # print unidecode.unidecode(p)

    unicodelist.sub()
    # for line in tagfile:
    #     uni = ""
    #     #print line.strip()
    #     tags = line.strip("\n").rsplit("/", 1)
    #
    #     p = unicode(tags[0],"utf-8")
    #     tagdict[p]=tags[1]
    #     uni = unidecode.unidecode(p)
    #     telugumap[uni]=p
    #     tel.append(uni)
    #
    # telNG = ngram.NGram(tel)

    telNG = ngram.NGram(unicodelist.tel)
    print time.clock() - start
    word = unicode('ಒಂದಾನೊಂದು', "utf-8")
    print time.clock() - start
    word = unidecode.unidecode(word)
    print time.clock()-start
    uniword = telNG.find(word)
    print time.clock() - start
    print uniword
    print unicodelist.telugumap[uniword]
    print unicodelist.tagdict[unicodelist.telugumap[uniword]]


    # for i in range(8):
    #     words= kan.readline().split()
    #     for word in words:
    #         wor = unicode(word,"utf-8")
    #         wor = unidecode.unidecode(wor)
    #         uniword = telNG.find(wor)
    #         str+= word+"/"+tagdict[telugumap[uniword]]+" "
    #         out.write(word+"/"+tagdict[telugumap[uniword]]+" ")
    #     i+=1

    print time.clock() - start
    for line in kan:
        words = line.split()
        str=""
        for word in words:
            print time.clock() - start
            wor = unicode(word,"utf-8")
            wor = unidecode.unidecode(wor)
            uniword = telNG.find(wor)
            print uniword
            print unicodelist.telugumap[uniword]
            print unicodelist.tagdict[unicodelist.telugumap[uniword]]

            str+= word+"/"+unicodelist.tagdict[unicodelist.telugumap[uniword]]+" "
            print time.clock() - start
        out.write(str+"\n")


if __name__ == '__main__':
    main()