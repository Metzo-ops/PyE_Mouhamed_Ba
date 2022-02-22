from posixpath import split
import don_inv
import csv
import date
import moyenne
liste = []
liste_note = []
with open("donnees.csv", encoding='utf8') as File:
    reader = csv.reader(File)
    don_inv.func_inv(reader)
    date.dat(reader) 

    for i in reader:
        print(i)
        liste.append(i)
        liste_note = liste[6].split("#")     
        moyenne.moy(liste_note)
