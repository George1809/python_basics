# Exerciții Recomandate - Usor (recomandat):

'''
1. Revizualizeaza intalnirea 5 si ia notite in caz ca ti-a scapat ceva
2. Vizualizeaza video despre Functii din 'Primii pasi in Programare'
(Daca nu ai facut-o deja)
3. Vizualizeaza video 7 despre OOP din 'Primii pasi in Programare'
Astfel, la intalnirea LIVE deja va fi a 2-a oara cand vei auzi conceptele
si sigur ti se vor intipari in minte mai bine.
https://www.itfactory.ro/8174437-intro-in-programare/

Pentru toate exercitiile
Apelati functia de cel putin 2 ori cu valori diferite pentru a testa
Daca functia are return, printati raspunsul

Response: Rezolvat
'''

# Exerciții - b. Dificultate: usor spre mediu:

print(' ')
print('● Exerciții - Dificultate: usor spre mediu.')
print(' ')


'''
1.Functie care sa calculeze si sa returneze suma a 2 numere
'''

print('1. Definim o functie care sa calculeze si sa returneze suma a 2 numere.')
print(' ')

def suma(nr1,nr2):
    total = nr1+nr2
    return total

valoare_suma = suma(2,4)
valoare_suma2 = suma(22,15)

print(f'Suma numerelor 2 si 4 este: {valoare_suma}.')
print(f'Suma numerelor 22 si 15 este: {valoare_suma2}.')


''' 
2. Functie care sa returneze TRUE daca un numar este par, FALSE pt impar
'''
print(' ')
print('2. Definim o functie care sa returneze TRUE daca un numar este par si FALSE daca un numar este impar.')
print(' ')

numarul_introdus = int(input('Introdu un numar pentru a se valida daca este par sau impar:'))

def par_impar(numar):

    if numar % 2 == 0:
        return True
    else:
        return False

rezultat_par_impar = par_impar(numarul_introdus)

print(rezultat_par_impar)

''' 
3. Functie care returneaza numarul total de caractere din numele tau complet.
(nume, prenume, nume_mijlociu) 
'''

print(' ')
print('3. Definim o functie care sa returneze numarul total de caractere din numele introdus.')
print(' ')

nume_introdus = input('Introdu un nume pentru a afla numarul total de caractere:')

def nr_caractere(nume):

    total_char = nume.replace(' ','')
    return len(total_char)

nr_total_caractere = nr_caractere(nume_introdus)

print(nr_total_caractere)

''' 
4. Functie care returneaza aria dreptunghiului
'''
print(' ')
print('4. Definim o functie care sa returneze aria unui dreptunghi.')
print(' ')


lungimea = int(input('Introdu lungimea dreptunghiului:'))
latimea = int(input('Introdu latimea dreptunghiului:'))

def arie_dreptungi(lungime,latime):

    calcul_arie = lungime * latime
    return calcul_arie

rezultat_arie = arie_dreptungi(lungimea,latimea)

print(f'Aria dreptunghiului este: {rezultat_arie}.')

''' 
5. Functie care returneaza aria cercului.
'''
print(' ')
print('5. Definim o functie care sa returneze aria unui cerc.')
print(' ')

diametru_cerc = int(input('Introdu diametrul cercului:'))

def arie_cerc(numar):

    pi = 3.14
    raza = diametru_cerc / 2
    calcul_arie = pi * (raza ** 2)

    return calcul_arie

valoare_arie = arie_cerc(diametru_cerc)

print(f'Aria cercului este: {valoare_arie}.')


''' 
6. Functie care returneaza True daca un caracter x se gaseste intr-un string dat. Fasle daca nu.
'''
print(' ')
print('6. Definim o functie prin care verificam daca un caracter se afla intr-un string sau nu, returnand TRUE sau FALSE.')
print(' ')

caracter = input('Introdu un caracter pentru a verifica daca se afla in textul dat:')
text = 'un text definit la intamplare'

def verificare_caracter(char):
    if char in text:
        return True
    else:
        return False

caracter_introdus = verificare_caracter(caracter)


print(f'Caracterul introdus se afla in textul dat? -> {caracter_introdus}')
print(f'Textul era: "{text}".')

