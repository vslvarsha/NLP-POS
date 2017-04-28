import sys
import time

def getTaggedData(fin):
    tagged_data = []
    lines = fin.readlines()
    for line in lines:
        words = line.split()
        for word in words:
            tagged_data.append(word)
    return tagged_data


def getTagCount(tagged_data):
    tag_count = {}
    for word in tagged_data:
        curent_word = word[:word.rfind('/')]
        tag = word[word.rfind('/')+1:]
        if tag not in tag_count:
            tag_count[tag] = 1
            print str(tag)
        else:
            tag_count[tag] += 1
    return tag_count

def getEmissionProbability(tagged_data, tag_count):
    wordplustag = {}
    for word in tagged_data:
        current_word = word[:word.rfind('/')]
        tag = word[word.rfind('/') + 1:]

        if current_word not in wordplustag:
            wordplustag[current_word]={}
            wordplustag[current_word][tag] = 1
        else:
            if tag not in wordplustag[current_word]:
                wordplustag[current_word][tag]=1
            else:
                wordplustag[current_word][tag]+=1

    for word in wordplustag:
        for t in wordplustag[word]:
            wordplustag[word][t] = (wordplustag[word][t] * 1.0) / tag_count[t]
    return wordplustag


def getTransitionProbability(raw_data, tag_count):
    transition = {}
    for line in raw_data:
        previous = ''
        words = line.split()
        for word in words:
            current_word = word[:word.rfind('/')]
            tag = word[word.rfind('/') + 1:]

            if previous == '':
                current = 'q0'
            else:
                current = previous

            if current not in transition:
                transition[current] = {}
                transition[current][tag] = 1
            else:
                if tag not in transition[current]:
                    transition[current][tag] = 1
                else:
                    transition[current][tag] += 1
            previous = tag

    #print transition
    for tag in transition:
        flag = 0
        total = 0
        for t in tag_count:
            if t not in transition[tag]:
                transition[tag][t] = 0
                flag = 1
        if flag == 1:
            for t in tag_count:
                transition[tag][t] += 1
        total = sum(transition[tag].values())

        for current in transition[tag]:
            transition[tag][current] = (transition[tag][current] * 1.0) / (total)

    return transition

def main():
    start = time.clock()
    '''if len(sys.argv) != 2:
        print "Missing the location of input data"
        sys.exit(1)
    else:
        f1 = sys.argv[1]
        fin = open(f1, 'r')'''

    fin = open('kannada_corpus_train_tagged.txt','r')

    tagged_data = getTaggedData(fin)
    #print tagged_data
    tag_count = getTagCount(tagged_data)
    print tag_count
    print len(tag_count)

    fin.seek(0)
    raw_data = fin.readlines()
    transition_probability = getTransitionProbability(raw_data, tag_count)
    #print transition_probability
    emission_probability = getEmissionProbability(tagged_data, tag_count)
    #print emission_probability

    fout = open('hmmmodel1.txt','w')
    fout.write(str(tag_count))
    fout.write('\n')
    fout.write(str(emission_probability))
    fout.write('\n')
    fout.write(str(transition_probability))
    fout.close()

    fin.close()
    print "Time taken"
    print (time.clock()-start)

if __name__ == '__main__':
    main()