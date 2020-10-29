#!/usr/bin/env python3
print('1.a')
favorite_things = ['chocolate', 'Livros da Nora Roberts', 'Histórias de detetive', 'Macarrão', 'Dormir']

print('1.b')
print(favorite_things)

print('1.c')
print(favorite_things[2])

print('1.d')
favorite_things[2] = 'Some nights - FUN.'

print('1.e')
print(favorite_things)

print('1.f')
favorite_things.append('Psych')
print(favorite_things)

print('1.g')
favorite_things.insert(0,'Batata')
print(favorite_things)

print('1.h')
favorite_things.insert(3,'Inverno')
print(favorite_things)

print('1.i')
favorite_things.pop(7)
print(favorite_things)

print('1.j')
favorite_things.pop(0)
print(favorite_things)

print('1.k')
favorite_things.pop(2)
print(favorite_things)

print('1.l')
string_f_t = ', '.join(favorite_things)
print(string_f_t)
                                            
