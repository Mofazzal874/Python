#Mofazzal Hosen
#KUET
#code source:Apna college : Introduction to Python Programming


#####Basics of Python 
#This codes will give a start in python 
#after learing it, you can learn----

#OOP in python ---if you want to move to placement , CP , programming
#Django framework -- if u want to learn development
#AI , Data science , ML - u can learn related module
#FIle Handling for development



name = input("What is your name ")
print(name)
genius = True

print("Hello " + name)


#-----------------------Type Conversion-------------------------------------------------------------------------------------------
#whatever you input in python or stores in a variable , it will always stored as a string
#so you need type conversion.Otherwise mathematical application among different things will not be possible

old_age = input("Enter your old age: ")
#new_age = old_age + 2  #this will give you error
new_age = int(old_age) + 2
print(new_age)

#you can also write float() , str()  , bool() 


number = 18 
float(number) 
#--------------------------------String-------------------------------------------------------------------------------------------
name = "Tony stark"
print(name.upper()) #name.upper() doesn't change the original string , it returns a copy of changed string
print(name.lower()) 

print(name.find('s')) # s.find() returns the index of the character in a given string 
#if the character doesn't happen in the function , then it returns NULL = -1 

print(name.find('stark')) #this will also print 5.starting position of stark


print(name.replace("Tony stark" , "Iron Man")) #this will change Tony stark with Iron man
#and you can also change a single character  in a string with replace function 
print(name.replace('T' , 'M')) #u can also send data as string like print.(name.replace("T" , "M"))

 

 #Note: replace function doesn't change the original string . It returns the copy of changed string 


 #--------------------------------------in function----------------------------------------------------------------------------------
#in function works like the traditional dictionary . if a word or string happens in another string 
#then the in function will return true otherwise false 

#for example:

print("stark" in name) #it will return True
print("Tony" in name) #it will return True 
print("Mony stark" in name) #it will return False 
print('k' in name) #True
print("p" in "pop") #True
print("t" in 't') #True



