import csv

f = open("guns.csv", 'r')

csvreader = csv.reader(f)

data = list(csvreader)

