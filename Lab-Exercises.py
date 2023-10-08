# This program takes a person's name and a number as input and squares the number.

# Step 1: Get the name input\
while(True):
    name = input("Enter your name: ")
    if name.isdigit() == False:
        break
    

# Step 2: Get the number input
while (True):
    number = input("Enter a number: ")
    if number.isdigit() == True: 
        break
# Step 3: Do Something™ with the number (square it)
number = int(number)
result = number ** 2

# Step 4: Display the result
print(f"Hello, {name}! The square of {number} is {result}")

# Hayden here! This part takes each character in their name and multiplies
# it by the number the user sent! 

newName = ''

for letter in name:
    letter *= number
    newName += letter

print(f"\nYour new silly name is\n{newName}")
