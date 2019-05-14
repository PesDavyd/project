### Зарисимость рейтинга от жанра

import csv
import matplotlib.pyplot as plt

filename = 'films.csv'

ganres = []
ganres_count = []
rate = []

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

with open(filename, 'r', newline = '') as file: #Заполнение count_ganres
    num = 0
    size2 = len(ganres)

    for num in range(size2):
        count = 0
        with open(filename, 'r', newline = '') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[7] == ganres[num]:
                    count += 1

            ganres_count.append(count)
file.close()

num = 0
for num in range(size2):

    sum_rate = 0

    with open(filename, 'r', newline = '') as file:
        reader = csv.reader(file)
        for row in reader:

            if row[7] == ganres[num]:
                row[3] = float(row[3])

                sum_rate += row[3]

        sum_rate /= ganres_count[num]
        sum_rate = round(sum_rate, 2)
        rate.append(sum_rate)
    
    file.close()

def bar_rate(a, x):
    plt.bar(a, x, color = 'purple')
   
    plt.grid()
    plt.xlabel('Ganre')
    plt.ylabel('Rate')
    plt.title('Rating dependence on genre')

    plt.show()

def pie_rate(a, x):
    plt.pie(a, labels = x)
    
    plt.title('Rating dependence on genre')
    plt.legend(loc = 'best')

    plt.show()

def line_rate(a, x):
    plt.title('Rating dependence on genre')
    plt.grid()

    plt.xlabel('Ganre')
    plt.ylabel('Rate')

    plt.plot(a, x, color = 'b', linestyle = '-', marker = 'o', markerfacecolor = 'purple')
    plt.show()

bar_rate(ganres, rate)
pie_rate(rate, ganres)
line_rate(ganres, rate)

print(rate, '\n', ganres)