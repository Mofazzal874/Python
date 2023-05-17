#---------------------NumberManipulation---------------
# round
print(round(8/3))   #3
# you can also do it by using int division( //)
print(8//3) #this will  print 2


# to round upto a decimal places----
print(round(8/3 , 2)) #rounding upto 2 decimal places
#main answer: 2.6666666666
# 2 decimal places : 2.67


#---------------------F-string--------------------
# lets say you have three variable of three datatypes
# you want to print it in a single line with other strings .This will be a hectic process 
# because you have to convert all of them from their datatypes to string(to concatenates with)
# to make this process easier , f string is necessary . Just put f before writing a string and variables
# in a curly braces and python will make the conversion itself
#example

height = 5          #int
weight = 53.2       #float
isBoy = True        #bool

print(f"Your details is height: {height} , your weight is: {weight} , you are a boy? : {isBoy}")