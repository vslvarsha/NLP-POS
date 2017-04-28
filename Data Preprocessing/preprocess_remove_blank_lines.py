#program to remove blank lines in the file
out = open("kannada_bible_clean.txt","w")
with open("kannada_bible.txt","r") as istr:
    new_par = False
    for line in istr:
        line = line.strip()
        if not line:  # blank
            new_par = True
            continue
        if new_par:
            out.write("\n")  # print a single blank line
        out.write(' '.join(line.split()))
        new_par = False