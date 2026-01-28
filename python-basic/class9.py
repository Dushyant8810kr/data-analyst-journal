#for loop questions;-

#Question!:-
"""n= int(input("Enter no. of times"))
for i in range(n):
    print(f"{i} :Hello world")"""


#Question2:-
"""n= int(input("Enter no. :"))
for i in range(1,n+1,1):
    print(i)"""


#Question3:-
"""n= int(input("Enter no. :"))
for i in range(n,0,-1):
    print(i)"""


#Question4:-
"""a=0
n= int(input("Enter no. :"))
for i in range(1,n+1,1):
    a+=i
print(a)"""


#Question5:-
"""a=1
n= int(input("Enter no. :"))
for i in range(1,n+1,1):
    a*=i
print(a)"""


#Question6:-
"""a=0
b=0
n= int(input("Enter no. :"))
for i in range(1,n+1):
    if i%2==0:
        a+=i
        
    else:
        b+=i

print(a)
print(b)"""


#question7:-
"""n= int(input("Enter no. :"))
for i in range(1,n+1):
    if n%i==0:
        print(i)
    else:
        pass"""


#Question8:-
"""fact_sum=0
n= int(input("Enter no. :"))
for i in range(1,n+1):
    if n%i==0:
        print(i)
        fact_sum+=i
    else:
        pass
print(f"your factors sums is :{fact_sum}")"""


#question9:-imp
"""a=int(input("Enter base :"))
b=int(input("Enter power :"))
power = a
for i in range(b-1):
    power = power*a
print(power)"""


#question10:-imp

#method1:-
"""n = int(input("give your number (prime checker) : "))
count = 0
for i in range(1,n+1):
    if n%i==0:
       count = count +1
if count ==1:
    print("your no. is unity")
elif count==2:
    print("your number is prime")
else:
    print("your number is composite")"""


#method2:-
"""n = int(input("give your number (prime checker) : "))
for i in range(2,n):
    if n%i==0:
       print("sorry your number is prime")
       break   # break is connect with "else" not with "if" they make the triangle of (for-> break -> else) if break works then else not work and vice versa.
else:
    print("your number is composite")"""


