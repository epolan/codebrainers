#!/usr/bin/env python

lista1 = [x**2 for x in range(1,100)]
lista2 = [x**3 for x in range(1,50)]

print(lista1,lista2)
#informujmy o dlugosci listy
print ("dlugosc listy pierwszej to {}, a drugiej to {}".format(len(lista1), len(lista2)))
print("dlugosc listy pierwszej to :", len(lista1)," to ", len(lista2))

#to jest petla po elemenrach listy lista1
for el in lista1:
    if el in lista2:
        print(el)
