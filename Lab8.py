# Yanet Rodriguez
# June 4, 2023

# Problem 1-checks if inputs are equal or not
print("")

def checkifequal():
    number1 = int(input("Enter a number between 1 and 10: "))
    number2 = int(input("Enter another number between 1 and 10: "))
    if number1 == number2:
        print("First number is equal to the second number")
    else:
        print("Numbers are not equal")
checkifequal()

print("")
#problem 2-Sums of two inputs

def sum():
    num1 = int(input("Enter a number between 1 and 10: "))
    num2 = int(input("Enter another number between 1 and 10: "))
    if num1 + num2 > 10:
        print("Sum is greater than 10")
    elif num1 + num2 < 10:
        print("Sum is lees then 10")
    else:
        print("Sum is equal to 10")
sum()

#Problem 3-Checks list for value
print("")

def findfive(list):
    if 5 in list:
        print("5 is in the list")
    else:
        print("5 is not on the list")
list = [2, 6, 8, 10, 6]
findfive(list)

#Problem 4- Checks if year is a leap year
print("")

def leapyear(year):
    if year % 4 == 0: #checks if year is divisible by 400
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


print(leapyear(1300))

#Problem 5-Checks if character can perform tasked with items in his lists
print("")
def tasks(items, status):
    if "rope" in items and "coat" in items and "first aid kit" in items and "slow" not in status:
        print ("Game character can perform task 1") #Checks if items are on his lists
    if "pan" in items and "groceries" in items and "small" not in status:
        print ("Game character can perform  task 2")
    if "pen" in items and "paper" in items and "idea" in items and "confusion" not in status:
        print ("Game character can perform  task 3")

items = ["pan", "paper", "idea", "rope", "groceries"]
status = ["slow"]

tasks(items, status)