''' 
7. Functie fara return, primeste un string si printeaza pe ecran:
    Nr de caractere lower case este x
    Nr de caractere upper case exte y

'''
print(' ')
print('7. Functie care afiseaza totalul de litere lower case si upper case dintr-un text.')
print(' ')

textul_upper_lower = input('Introdu un text cu litere mari si mici pentru a se afisa totalul de caractere cu litere mari si mici: ')

def lowercase_uppercase(text_upper_lower):
    text_upper_lower.replace(' ','')
    l = 0
    u = 0
    for litera in text_upper_lower:
        if litera.islower():
            l += 1
        else:
            u += 1

    print(f'Numarul de caractere lower este: {l}.')
    print(f'Numarul de caractere upper este: {u}.')

lowercase_uppercase(textul_upper_lower.replace(' ',''))

''' 
8. Functie care primeste o LISTA de numere si returneaza o LISTA doar cu numerele pozitive
'''
print(' ')
print('8. Functie care primeste o lista de numere, random, care returneaza o alta lista doar cu numerele pozitive.')
print(' ')


def poz(lista):
    lista_nr_pozitive = []
    for n in lista:
        if n > 0:
            lista_nr_pozitive.append(n)

    return lista_nr_pozitive


import random
lista_numere = []
for nr in range(0,50):
    numar_random = random.randint(-100, 100)
    lista_numere.append(numar_random)

pozitive = poz(lista_numere)

print(f'Lista initiala este: {lista_numere}')
print('')
print(f'Din lista initiala formam o alta lista doar cu numerele pozitive: {pozitive}.')

''' 
9. Functie care nu returneaza nimic. Primeste 2 numere si PRINTEAZA
    Primul numar x este mai mare decat al doilea nr y
    Al doilea nr y este mai mare decat primul nr x
    Numerele sunt egale. 
'''
print(' ')
print('9. Definim o functie care primeste 2 numere si printam care este mai mare sau daca numerele sunt egale.')
print(' ')


#nr_x = int(input('Introdu valoarea lui x:'))
#nr_y = int(input('Introdu valoarea lui y:'))


def comparare(x,y):

    if x > y:
        print('Valoarea lui x este mai mare decat valoarea lui y.')
    elif x < y:
        print('Valoarea lui y este mai mare decat valoarea lui x.')
    else:
        print('Numerele x si y sunt egale.')

#comparare(nr_x,nr_y) #cu numere preluate de la tastatura
comparare(5,2)
comparare(2,4)
comparare(3,3)

''' 
10. Functie care primeste un numar si un set de numere.
    Printeaza ‘am adaugat numarul nou in set’ + returneaza True
    Sau Printeaza ‘nu am adaugat numarul in set. Acesta exista deja’ + returneaza False

'''
print(' ')
print('10. Definim o functie care verifica un numar introdus si pe care il adauga intr-un set daca acel numar nu se afla in setul respectiv.')
print(' ')

sets = {1 ,2, 3, 4}
print(f'Setul initial este: {sets}.')
x = int(input('Numarul pe care doriti sa il introduceti in set: '))

def nr_set(nr,s):
    if nr not in s:
        sets.add(nr)
        print(f'Numarul introdus nu este in set, il adaugam, acum setul este: {s}.')
        return True
    else:
        print('Numarul exista in set, nu l-am putut adauga.')
        return False

verificare_finala = nr_set(x,sets)

print(verificare_finala)

# Exerciții - Optionale (may need google):

print(' ')
print('● Exerciții - Optionale (may need google).')

''' 
11. Functie care primeste o luna din an si returneaza cate zile are acea luna
'''
print(' ')
print('11. Definim o functie care primeste o luna din an si returneaza cate zile are acea luna.')
print(' ')

from calendar import monthrange

an = int(input('Introdu anul, intervalul 1900 - 2022:'))
luna = int(input('Introdu luna, 1-12:'))

def nr_zile_luna(anul,luna_an):

    if anul < 1900 or anul > 2022 or luna_an < 1 or luna_an > 12:
        print('Valoare invalida introdusa pentru an sau luna, respecta intervalul indicat.')
    else:
        zile_luna = monthrange(anul,luna_an)
        print(f'Luna {luna_an} selectata, din anul {anul}, are {zile_luna[1]} zile.')

