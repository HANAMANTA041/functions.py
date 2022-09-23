"""#continue:skipping the current iteration and continue with next iteration
list_number = list(range(0,21))
list_odd = []
for number in list_number:
    if number%2 ==0:
        continue
    list_odd.append(number) == 1
    print(list_odd)

#for i in number:
 #   pass #we can't use pass in loop ,int object is note iterable
def add_fun():#not give any error for future use
    pass
class Student:
    pass
for i in range(5):#for else,while else
    if i%2 == 0:
        print(i)
    else:
         break
else:
    print("Break is not executed")
    
for i in range(5):#for else,while else
    if i%2 == 0:
        print(i)
    
else:
    print("Break is not executed")

#assert statement:checking some condition if it true no error otherwise error,used in software conditi
#city = "Bengaluru"
#assert city == "Mumbai","city should be 'Mumbai'" 
city = "Mumbai"
assert city == "Mumbai","city should be 'Mumbai'" #used in unit testing
#function,class,module:avoids repeated code,we call when we require
def add_fun(a,b):
    return a+b
addition = add_fun(30,40)#positional arguments 30,40 goto a,b
print(addition)
#keyword argument has key and value
addition = add_fun(a = 50, b = 40,c = 20)
print(addition)
def add_fun(a,b,c):
    return a+b+c
addition = add_fun(30,40,20)#positional arguments 30,40 goto a,b
print(addition)
#keyword argument has key and value
addition = add_fun(a = 50, b = 40, c =20 )
print(addition)

def wish():
    print("Hello Good Morning")

wish()
wish()

def wish(name):
    print(f"Hello {name} Good Morning")

wish("Hbs")
wish("Odkar")

def wish(name):
    print(f"Hello {name} Good Morning")

wish("Hbs")
wish("Odkar")
return_value = wish("Anita")
print(f"Return value is {return_value}")#default return value is "None"

#In Python, a function can return any number of values.
def add_sub(a,b):
    add = a+b
    sub = a-b
    return add,sub

add,sub = add_sub(67,50)

print(f"The addition of two numbers is {add}")

print(f"The subtraction of two numbers is {sub}")

#Types of arguements:
#def add_fun(a,b):
#    --------
#    --------
#    add_fun(10,20)
#a,b are formal arguments where as 10,20 are actual arguments.
#variable legth arguements:def add_fun(*arg):

def sum_fun(*arg):
    total=0
    for number in arg:
        total=total+number
    print("The Sum=",total)

sum_fun()
sum_fun(10)
sum_fun(10,20)
sum_fun(10,20,30,40)

#We can mix variable length arguments with positional arguments.


def sum_fun(name,*arg):
    print(name)
    total=0
    for number in arg:
        total=total+number
    print("The Sum=",total)

sum_fun("Z")
sum_fun("A",10)
sum_fun("B",10,20)
sum_fun("C",10,20,30,40)


#We can declare key word variable length arguments also, for this we have to use **.

#Syntax:def sum_fun(**kwargs):pass
#We can call this function by passing any number of keyword arguments
#internally these keyword arguments will be stored inside a dictionar
def number_display(**kwargs):
    for k,v in kwargs.items():
        print(k, "=",v)

number_display(n1=10,n2=20,n3=30)
number_display(roll_no=100,name="Hbs",marks=70,subject="Java")

#Scope of variables:1.Global Variable 2.Local Variable
#Local variable defined in any function, has scope in that function only. We 
#can’t access that variable outside the function.
#Global variables are defined out of all the functions, accessible in whole program
#It is recommended to not to use global variable, because there can be 
#accidental change in global variable by any function and it is hard to debug.
1.Global Variable
a=10 #global variable
def print_number():
    print(a)

def display_number():
    print(a)

print_number()
display_number()

#2.Local Variable

def print_number():
    a = 100
    print(a)

#def display_number():
#   print(a)#invalid,you can't access local variable of other function

print_number()
#display_number() NameError:'a' is not defined

#Global keyword:avoids limitation of the local variables
a = 111
def print_number():
    global a
    a = 100 #i have changed value of global variable
    print(a)

def display_number():
    print(a)

print_number()
display_number()



#Write lambda function to sum two numbers
sum_number = lambda a,b:a+b

print(sum_number(10,20))

#Write a lambda function to preform square of number
square_number = lambda a:a*a

print(square_number(20))

#Program to filter only even number from the list
#without filter function
def isEven(x):
    if x%2==0:
        return True
    else:
        return False
l = [0, 5, 10, 15, 20, 25, 30]
l1 = list(filter(isEven,l))
print(l1)#[0, 10, 20, 30]

#With lambda function
l = [0, 5, 10, 15, 20, 25, 30]
l1 = list(filter(lambda x:x%2==0,l))
print(l1)#[0, 10, 20, 30]
l2 = list(filter(lambda x:x%2!=0,l))
print(l2)#[5, 15, 25]

#map() function:
#Ex:Double the elements in list
#without lambda function
l = [1, 2, 3, 4, 5]
def double_it(x):
    return 2*x
l1 = list(map(double_it,l))
print(l1)

#with lambda function
l = [1, 2, 3, 4, 5]
l1 = list(map(lambda x:2*x,l))
print(l1)

#Ex:Multiply elements in two lists
l1 = [1, 2, 3, 4]#All list should have same length
l2 = [2, 3, 4, 5]
l3 = list(map(lambda x,y:x*y,l1,l2))
print(l3)

#reduce() function:present in functool
#reduce() function reduces sequence of elements into a single element by applying the specified function.
#Ex:Sum of all elements in the list
from functool import *
l = [10, 20, 30, 40, 50]
result = reduce(lambda x,y:x+y,l)
print(result) #150

#Ex:functions are also objects
def fun_print():
    print("Hello")
print(fun_print)
print(id(fun_print))
print(type(fun_print))

#Ex:Use of docstring
def print_function():
    """"""Demonstrates triple double quotes
    docstrings and does nothing really""""""

    print("This is a simple print function")

print("Using __doc__:")
print(print_function. __doc__)

print("Using help:")
help(print_function)
"""
#Modules and Standard Modules:
#Ex:Module custommath.py
x = 888
def add(a, b):
    print("The Sum:",a+b)

def product(a, b):
    print("The Product:",a*b)

add(12, 5)
product(12, 5)

import custommath
print("Variable from custommath: ",custommath.x)
print("Addition using custommath function: ",custommath.add(12, 5))
print("Product using custommath function: ",custommath.product(12, 5))





    
    







