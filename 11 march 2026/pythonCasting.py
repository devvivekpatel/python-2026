# Casting in Python means converting one data type into another data type.

# In simple words:
# ➡️ Changing the type of a variable.

age = input("Enter your age")

# and here is the reason why should we use casting input always gives value as a string 
# So i want to perform some mathematical operations on it 

# num = age+ 5 it will give you error
# remember these things

num = 5 + int(age)

print(num)

# now we will cast some variables 

num1 = ('555.33')
print(num1)

num2 = float(num1)

print(num2)
