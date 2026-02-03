#Question1:-(print no.s in individual format in reverse order)
"""a = int(input("enter a number : "))

while a>0:
    print(a%10)
    a//=10"""


#Question2:-(sum of the digits of number)
"""a = int(input("enter a number : "))
sum=0
while a>0:
    x=a%10
    print(x)
    sum=sum+x
    a//=10
print("sum of digits are : ",sum)"""


#Question3:-(reverse a number)
"""a = int(input("enter a number : "))
rev=0
while a>0:
    rev = rev*10 + a%10
    a//=10
print("reverse of your number is :",rev)"""


#question4:-(checking palindrome number)
"""a = int(input("enter a number : "))
copy =a 
rev=0
while copy>0:
    rev = rev*10 + copy%10
    copy//=10
if rev==a:
    print("Your entered number is plaindrome")
else:
    print("your entered number is not palindrome")"""


#Question5:-(checking automorphic number)
"""a = int(input("enter a number : "))
copy =a 
count=0

square = a**2

while a>0:
    count = count +1
    a//=10

extract = square%(10**count)

if extract==copy:
    print("Your entered number is automorphic")
else:
    print("your entered number is not automorphic")"""
