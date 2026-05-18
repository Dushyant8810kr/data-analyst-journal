# Modules :- A file containinng pyhton code (functions,variables,classes etc) .It allows code reuse and organization.
# package :- is a directory of modules with an __init__.py,Enabling hierarcy.

# preexisting modules/library or inbuilds modules :- 
# import math
# import random   etc.


#CREATING AND USING OF MODULES :-
#1
"""
import math_utils
print(math_utils.add(10,20)) #30
"""

#2 use when you anly need specific functions
"""
from math_utils import add
print(add(20,30)) #50
"""

#3 use only when you need all the functions of a specific file 
"""
from math_utils import*
print(add(20,30))
"""


#PACKAGES :-
#1
from my_packages import math,string

#2
from my_packages.math import add
