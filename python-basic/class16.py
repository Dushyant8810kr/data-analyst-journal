#tuples:tuples is an in_built data structures in python.

#Tuples has heterogenous nature.
a = (12,12.4,"hello",print())

#Tuples has immutable nature
"""b = (1,2,3,4,5)
b[1] = 20  # there will be an error.
print(b)"""

#tuple can store duplicate values.
c = (1,2,2,2,2,2,3,3,3,3,4,4,4,4,4,4,5,5,5,5)

#Tuple unpacking :-
x,y,z = (10,20,30)
print(x)#10
print(y)#20
print(z)#30


#Important thing :-
m = ()
print(type(m)) #<class 'tuple'>

n = (1)
print(type(n)) #<class 'int'>(In this case the value '1' is assign to 'a' this means that they store like that a normal variables stores value a = 1)
#if you want to overcome this situation
#then simply return

k = (1,)
print(type(k)) #<class 'tuple'>


#Slicing :- slicing in tuples is same as list
t = (10,20,30,40,50)
print(t[:3]) 

#Imp:- in tuples we dont use the functions like append...
#for over come the situation we follow the given below steps:-

#Step 1:- firstly you want make a list

a = [1,2,3,4,5,6,7]

tup = tuple(a) # here we can make tuple for using the functions like append..



#traversing:-( by the values)
r = (1,9,4,32,44)

#1
for i in r:
    print(r)

#2
for j in range(len(r)):
    print(r[j])


#methods :- there are only to methods 1) counts   2) index
#help(tuple) by the help of this we find numbers of methods or functions are available in tuple.

p = (10,20,30,40,40,40,50,50)
print(p.count(40))
print(p.index(30))

