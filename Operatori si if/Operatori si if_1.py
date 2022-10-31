# Exerciții Recomandate - grad de dificultate: Ușor:

'''
1. Revizualizează întâlnirea 2 și ia notițe în caz că ți-a scăpat ceva.
2. Vizualizează din ‘Primii pași în Programare’ video.

- Operatori și Flow Control

Response: Rezolvat
'''

# Exerciții obligatorii - grad de dificultate: Ușor spre Mediu:

print(' ')
print('● Exerciții obligatorii - grad de dificultate: Ușor spre Mediu.')
print(' ')

'''
Pentru toate exercițiile se va folosi noțiunea de if în rezolvare.
Indirect vei exersa și operatorii în cadrul condițiilor ramurilor din if.
X poate fi inițializat direct în cod sau citit de la tastatură, după preferințe.
X este un int.
'''

'''
1. Explică cu cuvintele tale în cadrul unui comentariu cum funcționează un if
else.
'''

'''
Prin "if" verificam conditiile pe care le punem si in situatia in care sunt adevarate, 
se parcurge codul si afisam informatia sau executam anumite instructiuni, 
iar prin "else", daca nu sunt indeplinite conditiile specificate, afisam o alta informatie sau executam alte instructiuni. 
'''


'''
2. Verifică și afișează dacă x este număr natural sau nu.
'''

print('2. Verificam si afisam daca x este un numar natural.')
print(' ')


x = int(input('Introduceti un numar natural:'))

if x >= 0:
    print('Bravo, ai introdus un numar natural!')
else:
    print('Acesta nu este un numar natural, mai incearca o data.')


'''
3. Verifică și afișează dacă x este număr pozitiv, negativ sau neutru.
'''

print(' ')
print('3. Verificam si afisam daca x este un numar pozitiv, negativ sau neutru.')
print(' ')


x = int(input('Introduceti un numar:'))

if x == 1:
    print('Numarul introdus este pozitiv, dar poate fi si neutru in cazul in care se foloseste intr-o operatie de inmultire.')
elif x > 0:
    print('Numarul este pozitiv.')
elif x < 0:
    print('Numarul este negativ.')
else:
    print('Numarul este neutru.')


'''
4. Verifică și afișează dacă x este între -2 și 13.
'''

print(' ')
print('4. Verificam daca x se afla intre -2 si 13.')
print(' ')


x = int(input('Introduceti un numar:'))

if x >= -2 and x <= 13:
    print('Numarul se afla intre -2 si 13.')
else:
    print('Numarul se afla in afara intervalului stabilit, mai incearca.')



'''
5. Verifică și afișează dacă diferența dintre x și y este mai mică de 5.
'''


print(' ')
print('5. Afisam daca diferenta dintre x si y este mai mica de 5.')
print(' ')


x = int(input('Introduceti valoarea lui "x":'))
y = int(input('Introduceti valoarea lui "y":'))

if x - y < 5:
    z = x-y
    print(f'Rezultatul este {z}, deci diferenta dintre x si y este mai mica de 5.')
else:
    z = x - y
    print(f'Rezultatul este {z}, deci diferenta dintre x si y nu este mai mica de 5.')



'''
6. Verifică dacă x NU este între 5 și 27 - a se folosi ‘not’.
'''

print(' ')
print('6. Afisam daca x este sau nu intre 5 si 27, folosind operatorul logic "not".')
print(' ')


x = int(input('Introduceti un numar:'))

if not(x >= 5 and x <= 27):
    print('Numarul nu se afla in intervalul 5 - 27')
else:
    print('Numarul se afla in intervalul 5 - 27')


'''
7.
x și y (int)
Verifică și afișează dacă sunt egale, dacă nu afișează care din ele este mai
mare.
'''

print(' ')
print('7. Afisam daca x si y sunt egale, altfel afisam care este mai mare.')
print(' ')


x = int(input('Introduceti valoarea lui "x":'))
y = int(input('Introduceti valoarea lui "y":'))

if x == y:
    print('Valoarea lui x este egala cu valoarea lui y.')
else:
    if x > y:
        print('Valoarea lui x este mai mare decat valoarea lui y.')
    else:
        print('Valoarea lui y este mai mare decat valoarea lui x.')



'''
8.
X, y, z - laturile unui triunghi.
Afișează dacă triunghiul este isoscel, echilateral sau oarecare.
'''

