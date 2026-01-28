#loops:- we use loops for doing repetative task.
#for loop :-use when you know only no. of iterations 
#while loop:-use when you know only the conditions not the no. of iterations.

#range(start,stop,steps):- they return the range like from 1 to 10, 0 to 9 , ... with sepcific steps
#ran = range(1,10,1)

#Task1:-(print no.s from 10 to 40)
"""for i in range(10,41,1):
    print(i)"""

#Task2:-(print no.s from -10 to 20)
"""for i in range(-10,21,1):
    print(i)"""

#Task3:-(print no.s from 34 to 5)
"""for i in range(34,4,-1):
    print(i)"""

#Task4:-(print table of 5)
"""for i in range(5,51,5):
    print(i)"""

#Task5:-(print any no. table)
"""n = int(input("tell me the number you want table of : "))
for i in range(n,(n*10)+1,n):
    print(i)"""


#To print a string using for loop:-

#first method:-
"""s = "Dushyant kumar"
for i in s:
    print(i)"""

#second method:-
"""s = "Dushyant kumar"
for i in range(0,len(s),1):
    print(s[i])"""


#Some imp. things:-

#range(11) this signifies that they start from 0 with step=1.
