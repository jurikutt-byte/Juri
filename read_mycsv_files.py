# read_mycsv_files.py
import os

total = 0 # kogu veeru summa
count = 0 # Loe ridu Kokku


# Leia data kaustast kõik CSV failid
files = []

for filename in os.listdir('data'): #otsib Faili 'data' folderist
    if filename.endswith('.csv'): #otsib faili nimi mis lõppeb .csv
        files.append(filename)   # filename on faili nimi.

# Kuva leitud failid
print('CSV failid')

for x in range(len(files)):
# Küsimus! Mis väärtus In rangelen(files)) järgi tuleb? = 3 faili, kuna on kolm faili. (1-3)
    print(f'{x + 1}. {files[x]}')
# Loeb kui palju faile on sul loetud. (line 18) 
# Kasutaja Valib Faili
file_number = int(input(f'Vali fail 1-{len(files)}: '))

if file_number >= 0 and file_number <= len(files):
    filename = 'data/' + files[file_number - 1] #Paneb miinuse (1-3), aga loeb faili numbrit listi.
    f = open(filename, 'r') # Avab faili
    rows = len(f.readline().split(';')) # Teada mitu veergu on
    f.close() # paneb faili kinni
    row = int(input(f'Mitmes veerg liita? 1-{rows} ')) # f on vormindatud string
    if row >= 1 and row <= rows: 
        row -= 1 # row = row - 1
        with open(filename, 'r') as f:
            content = f.readlines()
        for line in content:
            line = line.strip()
            parts = line.split(';') # Eristab ; märgiga 
            if parts[row].isnumeric(): # Kui väärtused on numbrid
                total += int(parts[row]) # All loeb rida numbrit / Kui palju ridasi on
                count += 1
 
   
        # print(total, count)
        print('Veeru Summa: ' + str(total) + '.')  # Str(total) + '.' on number mis ise
        print(f'Kokku loeti {count} rida.')
     # Siin on printitud text mis laheb kaasa teisele. f laheb veergu alla.
 
    else: 
        print('Vigane Veeru Number.')

else: 
    print('Vigane Faili Number!')

    # las loeb kokku loetud ridasi