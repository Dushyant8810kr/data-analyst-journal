#LIST :-(List is heterogenous, means we store all data types in 'List'and all functions also)

a = [1,1.2,2j,"Dushyant",print(),str()] 
print(a)

# list can also store duplicates
b = [1,1,1,2,2,2,2,3,3,3,3]

#list is mutable (you can change the values of 'list')

# indexing :- Indexing method of list is same as Indexing method of string.
l = [10,20,30,40,50] # inddexing is start from 0 and goes like 1,2,3,4,5,.....(0,1,2,3,4...)(at index 0 we access 10 from list and so on according to their index number) it is like front tracking
# there is an "negative indexing" also which starts from -1 and goes like -2,-3,-4,-5....(-1,-2,-3,-4,-5....)(at index -1 we access 50 from list and so on according to their index number) it is like back-tracking

#Slicing:-
print(l[:3]) # [10,20,30] # In list the slicing method is also same as string slicing in which there are (start:stop:step)

"""
#string is immutable:-
s = "FATURE"
s[0] = 'N' # this shows an error because string is immutable

"""


"""

#but in list we change the list value easily as per our recuirement.
l=[10,20,30,45,50]
l[3] = 40
print(l[3]) # 40

"""



#Deep copy and shallow copy:-
"""
#1) reference copy:-
x = [10,20,30,40,50]
y = x # this thing is known as referencing in which we stores the locations of x to y

y[0]=100 # if we do changes in reference copy then te changes also reflects on the main list 
print(y)
print(x)

#2) shallow copy  :- If i want changes on shallow copy and i also want that no changs in main list then we use the shallow copy method
m = [10,20,30,90]
n = m.copy() # this is called shllow copy

n[0]=100
print(m) # this will not change
print(n) # this will change


#3 Deep copy :-
import copy

k = [99,87,47,67]
p = copy.deepcopy(k) # this means that they both targeting the same list or same location 

p[0]=100

print(k) # the both list changes because they both targetting the same location or same list.
print(p)


"""

#Imp thing :-(for better understanding of shallow copy and deep copy)
"""
import copy

q = [[10,20],[30,40]]

w1 = q.copy()               # shallow copy
w2 = copy.deepcopy(q)       # Deep copy

w1[0][0] = 999 
w2[1][0] = 888

print("original : ",a) # changed by shallow copy
print("shallow : ",w1)
print("Deep : ",w2)    # completely independent of changes in main list
"""


#traversing:- all the things are same as string.
"""
#method 1 :- By targeting the values or elements of list
x = [10,20,30,40,50]

for i in x:
    print(i)


#method:-by indexing
y = [10,20,30,40,50]

for i in range(len(y)):
    print(y[i])
"""

# help(list) :- by the use of this we know all the methods that are perform on list.

x = [10,10,20,30,45,45,2,2,10, 50,60]

# x.append(19) : Add an element at last of List.
# x.clear()    : clear or delete all the elements of list.
# print(x.count(10)) : counts a particular elemnts in a list.
# print(x.index(10)) : returns the index of a particular element of list.
# x.insert(2,25)     : insert 25 at index 2 in a list.
# x.pop()            : pop or delete the last(by default) or any particular index vaue by putting like x.pop(index)
# x.sort             : sort the whole list

