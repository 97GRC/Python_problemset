#!/usr/bin/env python3

#Questão 6
print('Questão 6')
n = [101, 2, 15, 22, 95, 33, 2, 27, 72, 15, 52]
num = [int(val) for val in n]
num_iter = iter(num)
for num in num_iter:
  if num % 2 == 0:
    print(num, 'é par')

#Questão 7
print('Questão 7')
n2 = [101, 2, 15, 22, 95, 33, 2, 27, 72, 15, 52]
num2 = [int(val2) for val2 in n2]
num_iter2 = iter(num2)
for num2 in num_iter2:
  if num2 % 2 == 0:
    par = num2
    print(par)
     
n3 = [101, 2, 15, 22, 95, 33, 2, 27, 72, 15, 52]
num3 = [int(val3) for val3 in n3]
num_iter3 = iter(num3)
for num3 in num_iter3:
  if num3 % 2 != 0:
    impar = num3
    print(impar)
