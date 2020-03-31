print("*************** Evaluating the quality of the book*******************\n\n")
# while True:
#     quality=input("How's the quality of book presented by customer(Good/Poor/Terrible)?:").upper()
#     if(quality[:1] != 'G' or 'P' or 'T'):
#         print('Error: Wrong input given. Type again!!!')
#         continue
#     else:
#         break
quality=input("How's the quality of book presented by customer(Good/Poor/Terrible)?:").upper()
pub=int(input("\nWhat's the publication year?:"))
cover= input("\nHardcover or Paperback(H/P)?:").upper()

# clear the screen
print('\n'*50)
print('**********EVALUATION REPORT****************')
# check the conditions
if(quality[:1]=='T'):
    print("\nReject the book")
elif(quality[:1]=='P'):
    print("\nOffer low price to the customer")
else:
    if(pub<2003):
        print("\nOffer low price")
    else:
        if(cover[:1]=='P'):
            print("\nOffer medium price to the customer")
        else:
            print("\nOffer high price to the customer")