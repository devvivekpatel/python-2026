print('List Comprehension')

firstList = ['abce','banana','kiwi','orange','owl']

print(firstList)

newList = [x for x in firstList if 'a' in x]

# newlist = [expression for item in iterable if condition == True]

print(newList)