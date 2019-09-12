import csv
from csv import DictReader
from decimal import Decimal

listaPrecios = []

with open('python.csv', newline='') as File:  
    reader = csv.reader(File)
    for row in reader:  
        listaPrecios.append(row[0].replace(',',"."))


#print(listaPrecios)
listaPrecios.reverse()
#print(listaPrecios)

for i in range(len(listaPrecios)):
    print(listaPrecios[i], end=" ")

     