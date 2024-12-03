#map->each object from a collection and forms a new collection.

a=[2,4,6,8,10,12,14,30,40]
b=[14,11,9,7,5,4,20,30]
print(list(map(max,a,b)))
print(list(map(min,a,b)))

'''a,b=input("enter the names:").split(",")
print(a+b)'''

'''a,b=int(input("enter the values").split(','))
print(a+b)'''

'''a,b=map(int,input("enter the values").split(','))
print(a+b)'''


'''Difference between library,modules and package

#Module

A module in python is a single python file that contains python code
It typically consists of functions,classes and variables that can be used in other python scripts or programs.
Examples of modules include math.py,random.py or mymodule.py

#package

A package in python is a directory containing one or more python modules and an __init__.py
The __init__.py file can be empty or contain intialisation code for the package.
Examples of packages include numpy,pandas or Django

#Library

Libraries can consist of multiple modules and packages,organised to serve a particular purpose or domain
Libraries can be standard libraries included with python or third party libraries that need to be installed separately.
Examples of library such as requests,numpy,pandas,matplotlib.
Standard libraries are part of the python distribution and include modules such as os,math and date and time.'''


'''Every python file is a module and import is a keyword.
Every python file is saved internally with variable name as __main__'''




