# Exerciții obligatorii - grad de dificultate: Ușor spre Mediu:

'''
Exerciții Recomandate - grad de dificultate: Ușor

1. Revizualizează întâlnirea 1 și ia notițe în caz că ți-a scăpat ceva.
2. Vizualizează din videoul ‘Primii pași în Programare’:

    - Variabile și Tipuri;
    - Operatori și Flow Control.

Response: Rezolvat
'''

# Exerciții obligatorii - grad de dificultate: Ușor spre Mediu:
print(' ')
print('● Exercitii cu grad de dificultate ușor spre mediu.')
print(' ')
'''
1. În cadrul unui comentariu, explică cu cuvintele tale ce este o variabilă.

Response: O variabila este o informatie stocata in memoria unui calculator, 
          care poate pastra o anumita valoare ce se poate apela ulterior prin intermediul variabilei. 
'''

'''
2. Declară și initializează câte o variabilă din fiecare din următoarele tipuri de
variabilă:

- string
- int
- float
- bool
'''

variabila_string = 'tema pentru cursul 1'
variabila_int = 1
variabila_float = 50.99
variabila_bool = True

'''3. Utilizează funcția type pentru a verifica dacă au tipul de date așteptat.'''

print('3. Printam tipul de date pentru fiecare variabila definita mai sus.')
print(' ')
print(f'Variabila "variabila_string" este de tip {type(variabila_string)}.')
print(f'Variabila "variabila_int" este de tip {type(variabila_int)}.')
print(f'Variabila "variabila_float" este de tip {type(variabila_float)}.')
print(f'Variabila "variabila_bool" este de tip {type(variabila_bool)}.')

'''
4. Rotunjește ‘float’-ul folosind funcția round() și salvează această modificare în
aceeași variabilă (suprascriere):
    - Verifică tipul acesteia.
'''

print(' ')
print('4. Rotunjire variabila "variabila_float", suprascriere si afisare valoare suprascrisa.')
print(' ')
print(f'Inainte de rotunjire, variabila "variabila_float" avea valoarea {variabila_float}.')
variabila_float = round(variabila_float)
print(f'Dupa rotunjire, variabila "variabila_float" are valoarea {variabila_float}.')
print(f'Printam tipul de date pentru variabila "variabila_float": {type(variabila_float)}.')

'''
5. Folosește print() și printează în consolă 4 propoziții folosind cele 4 variabile.
    Rezolvă nepotrivirile de tip prin ce modalitate dorești.
'''
print(' ')
print('5. Exercitiu rezolvat in consola.')
'''
Rezolvat si in consola, unde am defnit din nou variabilele ca la punctul 2 si apoi le-am printat. 

print(f'Astazi am terminat de facut {variabila_string}.')
print(f'Am luat nota {variabila_int} la examaneul de biologie.')
print(f'Mi-am cumparat un mouse in valoare de {variabila_float}.')
print(f'Factura platita: {variabila_bool}.')
'''

'''
6. Citește de la tastatură:
    - numele;
    - prenumele.
Afișează: 'Numele complet are x caractere'.
'''

print(' ')
print('6. Introducem numele si prenumele si afisam numarul de caractere pentru numele intreg.')
print(' ')
Nume = input('Nume')
Prenume = input('Prenume')
len_char = Nume + Prenume

print(f'Numele introdus mai sus, {Nume} {Prenume}, are {len(len_char)} caractere.')

'''
7. Citește de la tastatură:
    - lungimea;
    - lățimea.
Afișează: 'Aria dreptunghiului este x'.
'''


print(' ')
print('7. Definim lungimea si latimea si aflam aria. ')
print(' ')
Lungime = int(input('Lungime'))
Latime = int(input('Latime'))

print(f'Aria dreptunghiului este {Lungime * Latime}')


'''
8. Având stringul: 'Coral is either the stupidest animal or the smartest rock':

    - afișează de câte ori apare cuvântul 'the';
'''
print(' ')
print('8. Afisam de cate ori apare cuvantul "the" in textul "Coral is either the stupidest animal or the smartest rock".')
print(' ')
text = 'Coral is either the stupidest animal or the smartest rock'
print(text.count('the', 15))

'''
9.Acelasi string
 -inlocuieste the cu THE peste tot
 -printeaza rezultatul
'''

print(' ')
print('9. Din stringul de la punctul 8, afisam THE in loc de the.')
print(' ')
text_inlocuire = text[:15] + text[15:].replace('the','THE')
print(text_inlocuire)

'''
10. Același string:
    - Folosește un assert ca să verifici dacă acest string conține doar numere.
'''
print(' ')
print('10. Afisam daca textul de la punctul 8 este numeric.')
print(' ')
print(text.isnumeric())
print(' ')

# Exerciții Opționale - grad de dificultate: Mediu spre greu.
print('● Exercitii cu grad de dificultate mediu spre greu.')
print(' ')
'''
1. Exercițiu:
- citește de la tastatură un string de dimensiune impară;
- afișează caracterul din mijloc.
'''

print('1. Afisam carcterul din mijlocul unui cuvant.')
print(' ')
impar=input('Introdu textul impar:')
middle_character = round(len(impar) / 2)

if len(impar) % 2 == 0:
    print('Textul introdus trebuie sa fie par, incearca din nou.')
elif len(impar) == 3:
    print(f'Caracterul din mijlocul stringului "{impar}" este {impar[middle_character - 1]}')
else:
    print(f'Caracterul din mijlocul stringului "{impar}" este {impar[middle_character]}')


'''
2. Folosind o singură linie de cod :

    - citește un string de la tastatură (ex: 'alabala portocala');
    - salvează fiecare cuvânt într-o variabilă;
    - printează ambele variabile pentru verificare.
'''
print(' ')
print('2. Afisam un string format din 2 cuvinte si printam variabilele separat, pentru fiecare cuvant in parte.')
print(' ')
cuvant = input('Introduceti un string din 2 cuvinte: '); cuvant = cuvant.split(); cuvant1 = cuvant[0]; cuvant2 = cuvant[1]; print(cuvant1); print(cuvant2)
print(' ')

