import csv

filename = "films.csv"

films = [
    #start 2019
    #[id ,Название, год, рейтинг, бюджет, сбор в мире, страна, жанр, режисер, продюсер]
    [1, "Avengers: Endgame", 2019, 7.96, 356000000, 2485499739, 'USA', 'action movie', 'Anthony Russo', 'Kevin Feige'],
    [2, "How to Train Your Dragon: The Hidden World", 2019, 7.59, 129000000, 517430730, 'USA', 'cartoon', 'Din Deblua', 'Bonnie Arnold'],
    [3, 'Alita: Battle Angel', 2019, 7.23, 170000000, 404780321, 'USA', 'action movie', 'Robert Rodriguez', 'James Cameron'],
    [4, 'The Dirt', 2019, 7.18, '0', '0', 'USA', 'comedy', 'Jeff Tremaine', 'Allen Kovac'],
    [5, 'Dumbo', 2019, 7.08, 170000000, 310000000, 'USA', 'fantasy', 'Tim Burton', 'Justin Dpringer'],

    #start 2018

    [6, 'Green Book', 2018, 8.24, 23000000, 318091388, 'USA', 'comedy', 'Peter Farrelly', 'Jim Burke'],
    [7, 'Spider-Man: Into the Spider-Verse', 2018, 8.00, 90000000, 375414637, 'USA', 'cartoon', 'Bob Persichetti', 'Will Allegra'],
    [8, 'Avengers: Infinity War ', 2018, 7.99, 321000000, 2048359754, 'USA', 'action movie', 'Anthony Russo', 'Victoria Alonso'],
    [9, 'Bohemian Rhapsody', 2018, 7.99, 52000000, 903175016, 'UK', 'drama', 'Bryan Singer', 'Jim Beach'],
    [10, 'Isle of Dogs', 2018, 7.94, '0', 64241499, 'Germany', 'cartoon', 'Wes Anderson', 'Ben Adler'],

    #start 2017

    [11, 'Coco', 2017, 8.49, 175000000, 807082196, 'USA', 'cartoon', 'Lee Unkrich', 'Darla K Anderson'],
    [12, 'Three Billboards Outside Ebbing, Missouri', 2017, 8.12, 15000000, 159210164, 'UK', 'drama', 'Martin McDonagh', 'Martin McDonagh'],
    [13, 'Loving Vincent ', 2017, 7.90, 5618230, 42187665, 'UK', 'drama', 'Dorota Kabela', 'Ivan Mactaggart'],
    [14, 'Wonder ', 2017, 7.88, 20000000, 305937718, 'USA', 'drama', 'Stephen Chbosky', 'Michael Beugg'],
    [15, 'A Dog`s Purpose ', 2017, 7.80, 22000000, 204052467, 'India', 'drama', 'W Bruce Cameron', 'Holly Bario'],

    #start 2016

    [16, 'Zootopia', 2016, 8.32, 150000000, 1023784195, 'USA', 'cartoon', 'Brian Howard', 'Monica Lago-Kaytis'],
    [17, 'Kimi no na wa.', 2016, 8.10, 0, 357986087, 'Japan', 'cartoon', 'Makoto Shinkai', 'Kaitiro Ito'],
    [18, 'La La Land ', 2016, 8.02, 30000000, 446050389, 'USA', 'drama', 'Damien Chazelle', 'Fred Berger'],
    [19, 'Hacksaw Ridge', 2016, 8.00, 40000000, 175302354, 'Australia', 'drama', 'Mel Gibson', 'Michael Bassick'],
    [20, 'Dangal', 2016, 7.80, 9917600, 302895451, 'India', 'drama', 'Nitesh Tiwari', 'Aamir Khan']
]

with open(filename, 'w', newline= '') as file:
    writer = csv.writer(file)
    writer.writerows(films)
file.close()