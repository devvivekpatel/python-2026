firstList = ['gagan','ram','shyam',40,False,78.4]

for x in firstList:

    # very simple here is x stands for firstList's element tha's why it is printing firstlist's value 6 times
    # print(firstList)
    # so we will not use this one
    print(x)

# firstList.remove[0]
# print(firstList)
# here i will start from the 0 and it will go for the length of firstList
for i in range(len(firstList)):
    print(firstList[i])


# and this is the best way to access list's values
for index,value in enumerate(firstList):
    print(index,value)


# creating new list and for access i will use while loop

nameList = ['naman','gagan','rohit','ram']
print(nameList)

i =0

while i<len(nameList):
    print(nameList[i])
    i+=1

#     Looping Using List Comprehension
# List Comprehension offers the shortest syntax for looping through lists:
print('List Comprehension')
[print(x) for x in nameList]

