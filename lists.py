#list = used to store mulitple items in a single variable

food = ["pizza","hamburgers","hotdog","noodles"]
#change pizza to sushi
food[0] = "sushi"
#add 'ice cream' to the list

food.append("ice cream")
#remove 'hotdog'

food.remove("hotdog")

#remove the last element in the list
#food.pop()
 #insert a value
food.insert(0,"cake")

#sort list
#food.sort()


#print(food[0])

for x in food:
     print(x)