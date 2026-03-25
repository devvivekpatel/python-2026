thisList = ['gagan',3,'ram',55,True,'hii',5.65]

print(thisList)


# accessing python list items
print(thisList[0])
print(thisList[1:4])
print(thisList[-1])
print('using single index',thisList[1:])
print('using single index',thisList[:4])
# it will not go for -1 to -5 but it will allow -5 to -1
print(thisList[-5:-1])
print('The length of thisList is : ',len(thisList))
print('type of this  is : ',type(thisList))

# it will not work cause it will not go like this
# print(thisList[-1:-5])
# print(thisList[5:1])

if 'gagan' in thisList:
    print('gagan is present')

