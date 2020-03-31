from Product import *
from CheckOutRegister import *

while True:
    scannedItems = []
    print("------  Welcome to FedUni checkout!  -------")
    totalItems = 0
    while True:
        productId=input('Please enter the barcode/productId of your item:')
        result= CheckOutRegister.checkProductId(productId)

        if (result.price!=0.0):
            print(result.productName+",  "+result.description+" -  $"+str(result.price))
            scannedItems=scannedItems+[result]
            totalItems += 1

        else:
            print("This product doesn't exist in our inventory.")

        next_item= input('Would you like to scan another item? (Y/N):').upper()
        if (next_item[:1]=='Y'):
            continue
        else:
            break

    if(totalItems > 0):
        totalDue = 0.00
        receivedAmount= 0.00
        pendingAmount = 0.00
        excessAmount = 0.00
        for p in scannedItems:
            totalDue += p.price
        pendingAmount = totalDue

        # # ----------------------------------First function from task 4 integrated-----------------------------------------------
        # Function to: get the input from user which then is converted to float datatype along with validation criteria__
        def get_float(prompt):
            # set the value of variable 'value' to float with value 0.0 _
            value = float(0.0)
            # while loop which takes the input from user and checks the validation criteria _
            while True:
                try:
                    # takes the input from user and sets to variable 'value'
                    value = float(input(prompt))

                    # if condition check if value is less than 0.0
                    if value < 0.0:
                        print("We don't accept negative money!")
                        continue
                    # if value is greater than 0.0, break the loop
                    break
                # exceptional case handler for not floating input datatype
                except ValueError:
                    print('Please enter a valid floating point value.')
            # returns the value of variable 'value' into function
            return value
        # # -------------------------------------------------------------------------------


        # #--------------------------------------task 4 part2 function-----------------------

        # Function to: list out the products in the bag
        def bag_products(product_list):

            # initialize the list datatype called ‘bag_list’
            bag_list = []
            non_bagged_items = []
            MAX_BAG_WEIGHT = 5.0

            # for loop which iterates through the product_list
            for product in product_list:

                # if condition where weight of the product is greater than max bag weight
                if product.weight > MAX_BAG_WEIGHT:
                    product_list.remove(product)
                    non_bagged_items.append(product)

            # initializes the list ‘current_bag_contents’
            current_bag_contents = []
            current_bag_weight = 0.0

            # while loop with condition of atleast one item in product_list
            while len(product_list) > 0:

                # first item in product_list is set on variable ‘temp_product’
                temp_product = product_list[0]
                product_list.remove(temp_product)

                # if condition where sum of current bag of weight and temp_product_weight is less than max_bag_weight
                if current_bag_weight + temp_product.weight < MAX_BAG_WEIGHT:

                    # append the item temp_product to object current_bag_contents
                    current_bag_contents.append(temp_product)
                    current_bag_weight += temp_product.weight

                    # if condition where number of products in list is equal to 0 / null
                    if (len(product_list) == 0):
                        bag_list.append(current_bag_contents)

                # else condition which appends through the object bag_list ss
                else:
                    bag_list.append(current_bag_contents)

                    # sets the current_bag_contents variable to null list
                    current_bag_contents = []
                    current_bag_weight = 0.0

            # for loop which iterates through the bag_list
            for index, bag in enumerate(bag_list):
                output = 'Bag ' + str(index + 1) + ' contains: '

                # for loop which iterates through all items in bag
                for product in bag:
                    output += product.name + '\t'
                print(output, '\n')

            # enters into loop if non_bagged_items is greater than 0
            if (len(non_bagged_items) > 0):
                output = 'Non-bagged items: '

                # for loop which iterates through each item of non_bagged_items
                for item in non_bagged_items:
                    output += item + '\t'
                print(output, '\n')


        # -------------------------------------------------------------------------------------
        #
        while True:
            amount= get_float("\nPayment Due: $ {}. Please enter the amount to pay:".format(pendingAmount))

            if (amount < pendingAmount):
                pendingAmount -= amount
                receivedAmount += amount
                continue
            elif (amount > pendingAmount):
                receivedAmount += amount
                excessAmount=amount - pendingAmount
                # print('Amount to be returned to you as change:${}'.format(excessAmount))
                break
            else:
                receivedAmount = totalDue
                excessAmount=0
                break
        print("You have successfully made payment.\n-------------------- Final Receipt ------------------------\n")
        for items in scannedItems:
            print(items.productName, items.description+"\t"+"$"+"{}".format(items.price))
        print("-----------------------------------------------------")
        print("Total Amount Due:{}".format(totalDue))
        print("Total Received Amount:{}".format(receivedAmount))
        print("Change Given:{}".format(excessAmount))
        print("Thank You for shopping at FedUni!")
        nextChoice=input("(N)ext customer, or (Q)uit?").upper()
        if (nextChoice[:1]=='N'):
            print('\n\n\n')
            continue
        else:
            print("Bye Bye. Have a good day!!!")
            break



