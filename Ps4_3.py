#!/usr/bin/env python3

  #Método 1
lista_1 = ['a', 'bb', 'ccc']
copia_1 = lista_1
print(lista_1)
copia_1.append('dddd')
print(lista_1)

    #Método 2
lista_2 = ['aaaa', 'bbb', 'cc']
copia_2 = lista_2.copy()
print(lista_2)
copia_2.append('d')
print(lista_2)
