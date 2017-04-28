import sys
import time
import math
import ast
import operator

def POStagging(data,t,e,count):
    fout = open('hmmoutput1.txt', 'w+')
    for line in data:
        state = 0
        value = 0
        previous = 'q0'
        back_pointer = {}
        state_prob = {}
        words = line.split()
        for word in words:
            if word not in e:
                for tag in count:
                    maxvalue = -9999
                    if previous != 'q0':
                        if previous not in e:
                            previous_state_list = count.keys()
                        else:
                            previous_state_list = e[previous]
                        for p in previous_state_list:
                            if t[p][tag] != 0:
                                value = state_prob[state-1][p] + math.log(t[p][tag], 10)
                            if maxvalue < value:
                                maxvalue = value
                                if state not in state_prob:
                                    state_prob[state] = {}
                                    state_prob[state][tag] = value
                                else:
                                    state_prob[state][tag] = value

                                if state not in back_pointer:
                                    back_pointer[state] = {}
                                    back_pointer[state][tag] = p
                                else:
                                    back_pointer[state][tag] = p
                    else:
                        if t['q0'][tag] != 0:
                            value = math.log(t['q0'][tag],10)
                        if state not in state_prob:
                            state_prob[state] = {}
                            state_prob[state][tag] = value
                        else:
                            state_prob[state][tag] = value

                        if state not in back_pointer:
                            back_pointer[state] = {}
                            back_pointer[state][tag] = 'q0'
                        else:
                            back_pointer[state][tag] = 'q0'

            else:
                for tag in e[word]:
                    maxvalue = -9999
                    if previous != 'q0':
                        if previous not in e:
                            previous_state_list = count.keys()
                        else:
                            previous_state_list = e[previous]
                        for p in previous_state_list:
                            if t[p][tag] !=0 and e[word][tag]!= 0:
                                value = state_prob[state - 1][p] + math.log(e[word][tag], 10) + math.log(t[p][tag], 10)
                            if maxvalue < value:
                                maxvalue = value
                                if state not in state_prob:
                                    state_prob[state] = {}
                                    state_prob[state][tag] = value
                                else:
                                    state_prob[state][tag] = value

                                if state not in back_pointer:
                                    back_pointer[state] = {}
                                    back_pointer[state][tag] = p
                                else:
                                    back_pointer[state][tag] = p
                    else:
                        if t['q0'][tag] != 0 and e[word][tag] != 0:
                            value = math.log(e[word][tag], 10) + math.log(t['q0'][tag], 10)
                        if state not in state_prob:
                            state_prob[state] = {}
                            state_prob[state][tag] = value
                        else:
                            state_prob[state][tag] = value

                        if state not in back_pointer:
                            back_pointer[state] = {}
                            back_pointer[state][tag] = 'q0'
                        else:
                            back_pointer[state][tag] = 'q0'
            state = state +1
            previous = word
            #print back_pointer
            #print state_prob[state-1]

        tagged_data = ''
        temp = max(state_prob[state-1].iteritems(), key=operator.itemgetter(1))[0]
        tagged_data = words[state-1]+'/'+temp
        for i in range(len(words)-2, -1, -1):
            temp = back_pointer[i+1][temp]
            tagged_data += ' '+ words[i] + '/' + temp
        tagged_data = ' '.join(reversed(tagged_data.split()))
        #print tagged_data
        fout.write(tagged_data)
        fout.write('\n')
    fout.close()


def F1_score(tags,predicted):
    print len(tags)
    print len(predicted)
    if len(tags) == len(predicted):
        count = 0
        divide = len(tags)
        for i, j in zip(tags, predicted):
            if i == j:
                count += 1
            if j == 'UNK':
                divide = divide -1
        print count
        print divide
        accuracy = count * 1.0 / divide
        print accuracy
    else:
        print "OH-OH"

def main():
    start = time.clock()
    '''if len(sys.argv) != 2:
        print "Missing the location of input data"
        sys.exit(1)
    else:
        fin = open(sys.argv[1], 'r')'''

    #reading untagged data
    fin = open('kannada_corpus_dev_raw.txt','r')
    untagged_data = fin.readlines()
    fin.close()

    #reading model parameters
    fmodel = open('hmmmodel.txt','r')
    lines = fmodel.readlines()
    tag_count = ast.literal_eval(lines[0])
    emission_probability = ast.literal_eval(lines[1])
    transition_probability = ast.literal_eval(lines[2])
    fmodel.close()

    #POS tagging using Viterbi algorithm and writing to file
    POStagging(untagged_data, transition_probability, emission_probability, tag_count)


    tag = []
    predicted = []
    temp1 = []
    temp2 = []
    fout  = open('junk.txt','w')
    f1 = open('kannada_corpus_dev_tagged1.txt', 'r')
    dev_tagged = f1.readlines()
    for line in dev_tagged:
        words = line.split()
        temp1.append(len(words))
        for word in words:
            tag.append(word[word.rfind('/')+1:])
    f2 = open('hmmoutput1.txt', 'r')
    train_tagged = f2.readlines()
    for line in train_tagged:
        words = line.split()
        temp2.append(len(words))
        for word in words:
            predicted.append(word[word.rfind('/') + 1:])
    fout.write(str(tag))
    fout.write(str(predicted))
    print "Accuracy"
    print F1_score(tag, predicted)


    fout.close()
    f1.close()
    f2.close()


    print "Time taken"
    print time.clock()-start

if __name__ == '__main__':
    main()

