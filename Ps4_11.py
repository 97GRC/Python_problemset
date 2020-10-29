#!/usr/bin/env python3

#Questão 11
print('Questão 11')
dna = ['ATGCCCGGCCCGGC','GCGTGCTAGCAATACGATAAACCGG', 'ATATATATCGAT','ATGGGCCC']
dna_iter = iter(dna)
for dna in dna_iter:
  lenghts = len(dna)
  print(lenghts, dna , sep='\t')

#Questão 12
print('Questão 12')
dna2 = ['ATGCCCGGCCCGGC','GCGTGCTAGCAATACGATAAACCGG', 'ATATATATCGAT','ATGGGCCC']
dna_iter2 = iter(dna2)
dna3 = [len(dna2) for dna2 in dna_iter2+dna_iter2]
print(dna3)
