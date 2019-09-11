import csv
from csv import DictReader
import subprocess
process1 = subprocess.Popen(['scrapy', 'scrapy runspider example.py -o python.csv -t csv'])

with open('python.csv', newline='') as File:  
    reader = csv.reader(File)
    for row in reader:
        print(row)


