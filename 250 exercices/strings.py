un_sir = "Un test random care are si cifre 123 si cu spatii in plus   si cu diverse"

print(f'{un_sir.index("n")} - afisam idexul unui caracter dintr-un string')
print(f'{un_sir.count("t")} - numaram cate caractere sunt intr-un string')
print(f'{un_sir.find("re")} - gasim grupul de caractere intr-un string')
print(un_sir[1]) # afisam careacterul din string in functie de index
print(un_sir.lower()) # afisam totul cu litere mici
print(un_sir.upper()) # afisam totul cu litere mari
print(un_sir.startswith("U")) # verificam daca un string incepe cu un anumit caracter
print(un_sir.endswith("e")) # verificam daca un string se termina cu un anumit caracter
print(un_sir.strip(" ")) # strip() elimina spatii sau caractere doar la inceput si de la final de sir
print(un_sir.strip("Un")) # elimina de la final si inceput caracterele gasite
print(un_sir.replace("  ","")) # inclocuieste spatii cu ceva ce am pus, fara spatii de exemplu
print(un_sir.replace("U","u")) # inclocuieste spatii cu ceva ce am pus, fara spatii de exemplu
print(un_sir.split(" ")) # se face split la un string si se inlocuieste delimitatorul selectat si se fomreaza o lista. 
sir_fara_spatii_suplimentare = un_sir.replace("  ","") # eliminam spatiile suplimentare din text si cu split de mai jos afisam o lista curata
print(sir_fara_spatii_suplimentare.split(" ")) # se face split la un string fara spatii in plus
print(".".join(un_sir)) # introducere caracter/semn intre toate caracterele din string. 

'''
Exercise 1 - Strings
Given the code below, insert the correct negative index on line 3 in order to get the last character in the string.



How to solve a coding exercise:

Write your solution in the field below and then click on the Check Solution button.

If the solution you provide is incorrect, then try to understand the error message that appears on the right side of the screen, re-write your solution and press the Check Solution button again.

Finally, if you give up on this exercise and decide to move on, then click the Continue button.
'''

my_string = "In 2010, someone paid 10k Bitcoin for two pizzas."

