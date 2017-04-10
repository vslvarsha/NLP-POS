import unidecode
import ngram
import codecs
import time

tagdict = {}
telugumap = {}
tel = []

def sub():
    global tagdict
    global telugumap
    global tel

    start = time.clock()
    tagfile = open("telugu_clean_tagged.txt","r")

    for line in tagfile:
        uni = ""
        # print line.strip()
        tags = line.strip("\n").rsplit("/", 1)

        p = unicode(tags[0],"utf-8")
        tagdict[p] = tags[1]
        uni = unidecode.unidecode(p)
        telugumap[uni] = p
        tel.append(uni)
    print time.clock() - start


if __name__ == '__main__':
    sub()