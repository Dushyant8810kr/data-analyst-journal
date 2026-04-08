#questions on distionary :-Hashing

#1 count the frequency of elements of an array:-
"""
a = [1,1,1,1,2,2,2,3,3,3,4,4,4,5,5,5,5,6,6,6,7,7,7,7,8]

d={}                # creating the dictionary for the purpose of counting the frequency

for i in a:
    if i in d.keys():
        d[i] += 1           #if i exist in dict(d) then increase the value of key i
    else:
        d[i] = 1            # if not exist then make the key i in dict

print(d)
"""


#2 print the unique elements of an array:-
"""
a = [1,1,1,1,2,2,2,3,3,3,4,4,4,5,5,5,5,6,6,6,7,7,7,7,8]

d={}                # creating the dictionary for the purpose of counting the frequency

for i in a:
    if i in d.keys():
        d[i] += 1           #if i exist in dict(d) then increase the value of key i
    else:
        d[i] = 1            # if not exist then make the key i in dict

print(d.keys())   # dict_keys([1, 2, 3, 4, 5, 6, 7, 8])
"""


#3 :- leetcode 771    -> jewels and stones

#4 :- leetcode 1832   -> check if the sentence is panagram or not

#5 :- leetcode 2351   -> first letter to apppear twice

#6 :- leetcode 1748   -> sum of unique elements

#7 :- leetcode 2418   -> sort the people  

#8 :- check if two strings have same frequency map

"""
s1 = "aabbcc"
s2 = "baccab"

if len(s1) == len(s2):
    d={}
    for i in s1:
        if i in d.keys():
            d[i] += 1
        else:
            d[i] = 1
    
    for i in s2:
        if i in d.keys():
            d[i] -= 1
        else:
            print("An extra element was found")
    
    for i in d:
        if d[i] != 0:
            print("sorry your string are not same")
            break
    else:
            print("your string are same")


else:
    print("not same")

"""

#9 :- check if all characters of one string are exist in another string.
"""
s1 = "aabbcc"
s2 = "baccab"

if len(s1) == len(s2):
    d={}
    for i in s1:
        if i in d.keys():
            d[i] += 1
        else:
            d[i] = 1
    
    for i in s2:
        if i in d.keys():
            d[i] -= 1
        else:
            print("An extra element was found")
    
    for i in d:
        if d[i] != 0:
            print("sorry your  all characters of one string are not exist in another string properly.")
            break
    else:
            print("your all characters of one string are exist in another string.")


else:
    print("not same")
"""

#10 :-print the duplicate values of an array
"""
a = [1,1,2,2,2,3,3,4,4,4,4,5,5,5,5,6,6,7,7,7,7,8,0]

d = {}
for i in a:
    if i in d.keys():
        d[i] += 1
    else:
        d[i] = 1
print(d)
for i in d:
    if d[i]>1:
        print(i)"""

#11 :- leetcode 2404  -> most frequent even element

#12 :- leetcode 2283  -> check if number has equal digit count and digit value

#13 :- return all unique elements that appear in both the arrays.
"""
a = [1,2,2,3,5,5,6,6,6,6,7,7,9]
b = [1,22,3,3,4,4,5,5]

j = []
d = {}

for i in a:
    if i in d.keys():
        d[i] += 1
    else:
        d[i] = 1

for i in d.keys():
    if i in b:
        j.append(i)

print(j)
"""
        


