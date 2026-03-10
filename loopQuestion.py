# count the numbers of even and odd

even = 0
odd = 0

for i in range(12):
    if(i%2 == 0):
        even+=1
    else:
        odd+=1
    
 
print("Odd numbers are",odd, 'and the even is : ',even)


# printing a table

num = int(input('Enter a number'))

print("Your number is : ",num)

for i in range(1,11):
    print(num, " X ", i , '=', i*num)

# Sum of all numbers

total = 0

for i in range(6):
 total = total + i
print("the total is : ",total)


# Checking for given number is prime or not 

num = int(input("Enter a number "))
isPrime = True

for i in range(2,num):
   if num % i == 0 :
      isPrime = False

if isPrime:
   print("Given number is prime")
else:
   print("No, Given number is not prime")

# Now it's for the pattern

for i in range(1,5):
   print("*" *i)
   