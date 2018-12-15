#!/usr/bin/env bash

mkdir -p 2018.12.15.cwiczenia

echo "To j.est nasz skrypt"

#przekierowanie do pliku przez > gdy nadpisujemy lub dodajemy do końca do konca
echo "A to zostanie zapisane w pliku stdout.txt o godzinie" $(date) >> stdout.txt

echo "sprawdzamy czy rzeczywiscie plik stdout.txt zawiera nasz napis"

date

more stdout.txt
