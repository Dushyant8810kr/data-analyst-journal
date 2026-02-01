#while loop :-
"""a = 0

while a<10:
    print(a)
    a+=1"""

#task(print from 10 to 0):-
"""a = 10
while a>=0:
    print(a)
    a-=1"""

#break:-use of break is that when we runs the loop and at a specific condtion we want to stops the loop then we use "break"
"""for i in range(1,11):
    print(i)
    if i == 3:# when the loops terminate then 3 is also include and after that of 3 is not run.
        break"""

#continue:-use of continue is that when we runs the loop and at a specific condition we dont need this condition then loops not runs at this specific condition after that they continues to runs.
"""for i in range(1,11):
    if i == 3: #not print the specific condition which is '3' 
        continue
    print(i)"""

#else:- if breaks executed then else not executed and vice versa
for i in range(1,6):
    if i==6:
        break
    print(i)
else:#else is connected with for loop and if breaks executed then else not executed and vice versa.
    print("no break is executed")
 


