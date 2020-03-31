Products=[]
# initializing null to all variables
productId=''
productName=''
description=''
price=0.0

# class product created
class Product():
    # constructor for class product initialized
    def __init__(self, productId, productName, description, price):
        self.productId = productId
        self.productName = productName
        self.description = description
        self.price= price

    def display(self):
        print("ProductName: {0}".format(self.productName))
        print("Description: {0}".format(self.description))
        print("Price: {0}".format(self.price))

products=[]
# objects created to create new instances of class Product
product1 = Product("1","Milk", "Coles Full Cream 2L Milk Packet", 2.0)
product2 = Product("2","Bread", "Multigrain Bread", 1.5)
product3 = Product("3","Red Onions", "2 kg Coles Red Onions", 5.0)
product4 = Product("4","Bacon Strip", "MeatLover's Bacon Strip 500 gm pack", 6.50)
product5 = Product("5","Sausage Roll", "MeatLover's Sausage Roll 500 gm pack", 2.50)

# the instance of class Product placed in an array of objects called products
products = products + [product1]
products = products + [product2]
products = products + [product3]
products = products + [product4]
products = products + [product5]

