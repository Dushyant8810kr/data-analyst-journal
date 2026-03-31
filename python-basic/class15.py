#1 :- sum and average of list
"""
a = [10,20,30,40,50]

sum = 0                     # let the sum is 0
for i in range(len(a)):
    sum = sum + a[i]

print(f"sum of your list is {sum}")
print(f"avg. of your list is {sum/len(a)}")

"""


#2:- maximum element with index
"""
a = [1,45,39,56,9,37,22]

max = 0          #let the maximum number be 0 coz for comparison
index = 0        #let the index be 0 to return the index of max number

for i in range(len(a)):
    if a[i]>max:          # at this position the comparision is happening
        max = a[i]
        index = i

print(f"Your maximum number in list is {max} at index {index}")

"""


#3 print the first & second greatest number from list
"""
a = [1,45,39,56,9,37,33,90,91,22]

max1 = 0
max2 = 0
index1 = 0
index2 = 0

for i in range(len(a)):
    if a[i]>max1: 
        max2 = max1
        max1 = a[i]
        index2 = index1
        index1 = i
    elif a[i]> max2:
        max2 = a[i]
        index2 = i
print(f"Your first largest number in your is {max1} at index {index1}")
print(f"Your second largest number in your is {max2} at index {index2}")

"""

#4 :- check your list is sorted or not
"""
a = [12,13,17,18,37,53,58,55,72,85,90]

for i in range(len(a)-1):
    if a[i]<a[i+1]:
        continue
    else:
        print("Your list is not sorted")
        break
else:
    print("Your list is sorted")

"""


#swaping concept :-
"""
a = 12
b = 56

a,b = b,a
then the value of b is 12 and value of b is 56
"""



#5:- left rotation by 1 of list elements
"""
a=[10,20,30,40,50]

for i in range(len(a)-1):
    a[i],a[i+1] = a[i+1],a[i]  # this iis the swaping condition
print(a)

"""


#6:- Right rotation by 1 of list elements
"""
a = [10,20,30,40,50]
for i in range(len(a),0,-1):
    a[i],a[i-1] = a[i-1],a[i]
print(a)

"""

#7 :-left rotation by 1 of list elements
"""
k = int(input("How many time you want to rotate : "))
a=[10,20,30,40,50]

for i in range(k):
    for i in range(len(a)-1):
        a[i],a[i+1] = a[i+1],a[i]  # this iis the swaping condition
print(a)

"""

#8 :- reverse the list (Basic method)
"""
a = [10,20,30,40,50]
b=[]

for i in range(len(a)-1,-1,-1):
    b.append(a[i])
print(b)

"""


#9 :- reverse the list (2nd method)

"""

a = [10,20,30,40,50]
b= len(a)-1

for i in range(len(a)//2):
    a[i],a[b] = a[b],a[i]
    b = b-1
print(a)

"""

#10 :- linear search on list
"""
a = [1,20,8,31,99,57,45,33,9,99,201.101]
search = 102

for i in range(len(a)):
    if a[i] == search:
        print(f"Found element at index {i}")
        break
else:
    print("your element is not exist in list")
    
"""

#11 :- Binary search on list for search an element(array should be sorted before)
"""
a = [1,3,8,14,16,21,29,35,41,44,47,53,59,66,71,75,88]

search = 0

start = 0 
last = len(a)-1
mid = (start + last)//2

while start <= last:
    if a[mid] == search:
        print(f"Your search element found at index {mid}")
        break
    elif a[mid]<search:
        start = mid +1
        mid = (start + last)//2
    elif a[mid]>search:
        last = mid -1
        mid = (start + last)//2
else:
    print("Your search element is not exist")
    
"""

#12 :- bubble sort 
"""
a = [1,20,8,31,99,57,45,33,9,99,201,101]

for j in  range(len(a)-1):
    for i in range(len(a)-1-j):
        if a[i]>a[i+1]:
            a[i],a[i+1] = a[i+1],a[i]
print(a)

"""

#12 :- insertion sorting(pick smallest element and put this in its correct position)

"""
a = [1,20,8,31,99,57,45,33,9,99,201,101,22,31,53,69,112,228]

for i in range(len(a)-1):
    j = i + 1
    min = i 
    for k in range(j,len(a)-1):
        if a[k] < a [min]:
            min = k
    a[i],a[min] = a[min],a[i]

print(a)

"""


