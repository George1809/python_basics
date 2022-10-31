# Exerciții Recomandate - grad de dificultate: Ușor:

'''
1. Revizualizează întâlnirea 3 și ia notițe în caz că ți-a scăpat ceva.
2. Vizualizează din ‘Primii pași în Programare’ video

- Structuri de date
- Flow Control

Response: Rezolvat
'''

# Exerciții obligatorii - grad de dificultate: Usor spre Mediu:

print(' ')
print('● Exerciții obligatorii - grad de dificultate: Ușor spre Mediu.')


'''
Pentru toate exercițiile se va folosi noțiunea de if în rezolvare.
Indirect vei exersa și operatorii în cadrul condițiilor ramurilor din if.
X poate fi inițializat direct în cod sau citit de la tastatură, după preferințe.
X este un int.
'''

'''
1. Declară o listă note_muzicale în care să pui do re mi etc până la do
    ● Afișeaz-o.
    ● Inversează ordinea folosind slicing și suprascrie această listă.
    ● Printează varianta actuală (inversată).
    ● Pe această listă aplică o metodă care bănuiești că face același lucru,
        adică să îi inverseze ordinea. Nu trebuie să o suprascrii în acest caz,
        deoarece metoda face asta automat.
    ● Printează varianta actuală a listei. Practic ai ajuns înapoi la varianta
        inițială.
        
Concluzii: slicing e temporar, dacă vrei să păstrezi nouă variantă va trebui să
suprascrii lista sau să o salvezi într-o listă nouă. Metoda găsită de tine face
suprascrierea automat și permanentizează aceste modificări. Ambele variante
își găsesc utilitatea în funcție de ce ne dorim în acel moment.
'''

print('''
1. Declaram lista note muzicale si apoi facem operatiunile: afisam lista, inversam ordinea si suprascriem lista,
printam varianta actuala (inversata),aplicam metoda de inversare ordine lista, fara suprascriere,
printare varianta actuala a listei, pentru a ajunge la varianta initiala.''')
print(' ')

note_muzicale = ['Do','Re','Mi','Fa','Sol','La','Si','Do']
print('Avem lista initiala: [\'Do\',\'Re\',\'Mi\',\'Fa\',\'Sol\',\'La\',\'Si\',\'Do\'].')
print(' ')
print(f'Afisam lista initiala: {note_muzicale}.')
print(' ')

note_muzicale_invers = note_muzicale[::-1] #inversare lista prin slice.

print(f'Afisam inversata lista initiala: {note_muzicale_invers}.')
print(' ')

note_muzicale_invers.reverse()

print(f'Aplicam alta metoda de inversare lista si o afisam din nou: {note_muzicale_invers} (stare initiala).')


'''
2. De câte ori apare ‘Do’ in lista.
'''

print(' ')
print('2. De câte ori apare ‘Do’?.')
print(' ')

print(f'In lista de la punctul 1, nota "Do" apare de {note_muzicale.count("Do")} ori.')

'''
3.Având 2 liste, [3, 1, 0, 2] și [6, 5, 4]
    Găsește 2 variante să le unești într-o singură listă.
'''

print(' ')
print('3. Unim 2 liste, prin 2 metode.')
print(' ')

lista1_v1 = [3, 1, 0, 2]
lista2_v1= [6, 5, 4]

lista1_v1.extend(lista2_v1)

print('Avem listele: [3, 1, 0, 2] și [6, 5, 4].')


print(' ')
print(f'Varianta unu pentru unirea listelor - "metoda extend": {lista1_v1}')
print(' ')


lista1_v2 = [3, 1, 0, 2]
lista2_v2= [6, 5, 4]

lista_unita_v2 = lista1_v2 + lista2_v2

print(f'Varianta doi pentru unirea listelor - "lista 1 + lista 2": {lista_unita_v2}')

'''
4.
    ● Sortează și afișează lista generată la exercițiul anterior.
    ● Sortează numărul 0 folosind o funcție.
    ● Afișaza iar lista.
'''

print(' ')
print('4. Afisam si sortam listele de la exercitiul anterior.')
print(' ')

lista1_v1.sort()
lista_unita_v2.sort()

print(lista1_v1)
print(lista_unita_v2)

