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

marks_cpy.extend(99, 100 , 101) #it can extend the list by appending many things at once
marks_cpy.insert(0 , 94)
#to check if a number exist in a llist
print(94 in marks_cpy) #True
print(93 in marks_cpy) #False
#______________length of the list in python_______________________________________
print(len(marks))



marks.remove(97) #it removes the first occurence of x in the list .return ValueError if the item is not in the list


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


