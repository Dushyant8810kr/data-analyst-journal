#class 2 revision:-
"""
PYTHON REVISION NOTES (Class 2)
1.Print Function :-
print() : is used to display output on screen
print("Hello world")

2. Comments:-
Comments are not executed by Python
# Single line comment
"""" Multi-line comment """"

3. Variables :-
Variables are containers used to store data
a = 10
name = "Dushyant"

4. Variable Naming Rules:-
-> Cannot start with number : (1hello)
-> Cannot contain space : (hello world)
-> Can use underscore _ : (hello_world)
-> Can start with _ : (_name)

5. Naming Conventions:-
camelCase → dushyantKumar
PascalCase → DushyantKumar
snake_case → dushyant_kumar

6. Data Types:-
a = 10
b = 1.5
c = 2j
name = "Dushyant"
x = True

7. Type Checking:-
print(type(a))

8. Important Concepts:-
Python is Case Sensitive: True , true 
Dynamic Typing: a = 10 a = "hello"

9. String Rules
Strings must be inside quotes ("" or '')
 
YOUR MISTAKES (IMPORTANT):-
1. Incomplete Output: Write full output including type
2. Forgot printing types using print(type())
3. Careless spelling mistakes
 EXTRA UNDERSTANDING
"10" is string, 10 is integer
"10" + "20" = "1020", 10 + 20 = 30

"""

#class 3 :-
"""
PYTHON REVISION TEST (Class 2 : Strings, Slicing, Input):-


Section 1: Output Prediction:-

a = "NATURE"
print(a[2])  # T
print(a[-3])  # U

b = "sheriyans coding"
print(b[0:5])  # sher i
print(b[5:10])  # yans (with space)


Section 2: Slicing Logic :-

c = "hello i am data Scientist"
print(c[6:10])  # i am
print("Python"[::-1])  # nohtyP


Section 3: Concepts :-

Strings are immutable → cannot change directly
input() always returns string
Raw string ignores escape sequences


Section 4: Errors :-
a = "Hello"
a[0] = "Y"  # 
Error
age = int(input("Enter age: "))
print(type(name))  # 


Section 5: Boolean:-

name not defined
print(bool(0))    # False
print(bool(" "))  # True
print(bool(""))   # False

Challenge
name = input("Enter your name: ")
print(f"Hello {name}")
YOUR MISTAKES :-

1. Confusion in immutability strings
2. Reverse slicing not understood
3. Boolean concept mistake (' ' vs '')
4. Skipped challenge question

KEY CONCEPTS:-
Immutable → cannot modify string directly
[::-1] → reverse string
Truthy vs Falsy values matte

"""


#class 4 :-
"""
PYTHON REVISION NOTES (Class 4):-

1. Arithmetic Operators
Operator Meaning
+
Addition
Example
12 + 34 = 46
*
/
//
**
%

2. BODMAS Rule:-
print(10 + 2 * 5)
print((10 + 2) * 5)

3. Division Difference:-
print(12 / 5)   # 2.4
print(12 // 5)  # 2

4. Assignment Operators:-
a = 10
a = a + 5
a += 5

5. String Operations :-
print("hello" + " world")
print("hello" * 3)

6. Invalid Operation :-
print("hello" + 3)  # Error

7. Special Case:-
print("5" * 3)  # 555

8. Modulo Usage:-
print(10 % 2)
print(7 % 2)

YOUR MISTAKES :-
Subtraction
Multiplication
Division
12 - 34 = -22
12 * 34 = 408
12 / 5 = 2.4
Floor Division 12 // 5 = 2
Power
Modulo:-
1. Float vs Integer confusion (/ always float)
2. Incomplete concept explanation
3. Did not follow input requirement
5 ** 2 = 25
17 % 5 = 2

4. Weak explanation style:-
EXTRA UNDERSTANDING
print(5 + 2 * 3 ** 2)
 TASK
Revise and practice BODMAs

"""


#class 5 :-

"""
PYTHON REVISION NOTES (Comparison & Logical Operators):-

1. Comparison Operators:-
Operator Meaning
Example:-
==
Equal to
12 == 12 → True
!=
>
<
>=
<=


2. Boolean Results:-
print(12 == 12)
print(12 != 12)

3. Logical Operators :-
AND → all conditions true
OR → any one condition true
NOT → reverse result
print(10 > 5 and 20 > 10)
print(10 > 5 or 20 < 10)
print(not True)

4. Chained Comparison (Important):-
Not equal
Greater than
Less than
12 != 12 → False
10 > 5 → True
5 < 10 → True
Greater or equal 10 >= 10 → True
Less or equal
print(10 > 5 == True)
# means (10 > 5) and (5 == True)

5. Even Odd Logic:-
a = int(input())
if a % 2 == 0:
    print('Even')
else:
    print('Odd')
    
YOUR MISTAKES:-
1. Confusion in chained comparison
2. Weak explanation clarity
3. Minor formatting mistakes
 SUMMARY
Operator Rule
5 <= 10 → True
AND
All True



"""