print(lista1_v1[0])
print(lista_unita_v2[0])

'''
5. Folosind un if verifică lista generată la exercițiul 3 și afișează:
    ● Lista este goală.
    ● Lista nu este goală.
'''

print(' ')
print('5. Afisam daca listele de la exercitiul 3 sunt goale sau nu.')
print(' ')

if len(lista1_v1) == 0:
    print('Lista de la exercitiul 3 este goala.')
else:
    print('Lista de la exercitiul 3 nu este goala.')


'''
6. Folosește o funcție care să șteargă lista de la exercițiul 3.
'''

print(' ')
print('6. Stergem lista de la exercitiul 3.')
print(' ')

lista1_v1.clear()
print(f'In lista "lista1_v1" avem acum 0 elemente: {lista1_v1}.')


'''
7. Copy paste la exercițiul 5. Verifică încă o dată.
    Acum ar trebui să se afișeze că lista e goală.
'''

print(' ')
print('7. Verificam inca o data lista de la exercitiul 3, sa vedem daca este goala sau nu.')
print(' ')

if len(lista1_v1) == 0:
    print('Lista de la exercitiul 3 este goala.')
else:
    print('Lista de la exercitiul 3 nu este goala.')

'''
8. Având dicționarul dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
    Folosește o funcție că să afișezi Elevii (cheile)
'''

print(' ')
print('8. Afisam valorile cheilor din dictionarul "dict1".')
print(' ')

dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}

print(f'Avem dictionarul "dict1": {dict1}')
print(f'Valorile cheilor din dictionarul "dict1" sunt {dict1.keys()}')


'''
9. Printează cei 3 elevi și notele lor
    Ex: ‘Ana a luat nota {x}’
    Doar nota o vei lua folosindu-te de cheie
'''

print(' ')
print('9. Afisam notele elevilor din dictionarul "dict1".')
print(' ')

print(f'Avem dictionarul "dict1": {dict1}')
print(f'''Ana a luat nota {dict1["Ana"]}
Gigel a luat nota {dict1["Gigel"]}
Dorel a luat nota {dict1["Dorel"]}
''')

'''
10. Dorel a făcut contestație și a primit 6
    ● Modifică nota lui Dorel în 6
    ● Printează nota după modificare
'''

print(' ')
print('10. Modificam nota lui Dorel din 5 in 6 din dictionarul "dict1" si apoi o afisam.')
print(' ')

print(f'Avem dictionarul "dict1": {dict1}')
dict1['Dorel'] = 6
print(f'Initial, nota lui Dorel era 5, dar dupa contestatie acum nota este {dict1["Dorel"]}.')

'''
11. Gigel se transferă din clasă
    ● Căuta o funcție care să îl șteargă
    ● Vine un coleg nou. Adaugă Ionică, cu nota 9
    ● Printează noii elevi
'''

print(' ')
print('11. Stergem elevul Gigel din dictionarul "dict1" si adaugam elevul Ionică, cu nota 9.')
print(' ')

print(f'Avem dictionarul initial "dict1": {dict1}')

dict1.pop('Gigel')
dict1['Ionică'] = 9
print(f'Noii elevi din dictionarul "dict1" sunt {dict1.keys()}')


# Exerciții Opționale - grad de dificultate: Mediu spre greu (may need Google).

print('● Exerciții Opționale - grad de dificultate: Mediu spre greu (may need Google)')
print(' ')

'''
1. Ne imaginăm o echipă de fotbal pt teren sintetic.
    3 Schimbări maxime admise:
    ● Declară o Listă cu 5 jucători
    ● Schimbari_efectuate = te joci tu cu valori diferite
    ● Schimbari_max = 3
    Dacă Jucătorul x e în teren și mai avem schimbări la dispoziție
        - Efectuează schimbarea
        - Șterge jucătorul scos din listă
        - Adaugă jucătorul intrat
        - Afișază a intrat x, a ieșit y, mai ai z schimbări
    Dacă jucătorul nu e în teren:
        - Afișază ‘nu se poate efectua schimbarea deoarece jucătorul x nu e în
        teren’
    - Afișază ‘mai ai z schimbări’
Testează codul cu diferite valori

Google search hint
“how to check if item is în list python”
'''


