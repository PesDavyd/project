import csv
import matplotlib.pyplot as plt

filename = 'films.csv'

countries = []
countries_films = []



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

num = 0

size = len(countries)

for num in range(size):
    count = 0
    with open(filename, 'r', newline = '') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[6] == countries[num]:
                count += 1
        
        countries_films.append(count)
    file.close()

def films_bar(x, y):
    plt.bar(x, y, color = 'brown')

    plt.xlabel('Country')
    plt.ylabel('Films')
    
    plt.title('Top cinema-country')
    plt.legend(loc = 'best')

    plt.grid()
    plt.show()

def films_pie(x, y):

    plt.pie(x, labels = y)

    plt.title('Top cinema-country')

    plt.legend(loc = 'best')
    plt.show()

def films_line(x, y):
    
    plt.title('Top cinema-country')
    plt.grid()

    plt.xlabel('Country')
    plt.ylabel('Films')

    plt.plot(x, y, color = 'Orange', linestyle = '-', marker = '*', markerfacecolor = 'g')

    plt.show()

films_bar(countries, countries_films)
films_line(countries, countries_films)
films_pie(countries_films, countries)