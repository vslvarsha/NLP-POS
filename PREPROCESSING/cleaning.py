import string
import re

def main():
    fin = open('ajji kathe.txt', 'r')
    fout = open('clean_ajji_kathe.txt', 'w')
    data = fin.readlines()
    for line in data:
        clean_data = []
        words = line.split()
        for word in words:
            if word not in string.punctuation:
                clean_data.append(word)
        for word in clean_data:
            fout.write(word+" ")
        fout.write("\n")

    fin.close()
    fout.close()

if __name__ == '__main__':
    main()