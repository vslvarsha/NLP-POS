import string
import re

#preprocessing output from telugu tagger and pre-tagged corpus to get data in word/tag format


def getKannadaTaggedData(fin):
    tagged_data = []
    lines = fin.readlines()
    for line in lines:
        words = line.split()
        if words != [] and words[0][0] not in string.punctuation and not re.match("[a-zA-Z0-9]", words[0][0]):
            temp = words[1].split('.')
            word = words[0]+'/'+temp[0]
            tagged_data.append(word)
    return tagged_data


def getTeluguTaggedData(fin):
    tagged_data = []
    lines = fin.readlines()
    for line in lines:
        words = line.split()
        if words != [] and words[0][0] not in string.punctuation and not re.match("[a-zA-Z0-9]", words[0][0]):
            for word in words:
                if re.match("[A-Z]", word):
                    temp = word
                    break
            word = words[0]+'/'+str(temp)
            tagged_data.append(word)
    return tagged_data

def getCleanData(fin):
    clean_data = []
    lines = fin.readlines()
    for line in lines:
        if line.rstrip():
            words = line.strip()
            clean_data.append(words+"\n")
    return clean_data

def main():
    '''fin = open('kannada_tagged.txt', 'r')
    tagged_data = getKannadaTaggedData(fin)
    fout = open('kannada_clean_tagged.txt', 'w')
    for word in tagged_data:
        fout.write(word + "\n")
    fin.close()
    fout.close()

    fin = open('telugu_tagged.txt', 'r')
    tagged_data = getTeluguTaggedData(fin)
    fout = open('telugu_clean_tagged.txt', 'w')
    for word in tagged_data:
        fout.write(word + "\n")
    fin.close()
    fout.close()

    fin = open('kannada_bible_raw.txt', 'r')
    cleaned_data = getCleanData(fin)
    fout = open('kannada_bible_clean.txt', 'w')
    for word in cleaned_data:
        fout.write(word)
    fin.close()
    fout.close()

    fin = open('telugu_bible_raw.txt', 'r')
    cleaned_data = getCleanData(fin)
    fout = open('telugu_bible_clean.txt', 'w')
    for word in cleaned_data:
        fout.write(word)
    fin.close()
    fout.close()'''

    fin = open('bible_telugu_tagged.txt', 'r')
    tagged_data = []
    lines = fin.readlines()
    for line in lines:
        words = line.split()
        if words != [] and words[0][0] not in string.punctuation and not re.match("[a-zA-Z0-9]", words[0][0]):
            for word in words:
                if re.match("[A-Z]", word):
                    temp = word
                    break
            word = words[0] + '/' + str(temp)
            tagged_data.append(word)

    fout = open('bible_telugu_clean_tagged.txt', 'w')
    for word in tagged_data:
        fout.write(word + "\n")
    fin.close()
    fout.close()

    '''mismatch_count = 0
    f_kannada = open('kannada_bible_clean.txt', 'r')
    f_telugu = open('telugu_bible_clean.txt', 'r')
    lines_kannada = f_kannada.readlines()
    lines_telugu = f_telugu.readlines()
    for l1,l2 in zip(lines_kannada,lines_telugu):
        words_kannada = l1.strip().split()
        words_telugu = l2.strip().split()
        if len(words_kannada) != len(words_telugu):
            print "Mismatch"
            mismatch_count +=1
    print mismatch_count'''

if __name__ == '__main__':
    main()