print(' ')
print('8. Afisam tipul de triunghi in functie de lungimea laturilor x, y si z.')
print(' ')



x = int(input('Introduceti valoarea lui "x":'))
y = int(input('Introduceti valoarea lui "y":'))
z = int(input('Introduceti valoarea lui "z":'))

if x == y ==z:
    print('Triunghiul este echilateral.')
elif x == y != z or x == z != y or z == y != x:
    print('Triunghiul este isoscel.')
else:
    print('Este un triunghi oarecare.')


'''
9. Citește o literă de la tastatură.
    Verifică și afișează dacă este vocală sau nu.
'''

print(' ')
print('9. Afisam o litera si verificam daca este vocala.')
print(' ')


vocale = 'aeiou'
litera = input('Introduceti o vocala:')

if len(litera)>1:
    print('Ati introdus mai multe litere, introduceti doar o litara, incerati din nou.')
elif vocale.count(litera.lower()) == 1:
    print('Litera introdusa este o vocala.')
else:
    print('Litera introdusa nu este o vocala, incearca din nou.')


'''
10.Transformă și printează notele din sistem românesc în >
    Peste 9 => A
    Peste 8 => B
    Peste 7 => C
    Peste 6 => D
    Peste 4 => E
    4 sau sub => F
'''

print(' ')
print('10. Transformam notele in calificative si afisam calificativul in functie de nota introdusa.')
print(' ')


nota = int(input('Introduceti nota:'))

if nota <= 0 or nota > 10:
    print('Nota este invalida, incearca din nou!')
elif nota >= 9:
    print(f'Pentru nota {nota} ai calificativul "A".')
elif nota == 8:
    print(f'Pentru nota {nota} ai calificativul "B".')
elif nota == 7:
    print(f'Pentru nota {nota} ai calificativul "C".')
elif nota == 6:
    print(f'Pentru nota {nota} ai calificativul "D".')
elif nota > 4:
    print(f'Pentru nota {nota} ai calificativul "E".')
else:
    print(f'Pentru nota {nota} ai calificativul "F".')


# Exerciții Opționale - grad de dificultate: Mediu spre greu.

print('● Exercitii cu grad de dificultate mediu spre greu.')
print(' ')

'''
1.Verifică dacă x are minim 4 cifre (x e int).
    (ex: 7895 are 4 cifre, 10 nu are minim 4 cifre)
'''
print(' ')
print('1. Verificam daca x are minim 4 cifre.')
print(' ')



x = int(input('Introduceti un numar:'))
nr_char = len(str(x))


if nr_char >= 4:
    print(f'Numarul {x} are cel putin 4 cifre, este format din {nr_char} cifre.')
else:
    print(f'Numarul {x} nu depaseste 4 cifre.')


'''
2.Verifică dacă x are exact 6 cifre.
'''

print(' ')
print('2. Verificam daca x are exact 6 cifre.')
print(' ')

x = int(input('Introduceti un numar:'))
nr_char = len(str(x))


if nr_char == 6:
    print(f'Numarul {x} are exact 6 cifre.')
else:
    print(f'Numarul {x} nu respecta numarul de cifre, incearca din nou.')

'''
3.Verifică dacă x este număr par sau impar (x e int).
'''


print(' ')
print('3. Verificam daca x este numar impar sau par.')
print(' ')


x = int(input('Introduceti un numar:'))

if x % 2 == 0:
    print('Numarul introdus este par.')
else:
    print('Numarul introdus este impar')



'''
4. x, y, z (int)
    Afișează care este cel mai mare dintre ele?
'''

print(' ')
print('4. Afisam care este cel mai mare numar.')
print(' ')



x = int(input('Introduceti valoarea lui "x":'))
y = int(input('Introduceti valoarea lui "y":'))
z = int(input('Introduceti valoarea lui "z":'))



if x > y and x > z and x != y and x !=z:
    print('Valoarea lui "x" este mai mare decat valorile lui y si z.')
elif y > x and y > z and y!= x and y != z:
    print('Valoarea lui "y" este mai mare decat valorile lui x si z.')
else:
    if z > x and z > y and z != x and z != y:
        print('Valoarea lui "z" este mai mare decat valorile lui x si y.')
    else:
        print('Numere dublate, nu s-a putut determina care este cea mai mare valoare.')


