#set:-
"""
s = {}
print(type(s)) #<class 'dict'> because dictionary is the pair key and value (this is known as empty dictionary)
"""

#1
"""
s = {10,20,30,40,50}
print(type(s)) #<class 'set'>

"""

#you can only store hasable values in set.
"""s = {10,"hello",(10,20,30)}

print(hash(10)) """# hasable numbers are exactly of same value of number (10)

#eroor:- we can't store a list into set but tuple can. because we cant change a list to hasable number.


#set has unordered nature.
"""s = {10,10,50,20,60,80}

print(s)"""#{80, 50, 20, 10, 60} this happens because the set stores their element by their their hash values (this thing is known as unordered nature.)



#set can't have duplicate values
"""s = {10,0,10,20,20,30,30,30,30,30}

print(s)""" #{0, 10, 20, 30} not prints the duplicate values


#set dont have indexing to access the elements of set becuase of unordered nature.so we cant do slicing in set.

# set constructer:-
#firstly you make list then convert it to set.
"""a = [1,2,3,3,3,10,9,913,31,31,55,44,33,9,9,11,11,11]

s = set(a)
print(s)""" #{1, 2, 3, 33, 9, 10, 11, 44, 913, 55, 31}



#traversing on set:-you can traverse the set on the basis of hash values
# there is no traversing on index values
"""
s = {10,36,23,45,99,87,62,102,11,39,55,67}

for i in s:
    print(i)
"""


#set heavily depends on methods refer W3 school

#1 add() method:-
s = {10,50,30,40}

#1 add() method:-
#s.add(20): randomly add the value in set

#2 clear():-
#s.clear() : clear all the set elements of set.

#3 difference():-
s1 = {10,20,30,40}
s2 = {30,40,50,60}

#print(s1.difference(s2)) #{10, 20}
#print(s2.difference(s1)) #{50, 60}

#short hand method:-
#print(s1 - s2)  #{10, 20}
#print(s2 - s1)  ##{50, 60}

#4 discard():-
#s1.discard(10)  # removes specified elements from set.


#5 intersection(&):- intersection operator -> & (return common elements between sets)
#print(s1 & s2) #{40,30}

#6 isdisjoint() :-return true/False on the basis of intersection between sets

#7 issubset(<=) :- return true if all elements of set is found on another set.

#8 pop() :- removes an element from set

#9 remove() :- same as discard.

#10 symmetric_difference(^) :- remove the common elements between sets and return other left elements of both sets.

#11 union(|) :- merge all elements of sets.