nr_zile_luna(an,luna)

''' 
12. Functie calculator care sa returneze 4 valori 
    Suma, diferenta, inmultirea, impartirea a 2 numere

'''
print(' ')
print('12. Definim o functie care returneaza: suma, diferenta, inmultirea si impartirea a doua numere.')
print(' ')


numarul_1 = int(input('Introdu primul numar:'))
numarul_2 = int(input('Introdu al doilea numar:'))


def calcule(n1, n2):
    calcul_1 = n1 + n2
    calcul_2 = abs(n1 - n2)
    calcul_3 = n1 * n2
    calcul_4 = n1 / n2

    return calcul_1, calcul_2, calcul_3, calcul_4

rezultate = calcule(numarul_1, numarul_2)
print(' ')
print(f'''Pe baza numerelor introduse mai sus, avem urmatoarele rezultate:
- pentru adunare: {rezultate[0]}
- pentru diferenta: {rezultate[1]}
- pentru inmultire: {rezultate[2]}
- pentru impartire: {rezultate[3]}
''')


''' 
13. Functie care primeste o lista de cifre (adica doar 0-9)
Ex: [1, 3, 1, 5, 9, 7, 7, 5, 5]
Returneaza un DICT care ne spune de cate ori apare fiecare cifra
=> dict {
0: 0
1 :2
2: 0
3: 1
4: 0
5: 3
6: 0
7: 2
8: 0
9: 1
}
'''
print(' ')
print('13. Definim o functie care preia o lista si numara de cate ori apare un numar in lista respectiva, formand apoi un dict cu rezultatul.')
print(' ')

from collections import Counter
import random

def count_nr_lista(lista_nr):
    dict = {}
    for nr_l in range(0, 10):
        if nr_l in lista_nr:
            total_nr_lista = Counter(lista_nr)
            dict[nr_l] = total_nr_lista[nr_l]
        else:
            dict[nr_l] = 0
    return dict

dimensiune_lista = int(input('Introdu dimeniunea listei, un numar intre 10 si 30: '))

while dimensiune_lista < 10 or dimensiune_lista > 30:
    print('Numar invalid, incearca iar si respecta intervalul indicat. ')
    dimensiune_lista = int(input('Introdu dimeniunea listei, un numar intre 10 si 30: '))

lista_nr = []
for nr in range(0,dimensiune_lista):
    numar_random = random.randint(0, 9)
    lista_nr .append(numar_random)

nr_dict = count_nr_lista(lista_nr)
print('')
print(f'''Lista generata este: 

{lista_nr}''')
print('')
print(f'''Generam un dict unde afisam totalul pe fiecare numar din lista de mai sus:

{nr_dict}''')

''' 
14. Functie care primeste 3 numere
    Returneaza valoarea maxima dintre ele
'''
print(' ')
print('14. Definim o functie care primeste 3 numere, urmand apoi sa returnam valoarea cea mai mare.')
print(' ')

nr_1 = int(input('Introdu primul numar: '))
nr_2 = int(input('Introdu al doilea numar: '))
nr_3 = int(input('Introdu al treilea numar: '))

def nr(nr1, nr2, nr3):
    max_nr = [nr1,nr2,nr3]
    return max(max_nr)

numar_maxim = nr(nr_1,nr_2,nr_3)
print(f'Numarul maxim este: {numar_maxim}.')

''' 
15. Functie care sa primeasca un numar si sa returneze suma tuturor numerelor de la 0 la acel numar
    Ex: daca dam nr 3
    Suma va fi 6 (0+1+2+3)
'''
print(' ')
print('15. Definim o functie care primeste un numar si generam suma numerelor de la 0 pana la numarul definit.')
print(' ')

nr_suma = int(input('Introdu un numar pentru a se calcula suma, incepand de la 0 pana la numarul definit: '))



def suma_nr(nr_s):

    incrementare = 0
    suma = 0

    while incrementare <= nr_s:
        suma = suma + incrementare
        incrementare += 1

    return suma

total_suma = suma_nr(nr_suma)
print('')
print(f'Suma numarului introdus este: {total_suma}.')


# Exerciții - BONUS:

