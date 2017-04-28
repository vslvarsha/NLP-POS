# -*- coding: utf-8 -*-
from decimal import *
crfout = open("crf_ajji_25k4.txt","r")
correct = 0
incorrect = 0
for line in crfout:
    line = line.split()
    if line:
        if line[1]==line[2]:
            correct+=1
        else:
            incorrect+=1

print correct
print incorrect
print Decimal((Decimal(correct)/Decimal((correct+incorrect))))*Decimal(100)