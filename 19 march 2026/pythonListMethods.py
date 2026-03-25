# Append 
# To add an item to the end of the list, use the append() method:

myList = ['ram','shyam',100,'naman',False]
print(myList)

myList.append('roshan') 
print(myList)

# Insert
# to add an item with the specific index you can use insert method

myList.insert(0,'shudhanshu')
print(myList)
print(len(myList))

# Extend
# below way is adding ranveer single single character

newList = list(('ranveer'))
newList = list(('Raj','sivek'))
newList.append(300)
newList.append("Aarti")
print(newList)
print(len(newList))

myList.extend(newList)

print("This is new main list :",myList)
print('Now, The length of new myList is : ',len(myList))

# The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.).
# extending is not only use for extend a list it can also be use for tuples, sets etc.

thisTuple = ('joshi','vinay')

myList.extend(thisTuple)
print(myList)
print("Now the length of the MYlIST IS : ",len(myList))

