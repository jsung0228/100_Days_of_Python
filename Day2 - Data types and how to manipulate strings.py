#Data Types
#String

#The bracket subscripts and gets only a part of the string
print("Hello"[0])
print("Hello"[4])

#The plus sign is interpreted as a string concatenation
print("123"+"345")

#Integer
print(123 + 345)
print(123_456_789) #You can add underscore in place of commas

#Float
3141.59


#Boolean - True or False, has to start with T or F
True
False

#Data type conversion - you can only concatenate Strings with Strings
# num_char = len(input("What is your name?"))
print("Your name has " + str(len(input("What is your name?"))) + " characters.")

#Program adding the first and second digit of the inputted integer
a = input("Input an integer")
result = int(a[0]) + int(a[1])
print(result)


#Number manipulation
#Getting the value of the division result
print(8//3)

#Short handled writing for calculation with previous version
score = 0
score +=1
print(score)

#F-String allows us to by typing in front of the double quotes
score = 0
height = 1.8
isWinning = True
print(f"your socre is {score}, your height is {height}, you are winning is {isWinning}")

#Project
age = input("What is your current age?")
days = int(age)//365
weeks = int(age)//52
months = int(age)//12

print(f"You have {days} days, {weeks} weeks, and {months} months old.")
