#1
"""
#file handling :- File handling in python ,as the name suggest it deals with files with python.
#that means creating,reading,updating and deleting(CRUD) operations in differnt files.
"""

#2
"""
file = open("python-basic/class13.py")

print(file.read())
"""


#3
"""
open() - this function needs 2 parameters 1: file location  2:operations(r,a,w,x)
r -> for read the file.Give error if file does not exist
a -> for appending in file.Create a file as well.
w -> overwriting in fike.Create if it does not exist.
x -> Create a file.give error if file already exist.
"""

#4
"""
#open("pull.txt","x") _>for creating a file(usually not used)

file = open("push.txt","w")
file.write("This is a sample file that i have created.")
file.close()                #for closing the file

"""

#5
"""
with open("python-basic/class13.py") as fs:       #by th use of this we will automatically exiting the file as our work done.
    print(fs.read())

"""
