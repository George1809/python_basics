print("\n-------------------------------------------------------\n")
print("SET 1 - Functii ca obiecte (fundatia)")
print("\n")
# Scop: sa intelegi ca functiile sunt valori si pot fi manipulate ca orice obiect.

# 1 Scrie o functie add(a, b) si atribuie-o unei variabile f. Apeleaza functia prin f.

def add(a,b):
    return (a,b)

f = add
print(f("aaa","aaa"))

# 2 Creeaza o lista care contine 3 functii diferite. Parcurge lista si apeleaza fiecare functie.

def func_1(x,z):
    return x+z


def func_2(a,b):
    return a*b

def func_3(v,n):
    return v/n


lst = [(func_1,(2,3)),(func_2,(5,5)), (func_3,(7,2))]


for i,j in lst:
    print(i, *j)
    print(i(*j))

# for i in (func_1(2,3),func_2(5,5),func_3(7,2)):
#     print(i)


# 3 Scrie o functie apply(func, a, b) care primeste o functie ca parametru si o aplica.


def func(x,c):
        return x+c


def apply(func, a, b):
    
    return  func(a,b)



print(apply(func,2,2))

# 4 Scrie o functie care returneaza o functie, fara sa o apeleze.


def f1():
    def f2():
        def f3():
            return "Helllllo!!!"
        return f3
    return f2


f = f1()
ff = f()
print(ff())


#----------------

def a_func():
    return "Aaaaaaaaaaaaaaa"

b = a_func()
print(b)


print("\n-------------------------------------------------------\n")

print("SET 2 – Functii in functii (nested functions)")

print("\n")
# Scop: acomodarea cu def in def.

# 1 Scrie o functie care contine o functie interna si o apeleaza.

def function_1():
    def function_2(a,b):
        return a*b
    return function_2


x1 = function_1()
print(x1(2,4))




# 2 Scrie o functie externa care returneaza functia interna.

def extern():
    def intern():
        return intern
    return intern

x2 = extern()
print(x2)

# 3 Apeleaza functia returnata din exterior.


def extern():
    def intern():
        return intern
    return intern

x3 = extern()
print(x3())


# 4 Afiseaza din functia interna o variabila definita in functia externa

def extern():
    a = 5
    def intern():
        return a
    return intern

x4 = (extern())
print(x4())



print("\n-------------------------------------------------------\n")
print("SET 3 - Closure")
print("\n")
# Scop: intelegerea memoriei functiilor.

# 1 Scrie o functie care primeste un numar si returneaza o functie care adauga acel numar.

def func10(x):
    def sub_func10(y):
        return x+y
    return sub_func10

f10 = func10(10)
print(f10(10))


# 2 Creeaza doua functii diferite din aceeasi functie externa si testeaza-le.

def func11():
    def sub_func11_1():
        return "Sub_func11_1"
    
    def sub_func11_2():
        return "Sub_func11_2"

    return sub_func11_1, sub_func11_2



f11 = func11()

for i in range(0, len(f11)):
    print(f11[i]())
print("............")
for i in f11:
    print(i())

# 3 Demonstreaza ca functia interna pastreaza valoarea dupa terminarea functiei externe.

def func12():
    x = 4
    y = 5
    def sub_func12():
        return x, y
    return sub_func12


f12 = func12()
print(f12())
print(f12.__closure__)
print(f12.__closure__[1].cell_contents)

# 4 Modifica o variabila din exterior folosind nonlocal.

def func13():
    x = 14
    def get_x():
        return x    
    def sub_func13():
        nonlocal x
        x = 12
        return x

    return sub_func13, get_x

f13, f14 = func13()


print(f14(),f13())

 
print("\n-------------------------------------------------------\n")
print("SET 4 - Functie care primeste alta functie")
print("\n")
# Scop: mecanismul de baza al decoratorilor.

# 1 Scrie o functie wrapper(func) care afiseaza ceva si apeleaza func.

def func(b,c):
    return b+c

def wrapper(func):
    return func



print(wrapper(func))

def func1():
    return "Salutare"


def wrapper1(f):
    print("Apelam functia")
    return f()

print(wrapper1(func1))

print(".....................")
def func2():
    return "Salut"

def wrapper2(f):
    print("Inainte de apel")
    result = f()
    print("Dupa apel")
    return result

print(wrapper2(func2))



print(".....................")
# 2 Transmite o functie simpla in wrapper si ruleaza rezultatul.

# def func15(n):
#     if n % 2 == 0:
#         return "Se imparte exact!"
#     else:
#         return "Este un rest!"


# def wrapper15(f5,n):
#     print("Rezultatul functiei \"func15\" este:")
#     return f5(n)


def func15(b,n,m,l,j):
    return f"Numerele preluate prin argumente pozitionale sunt:\n{b},{n},{m},{l},{j}"

def wrapper15(f, *args):
    print("Rulez functia...")
    return f(*args)

f15 = wrapper15(func15,6,7,8,123,44)

print(f15)


print(".....................")
# 3 Modifica wrapper astfel incat sa faca ceva inainte si dupa apel.


def func16(val1, val2):
    return val1, val2


def wrapper16(ff,*args):
    ff3 = args[0] + args[1]
    print(ff3)
    fff = ff(*args)

    return (fff[0]+3) + (fff[1] +4)

f16 = wrapper16(func16, 5,6)
print(f16)



# 4 Returneaza o functie noua din wrapper.




def wrapper17():
    print("Inainte de def")
    def sub_func17(x):
        return x
    return sub_func17

ff17 = wrapper17()
print(ff17(5))