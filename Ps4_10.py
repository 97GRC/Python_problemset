#!/usr/bin/env python3
import sys

#Questão 10
print('Questão 10')
first = sys.argv[1]
last = sys.argv[2]

if first.isdigit() and last.isdigit():
  first = int(first)
  last = int(last)
  count = [z for z in range(first, last)]
  print(count)

   #Printar apenas números pares
count_iter = iter(count)
for count in count_iter:
  if count % 2 == 0:
    print(count, '')
