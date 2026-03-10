
for i in range(10,6,-1):
    print(i)

numbers = [10,30,40,50,20,3,4,5]
largest = numbers[0]

for i in numbers:
    if largest<i:
        largest=i
print("largest is : ",largest)


# count vowels in the name

name = 'vivek patel'

count = 0

for i in name:

    if  i in 'aeiou':
        count+=1
print("Total numbers of vowel is : ",count)