from IPython.display import clear_output

# have a class called cart that retains items and has methods to add, remove, and show

# step #1: create the cart class
class Cart():
    # when instantiated, cart object should define empty list for items
    def __init__(self):
        self.items = []

    # create a method to show cart
    def showCart(self):
        clear_output()
        print("Items in your cart: ")
        for item in cart.items:
            print(item)

    # create a method to add to cart
    def addItem(self, item):
        clear_output()
        self.items.append(item)

    # create a method to remove from cart
    def removeItem(self, item):
        pass

    def clearCart(self):
        clear_output()
        print('Your cart is now empty.')
        self.items.clear()


# create instance of cart object with empty list

cart = Cart()


# start the while loop until user quits

shopping = True

while shopping:
    # ask for input
    ans = input("Would you like to add/remove/show/quit? ").lower()

    # base case
    if ans == 'quit':
        shopping = False
    # ask if they would like to add, remove, show, perform steps using cart methods

    elif ans == 'add':
        item = input("What would you like to add? ")
        cart.addItem(item)
    elif ans == 'remove':
        if len(cart) <= 0:
            print("There are no items in the list")
            continue
        item = input("What would you like to remove? ")
        cart.removeItem(item)
    elif ans == 'show':
        cart.showCart()
    elif ans == 'clear':
        cart.clearCart()

    else:
        print("That is not an option. Try again")
