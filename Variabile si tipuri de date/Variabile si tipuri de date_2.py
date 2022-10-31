# Exerciții Opționale - grad de dificultate: Mediu spre greu.
print('● Exercitii sesiuni studiu in echipa.')
print(' ')
'''
1. Exercițiu:
    - citește un string de la tastatură (ex: alabala portocala);
    - salvează primul caracter într-o variabilă - indiferent care este el, încearcă
    cu 2 stringuri diferite;
    - capitalizează acest caracter peste tot, mai puțin pentru primul și ultimul
    caracter => alAbAlA portocAla.
'''

print('1. Marim peste tot intr-un string prima litera afisata, insa fara sa marim litera la inceput si sfarsit de string.')
print(' ')
capit = input('Introdu un string format din cel putin 2 cuvinte:')
primul_caracter = capit[0]
ultimul_caracter = capit[-1]
string_replace = capit.replace(primul_caracter, primul_caracter.upper())
format_final = primul_caracter.lower() + string_replace[1:-1] + ultimul_caracter.lower()
print(format_final)
print(' ')

'''
2.Exercițiu:
    - citește un user de la tastatură;
    - citește o parolă;
    - afișează: 'Parola pt user x este ***** și are x caractere';
    - ***** se va calcula dinamic, indiferent de dimensiunea parolei, trebuie să
afișeze corect.
eg: parola abc => ***
parola abcd => ****
'''
print(' ')
print('2. Afisam parola de forma *** si numarul de caractere, in functie de parola introdusa.')
user = input('Introduceti userul:')
parola = input('Introduceti parola:')
asterix = '*'
parola_ascunsa = asterix * len(parola)

print(f'Parola utilizatorului {user} este {parola_ascunsa} si are {len(parola)} caractere.')