'''
5.
X, y, z - reprezintă unghiurile unui triunghi
    Verifică și afișează dacă triunghiul este valid sau nu.
'''

print(' ')
print('5. Pe baza unghiurilor, afisam daca triunghiul este valid sau nu.')
print(' ')


x = int(input('Introduceti valoarea lui "x":'))
y = int(input('Introduceti valoarea lui "y":'))
z = int(input('Introduceti valoarea lui "z":'))

if x < 30 or y <30 or z < 30 or x > 180 or y > 180 or z > 180:
    print('Unghi neacceptat, reintrodu valorile.')
elif x + y + z == 180:
    print('Trinunghi valid.')
else:
    print('Trinunghi invalid.')


'''
6. Având stringul: 'Coral is either the stupidest animal or the smartest rock'
    ● Citește de la tastatură un int x
    ● Afișează stringul fără ultimele x caractere
    Exemplu: dacă ai ales 7 => 'Coral is either the stupidest animal or the smarte'
'''

print(' ')
print('6. Afisam textul "Coral is either the stupidest animal or the smartest rock" fara ultimele caractere, in functie de numarul de la tastatura')
print(' ')



x = int(input('Introduceti un numar:'))
text = 'Coral is either the stupidest animal or the smartest rock'


print(f'Text original: "{text}"')
print(f'Textul de mai sus are {len(text)} caractere.')
print(f'Afisam text: "{text[0:-x]}".')
print(f'Dupa ce se afiseaza textul fara ultimele caractere, in functie de numarul de la tastatura, textul mai are {len(text)-x} caractere.')



'''
7. Același string. Declară un string nou care să fie format din primele 5
caractere + ultimele 5.
'''

print(' ')
print('7. Pe baza textului de la punctul 6, afisam un text nou format din primele 5 caractere si ultimele 5. ')
print(' ')

print(f'Text original: "{text}"')

primele5 = text[:5]
ultimelel5 = text[-5:]


print(f'Text nou primele 5 caractere + ultimele 5 caractere => "{primele5+ultimelel5}".')

'''
8. Același string.
    ● Salvează într-o variabilă și afișează indexul de start al cuvântului rock (hint:
    este o funcție care te ajuta sa faci asta)
    ● Folosind această variabilă + slicing, afișează tot stringul până la acest
    cuvânt
    ● output: 'Coral is either the stupidest animal or the smartest'
'''

print(' ')
print('8. Tot pentru textul de la punctul 6 salvam variabila cu ultimul cuvant, "rock", si afisam textul fara acel cuvant')
print(' ')

rock = text.index('rock')
rock_nospace = text.index('rock') - 1

print(f'Indexul de start al cuvantului "rock" este {rock}')
print(f'Text nou: "{text[0:rock_nospace]}"')

# Exerciții Bonus (may need google).

print(' ')
print('● Exerciții Bonus.')
print(' ')

'''
11. Joc ghicit zarul
Caută pe net și vezi cum se generează un număr random
Ne imaginăm ca dai cu zarul și salvăm acest număr în dice_roll
Ia numărul ghicit de la utilizator
Verifică și afișează dacă utilizatorul a ghicit
Vei avea 3 opțiuni
● Ai pierdut. Ai ales un numar mai mic. Ai ales x dar a fost y.
● Ai pierdut. Ai ales un numar mai mare. Ai ales x dar a fost y.
● Ai ghicit. Felicitări! Ai ales x si zarul a fost y.
'''

print(' ')
print('11. Ghiciti zarul.')
print(' ')

import random

dice_roll = random.randint(1,6)
user_roll = int(input('Introdu un numar de pe zar:'))

if user_roll > 6 or user_roll < 1:
    print('Numarul introdus nu se gaseste pe zar, incearca din nou, introdu un numar de la 1 la 6.')
elif dice_roll == user_roll:
    print(f'Bravo, ai nimerit zarul! Ai ales {user_roll} si era {dice_roll}.')
elif user_roll > dice_roll:
    print(f'Ai pierdut. Ai ales un numar mai mare. Ai ales {user_roll} dar a fost {dice_roll}, mai incearca.')
else:
    print(f'Ai pierdut. Ai ales un numar mai mic. Ai ales {user_roll} dar a fost {dice_roll}, mai incearca.')
