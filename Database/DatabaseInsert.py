import sqlite3

conn = sqlite3.connect('music.db')

c = conn.cursor()

f = open('fisier.txt') #numele fisierului in care ai extras datele

#citim fiecare linie din fisier, ii facem split dupa un separator unic, se fac operatii cu cuvintele reuzultate, dupa care se insereaza in BD

for line in f:
    words = line.split('separator')  #inlocuiesti cu simbolul corect

    #operatii cu cuvintele


#dupa ce prelucrezi datele, formeaza un nou fisier cu toate datele complete pentru baza de date, in aceasta ordine:
#artist, songTitle, genre, musicData
#acolo unde nu ai informatiile, gen lyrics, pune 0 ca linia pe care o formezi in fisier sa aiba toate datele pentru inserare

file = open ('noul fisier cu toate informatiile')
for line in file:
    c.execute('insert into music values (?,?,?,?)', line)

conn.commit()