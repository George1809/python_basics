nr1 = 10
nr2 = 5
nr3 = 3
nr4 = 2.5


print(nr1, nr2, nr3, nr4)
print(type(nr1), type(nr4))
print(nr1 - nr2)
print(nr2 - nr1)
print(nr1 / nr2)
print(nr1 / nr3)
print(nr1 % nr2) # restul impartirii - modulo
print(nr1 % nr3) # restul impartirii - modulo
print(nr1 ** 2, nr3**2) # ridicare la putere
print(3 / 2) # float rezultat
print(3 // 2) # cu rotunjire rezultat, partea intreaga
print(100 - 5 ** 2 / 5 * 2) # se fac operatiunile in ordine, asa cum ar trebui
print(int(nr4)) # rotunjire valoare
print(float(nr3)) # adauga zecimala 0
print(abs(nr1)) # valoare absoluta
print(abs(-nr1)) # valoare abosulta, dispare minusul
print(max(nr2,nr3,nr1)) # afiseaza valoarea maxima
print(min(nr2,nr3,nr1)) # afiseaza valoarea minima
print(pow(nr2,nr3,nr1)) # daca e cu doua argumente e echivalent cu nr ** nr(la putere), dar cu 3 argumente inseamna (nr2 ** nr3) % nr1 (modulo)
print((1 == 1) and (2 == 2)) # ambele sunt adevarate deci e true
print((1 == 1) or (2 == 2)) # ori una ori alta true inseamna ca e true
print(not(1 == 1)) # false ca nu e adevarat ca 1 nu este egal cu 1
print(not(1 == 2)) # ftrue, pentru ca e adevarat ca 1 nu este egal cu 2
print(bool(None))
print(bool(0))
print(bool(2))
print(bool("Blabla"))
print(bool(""))