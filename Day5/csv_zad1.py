# dane odzielone przecinkiem lub innym znakiem
import csv
from dataclasses import fields

fields = ['name', 'branch', 'year', 'cgpa']
row = ["Patryk", "coe", "3", "90"]
fielename = 'records.csv'
with open(fielename, "w", newline="") as fh:
    csvwriter = csv.writer(fh)
    csvwriter.writerow(fields)
    csvwriter.writerow(row)
read_fields = []
read_row = []

with open(fielename, "r") as f:
    csvreader = csv.reader(f)
    print(csvreader)

    read_fields = next(csvreader)

    for row in csvreader:
        read_row.append(row)
print(read_fields)
print(5*"-")
print(read_row)

