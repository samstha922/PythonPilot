import os
print("*************Welcome to Parchment Box - Book Shop**************\n\n")
choice= int(input("Press '1' to calculate Annual Projection of Expenses of Running Parchment Box \nPress '2' to Evaluate the book\nPress '3' to exit\n:"))

# ----------task1: annual projection of expenses-----------------
if (choice == 1):
    # expense on all staff wages
    print("*************** Calculating Annual Expense on staff wages*******************\n\n")
    wksPerYear=52

    aHr=float(input('Enter the working hours per week for Augusta:'))
    aCph=float(input('\nEnter work cost per hour for Augusta:'))

    bHr=float(input('\nEnter the working hours per week for Brutus:'))
    bCph=float(input('\nEnter work cost per hour for Brutus:'))

    cHr=float(input('\nEnter the working hours per week for Caitlin:'))
    cCph=float(input('\nEnter work cost per hour for Caitlin:'))

    oWk= float(input('\nSince temporary staff is also hired in replacement of Caitlin, enter the number of weeks the Temporary Staff works in a year:'))
    oCph= float(input('\nEnter work cost per hour for Temporary Staff:'))

    aWageYr= aHr*aCph*wksPerYear
    bWageYr= bHr*bCph*wksPerYear
    cWageYr=cHr*cCph*wksPerYear
    oWageYr=oCph*oWk*cHr

    expenseStaff= aWageYr+bWageYr+cWageYr+oWageYr

    # expense on other utilities
    print("\n\n*************** Calcualting Annual Expense on other utilities*******************\n\n")
    rent= float(input('Enter the annual expense on rent and insurance:'))
    utility=float(input('\nEnter the expenses on other utilities per month:'))
    utilityYear= utility*12

    expenseOther=rent + utilityYear

    #calculating total expense
    expenseTotal= expenseStaff + expenseOther

    #displaying the projected annual expense
    os.system('cls')
    #print ("\n" * 50)
    #unused_variable = os.system("cls") # on windows
    print("The Projected annual expenses on staff wages is: ${}".format(expenseStaff))
    print("\n\nThe Projected annual expenses on other utilities is: ${}".format(expenseOther))
    print("\n\nHence the total Projected annual expenses is: ${}".format(expenseTotal))





#---------------------task2: evaluation of offer--------------------------
elif(choice == 2):
    print("*************** Evaluating the quality of the book*******************\n\n")
    # while True:
    #     quality=input("How's the quality of book presented by customer(Good/Poor/Terrible)?:").upper()
    #     if(quality[:1] != 'G' or 'P' or 'T'):
    #         print('Error: Wrong input given. Type again!!!')
    #         continue
    #     else:
    #         break
    quality = input("How's the quality of book presented by customer(Good/Poor/Terrible)?:").upper()
    pub = int(input("\nWhat's the publication year?:"))
    cover = input("\nHardcover or Paperback(H/P)?:").upper()

    # clear the screen
    os.system('cls')
    #print('\n' * 50)
    print('**********EVALUATION REPORT****************')
    # check the conditions
    if (quality[:1] == 'T'):
        print("\nREJECT the book")
    elif (quality[:1] == 'P'):
        print("\nOffer LOW PRICE")
    else:
        if (pub < 2003):
            print("\nOffer LOW price")
        else:
            if (cover[:1] == 'P'):
                print("\nOffer MEDIUM PRICE")
            else:
                print("\nOffer HIGH PRICE")

#---------for choice '3'-------------------
elif(choice == 3):
    #print('\n'*50)
    os.system('cls')
    print("THANK YOU AND GOOD BYE!!!")

input()# this is to make python shell not directly exit after displaying output
