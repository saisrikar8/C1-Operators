'''
Review
Data Type
1. integer; int()
2. floating point; float()
3. boolean; bool()
4. string; str()

num = 4
#I am 4 years old
print("I am " + str(num) + " years old")


Variable name:
1. Must star with a letter
2. No symbols except _
3. numbers, letters can follow after thee first letter.
4. No space at all


01/21/2021
Operators

1.Math Operators(Arthimeti Operators)
Addition, +
Subtraction, -
Multiplication, *
Division, / (//, Quotient without decimal, ends with only type int)

5 / 2 = 2.5
5 // 2 = 2


Modulo(remainder), %
5 % 2 = 1
1 % 3 = 1
2 % 3 = 2
3 % 3 = 0
10 % 2 = 0

Exponent(powers), **

2 ** 2 = 4
3 ** 4 = 3 * 3 * 3 * 3 = 81



2.Assignment Operators
    -Rule Using Assignment Operators:
      A variable must be declared befor using assignment operators with the variable

    -Used to assign values to variables
    variable = data/value
    variable = input(prompt)

    0. simple Assignment, =
    1. Addition Assignment=+

        A += B 
        A = A + B 
    2. Subtraction Assignment, -=
        A -= B
        A = A - B
    3. Multiplly Assignment *=
    4.Divide Assignment /= (//=)
    5. Modulo Assignment, %=
    6. Exponent Assignment, **=

Ex)
a = 5
a += 2 #Equivalent to: a = a + 2
print(a) # Result: 7



3.Comparison operators(Relational Operators)
  -Used to compare values for conditions, Reeturns booleans after evaluations.

-Rule: Using Comparing Opeerators
  Two objects aree required such as a variable or raw data/value

  a. Equal to, ==
  b. not equal to, !=
  c. less than <
  d. less than or equal to, <=
  e. greater than, >
  f. greater than or equal to, >=

Ex)
a = 4
print(a > 4)


'''
a = 0

while(a < 10):
  print(a)
  a += 1 # a = a + 1  


'''
a   a < 10    print()  a += 1
0     True      0         1
1     True      1         2 
2     True      2         3
3     True      3         4
4     True      4         5
5     True      5         6
6     True      6         7
7     True      7         8
8     True      8         9
9     True      9        10
10    False


'''


# Math Operator (Arithmetic Operators)
x=7
y=2

# x + y = 7 + 2 = 9
print("x + y = " + str(x + y))

# x - y = 7 - 2 = 5
print("x - y = " + str(x - y))

# *
print("xy = " + str(x*y))





#Assignment Opeerators
x1 = 5
x2 = 3

x1 += 7 # x1 = x1 +7 = 5+7 = 12
print(x1)

x1 -= x2# x1 = x1-x2 = 12-3 = 9
print(x1)

x2 *= 2
print(x2)

x2 /= 3 
print(x2)

x1 %= 7
print(x1)

x1 **= x2
print(x1)