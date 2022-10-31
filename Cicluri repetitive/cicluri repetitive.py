# Exerciții Recomandate - Usor (recomandat):

'''
1. Revizualizeaza intalnirea 4 si ia notite in caz ca ti-a scapat ceva
2. Vizualizeaza video despre Flow Control din 'Primii pasi in Programare'
(Daca nu ai facut-o deja)
3. Vizualizeaza video 5 despre Functii din 'Primii pasi in Programare'
Astfel, la intalnirea LIVE deja va fi a 2-a oara cand vei auzi conceptele
si sigur ti se vor intipari in minte mai bine.
https://www.itfactory.ro/8174437-intro-in-programare/

Iteratiile sunt greute, deoarece necesita putina gandire algoritmica
Va rog sa imi scrieti pe slack unde intampinati dificultati si va ajut
Daca stati blocati > 30 min, cereti indiciu

Response: Rezolvat
'''

# Exerciții - Dificultate medie (Faceti cat puteti din ele):

print(' ')
print('● Exerciții - Dificultate medie (Faceti cat puteti din ele).')
print(' ')

'''
1. 
Avand lista 
masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel'] 

    a. Folositi un for ca sa iterati prin toata lista si sa afisati
       ‘Masina mea preferata este x’
    b. Faceti acelasi lucru cu un for each
    c. Faceti acelasi lucru cu un while
'''

print('1. Folosind "for" si "while" vom parcurge lista definita si afisam valorile sub forma "Masina mea preferata este x".')
print(' ')

masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']

print(f'Lista definita este: {masini}')

for i in range(len(masini)):
    if masini[i] == 'Volvo':
        print(f'a. Masina mea preferata este {masini[i]}')

for car in masini:
    if car == 'Volvo':
        print(f'b. Masina mea preferata este {car}')


masina = 0

while len(masini) > masina:
    masina += 1
    if masini[masina] == 'Volvo':
        print(f'c. Masina mea preferata este {masini[masina]} ')
    break
''' 
2.
Aceeasi lista
Folositi un for
In for
   Modificati elementele din lista astfel incat sa fie scrie cu majuscule, exceptand primul si ultimul
Printati varianta finala a listei

'''
print(' ')
print('2. Pe baza listei de la exercitiul 1 modificam elementele cu majuscule, exceptand primul si ultimul".')
print(' ')



print(f'Lista definita este: {masini}')
print(' ')

print('Varianta 1 exercitiu 2:')
print(' ')
for element in range(len(masini)):
    if element == 0:
        print(masini[element])
    elif element > 0 and element < (len(masini)-1):
        print(masini[element].upper())
    else:
        print(masini[element])

print(' ')
print('Varianta 2 exercitiu 2:')
print(' ')


for element in range(len(masini)):
    if element > 0 and element < (len(masini)-1):
        masini[element] = masini[element].upper()

print(f'''Printam lista avand elemente cu majuscule, exceptand primul element si ultimul element:'
{masini}''')

''' 
3.
Aceeasi lista, 
Vine un cumparator care doreste sa cumpere un Mercedes
Iterati prin ea prin for each
Daca masina e mercedes (if)
   Printam ‘am gasit masina dorita de dvs’
   Iesim din ciclu folosind un cuvant cheie care face acest lucru
Altfel
   Printam Am gasit masina X. Mai cautam	
'''
print(' ')
print('3. Afisam masina preferata a cumparatorului, "Mercedes".')
print(' ')

masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']

print(f'Lista definita este: {masini}')
print(' ')

for masina_preferata in masini:
    if masina_preferata == 'Mercedes':
        print('Am gasit si avem disponibila masina dorita de dumneavoastra, Mercedes.')
        break
    else:
        print(f'Am gasit masina {masina_preferata}, mai cautam. ')

''' 
4.
Aceasi lista
Vine un cumparator bogat dar indecis. Ii vom prezenta toate masinile cu exceptia Trabant si Lastun. 
Daca masina e Trabant sau Lastun
   Folositi un cuvant cheie care sa dea skip la ce urmeaza
Printati S-ar putea sa va placa masina x

'''
print(' ')
print('4. Prezentare masini cumparator, fara masinile "Trabant" si "Lastun".')
print(' ')

masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']

print(f'Lista definita este: {masini}')
print(' ')

for element in masini:
    if element == 'Trabant' or element == 'Lastun':
        continue
    print(f'S-ar putea sa va placa masina {element}.')

