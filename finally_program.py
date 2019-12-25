import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import random

df = pd.read_csv('moscow_hydro.csv', sep=';')
df = pd.DataFrame(df)  # Create pandas data frame from csv-file

nulls = df.isnull().sum()  # Find all None-position in every columns

df = df.drop(columns=[
    'ff10', 'ff3', 'W1',
    'W2', 'Tn', 'Tx',
    'Cm', 'Ch', 'RRR',
    'tR', 'E', 'Tg',
    "E'", 'sss', 'Unnamed: 29'
])  # Drop all columns where None > 50%

cor = df.corr(method='spearman')  # Do correlation


def cor_visual(cor_):  # Visual correlation-matrix
    plt.figure(figsize=(5.5, 5.5))
    sns.heatmap(cor_, annot=True)
    plt.title('Correlation matrix')
    plt.show()


def visual(x_pos, y_pos, name):  # Visual dependence
    x = x_pos
    y = y_pos

    plt.grid()

    colors_ = ['red', 'green',
        'blue', 'brown',
        'black', 'lime',
        'orange', 'purple']

    y_label = []
    x_label = []

    num = -1
    count = 0

    for i in name:
        if i != ' ':
            y_label.append(i)
        else:
            num = count
            break
        count += 1

    i = name[count + 3]
    for i in name:
        x_label.append(i)

    x_l = ''
    for i in x_label:
        x_l += i

    y_l = ''
    for i in y_label:
        y_l += i

    styles_ = ['--', '-', '-.', ':']
    markers_ = ['.', 'x', 'o']
    face_ = ['red', 'green',
        'blue', 'brown',
        'black', 'lime',
        'orange', 'purple']

    plt.plot(x, y, color=random.choice(colors_), linestyle=random.choice(styles_), markerfacecolor=random.choice(face_), marker=random.choice(markers_))  # Simple line graphic
    plt.xlabel(x_l)
    plt.ylabel(y_l)
    plt.title(name)
    plt.show()

    plt.bar(x, y, color=random.choice(colors_))  # Histogram
    plt.xlabel(x_l)
    plt.ylabel(y_l)
    plt.title(name)
    plt.show()

    plt.scatter(x, y, color=random.choice(colors_), marker=random.choice(markers_))  # scatter plot
    plt.xlabel(x_l)
    plt.ylabel(y_l)
    plt.title(name)
    plt.show()


query_ = int(input('Input Your graphic (correlation = 1 or dependence = 2, completion program = 3): '))

while query_ != 3:
    if query_ == 1:
        cor_visual(cor)

    elif query_ == 2:
        visual(df.Td, df.Temp, 'Temp / Td')
        visual(df.VV, df.Temp, 'Temp / VV')
        visual(df.P, df.Po, 'Po / P')
        visual(df.P, df.Po, 'Po / p')
        visual(df.Po, df.P, 'P / Po')
        visual(df.VV, df.P, 'P / VV')
        visual(df.Temp, df.VV, 'VV / Temp')
        visual(df.Po, df.VV, 'VV / Po')
        visual(df.Temp, df.Td, 'Td / Temp')
        visual(df.VV, df.Td, 'Td / VV')
        visual(df.VV, df.U, 'U / VV')
        visual(df.U, df.VV, 'VV / U')

    query_ = int(input('Input Your graphic (correlation = 1 or dependence = 2, completion program = 3): '))

print('\n\nProgram completion')