print(' ')
print('1. Joc echipa de fotbal si schimbari in echipa.')
print(' ')



'''
jucatori = ['George','Alexandru','Mihai','Catalin','Ion']
print(jucatori)
print(' ')

schimbari_efectuate = 0
nr_schimbari = 3

if jucator_schimbat in jucatori:
    schimbari_efectuate += 1
    nr_schimbari -= 1
    print(f'Atentie, facem schimbare!')
    jucatori.remove(jucator_schimbat)
    jucatori.append(jucator_intrat)
    print(f'Ai facut o schimbare, mai ai {nr_schimbari} schimbari')
    print(jucatori)
else:
    print(f'Jucatorul nu exista, mai ai {nr_schimbari} schimbari, trebuie sa fie un jucator din teren')
    print(jucatori)
    jucatori.remove(jucator_schimbat)
    jucatori.append(jucator_intrat)

jucator_schimbat = input('Ce jucator iese:')
jucator_intrat = input('Ce jucator intra:')

if jucator_schimbat in jucatori:
    schimbari_efectuate += 1
    nr_schimbari -= 1
    print(f'Atentie, facem schimbare!')
    jucatori.remove(jucator_schimbat)
    jucatori.append(jucator_intrat)
    print(f'Ai facut o schimbare, mai ai {nr_schimbari} schimbari')
    print(jucatori)
else:
    print(f'Jucatorul nu exista, mai ai {nr_schimbari} schimbari')


jucator_schimbat = input('Ce jucator iese:')
jucator_intrat = input('Ce jucator intra:')

if jucator_schimbat in jucatori:
    schimbari_efectuate += 1
    nr_schimbari -= 1
    print(f'Atentie, facem schimbare!')
    jucatori.remove(jucator_schimbat)
    jucatori.append(jucator_intrat)
    print(f'Ai facut o schimbare, mai {nr_schimbari} schimbare')
    print(jucatori)
else:
    print(f'Jucatorul nu exista, mai ai {nr_schimbari} schimbare')
'''

jucatori = ['George','Alexandru','Mihai','Catalin','Ion']
print(jucatori)
print(' ')

nr_schimbari = 3

while nr_schimbari > 0:
    nr_schimbari -= 1
    jucator_schimbat = input('Ce jucator iese:')
    jucator_intrat = input('Ce jucator intra:')
    if jucator_schimbat in jucatori and nr_schimbari > 1:
        print('Atentie, facem schimbare!')
        jucatori.remove(jucator_schimbat)
        jucatori.append(jucator_intrat)
        print(f'A iesit {jucator_schimbat} si a intrat {jucator_intrat}, mai ai disponibile {nr_schimbari} schimbari.')
        print(f'Acum in teren sunt jucatorii: {jucatori}')
    elif jucator_schimbat in jucatori and nr_schimbari == 1:
        print('Atentie, facem schimbare!')
        jucatori.remove(jucator_schimbat)
        jucatori.append(jucator_intrat)
        print(f'A iesit {jucator_schimbat} si a intrat {jucator_intrat}, mai ai {nr_schimbari} schimbare disponibila.')
        print(f'Acum in teren sunt jucatorii: {jucatori}')
    elif jucator_schimbat in jucatori and nr_schimbari == 0:
        print('Atentie, facem schimbare!')
        jucatori.remove(jucator_schimbat)
        jucatori.append(jucator_intrat)
        print(f'A iesit {jucator_schimbat} si a intrat {jucator_intrat}.')
        print(f'Nu mai ai schimbari disponibile.')
        print(f'In teren au ramas jucatorii: {jucatori}')
    elif nr_schimbari == 1:
        nr_schimbari += 1
        print('Jucatorul nu este in teren, trebuie sa alegi un jucator existent in teren')
        print(f'Jucatorii prezenti in teren sunt: {jucatori}')
        print(f'Mai ai {nr_schimbari} schimbari disponibile.')
    else:
        nr_schimbari += 1
        print('Jucatorul nu este in teren, trebuie sa alegi un jucator existent in teren')
        print(f'Jucatorii prezenti in teren sunt: {jucatori}')
        print(f'Mai ai {nr_schimbari} schimbare disponibila.')