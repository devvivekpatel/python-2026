print("hello world")

# Created using constructor
newList = list((1,40,43,'gagan'))
print(newList)

# This is how you can change the value of a list

newList[0] = 100
print(newList)
print(len(newList))

newList[0] = 'naman'
print(newList)


# below is a wrong way to define
# 'vivek' is a string, and Python treats a string like a sequence of characters.

# newList[0:2] = 'vivek'

newList[0:2] = ['vivek']
print(newList)
print(len(newList))


newList.insert(0,'tiger')
print(newList)