''' 
5. 
Modernizati parcul de masini
Creati o lista goala, masini_vechi
Iterati prin masini
Cand gasiti Lastun sau Trabant:
Salvati aceste masini in masini_vechi
Suprascrieti-le cu ‘Tesla’ (in lista initiala de masini)
Printati Modele vechi: x
Modele noi: x
'''
print(' ')
print('5. Modernizare parc auto, scoatem din lista initiala masinile "Trabant" si "Lastun" si suprascriem cu "Tesla".')
print(' ')

print(f'Lista initiala definita este: {masini}')
print(' ')

masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
masini_vechi = []
masini.append('Tesla')

for element in masini:
    if element == 'Trabant' or element == 'Lastun':
        masini.remove(element)
        masini_vechi.append(element)

print(f'Afisam lista initiala modernizata: {masini}')
print(f'Afisam lista cu masinile vechi "Trabant" si "Lastun": {masini_vechi}')


''' 
6. 
Avand dict
pret_masini = {
    'Dacia': 6800,
    'Lastun': 500,
    'Opel': 1100,
    'Audi': 19000,
    'BMW': 23000
}
Vine un client cu un buget de 15000 euro
Prezentati doar masinile care se incadreaza in acest buget
Iterati prin dict.items() si accesati masina si pretul
Printati Pentru un buget de sub 15000 euro puteti alege masina x
Iterati prin lista
'''

print(' ')
print('6. Printam masinile cu valoare sub 15000 EUR.')
print(' ')

pret_masini = {
    'Dacia': 6800,
    'Lastun': 500,
    'Opel': 1100,
    'Audi': 19000,
    'BMW': 23000
}

print(f'Avem urmatorul dict: {pret_masini}')
print(' ')
dict_itmes = pret_masini.items()


'''
for masina in pret_masini:
    if pret_masini[masina] < 15000:
         print(f'Pentru un buget de sub 15000 EUR puteti alege masina: {masina}.')
'''

for masina in dict_itmes:
    if masina[1]<15000:
        print(f'Pentru un buget de sub 15000 EUR puteti alege masina:{masina[0]}')



''' 
7. 
Avand lista
numere = numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
Iterati prin ea
Afisati de cate ori apare 3
(nu aveti voie sa folositi count)

'''

print(' ')
print('7. Printam de cate ori apare cifra 3 in lista data, fara metoda "count()".')
print(' ')

numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
print(f'Lista este: {numere}')
print(' ')

nr=0
for nr_3 in numere:
    if nr_3 == 3:
        nr += 1

print(f'Numarul 3 apare in lista "numere" de {nr} ori.')

'''  
8. 
Aceeasi lista
Iterati prin ea
Calculati si afisati suma numerelor
(nu aveti voie sa folositi sum)
'''

print(' ')
print('8. Pe baza listei de la exercitiul 7, afisam suma numerelor, far metoda "sum()".')
print(' ')


print(f'Lista este: {numere}')
print(' ')

sum = 0
for nr in numere:
    sum = sum + nr

print(f'Suma numerelor din lista "numere" este: {sum}.')

'''  
9. 
Aceeasi lista
Iterati prin ea
Afisati cel mai mare numar
(nu aveti voie sa folositi max)
'''

print(' ')
print('9. Pe baza listei de la exercitiul 7, afisam cel mai mare numar din lista, fara metoda "max()".')
print(' ')


print(f'Lista este: {numere}')
print(' ')

max = 0
for nr in numere:
    if nr > max:
        max = nr

print(f'Din lista "numere", numarul {max} este cel mai mare.')

'''  
10. 
Aceeasi lista
Iterati prin ea
Daca numarul e pozitiv, inlocuiti-l cu valoarea lui negativa
Ex: daca e 3, sa devina -3
Afisati noua lista
'''

print(' ')
print('10. Pe baza listei de la exercitiul 7, afisam numerele pozitive ca fiind negative si numerele pozitive ca fiind negative.')
print(' ')

print(f'Lista initiala este: {numere}')
print(' ')



for nr in range (len(numere)):
    if numere[nr] > 0:
        numere[nr] = numere[nr] * -1
    else:
        numere[nr] = abs(numere[nr])

print(f'Afisam lista transformata conform cerintei: {numere}')

# Exerciții - Optionale (may need google):

print(' ')
print('● Exerciții - Optionale (may need google).')

'''  
11. 
alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
numere_pare = []
numere_impare = []
numere_pozitive = []
numere_negative = []
Iterati prin lista alte_numere 
Populati corect celelalte liste
Afisati cele 4 liste la final

'''

print(' ')
print('11. Pe baza listei de la exercitiul 7, afisam numerele pozitive ca fiind negative si numerele pozitive ca fiind negative.')
print(' ')

alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
numere_pare = []
numere_impare = []
numere_pozitive = []
numere_negative = []
print(f'Lista este: {alte_numere}')
print(' ')



