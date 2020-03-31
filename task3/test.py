Products = []

Scanned = []

class CheckOutRegister:
    def __init__(self):
        return;

class Product:

    # Brand_Name = ""

    # Product_Description = ""

    # Barcode_Number = ""

    # Price = 0.0



    def __init__(self, Brand, Description, Barcode, Price):

        self.Brand_Name = Brand

        self.Product_Description = Description

        self.Barcode_Number = Barcode

        self.Price = Price

        return

    def CheckBarCode(self, barcode):



        TheProduct = Product("", "", "", 0.0)

        for prod in Products:

            if (barcode.__eq__(prod.Barcode_Number)):

                TheProduct = prod

                break
        return TheProduct

prod1 = Product("Ice-cream", "Vanilla 2L", "1", 3.80);

prod2 = Product("Cheese", "Cheddar - 500 mg", "2", 3.70);

prod3 = Product("Sprite", "250ml", "3", 1.80);

prod4 = Product("Chips", "Aldi Original", "4", 2.50);

prod5 = Product("Shampoo", "Garnier Silk", "5", 6.50);



Products = Products + [prod1];

Products = Products + [prod2];

Products = Products + [prod3];

Products = Products + [prod4];

Products = Products + [prod5];



while (1):

    print("--------------------------------")

    print("Welcome to the grocery supermarket!")

    print("--------------------------------")



    total = 0

    while (1):

        barcode = input("Please enter the barcode of your item: ")
        result = prod1.CheckBarCode(barcode)

        if (result.Price != 0.0):

            print(result.Brand_Name, ", ", result.Product_Description, ": ", result.Price)

            Scanned = Scanned + [result]

            total = 1

        else:

            print("No product as found with the input barcode")



        choice = input("Scan Another product? (Y/N)")

        if (choice.__eq__("Y") or choice.__eq__("y")):

            continue

        else:

            break



    if (total == 1):

        duepayment = 0.0

        paymentneeded = 0.0

        receivedpayment = 0.0

        for p in Scanned:

            duepayment = duepayment + p.Price



        paymentneeded = duepayment



        amount = 0.0

        while (1):

            print("\nDue Payment: $", duepayment, "Enter ammount to pay: ")

            amount = float(input())

            if (amount < 0.0):

                print("We don't accept negative money!")

            else:

                if (amount < duepayment):

                    duepayment = duepayment - amount

                    receivedpayment = receivedpayment + amount

                else:

                    receivedpayment = receivedpayment + amount

                    break;



        print("----------- Final Receipt -----------\n")



        for s in Scanned:

            print(s.Brand_Name + ", " + s.Product_Description + "\t\t$", s.Price)



        print("\nTotal amount due: \t$", paymentneeded)

        print("Total Given: \t\t$", receivedpayment)

        print("Change given: \t\t$", receivedpayment - paymentneeded)



        print("\nThank you for stopping by for shopping!")



    next = input("(N)ext Customer, or (Q)uit?")

    if (next.capitalize().__eq__("N")):

        print("\n\n\n")

        continue

    else:

        break;



print("Done")

