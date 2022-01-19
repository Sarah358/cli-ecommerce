# main file 
import product,customer,purchase

# main function
def main():

    # creating options  
    while True:
        print("""

        MAIN MENU

        1. Customers

        2.  Products

        3. Purchases

        4. Quit

        """)  
        choice1 = int(input("Enter an option:"))  

        # choice 1
        if choice1 == 1:
            print()
            customer.display_customer_menu()
            pass
        elif choice1 == 2:
            print()
            product.display_product_menu()
            pass
        elif choice1 == 3:
            purchase.display_purchase_menu()
            print()
            pass
        elif choice1 == 4:
            print()
            print("Thank you for using this app!!!!")
            print()
            break
        else:
            print()
            print('Oops! Incorrect choice. Please try again! ')






if __name__ == "__main__":
    main()