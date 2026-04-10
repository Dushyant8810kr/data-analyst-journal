#lambda function :- by the use of lambda function we write the anonymous or short function in one line.

#long format :-
"""

def addition(a,b):
    return a+b
print(addition(12,12))
"""

#short format by lambda function :-

#1
"""
square = lambda a : print(a**2)
square(12) #144

"""

#2
"""
add = lambda x,y : x+y

print(add(12,13))  #25

"""


#map :- purpose is simple (apply function to every items of an iterable(list ,tuple ,dict etc. ) and return  new iterable.)

#syntax :- map(function,iterable) at function place you use a lambda funtion or any full function.


#1 :-
"""
a = [1,2,3,4]

l = map(lambda x : x**2,a)

print(list(l))  #[1, 4, 9, 16]

"""

#2 :-
"""
def square(x):
    return x**2
a = [1,2,3,4]
l = map(square,a)

print(list(l))  #[1, 4, 9, 16]

"""

#filter :- 
#purpose :- filter item from an iterable based on condition.

#syntax :- filter(function,iterable)
"""
a = [1,2,3,4,5]

l = filter(lambda x : x%2==0,a)

print(list(l))

"""



#zip :-
#purpose :- combine multiple iterables inton paisrs of elements.

#syntax :- map(iterable 1, iterable 2 ,.....)
"""
name = ["Dushyant","suraj","Jatin"]
age = [24,21,22]

comb = zip(name,age)
#print(list(comb))
print(dict(list(comb)))

"""


#short cut to write code:-

#list comprehensions :-
"""
a = [1,2,3,4,5,6,7,8,9]

l = [i for i in a if i %2==0 ]
print(l)

"""
#set:-
"""
a = [1,2,3,4,5,6,7,8,9]

l = {i for i in a if i %2==0} 
print(l)

"""

#Dict :-
"""
a = [1,2,3,4,5,6,7,8,9]

l = {i:i**2 for i in a if i %2==0} 
print(l)
"""


#generator :-
#purpose :- generator is a special type of iterator that generate item one by one instead of storing the entire sequence in memory.

#why use the :-
#saves the memory for lrge data sets

#Efficient for lazy evaluation (compue value only when needed)
"""
def my_generator():
    for i in range(5):
        yield i

gen = my_generator()
print(next(gen)) #0
print(next(gen)) #1
print(list(gen)) #[2, 3, 4]

"""
#generator comprehension :-
"""
sequence = (i**2  for i in range(5))

print(next(sequence)) #0
print(next(sequence)) #1
"""

#Decorator :-

#1:-
"""
def my_decorator(func):
    def wrapper():
        print("hello i print before")
        func()
        print("hello i print after")
    return wrapper



@my_decorator
def say_hello():
    print("hello")

say_hello()
"""

#2:-
def decorator(func):
    def wrapper(a,b):
        print("your addition of numbers is :")
        func(a,b)
        print("thankyou for using this")
    return wrapper




@decorator
def add(a,b):
    print(a+b)

add(12,12)