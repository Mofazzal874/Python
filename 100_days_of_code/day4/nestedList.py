#------------------nested List--------------
#lets take an example we have two list of fruits and vegetables 
# now we want to contain them in one list .How do 
# we do it???


fruits = ["strawberries" , "Bananas" , "Grapes" , "Peaches" , "cherries" , "Apples"] 
vegetables = ["Spinach" , "Kale" , "Tomatoes" , "Celery" , "Potatoes"] 

dirty_dozon = [fruits , vegetables] #now these two lists can be used as one
print(dirty_dozon)  #this will print them as one 
print(dirty_dozon[0])    #['strawberries', 'Bananas', 'Grapes', 'Peaches', 'cherries', 'Apples']
print(dirty_dozon[1])    #['Spinach', 'Kale', 'Tomatoes', 'Celery', 'Potatoes']
print(dirty_dozon[1][3]) #Celery

