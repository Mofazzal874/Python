# Random Module
#what is a module ?its like the library in c/c++ to make a program shorter



# this is a concept we are familiar with ,
# when we want to create a computer program , that has a certain degree of 
# of unpredictibility , like  puzzle game that has falling patterns of rock and 
# you have to make them similar so they could go vanish 
#this is an example of ramdomization , because u don't know whats gonna fall
#creating ramdonness is easy in our daily to daily life 
# but machines only operates in deterministic way or predictable way .
# so how can we create ramdonness??how do we wrangle this machines ??

# python uses "mersenne twister pseudorandom generator".U can see this in wikipedia 
# and also a video  on khan academy on title"Pseudorandom Number generators" to fully 
# understand the mechanism

#"AskPython" is a website where you can search your desired topics
#https://www.askpython.com/python-modules/python-random-module-generate-random-numbers-sequences

#example

import random #you can also include /import your own created module/library


random_integer = random.random()  #this will return a random floating point number  between 0 to 1 (exclusive both 0 and 1)
print(random_integer)

#how to create a random decimal number between 0 to 5 ???
#you can simply do it by multiplying the floating point number from random() function 
# for example 0.2*5 is equal 1 
# so you can get 0.00000..... t0 4.99999999... ranged random decimal number by multiplying the the number by 5(random_integer*5)

print(random_integer*5)
random_integer = random.randint(1, 10)  #this will return a random integer between a and b (both inclusive)
print(random_integer)

#you can also make lottery projects or head or tails with this random number generator 
#Remember to use the random module
#Hint: Remember to import the random module here at the top of the file. 🎲
	 
#Write the rest of your code below this line 👇
import random

HOrT = random.randint(0,1)
if(HOrT == 1 ):
    print("Heads")
else:
    print("Tails")

