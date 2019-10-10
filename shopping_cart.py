def shopping_cart():

        cart = []

        while True:
            command = input("What would you like to do? (add item / delete item / view list / quit) ").lower()

            if command[0].lower() == 'q':
                print("Quitting Cart Program")
                break

            elif command[0] == 'a':
                item = input("What item would you like to add? ")
                cart.append(item)
                print("Added Item")
            elif command[0] == 'd':
                item = input("What item would you like to delete? ")
                try:
                    cart.remove(item)
                    print(f"Deleted {item}")
                except:
                    print(f"Item '{item}' not found in cart. Please try again. ")

            elif command[0] == 'v':
                print("Items in Cart: ", end=' ')
                for i in cart:
                    print(i, end=' ')
            else:
                print("Please enter valid command.")

        # print cart when exiting program
        for i in cart:
            print("Items in cart: ", i, end=' ')

shopping_cart()
