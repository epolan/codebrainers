#!/usr/bin/env python

lista1 = [x**2 for x in range(1,100)]
lista2 = [x**3 for x in range(1,50)]

print(lista1,lista2)

print ("dlugosc listy pierwszej to {}, a drugiej to {}".format(len(lista1),len(lista2)))
print("dlugosc listy pierwszej to :",len(lista1)," to ",len(lista2))
#to jest petla po elemenrach listy lista1
for el in lista2:
    #wypisuje elementy listy
    print(el)

#definiujemy liczbe
liczba = 25

#instrukcja waunkow.Sorawdzamy czy liczba wystepuje w lista2
if liczba in lista2:
    #jesli tak to wypisz
    print(liczba, "jest w lista")
else:
    #jesli nie to wpisz
    print(liczba, "nie ma w lista2")    