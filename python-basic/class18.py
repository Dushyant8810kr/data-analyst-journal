#Dictionary:-Dictionary is used to store multiple values in Key:Value format 
#Dictionary syntax {} with key value pairs

d = {1:10,"hello":20,3:30}

print(type(d)) #<class 'dict'>

# In older version of pyhton like before version 3.7 dictioneries are in unorderd
# But in modern python version the dictionaries are in ordered manner.
# like in "list" we access the element by their index and in dictionar we use key to access the value.
# key can be of any data type

print(d['hello']) #20
print(d[1])       #10


#IMP :- Dictionaries are mutable(change),we can change only the value not the key.

d["hello"] = 1000    # i am changing the values according to their key.

#IMP :- we only give the duplicate values not the duplicate Keys in dictionaries this will cause the accessing method for accesing the values.



# Dictionary constructor(Creation method) :-
"""
#1
b = dict(name = "Dushyant",age = 24,gender = "Male")
print(b)

#2
a = dict([("name","Suraj"),("age","24"),("gender","male")])
print(a)

"""

#Dictionary traversing :-Traversing can be done on the basis of keys as well as values
"""
#1
a = {10:100,20:200,30:300}

for i in a:
    print(i)    #acessing the key
    print(a[i]) #accessing the values according to their keys

#2
for i in a.values():
    print(i)
"""

#Dictionary methods :- there are not such methods in dictionary   (help(dist))

#1:-
#clear() : clear all the items of dictionary

#2:-
#copy() : return the shallow copy of dictionary

#3:-
#get() : returns the values of keys if key exist in the dictionary,else default

#4:-
#items() :- return the set-like object providing the view on the dict's items

#5:-
#keys() :- return the set-like object providing the view on the dict's keys

help(dict)

#6:-
#pop() :- D.pop(k[,d]) -> v, remove specified key and return the corresponding value.  If the key is not found, return the default if given; otherwise,raise a KeyError.

#7:-
#popitem : Remove and return a (key, value) pair as a 2-tuple.Pairs are returned in LIFO (last-in, first-out) order .Raises KeyError if the dict is empty


#8:-
"""a = {10:100,20:200,30:300}
b = {40:400,50:500,60:600}

a.update(b)    # merge dict b to dict a


print(a)"""


