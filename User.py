import datetime
import time


class User:

    def viewinv(self):
        if len(self.stock) == 0:
            print("Inventory is Empty")
            return
        print("_" * 56)
        print("|", "CATEGORY".center(20), "|", "PRODUCT".center(20), "|", "PPRICE")
        print("-" * 56)
        for key, values in self.stock.items():
            for k, y in values.items():
                print("|", key.center(20), "|", k.center(20), "|", y.center(5), "|")
                key = ''
            print("-" * 56)

    def viewcart(self):
        if len(self.basket) == 0:
            print("Cart is Empty")
            return
        # import pdb;pdb.set_trace()
        print("_" * 43)
        print( "ITEM".center(20), "|", "QUANTITY".center(15))
        print("-" * 43)
        for key, value in self.basket.items():
            print( key.center(20), "|"," "*7, value[1])
        print("-" * 43)
        print()

    def invoice(self):
        print("Generating Invoice")
        total = 0
        for i in range(5):
            print('.')
            time.sleep(1)
        print()
        print("_" * 94)
        print("INVOICE".center(94))
        print("_" * 94)
        print("TIME STAMP:", datetime.datetime.now())
        print("_" * 94)
        print("|", " " * 8, "ITEM", " " * 7, "|", " " * 6, "PRICE", " " * 6, "|", " " * 6, "QUANTITY", " " * 6, "|",
              " " * 6, "TOTAL", " " * 6, "|")
        print("-" * 94)
        for key, value in self.basket.items():
            total+=int(value[0])*value[1]
            print("|",key.center(21),"|",value[0].center(21),"|"," "*8, value[1]," "*8,"|"," "*6, int(value[0])*value[1], " "*6, "|")
        print("-" * 94)
        if total > 10000:
            print("|", " " * 8, "Total Bill", " " * 50,total)
            print("|", " " * 8, "Discount", " " * 53,500)
            print("|", " " * 8, "Discounted Bill", " " * 45,total-500)
        else:
            print("|", " " * 8, "Final Bill", " " * 50, total)

    def signout(self):
        print("Thanks For Shopping With Us")
        return


class Admin(User):
    def __init__(self):
        super(User, self).__init__()

    def login(self):
        while self.choice != 6:
            print("         Welcome Admin ")
            print("\nPress 1 For Viewing Available Products"
                  "\nPress 2 To Add Category\Product"
                  "\nPress 3 To Add Product"
                  "\nPress 4 To View Cart "
                  "\nPress 5 To view last Generated Invoice "
                  "\nPress 6 To Log Out")
            print()
            self.choice = int(input().strip())
            self.selection(self.choice)

    def selection(self, inp):
        controller = {
            1: self.viewinv,
            2: self.addcat,
            3: self.addprod,
            4: self.viewcart,
            5: self.invoice,
            6: self.signout
        }
        controller.get(inp, lambda: 'Invalid')()
        return

    def addcat(self):
        cat = str(input("Enter Category of Product to Add\n"))
        if cat not in self.stock:
            ci = input("Do you want to add Product too (y/n)")
            if ci in('y', 'yes'):
                item = str(input("Enter The Name of Product to Add\n"))
                price = str(input("Enter The Price\n"))
                self.stock[cat] = {item:price}
            elif ci in('n', 'no'):
                self.stock[cat] = {}
        else:
            print("Category Already Present In Inventory")
        print('Do You Want to Add Any Other Category(y/n)')
        c = input()
        if c.lower() == "y":
            self.addcat()
        else:
            return

    def addprod(self):
        cat = str(input("Enter Category of Product to Add\n"))
        if cat in self.stock:
            item = str(input("Enter The Name of Product to Add\n"))
            if item not in self.stock[cat].keys():
                price = str(input("Enter The Price\n"))
                self.stock[cat].update({item:price})
            else:
                print("Product Already Present In This Category")
        else:
            print("Category Not Present In Inventory")
        print('Do You Want to Add Any Other Product(y/n)')
        c = input()
        if c.lower() == "y":
            self.addprod()
        else:
            return


class Customer(User):
    def __init__(self):
        super(User, self).__init__()

    def login(self):
        while self.choice != 6:
            print("          Welcome Customer""\n         Thanks For Selecting Us")
            print("-" * 70)
            print("Press 1 For Viewing Available Products"
                  "\nPress 2 To Add Product To Cart"
                  "\nPress 3 To View Cart"
                  "\nPress 4 To Remove Product From Cart"
                  "\nPress 5 To Print Invoice"
                  "\nPress 6 To Sign Out\n")
            self.choice = int(input("\n").strip(' '))
            self.selection(self.choice)

    def selection(self, inp):
        controller = {
            1: self.viewinv,
            2: self.additem,
            3: self.viewcart,
            4: self.remove,
            5: self.invoice,
            6: self.signout
        }
        controller.get(inp, lambda: 'Invalid')()
        return

    def additem(self):
        print("Do you want to see Inventory? (yes/y) or press any other key to skip \n")
        inv_input = input().strip(' ')
        if inv_input.lower() in ['yes','y']:
            self.viewinv()
        cat = input("Enter Category of Product to Add\n")
        if cat in self.stock:
            item = input("Enter The Name of Product to Add\n")
            if item in self.stock[cat]:
                print("Price Of Product Is ", self.stock[cat][item])
                print("Do You Wish To Add The Product(y/n)")
                c = input()
                if c.lower() == "y":
                    quantity = int(input("Enter The Quantity\n"))
                    if len(self.basket) != 0 and (cat+" "+item in self.basket):
                        self.basket[cat+" "+item][1]+=quantity
                    else:
                        self.basket[cat+" "+item] = [self.stock[cat][item], quantity]
            else:
                print("Product Not Present In This Category")
        else:
            print("Category Not Present In Inventory")
        print('Do You Want to Add Any Other Product(y/n)')
        c = input()
        if c.lower() == "y":
            self.additem()
        else:
            return

    def remove(self):
        item = input("Enter Product Name To Remove\n")
        if item in self.basket:
            del self.basket[item]
            print("Product Removed Successfully")
        print('Do You Want to Remove Any Other Product(y/n)')
        c = input()
        if c.lower() == "y":
            self.remove()
        else:
            return
