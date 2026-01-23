#string :- every string has their index and the index is starts from 0 and goes to 1,2,3,4...... 
# and their have negative index also and they starts from -1,-2,-3..... and at index -1 E will print
a = "NATURE"

print(a[0]) #a[0] signifies that we print the value N (NATURE) because this the value N of string NATURE is at index 0
print(a[-1])


#slicing:-prints only a particular part of a string like sheri,cod,coding,codin yans etc.
b="sheriyans coding "
print(b[0:9:1]) #b[0:8:1] this signifies that we print the particular part of a string by means that we start from the 0th index and goes to 8 index (imp thing when you need upto 8th index then you put 9 one extra no. by defaut ) after last collon you put the steps .

#there are default value as well
print(b[::])#this line of code print from 0th index to end index of a string and steps is 1 by default.
print(b[:])# we dont need steps colon because this line of code self dependet of (step=1). if you need steps in your print of sttring the use two collons otherwise not.



# Task 1:-
c="hello i am data Scientist"
print(c[0:5])#hello
print(c[11:15])#data
print(c[16:25])#Scientist

#Imp:- Strings are immutable in nature means that you cannot change the string.


#print statement ways:-

age = 21
des= "data scientist"

#1 :- This is not a good method 
print("my age is ",age,"my designation is",des)

#2 :-using formatted method :- This is a well method and widely used method.
print(f"hello my age is {age} and my designation is {des}.")


# Escaping sequence :-
#1
print(f"hello my name is Dushyant\n and my age is 21 ") # \n is an escaping sequence and it is used to print the thing in next line.
                                                        # there are many types of Escaping sequence like \t -. for tab (use 5 tab spaces) , \b->for backspace etc.

#2 raw sttring :- escaping sequences are not worked in raw string.
print(r"hello my name is Dushyant\n and my age is 21") #\n not work 

#Type conversions :-

d=23
print(type(a))#this line of code shows that the type of 'a' is int
a=str(a) # here in this line we convert the type of 'a' from int to string
print(type(a)) # this line of code shows that the type of 'a' is string

#conversion is happening at psbl thingsfor example
""" 
b="hello"
print(type(b)) #this line of code shows that the type of 'b' is string 
b=int(b) # this conversion is not possible 
if b="23"
b=int(b)
print(type(b)) # this line of code is possible.

"""


#there are so many typeconversions int(),str(),float(),bool()

x=21 # bool() -> True for non zero value , bool()-> false for 0

y="hello" # bool() -> True for non zero string , bool()-> false for empty string

print(bool(x))

"""
Truthy values:-almost every thing.
falsy value :- 0,0.0, false,"",{},(),[]
"""

#input statement ways:-

#1
name = input("hello what is your name ?")

print(name)
print(type(name))#type of "name"is string (by default all the things are stored in string manner when you take an input from user)

#2
age = int(input("hello what is your name ?")) #type conversion

print(age)
print(type(age))#type is int
