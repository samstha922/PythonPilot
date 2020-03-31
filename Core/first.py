print("Hellow world")
print("    /")
print("   /  |")
age=70
name="sam"
# print(name+"\n"+" is "+str(age))
# print(name.index("a"))
# print(name.replace("sam","ram"))
# a = input("Enter the first no.:")
# # a = int(a)
# valid_a=""
# def print_name(valid_a):
#     pass
# if a.isalpha():
#     print("Your name is :"+a)
# else:
#     print("Wrong inputs")

# # lists
# friend =["Kevin",'Sam','Ram']
# friend.insert(1,'Saisha')
# friend.sort()
# print(friend)
#tuples is in brackets; used for data that doesn't need to be changed; it cant be changed; accessed with []
coordinates = (4,5)
print(coordinates[1])

# functions
# def sayHi():
#     print("Hello User")
#
# sayHi()
# # if , else, elif
#
# meat = false
# pasta = false
#
# meat = input("Are you needing meat?? (Y/N)")
# if(meat == 'Y' or meat == 'y'):
#     print('Steak ordered')
# else:
#     pasta=input('Do you want pasta (Y/N)')
#     if(pasta == 'Y' or pasta == 'y'):
#         print('Spaghetti and meatballs ordered')
#
#     else:
#         print('Salad ordered')
#  # key value pair; dictionary {}
# monthConversions = {
#      'Jan' : 'January',
#      'Feb' : 'February',
#      'Mar': 'March'
# }
# print(monthConversions.get('Jani','Not a valid key'))

# while loop
# secret_word= "girrafe"
# guess_limit = 3
# count = 1
# your_word = ""
# while (your_word != secret_word):
#     your_word = input("Enter your guess word:")
#     count+=1
#     if count>guess_limit:
#         print("YOu missed your chances")
#         break
# if(your_word == secret_word):
#     print("Congratulations")

# for loop ----range(3,10)
# Girrafe = ['sam',1,0.01,{'ram'}]
# for letter in Girrafe:
#     print(type(letter))
# # 2d lists
# number_grid =[
#     [1,2,3],
#     [4,5,6],
#     [7,8,9],
#     [0]
# ]
# print(number_grid[0][0])
#
# # nested for loop
# for row in number_grid:
#     for column in row:
#         print(column)

# Build a translator --- 2.52 - 3.00

# # try ...except
# try:
#     number = int(input("Enter a number:"))
#     print(number)
# except ValueError as e:
#     print(e)
# except ZeroDivisionError:
#     print('zero division error')

# File handling ;; w - overrides and creates a new file everytime; 'a' adds on the bottome of the file;
# employee_file = open("employees.txt","w")
# employee_file.write("Toby - HR")
# employee_file.close()

#
# employee_file = open("employees.txt","a")
#
# employee_file.write("\nYoyo")
# employee_file.close()

# modules and pip ;;; using external library
def print_name(name):
    print(name)
feet_in_mile = 1000
beatles =["Rom","Son","Kom"]

from random import randint
def roll_a_dice(number):
    value = randint(0, number)
    print(value)

