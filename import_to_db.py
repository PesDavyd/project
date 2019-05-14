import csv
import mysql.connector
from mysql.connector.errors import IntegrityError
import matplotlib.pyplot as plt
import numpy as np

countries = [] #Лист со странами который будет заполняться по ходу программы
ganres = [] #Пустой лист с жанрами
rate = [] #Пустой лист для рейтинга от жанра
budget = [] # Лист с бюджетом, распределенный по жанрам
countries_films = [] # Лист с кол-ом фильмов каждой страны
ganres_count = [] # Лист с кол-вом картин каждого жанра

try:
    mydb = mysql.connector.connect(
    host="localhost",
    user="root" ,
    passwd="School2009"
    )

    print(mydb)

    mycursor = mydb.cursor()

    mycursor.execute("CREATE DATABASE IF NOT EXISTS db1")
    mycursor.execute("use db1")

    mycursor.execute("""CREATE TABLE IF NOT EXISTS films(
        id INTEGER PRIMARY KEY,
        film_name TEXT,
        year INTEGER,
        rate TEXT,
        budget BIGINT,
        cash_collection BIGINT,
        country VARCHAR(15),
        genre TEXT,
        director TEXT,
        producer TEXT);
        """)
except:
    print("\n\n\n\nSomewhere little error, just fix it :c\n\n\n\n")

finally:
    filename = "films.csv"

    with open(filename, 'r', newline = '') as file:
        reader = csv.reader(file)
        for row in reader:

            num = 0
            for num in range(10):
                if row[num] == '-':
                    row[num] == 0
            try:

                mycursor.execute("""
                    INSERT INTO films(id, film_name, year, rate, budget, cash_collection, country, genre, director, producer)
                    VALUES('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')
                """
                %(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9])
                )

            except:
                None
                
            
            finally:
               
                
                range_list1 = len(countries)
                count_doubles = 0
                x = 0

                for x in range(range_list1):
                    if row[6] == countries[x]:
                        count_doubles += 1

                if count_doubles == 0:
                    countries.append(row[6])

                range_list2 = len(ganres)
                count_doubles2 = 0
                y = 0

                for y in range(range_list2):
                    if row[7] == ganres[y]:
                        count_doubles2 += 1

                if count_doubles2 == 0:
                    ganres.append(row[7])
    
    file.close()

    num = 0

    size = len(countries)
    size2 = len(ganres)
        
    for num in range(size): #Заполнение countries_films
        count = 0
        with open(filename, 'r', newline = '') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[6] == countries[num]:
                    count += 1
            
            countries_films.append(count)
        file.close()

    num = 0

    for num in range(size2): #Заполнение ganres_count
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

    num = 0
    for num in range(size2): #Заполнение rate

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

    def pie(x, y):   #ganres_count, ganres, countries, countries_films
       
        plt.pie(x, labels = y)

        plt.title('Top ganres of 2016 - 2019')
       
        plt.legend(loc = 'upper right')
        plt.show()
    def bar(x, y):
        
        plt.bar(y, x, color = 'purple')

        plt.title('Top ganres of 2016 - 2019')

        plt.xlabel('Ganres')
        plt.ylabel('Volume films')

        plt.grid()
        plt.show()
    def line(x ,y):

        plt.plot(y, x, color = 'g', linestyle = '--', marker = '.', markerfacecolor = 'r')

        plt.xlabel('Ganres')
        plt.ylabel('Volume films')

        plt.grid()
        plt.show()

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

    films_bar(countries, countries_films) ##=\
    films_line(countries, countries_films)##===>Зависимость кол-ва фильмов от страны
    films_pie(countries_films, countries) ##=/

    bar_rate(ganres, rate) ##=\
    pie_rate(rate, ganres) ##===>Зависимость рейтинга от жанра
    line_rate(ganres, rate)##=/

    bar_budget(ganres, budget) ##=\
    pie_budget(budget, ganres) ##===>Зависимость бюджнта от жанра
    line_budget(ganres, budget)##=/

    pie(ganres_count, ganres) ##=\
    bar(ganres_count, ganres) ##===>Зависимость количества фильмов от жанра
    line(ganres_count, ganres)##=/
