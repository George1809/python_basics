# 1. Slice s1. Slice si operatii pe sirurii operatii pe siruri


# 1. Scrie o functie `middle_three(s: str) -> str` care primeste un string cu lungime impar si intoarce cele 3 caractere din mijloc.



def middle_three(x):
    if len(x) % 2 == 0:
        print("Lungimea este para, functia va returna rezultat doar in cazul unui sir cu o lungime impara")
    else:
        mid = round(len(x) / 2)
        min = mid - 2
        plus = mid + 1
        impar = x[min:plus]
        print(impar)


middle_three("abbbccvadsfasdfasdf")

# 2. Scrie o functie `every_second_char(s: str) -> str` care intoarce un nou string format din fiecare al doilea caracter (incepand de la indexul 0).


def every_second_char(x):
    return (x[::2])


rez = every_second_char("banana for you")
print(rez)




def every_second_char_v2(x):
    l = []
    for i in range(len(x)):      
        if i % 2 == 0:
            l.append(x[i])
    return l


rez1 = every_second_char_v2("banana for you")
print(rez1)


def every_second_char(a_string):
    for i in a_string:
        new_string = []
        new_string.append(a_string[::2])
    return new_string

rez2 = every_second_char("banana for you")
print(rez2)

# 3. Avand un string de forma `"nume@domeniu.ext"`, scrie o functie `hide_email(email)` care mascheaza tot ce este intre primul si ultimul caracter al partii de nume cu `*`. Exemplu: `"alexandru@exemplu.ro"` → `"a******u@exemplu.ro"`.



def hide_email(email):
    char_find = email.find("@")
    before_domain = len(email[:char_find])
    email_domain = email[char_find:]
    final_hide_email = email[:1] + ("*" * (before_domain-2)) + email[char_find-1] + email_domain
    return final_hide_email



rez3 = hide_email("george.nicolae86@yahoo.com")
print(rez3)




test = "asdfasdfax@zsdfasdfasdf.com"

email_name, email_domain = test.split("@", 1)

print(email_name)
print(email_domain)
print(email_name[0] + "*" * (len(email_name)- 2) + email_name[-1] + "@" + email_domain)


### 2. Liste, liste comprehensions

# 1. Scrie o functie `unique_sorted(nums)` care:
#    - primeste o lista de int-uri
#    - elimina duplicatele
#    - intoarce o lista sortata crescator.

def unique_sorted(nums):
    list_unique = set(nums)
    list_sort = sorted(list_unique)
    return nums, list_unique,list_sort


rez4 = unique_sorted([1,2,1,1,5,6,2,8,9,23,434,5,2,5456,2,46,456,79,77,4465,13,45,66,77,99,12,1])
print(rez4)


def unique_sorted_2(nums2):
    return sorted(set(nums2))

rez5 = unique_sorted_2([2,2,2,2,3,4,5,66,7,2,4,8,9,0])
print(rez5)


# 2. Scrie o functie `flatten(list_of_lists)` care primeste o lista de liste de int-uri si intoarce o singura lista cu toate elementele (platita).

def flatten(list_of_lists):
    list1 = list_of_lists[0]
    list2 = list_of_lists[1]
    list3 = list_of_lists[2]
    list4 = list_of_lists[3]
    return list1 + list2 + list3 + list4

rez6 = flatten([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
print(rez6)


def flatten_1(list_of_lists):
    return list_of_lists[0] + list_of_lists[1] + list_of_lists[2] + list_of_lists[3]

rez7 = flatten_1([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
print(rez7)


def flatten_2(list_of_lists):
    list_concat = []
    for i in range(len(list_of_lists)):
        list_concat += list_of_lists[i]

    return list_concat

rez8 = flatten_2([[1,2,3,4],[5,6,7,8],[9,10,11,12],[9,10,11,12],[9,10,11,12],[9,10,11,12]])
print(rez8)


# 3. Folosind list comprehension, scrie o functie `squares_of_even(nums)` care intoarce patratul numerelor pare din lista `nums`.


def squares_of_even(nums):
    pare_square = []
    for n in nums:
        if n % 2 == 0:
            pare_square.append(n ** 2)       
    return pare_square


rez9 = squares_of_even([1,2,3,4,5,6,7,8,9,10,11,12,13,44,55,66,77,88,99,100,105,110])
print(rez9)

nums = [1,2,3,4]
result = [n ** 2 for n in nums if n%2 ==0]
print(result)



### 3. Dict, set, operatii pe colectii

''' 7. Ai o lista de tuple de forma `[(nume, scor), ...]`. Scrie o functie `group_scores(pairs)` care intoarce
un dict de forma `{nume: [lista_scoruri]}`.
'''

def group_scores(pairs):
    result = {}

    for name, score in pairs:
        print(name)
        print(score)
        if name not in result:           
            result[name] = []
            print(result[name])
        result[name].append(score)
        print(result[name])
    return result

rez10 = group_scores([("George", "5"),("George", "8"), ("Teste", "10"), ("Teste", "11"), ("George", "21")])
print(rez10)



blabla = {}


blabla["George"]= "5"
print(blabla)


# 8. Scrie o functie `common_keys(d1, d2)` care primeste doua dict-uri si intoarce un set cu cheile care apar in ambele.

def common_keys(d1, d2):
    all = set(d1.keys()).intersection(set(d2.keys()))
    return all


rez11 = common_keys(
    {"George":"A", "George":"b", "teste":"none"},
    {"Prime":"yes","Second":"none","Third":4, "George":"teste"}
)
print(rez11)

# 9. Scrie o functie `invert_dict(d)` care inverseaza un dictionar de forma `{cheie: valoare}` in `{valoare: lista_chei}` 
# (daca mai multe chei au aceeasi valoare).


def invert_dict(the_dict):
    result = {}
    for key in the_dict:
        if the_dict[key] not in result:
            result[the_dict[key]] = []
        result[the_dict[key]].append(key)

    return result

rez12 = invert_dict({"Prime":"yes","Second":"Cicaleta","Third":"yes", "Georgee":"teste","Primee":"nope","Georgel":"teste", "Vio":"teste"})
print(rez12)

bb = {"Prime":"yes", "Second":"yes"}


new = {}
for i in bb: 
    print(i)
    print(bb[i])
    if bb[i] not in new:
        print(bb[i])
        new[bb[i]] = []
    new[bb[i]].append(i)
print(new)


# print(list(bb.keys()))
# print(list(bb.values()))



### 4. Functii, *args, **kwargs, decoratori

# 10. Scrie un decorator `time_call` care afiseaza timpul de executie al unei functii (foloseste `time.perf_counter()`).





# 11. Scrie un decorator `debug` care afiseaza numele functiei, argumentele primite si valoarea de retur.
# 12. Scrie o functie `safe_div(a, b, *, default=None)` care imparte `a` la `b` si intoarce `default` daca apare
#  `ZeroDivisionError` sau `TypeError`.
