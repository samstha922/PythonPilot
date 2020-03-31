from Product import *
class CheckOutRegister():
    def __init__(self):
        return

    # function to scan the ProductId from the enlisted products (equivalent to scan_items)
    def checkProductId(productId):
        # default object of Product class where attributes instantiated to null
        specificProduct = Product("", "", "", 0.0)
        for prod in products:
            # checking if the productId is equal to user input productId(barcode)
            if (productId.__eq__(prod.productId)):
                # putting the values of array of objects called 'prod' in object specificProduct
                specificProduct = prod
        # returns default values in specificProduct if no productId found
        return specificProduct


