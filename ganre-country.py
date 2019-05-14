import csv
import matplotlib.pyplot as plt

filename = 'films.csv'

ganres = []
countries = []

with open(filename, 'r', newline = '') as file:
    reader = csv.reader(file)
    for row in reader:

        num = 0
        range_list1 = len(countries)
        count_doubles = 0
        x = 0

        for x in range(range_list1):
            if row[6] == countries[x]:
                count_doubles += 1

        if count_doubles == 0:
            countries.append(row[6])

with open(filename, 'r', newline = '') as file: #Заполнение ganres
    reader = csv.reader(file)
    for row in reader:
        range_list2 = len(ganres)
        count_doubles2 = 0
        y = 0
        for y in range(range_list2):
            if row[7] == ganres[y]:
                count_doubles2 += 1

        if count_doubles2 == 0:
            ganres.append(row[7])   
file.close()

print(ganres)