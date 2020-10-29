#!/usr/bin/env python3

#Questão 1
fav_thinks = {'book': 'Trilogia A escolhida', 'song': 'Some nights', 'tree': 'Farinha-seca'}
print(fav_thinks)

#Questão 2
print(fav_thinks['book'])

#Questão3
fav_t = 'book'
print(fav_thinks[fav_t])

#Questão 4
print(fav_thinks['tree'])

#Questão 5
fav_thinks['organism'] = 'bird'
print(fav_thinks)

fav_t = 'organism'
print(fav_thinks[fav_t])

#Questão 6
import sys

print(fav_thinks.keys())
fav_list = [fav_thinks.keys()]
print(fav_list[1])

#choice = sys.argv[1]





