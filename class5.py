#comparison operator :- the name suggest that we do comparisons using comparison operators and the result are in the form of boolean(true 1 or false 0)
# == , != , > , < , <= , >=
a=12
b=45

#print(b>a) True
#print(a==b) False
#print(a!=b) True
#print(12>=12) True (only if one condtion is ture the return True otherwise False)

#Extra things:-

#1
print((12==12)==True) #True

#2
print((12==12)!=True) #False


#Logical opertor:- generally used with comparison operator ( and , or ,not )

#And operator :-all conditions are ture then the final answer is True otherwise False
print(12 == 12 and 56>100  and 100>13)#False

#or operator:-or operator is just opposite of and operator in this opertaor if only one condition is true they print true if all flase then they print False
print(12==98 or 98==17 or 15 ==95)#False
print(12==98 or 98==17 or 95 ==95)#True

#not operator :- this opertor reverses the condition answer
print(not 12 == 12)#False
print(not 12 == 12 == False)#True



