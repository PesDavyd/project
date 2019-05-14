### Пускай средний бюджет от жанра

import csv
import matplotlib.pyplot as plt

filename = 'films.csv'

ganres = []
budget = []
ganres_count = []

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

q = 0
for q in range(size2): #Заполнение budget

    summ = 0

    with open(filename, 'r', newline = '') as file: 
        reader = csv.reader(file)
        
        for row in reader:

            if row[7] == ganres[q]:
                row[4] = int(row[4])
                summ += row[4]

        summ /= ganres_count[q]
        summ = int(summ)

        budget.append(summ)


    file.close()

def bar_budget(a, b):
    plt.bar(a, b, color = 'r')

    plt.xlabel('Ganre')
    plt.ylabel('Budget')

    plt.grid()
    plt.show()
def pie_budget(a, b):
    plt.pie(a, labels = b)
    plt.legend(loc = 'best')

    plt.show()
def line_budget(a, b):
    plt.plot(a, b, color = 'g', linestyle = '--', marker = 'o', markerfacecolor = 'brown')

    plt.xlabel('Ganre')
    plt.ylabel('Budget')
    plt.grid()

    plt.legend(loc = 'best')

    plt.show()


print(ganres, '\n', ganres_count, '\n', budget)
# bar_budget(ganres, budget)
# pie_budget(budget, ganres)
line_budget(ganres, budget)