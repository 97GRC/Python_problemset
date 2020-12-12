#!/usr/bin/env python3

#Problemset 10
#Questão 4

import sys

File = sys.argv[1]
lenght = int(sys.argv[2])

fastaDict={}
seqName=''
newData=''
with open(File,"r") as file_object:
    for line in file_object:
        line = line.rstrip()
        if(line.startswith(">")):
            seqName=line.split(' ')[0]
            seqName=seqName.replace('>','')
            newData=''
        else:
            newData += line
            fastaDict[seqName] = newData

Id = fastaDict.keys()
Id_str = [str(i) for i in Id]
seq = fastaDict.values() #Lista apenas com as sequencias de DNA
seq_str = [str(i) for i in seq] #Transformando as sequências em string

dna = 'TAGTAGCTAGTCGAATCGCCGATGATGCTATCGACTACGATCGATGCATGCATGCATGCATGCATGCATCGATGCATGCATGCATGCATGCATCGATCGATCGATGCATGCATGCATGCATGCATCGATGCATGCATCGCCGCGGCATATATATACTGGGCGCTAATTA'

def dna_split(dna, lenght):
        n = lenght
        dna2 = dna.replace('\n','')
        dna_list = [dna2[i:i+n] for i in range(0, len(dna2), n)]
        dna3 = '\n'.join(dna_list)
        return dna3


#print(dna_split(seq_str[0], 80))

value = 0
seq_edit = []
for i in seq_str:
	edit = seq_str[value]
	value += 1
	split = [dna_split(edit, lenght)]
	seq_edit.append(split)

print(seq_edit)

