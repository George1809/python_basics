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

un_sir1 = "testtex1t"
print(un_sir1.capitalize()) # capitalizare prima litera din string
print(un_sir.lstrip() + " test") # elimina toate spatiile de la inceput de string
print(un_sir.rstrip() + " test") # elimina toate spatiile de la final de string
print(un_sir.title()) # capitalizeaza sau face ca toate cuvintele dinstr-un string sa inceapa cu litera mare
print(un_sir1.isalnum()) # returneaza True daca toate caracterele din string sunt alfanumerice
print(un_sir1.isalpha()) # returneaza True daca toate caracterele sunt doar litere (fara cifre, fara spatii)
print (un_sir1.isdigit(), un_sir1.islower(), un_sir.isnumeric(),un_sir.isspace(),un_sir.istitle(),un_sir.isupper())
# doar digit, True daca toate literele din string sunt cu litere mici, doar caractere numerice, doar spatii, daca toate cuvintele sunt titlecaseed, True daca toate literele din string sunt majuscule

print(un_sir + " " + un_sir1) # concatenare text cu +
print("a" in un_sir) # verificare daca un caracter este intr-un string
print("x" not in un_sir) # verificare ca un caracter nu este intr-un string
print("Cisco model: %s, %d WAN slots, IOS %f" % ("2600XM", 2, 12.4)) # model vechi de formatare cu %: %s e string si %d este integer si %f este float -> "un text cu %s si %d" % (valoare1, valoare2)
print("Cisco model: %s, %d WAN slots, IOS %.f" % ("2600XM", 2, 12.4))
print("Cisco model: %s, %d WAN slots, IOS %.1f" % ("2600XM", 2, 12.4))
print("Cisco model: %s, %d WAN slots, IOS %.2f" % ("2600XM", 2, 12.4))
print("Cisco model: {}, {} WAN slots, IOS {}".format("2600XM", 2, 12.4)) # alt tip de format
print("Cisco model: {0}, {1} WAN slots, IOS {2}".format("2600XM", 2, 12.4)) # la fel, alt timp de format si printare string

# string slicing (important!)
print(" ")
un_sir2 = "O E2 10.110.8.9 [160/5] via 10.119.254.6, 0:01:00, Ethernet2"

print(un_sir2[5:14]) # slice starting ar index 5 up to, but not including, index 14
print(un_sir2[5]) # exact index 5
print(un_sir2[5:]) # arata tot textul pronind de la index 5
print(un_sir2[:14]) # arata tot textul pana la index 14 dar nu afiseaza si index 14