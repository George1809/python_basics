# EXERCIȚII SESIUNI STUDIU ÎN ECHIPĂ

print(' ')
print('● EXERCIȚII SESIUNI STUDIU ÎN ECHIPĂ.')
print(' ')


'''
1. Citește de la tastatură un string
    Verifică dacă primul și ultimul caracter sunt la fel. Se va folosi un assert
    Atenție: se dorește ca programul să fie case insensitive - 'apA' e acceptat
'''

print('1. Verificam daca primul si ultimul caracter dintr-un string sunt la fel, indiferent daca sunt caractere cu litere mari sau mici.')
print(' ')

s_text = input('Introduceti un string:')

assert s_text[0].lower() == s_text[-1].lower(), 'Caracterele nu corespund, verifica primul si ultimul caracter din string, ar trebui sa fie la fel.'

print('Primul si ultimul caracter din string sunt la fel.')


'''
2. Având stringul '0123456789'
    ● Afișează doar numerele pare
    ● Afișează doar numerele impare
    (hint: folosește slicing, controlează din pas)
'''

print(' ')
print('2. Afisam numerele pare si numerele impare.')
print(' ')

sir_nr = '0123456789'

print(f'Din sirul de numere "{sir_nr}", numerele pare sunt: {sir_nr[0:9:2]}.')
print(f'Din sirul de numere "{sir_nr}", numerele impare sunt: {sir_nr[1:10:2]}.')
