print('In this file we are going to learn how we can remove values')

# remove method

removeList = [50,55,50,'deepak','som',True,900]
print(removeList)
print('The length of the removeList is : ',len(removeList))

removeList.remove(50)
print(removeList)
print("Now the length of removeList is : ",len(removeList))

# remove method removes first value of the list for example if there are 2 'gagan' it will remove the first one 

# pop method
# in pop method you can specify index and if you will not specify the index then it will remove the  value of last index

removeList.pop()
print(removeList)


removeList.pop(1)
print(removeList)



# using del keyword it can clr the whole list and also able to remove the specified index

del removeList[3]
print(removeList)

del removeList
# now removeList is empty that's why it is not defined
# print(removeList)


# clear() method
# clear method can clear the whole list without deleting it will just clr the whole list and it will also remember the list
# del completely delete the list while clear just clr the list

newList = [1,2,3,5]
print(newList)
print("And the type of this list is : ",type(newList))

newList.clear()
print(newList)