#-----------------------------------arithmatic operators in Python----------------------------------------------------------------
print(5+2) #7                               #addition
print(5*2) #10                              #multiplication
print(5/2) #2.5 (not 2)                     #division 
print(5//2) #2(this will print integer)     #int division
print(5 % 2) #1                             #modulo 
print( 5**2) #25                          #power operator


#-------------------------------------Comparison Operators in Python--------------------------------------------------------------
#these operators take expression and returns true or false 
print(3>2) #True

print(3 == 2) #True
print(3 != 3) #False
print(3 != 2) #True


print( 2 > 3 or 2 > 1  )  #True          # or operator
print( 3 > 2 and 2 < 1 )  #False         #and operator
print( not 2 > 3)  #True                  #not operator



#------------------------------------Conditional statements(if else)------------------------------------------------------------
age = 19 
if age >= 18:                     #here ":" (colon) is used to show the compiler that we are
    print("You are an adult")      #going to use a block of sentence or statement under this condition
    print("You can vote")
elif age < 18 and age > 3:
    print("you are in school")
else:
    print("You are a child")
print("Thank you ")




#--------------------------------------range() function in python-------------------------------------------------------------
numbers = range(5) #this numbers variable will store a list of numbers from 0 to 4 like 0 , 1, 2, 3, 4
print(numbers) #output:range(0 , 5)



#------------------------------------------loop in Python----------------------------------------------------------------------
i = 1 
while i <= 5:
    print(i * "*")  #this is actually string concatenation.if u multiply a number x with a string
    i= i+1          #then , the string will be concatenated x times 
                    # OUTPUT:
                    #*
                    #**
                    #***
                    #****
                    #*****
    
x = 0
for x in range(5) :  #range() is a function 
    print(x + 1)  # 1 2 3 4 5

#---------------------------------------------list in Python-------------------------------------------------------------------------
#list is a complex data types , it can store data like array and can be accessed like array

marks = [95 ,98 , 97]   #marks is a list
print(marks[0])

#But one intersting fact in Python is  -- in c++ or other similar programming language you can not have negative
#index number like -1 , -2 ,-3 
#but in python you can also have negative index .lets say you have 5 data in a list . so -1 index means the last data in the list , 
# -2 means before the last data and it goes on like this
#Example:

print(marks[-1]) #97
print(marks[-2]) #98
print(marks[-3]) #95
#print(marks[-4]) #this will give u an error because you don't have a data with index -4

#________list copying__________________________________________________________
#lets just say you have to copy a list from index a to b from another index .....
#so have to write it like this :  list_cpy = lst[a:b+1]
#it will copy from a to b into the new list 

marks_cpy = marks[0:2]

for x in marks_cpy:
    print(x)


#_____taking input in list/appending in list____________________________________
#it will always append data at the last of the list
marks_cpy.append(99)

#But if u want to push data into your desired location in the list , you can use 
#insert(index , data)
marks_cpy.insert(0 , 94)
#to check if a number exist in a llist
print(94 in marks_cpy) #True
print(93 in marks_cpy) #False
#______________length of the list in python_______________________________________
print(len(marks))


#__________to clear a list___________________________________________________________
marks.clear()   #output:[]










#-------------------------------------------Break and Continue-------------------------------------------------------------
students = ["abu" , "babu" , "gabu" , "dabu" , "labu"  , "kabu"] 

for student in students:
    if student == "babu":
        continue
    if student == "labu":
        break
    print(student)
    



#--------------------------------------------Tuple--------------------------------------------------------------------------

#tuple is just like list but  immutable means if you make a tuple u can't change it.Like u can't
#addition , assignment , delete , modify , replace in a tuple 


marks = (95 , 98 ,97)    #marks is a tuple . You can write the tuple with first parenthesis
#marks[0] = 99            #you can't do a operation  like this.This will give u error


#if you define a set of data without any parenthesis , it will be tuple by default
#Like this--

mark = 95 , 98 , 97         #This is a tuple by default

stu = "abu" , "babu" , "gabu"   #is also a tuple


#_______________Tuple operation_________________________________________________________


#01.Count 
#tuple can count how many times a number happens in a tuple
#For example :

cnt = (95 , 98 , 97 , 95 , 97 , 97)
print(cnt.count(97))             #3


#02.Index finding 
#tuple.index(num) returns the index of the that number in the tuple

print(cnt.index(97))    #2








#--------------------------------------SET---------------------------------------------------------------------------------------
#set only stores the unique element happens in a list 
#you have to use curly braces to make a set 
#set is unordered
#you can't access set with indexing like Set[0] .This will give u error 
#You can only iterate through the set and it will print the output in any order


#so [] = list
#   {} = set
#   () = tuple


Set = {95 , 96 , 96 , 97 , 97 , 97} 
#print(Set[0])   #this will give u error

for stu in Set:
    print(stu)      #97 96 95






#------------------------------------Dictionary------------------------------------------------
#Its like the map structure in c++.
#It has a key and value in it 

#syntax:   dictionary = {"key" : value}

#accessing: print(marks["key"])
#inserting: dictkonary["key"] = value
#changing existing value:    dictkonary["key"] = value



diction = {"abu": 95 , "babu" : 96 , "gabu": 97 , "dabu":98}
print(diction["abu"])       #95

print(diction) #     'abu': 95 , 'babu' : 96 , 'gabu': 97 , 'dabu':98






#--------------------------------------Functions----------------------------------------
#1.In-Bulit functions           int() , bool() , str()
#2. Module Functions            
#3.User_defined Functions


#________________Module Functions__________________________________________

#when related functions and related variables are stored in a same file ,then its 
#called a module.There are many module in python 
#for example to do math related work , you can import math module and use its functions



import math
print(dir(math)) #This will print all the functions in the math module 

#you don't have to import the whole math module 
#you can also import the desired function from a module
#for exaomple you want to use the sqrt function in your python program 
#you can simply write it like this______

from math import sqrt
print(sqrt(4))  #2.8
print(sqrt(16)) #4.0


#you can also import all function from a module 
#you can import by using a "*" notation

from math import *

#now you can use all the function 




#_________________________User_defined Functions___________________________________


#syntax :
#    def function_name(parameters):
#         //do something

def print_sum(first , second):
    print(first+second)


#function calling:

print_sum(1,2)  #3


#by default passing :
#you can also a set a parameter with a particular value by assigning a number in it like__

def print_su(first , second = 4) :  #u just assign second parameter with 4 
    print(first+second)

#now you can pass only one value to the function while calling it , it won't create any problem..
print_su(1)    #5
