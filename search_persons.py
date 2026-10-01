# search persons.py
"""
Küsi kasutajalt nime (ees või pere) (ainult 1 mitte mõolemad) ja otsi seda. väljasta leidmise puhul kogu faili rida-
Kasutame import csv varianti
Tõstutundeta (leiab kirja, minimaalselst 2 tähte)
Otsitav frass võib olla ka käsureal
"""
import csv
import sys # Käsureal infolugemise jaoks vajalik import

filename = 'persons/Persons.csv'
total = 0 # Mitu isikut leiti

if len(sys.argv) > 1:
    phrase = sys.argv[1] # Käsurealt saadi nimi
else: 
    phrase = input('Sisestua otsitav nimi (min. 2 märki): ')

if len(phrase) > 1:
    phrase = phrase.lower()

    with open(filename, 'r', encoding='utf-8') as f: #Avab faili
        content = csv.reader(f, delimiter=';')
        next(content) # Lugemisjärg teisel real

        for row in content:
            first_name = row[0].lower()
            last_name = row[1].lower()

            if phrase == first_name or phrase == last_name:
                print(';'.join(row))
                total += 1
        if total > 0:
            print(f'\nLeiti {total} isikut')


else: 
    print('Otsingu fraas on liiga lühike!!')