print(' ')
print('● Exerciții - BONUS.')

''' 
16. Functie care primesete 2 liste de numere (numerele pot fi dublate)
    Returnati numerele comune 

    Ex:
    list1 = [1, 1, 2, 3]
    list2 = [2, 2, 3, 4]
    Raspuns: {2, 3}
'''
print(' ')
print('16. Definim o functie care primeste 2 liste de numere, unde se afla si numere dublate, urmand apoi sa returnam numerele comune din cele 2 liste.')
print(' ')

import random

def numere_comune(l1,l2):

    setul = set(l1)
    elemente_comune = setul.intersection(l2)
    return l1, l2, elemente_comune

lista_nr_1 = []
lista_nr_2 = []
for nr in range(0,10):
    numar_random = random.randint(0, 9)
    lista_nr_1.append(numar_random)

    numar_random = random.randint(0, 9)
    lista_nr_2.append(numar_random)

lista_elemente_comune = numere_comune(lista_nr_1,lista_nr_2)

print(f'Elementele din prima lista sunt: {lista_elemente_comune[0]}.')
print(f'Elementele din a doua lista sunt: {lista_elemente_comune[1]}.')
print(f'Elementele comune ale celor 2 liste sunt: {lista_elemente_comune[2]}.')

''' 
17. Functie care sa aplice o reducere de pret
    Daca produsul costa 100 lei si aplicam reducere de 10%
    Pretul va fi 90
    Tratati cazurile in care reducerea e invalida. De ex o reducere de 110% e invalida
'''
print(' ')
print('17. Definim o functie care aplica un discount unui produs. In cazul in care discount-ul este invalid, afisam asta.')
print(' ')

pret = int(input('Introdu pretul produsului/serviciului: '))

discount = float(input('Introdu valoarea de discount: '))


def discount_produs_serviciu(pretul,discountul):

    valoare_cu_discount = pretul - ((round(discountul,2) / 100) * pretul)
    return valoare_cu_discount


while discount < 0.1 or discount > 100:
    print('Valoarea de discount este invalida, foloseste o valoare de discount corecta, de la 0.1% pana la 100%.')

    discount = int(input('Introdu valoarea de discount: '))

valoare_finala_cu_discount = discount_produs_serviciu(pret,discount)

print(f'Pentru pretul de {pret} Lei, cu un discount de {round(discount,2)}% aplicat, valoarea finala cu discount este de {round(valoare_finala_cu_discount,2)} Lei.')

''' 
18. Functie care sa afiseze data si ora curenta din ro
(bonus: afisati si data si ora curenta din China)
'''
print(' ')
print('18. Definim o functie care afiseaza data si ora din Romania, dar si din China.')
print(' ')

from datetime import datetime
import pytz

def ore_tari(ro,chi):
    tara_romania = pytz.timezone(ro)
    data_ora_prezent_romania = datetime.now( tara_romania)

    tara_china = pytz.timezone(chi)
    data_ora_prezent_china = datetime.now(tara_china)

    return data_ora_prezent_romania,data_ora_prezent_china


tara_ro, tara_chi = ore_tari('Europe/Bucharest','Asia/Shanghai')

print(f'Data si ora din prezent, din Romania: {tara_ro}')
print(f'Data si ora din prezent, din China: {tara_chi}')


''' 
19. Functie care sa afiseze cate zile mai sunt pana la ziua ta / sau pana la craciun daca nu vrei sa ne zici cand e ziua ta :)
'''
print(' ')
print('18. Definim o functie care afiseaza cate zile mai sunt pana la ziua mea.')
print(' ')

from datetime import date


def ziua_mea_and_craciun(eu,craciunul):

    prezent = date.today()

    zile_pana_la_ziua_mea = eu - prezent
    zile_pana_la_craciun = craciunul - prezent

    return  zile_pana_la_ziua_mea,zile_pana_la_craciun

ziua_mea = date(2023,9,18)
craciun = date(2022,12,25)

zile_eu, zile_craciun = ziua_mea_and_craciun(ziua_mea,craciun)

print(f'Pana la ziua mea mai sunt {zile_eu.days} zile.')
print(f'Pana la Craciun mai sunt {zile_craciun.days} zile.')
