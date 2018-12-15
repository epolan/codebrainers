




#!/usr/bin/env bash
grep -c -i Hamlet william.sheakespeare
grep -c -i Ophelia william.sheakespeare
grep -c -i "Lady Macbet" william.sheakespeare
grep -c -i Lady william.sheakespeare

#definiujemy plik
text=william.sheakespeare
#definiujemy liste imion
names="Hamlet Macbeth Ophelia Henr all also"

# robimy petle po kolejnych imionach
for name in  $names
do
#wyswietlamy nazwe zmiennej
echo -name $name ":"

#sprawdzany ile razy zmienna wystepuje w pliku
grep -c $name $text 
grep -c -i $name $text
grep -c -i -w $name $text
grep -c -i $name $text
done

text="Praca skonczona"

echo $text