for nr in alte_numere:
    if nr % 2 == 0:
        if nr > 0:
            numere_pozitive.append(nr)
        else:
            numere_negative.append(nr)
        numere_pare.append(nr)
    else:
        if nr > 0:
            numere_pozitive.append(nr)
        else:
            numere_negative.append(nr)
        numere_impare.append(nr)

'''
for nr in alte_numere:
    if nr > 0:
        numere_pozitive.append(nr)
    else:
        numere_negative.append(nr)
'''

print(f'Lista numerelor pare preluate din lista "alte_numere" este: {numere_pare}')
print(f'Lista numerelor impare preluate din lista "alte_numere" este: {numere_impare}')
print(f'Lista numerelor pozitive preluate din lista "alte_numere" este: {numere_pozitive}')
print(f'Lista numerelor negative preluate din lista "alte_numere" este: {numere_negative}')

'''  
12. 
Aceeasi lista
Ordonati crescator lista fara sa folositi sort
Va puteti inspira vizual de aici
https://www.youtube.com/watch?v=lyZQPjUT5B4
'''

print(' ')
print('12. Pe baza listei de la punctul 11 ordonam numerele din lista crescator, fara sa folosim metoda "sort()".')
print(' ')

print(f'Lista este: {alte_numere}')
print(' ')

for nr in range (0,len(alte_numere)-1):
    for nr2 in range(nr+1,len(alte_numere)):
        if (alte_numere[nr] > alte_numere[nr2]):
            alte_numere[nr],alte_numere[nr2] = alte_numere[nr2],alte_numere[nr]

print(f'Lista ordonata este: {alte_numere}')


'''  
13. 
Ghicitoare de numar
numar_secret = Generati un numar random intre 1 si 30
Numar_ghicit = None
Folosind un while
   User alege un numar
   Programul ii spune:
Nr secret e mai mare
Nr secret e mai mic
Felicitari! Ai ghicit!
'''

print(' ')
print('13. Ghicim numarul.')
print(' ')

import random

numar_secret = random.randint(1, 30)
numar_ghicit = None
nr_incercari = 0

print('Ghiceste numarul, ai maxim 10 incercari!')
while numar_ghicit != numar_secret and nr_incercari < 10:
    nr_incercari += 1
    numar_secret = random.randint(1, 30)
    numar_ghicit = int(input('Introdu numarul tau:'))
    if numar_ghicit < 1 or numar_ghicit > 30:
        print('Nu ai introdus un numar valid, trebuie sa fie un numar in intervalul 1 <-> 30.')
    elif numar_ghicit > numar_secret:
        print(f'Numarul ghicit este mai mare, ai introdus {numar_ghicit} si numarul de ghicit era {numar_secret}.')
    elif numar_ghicit < numar_secret:
        print(f'Numarul ghicit este mai mic, ai introdus {numar_ghicit} si numarul de ghicit era {numar_secret}.')
    else:
        if nr_incercari == 1:
            print(f'Felicitari, ai ghicit numarul, numarul secret a fost {numar_secret}, ai ghicit din prima.')
        else:
            print(f'Felicitari, ai ghicit numarul, numarul secret a fost {numar_secret}, ai ghicit din a {nr_incercari}-a incercare.')

    if nr_incercari == 10:
        print('Ai atins numarul maxim de 10 incercari, reia jocul si incearca sa ghicesti din nou.')


'''  
14. 
Alegeti un numar de la tastatura
Ex:7
Scrieti un program care sa genereze in consola urmatoarea piramida
1
22
333
4444
55555
666666
7777777

Ex:3
1
22
333

'''

print(' ')
print('14. Afisam numarul introdus la tastatura sub forma de piramida.')
print(' ')

nr_tastatura = int(input('Introdu un numar, pentru a forma piramida:'))
piramida = 0


while piramida < nr_tastatura:
    if nr_tastatura > 9:
        print('Trebuie sa introduci maxim numarul 9.')
        nr_tastatura = int(input('Introdu un numar:'))
    else:
        piramida += 1
        print(str(piramida) * piramida)

#reusit si din consola

'''  
15. 
tastatura_telefon = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9],
  [0]
]
Iterati prin lista 2d
Printati ‘Cifra curenta este x’
(hint: nested for - adica for in for)
'''

print(' ')
print('15. Afisam care este cifra curenta.')
print(' ')

tastatura_telefon = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9],
  [0]
]

for linie_tastatura in tastatura_telefon:
    for nr_tastatura in linie_tastatura:
        print(f'Numarul curent de pe tastatura este: {nr_tastatura}.')
