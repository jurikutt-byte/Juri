# read_persons.py
"""
KASUTAJANIMI
    eesnimi.perenimi
    läbivalt väikeste tähtedega
    eemaldada rõhumärgid
    eesnimes tühik ja sidekriips kaotada
EEPOSTIAADDRESS: 
    kasutajanimi@asutus.com
KELLELE TEHA: 
    Sündinud 1990 - 1999
UUS FAIL: 
     Sisaldab päist
     Eesnimi;Perenimi;Isikukood;kasutajanimi;eepost
"""
# Rõhudemärgi eemaldus; Õ,Ü,Ö.ä etc
# Source - https://stackoverflow.com/a/518232
# Posted by oefe, modified by community. See post 'Timeline' for change history
# Retrieved 2026-10-01, License - CC BY-SA 3.0
import unicodedata

src = 'persons/Persons.csv'
dst = 'results/Persons_accounts.csv'
domain = '@asutus.com'
header = ['Kasutajanimi', 'EPOST']


def strip_accents(s):
   return ''.join(c for c in unicodedata.normalize('NFD', s)
                  if unicodedata.category(c) != 'Mn')
# print(strip_accents('õüäöÖÜÕÄ'))   #eemaldab rõhumärgid 21-25
with open(src, 'r', encoding='utf-8') as s:
   with open(dst, 'w', encoding='utf-8') as d:
      content = s.readlines()   # loe kõik read
      old_header = content[0].strip().split(';') # Eristab kättesaadavamaks
      new_header = ';'.join(old_header[:2] + old_header[4:] +header)
      # Kirjuta Päis Faili
      d.write(new_header + '\n')

      for line in content[1:]:
         parts = line.strip().split(';') # Split eraldub teisele joonele, sama splittiga erisatama. Saada numbri lugesin 0-1-2- nimest
         year = int(parts[2].split('.')[2])   #Year saada on arvutatud int, parts, 2 split . 2, jam u.

         if 1990 <= year <= 1999:
            first_name = parts[0]
            last_name = parts[1]
# eemalda eesnimest tühik ja sidekriips
            first_name = first_name.replace(' ', '')          #asendada eesnimi millega
            first_name = first_name.replace('-', '')

            # Loo kasutajanimi
            username = '.'.join([first_name, last_name]).lower() #.lower() teeb väiksemaks, 
            username = strip_accents(username)

            # E-post
            email = username + domain

            new_line = ';'.join(parts[:2] + parts[4:] + [username, email])
            d.write(new_line + '\n') # Et asutada uue faili, lihtsalt kasuta uus rida ehk epostiga. D.write(new_line + '\n')


            print(new_line)

# Newline tuleb kirjutada faili, et teeks faili tootud nimedega. (nagu persons_acounts.csv)            
