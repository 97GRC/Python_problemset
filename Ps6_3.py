#!/usr/bin/env python3

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

