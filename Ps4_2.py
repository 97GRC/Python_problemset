#!/usr/bin/env python3

taxa = 'sapiens erectus neanderthalensis'
print(taxa)
print(taxa[1])
print(type(taxa))
species = taxa.split()
print(species)
print(species[1])
print(type(species))
ordem_alf = sorted(species)
print(ordem_alf)
ordem_len = sorted(species, key=len)
print(ordem_len)

