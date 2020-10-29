#!/usr/bin/env python3

#Questão 1
file1 = open('Python_06.txt')
contents = file1.read()
print(contents)


file1_upper = contents.upper()
print(file1_upper)

#Questão 2
file2 = open('Python_06_uc.txt', 'r')
contents2 = file2.readlines()
contents2.append(file1_upper)

file2 = open('Python_06_uc.txt', 'w')
file2.writelines(contents2)

file2.close()

#Questão 3
seq = open('Python_06.seq.txt')
contents3 = seq.read()
print(contents3)
print('')

reverse_seq = contents3.replace('A', 'B')
reverse_seq = reverse_seq.replace('C', 'D')
reverse_seq = reverse_seq.replace('G', 'H')
reverse_seq = reverse_seq.replace('T', 'U')
reverse_seq = reverse_seq.replace('B', 'T')
reverse_seq = reverse_seq.replace('D', 'G')
reverse_seq = reverse_seq.replace('H', 'C')
reverse_seq = reverse_seq.replace('U', 'A')
print(reverse_seq)

# Colocar a saída num arquivo a partir da linha de comando (>)

#Questão 4
seq2 = open('Python_06.fastq')
contents4 = seq2.readlines()

for lines in contents4:  
    print(lines)

count_line = sum(1 for line in contents4)
print('A quantidade total de linhas é:', count_line)

#for lines in contents4:
#    comp_lines = len(lines)

#comp_total = len(contents4)
#print(comp_total)

#Questão 5
