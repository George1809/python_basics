# Teorie:
# 

print("\n================ FUNCTII SIMPLE – NIVEL USOR ================\n")

print("1. Functie care returneaza dublul unui numar.")

def es_func1(x):
    return x*2

rez1 = es_func1(4)
print(rez1)

print("----------------------")
print("2. Functie care returneaza patratul unui numar.")

def es_func2(x):
    return x ** 2

rez2 = es_func2(11)
print(rez2)

print("----------------------")
print("3. Functie care verifica daca un numar este par.")

def es_func3(x):
    if x % 2 == 0:
        return f"Numarul {x} este par!"
    else:
        return f"Numarul {x} este impar!"

# def es_func3(x):
#     return x % 2 == 0   in cazul asta doar verifica, prin Treu si False daca e adevarat


rez3 = es_func3(11)
print(rez3) 
rez3_1 = es_func3(10)
print(rez3_1) 

print("----------------------")
print("4. Functie care returneaza maximul dintre doua numere.")

def es_func4(x,y):
    return max(x,y)


rez4=es_func4(12523,3563455)
print(rez4)

print("----------------------")
print("5. Functie care returneaza lungimea unui string.")

def es_func5(b):
    return len(b)

rez5 = es_func5("aslfkjaslfkjhalskdfhasdfjrh;wrlgnas.dvmnasmd.fm.nasdfkla;sdjfklasdfj'; aksdfj;alskdfj")
print(rez5)

print("----------------------")
print("6. Functie care returneaza suma unei liste.")

def es_func6(g):
    return sum(g)


rez6 = es_func6([1,2,3,11,3123,245,456,67356,23,3,5,6,3467346])
print(rez6)


print("----------------------")
print("7. Functie care returneaza ultimul element din lista.")

# def es_func7(last):
#     return last   #aici nu returneaza, returneaza toata lista de fapt si fac print cu slice

def es_func7(last):
    return last[-1]  # aici se returneaza de fapt ultima lista si doar fac print la rezultat, de inteles mereu si atentie la return si ce se cere la return

rez7 = es_func7([1,4,56,7,68,8,8,9,9,9,8,6,5,23452354])
print(rez7)



# print("----------------------")
# print("8. Functie care verifica daca un numar este pozitiv.")
# print("----------------------")
# print("9. Functie care returneaza valoarea absoluta.")
# print("----------------------")
# print("10. Functie care afiseaza un mesaj personalizat.")

# print("\n================ FUNCTII SIMPLE – NIVEL MEDIU ================\n")

# print("1. Functie care returneaza suma numerelor pare din lista.")
# print("----------------------")
# print("2. Functie care numara elementele mai mari decat o valoare.")
# print("----------------------")
# print("3. Functie care elimina duplicatele din lista.")
# print("----------------------")
# print("4. Functie care construieste un dictionar numar -> patrat.")
# print("----------------------")
# print("5. Functie care inverseaza un string folosind for.")
# print("----------------------")
# print("6. Functie care verifica daca toate valorile sunt pozitive.")
# print("----------------------")
# print("7. Functie care returneaza minimul si maximul.")
# print("----------------------")
# print("8. Functie care foloseste while pentru a calcula suma.")
# print("----------------------")
# print("9. Functie care grupeaza pare/impare.")
# print("----------------------")
# print("10. Functie care calculeaza media valorilor.")

# print("\n================ FUNCTII SIMPLE – NIVEL GREU ================\n")

# print("1. Functie care calculeaza frecventa elementelor.")
# print("----------------------")
# print("2. Functie care returneaza top 3 valori.")
# print("----------------------")
# print("3. Functie care verifica daca lista este sortata.")
# print("----------------------")
# print("4. Functie care valideaza parola.")
# print("----------------------")
# print("5. Functie care construieste histograma.")
# print("----------------------")
# print("6. Functie care filtreaza valori dupa conditii multiple.")
# print("----------------------")
# print("7. Functie care simuleaza catalog note.")
# print("----------------------")
# print("8. Functie care combina liste intr-un dictionar.")
# print("----------------------")
# print("9. Functie care proceseaza lista de dictionare.")
# print("----------------------")
# print("10. Functie care implementeaza cautare custom.")