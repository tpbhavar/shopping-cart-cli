from User import Admin, Customer
class ShoppingCart(Admin, Customer):
    def __init__(self):
        self.stock = {'Men': {'Jeans': '10', 'Shirt': '20', 'T-shirt': '30'}, 'Women': {'Top':'10', 'Jeans':'20', 'Dress':'30'}, 'Kid': {'Jeans':'10', 'Shorts':'20', 'Shirt': '30','T-shirt':'15'}}
        self.basket = {}

    def login(self):
        loop_choice = 'y' or 'n'
        while loop_choice.lower() in ('y', 'yes'):
            self.choice = None
            print("_" * 54)
            print("            WELCOME TO ONLINE RETAIL SHOP")
            print("_" * 54)
            print("Please select the user type (1/2)")
            c_inp = input("\t1.Admin \n \t2.Customer \n")
            if c_inp == "1":
                Admin.login(self)
            elif c_inp == "2":
                Customer.login(self)
            print("Do You Want To Shop Again(y/n)")
            loop_choice = input()

b = ShoppingCart()
b.login()