import csv
from csv import DictReader

with open('insurance.csv', newline= '') as insurance_data:
    data = DictReader(insurance_data, delimiter = ',')
    for row in data:
        print(row))


