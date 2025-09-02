'''
If / Elif / Else conditionals - executing code based on one or more conditions being evaluated as True or False; the "elif" and "else" clauses are optional

Equals: a == b
Not Equals: a != b
Less than: a < b
Less than or equal to: a <= b
Greater than: a > b
Greater than or equal to: a >= b
and
or
'''

x = 5
#x = 3
#x = 6

if x > 5:
    print("Nu e adevarat")
elif x == 5:
    print("Asta e adevarata")
else:
    print("x nu este mai mare decat 5")

print("")
#nested if

y = 41

if y > 10:
  print("Above ten,")
  if y > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")


print("")
# both conditions are True - and

a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")


print("")
# at least one of the conditions is True - or

a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")

