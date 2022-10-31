# EXERCIȚII SESIUNI STUDIU ÎN ECHIPĂ

print(' ')
print('● EXERCIȚII SESIUNI STUDIU ÎN ECHIPĂ.')
print(' ')


'''
Set
zile_sapt = {'luni', 'marți', 'miercuri', 'joi', 'vineri', 'sâmbăta', 'duminică'}
weekend = {'sâmbăta', 'duminică'}
    ● Adaugă în zilele_sapt ‘luni’
    ● Afișează zile_sapt
'''

print('1. Adaugam ziua "luni" in setul "zile_sapt" si apoi il afsam.')
print(' ')

zile_sapt = {'luni', 'marți', 'miercuri', 'joi', 'vineri', 'sâmbăta', 'duminică'}
weekend = {'sâmbăta', 'duminică'}

print(f'Afisam setul inainte de a adauga ziua "luni": {zile_sapt}')
zile_sapt.add('luni')
print(f'''Afisam setul dupa ce incercam sa adaugam ziua "luni": {zile_sapt}. '
Setul afiseaza valori unice, ziua "luni" exista deja in set, nu s-a mai putut adauga inca o data. ''')

'''
2.Folosește un if și verifică dacă:
    ● Weekend este un subset al zilelor din săptămânii.
    ● Weekend nu este un subset al zilelor din săptămânii.
'''

print(' ')
print('2. Verificam daca weekend-ul este sau nu un subset al zilelor saptamanii.')
print(' ')

if weekend.issubset(zile_sapt):
    print('"Weekend" este un subset al zilelor saptamanii.')
else:
    print('"Weekend" nu este un subset al zilelor saptamanii.')

'''
3. Afișează diferențele dintre aceste 2 seturi.
'''

print(' ')
print('3. Afisam diferentele dintre seturile "zile_sapt" si "weekend"')
print(' ')

print(f'''Seturile sunt:
- "zile_sapt": {zile_sapt}
- "weekend": {weekend}''')

print(f'Diferenta dintre cele 2 seturi este: {zile_sapt.difference(weekend)}')

'''
4. Afișează intersecția elementelor din aceste 2 seturi.
'''

print(' ')
print('4. Afisam intersectia elementelor din cele 2 seturi.')
print(' ')

print(f'Intersectia celor 2 seturi/elementele comune ale seturilor: {zile_sapt.intersection(weekend)}')
