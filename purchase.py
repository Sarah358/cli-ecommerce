

# purchase menu

def display_purchase_menu():

    # creating options  
    while True:
        print("""

        Purchases Menu

        1. Make a purchase

        2. List all purchases

        3. Search for a purchase

        4. Quit

        """)  
        choice4 = int(input("Select Purchase option:"))  

        # choice 1
        if choice4 == 1:
            print()
            make_purchase()
        elif choice4 == 2:
            print()
            list_purchases()
        elif choice4 == 3:
            print()
            search_purchase()
        elif choice4 == 4:
            print()
            break
        else:
            print()
            print('Oops! Incorrect choice. Please try again! ')


# required functions

# function to make purchase 
def make_purchase():
    pass


# function to list all purchases
def list_purchases():
    pass



# function to search for a purchase with customer id or product id
def search_purchase():
    pass
