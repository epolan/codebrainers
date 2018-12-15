#!/usr/bin/env python

imiona = ["Hamlet", "Macbeth", "Ophelia", "Henry"]

for imie in imiona:
    print("Jam jest {}" .format(imie))


sonet42 = """ That thou hast her it is not all my grief,
And yet it may be said I loved her dearly,
That she hath thee is of my wailing chief,
A loss in love that touches me more nearly.
Loving offenders thus I will excuse ye,
Thou dost love her, because thou know’st I love her,
And for my sake even so doth she abuse me,
Suff’ring my friend for my sake to approve her.
If I lose thee, my loss is my love’s gain,
And losing her, my friend hath found that loss,
Both find each other, and I lose both twain,
And both for my sake lay on me this cross,
  But here’s the joy, my friend and I are one,
  Sweet flattery, then she loves but me alone.
(END)"""

#for i in sonet 42.splitlines
 #   print (i, end=" ")
 
for line in sonet42.splitlines():
    for word in line.split():
        if "sake" in word:
            print(line)
    #for word in line.split():
    #sprawdzamy czy word jest równe "love"
# if word =="love":
#print(word, line)
print("podaj słowo, które chcesz wyszukać:")
slowo = input()
for line in sonet42.splitlines():
    for word in line.split():
        if slowo in word:
            print(line)
