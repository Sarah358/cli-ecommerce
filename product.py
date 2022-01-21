

# product menu

from operator import add


def display_product_menu():

    # creating options  
    while True:
        print("""

        Products Menu

        1. List all Products

        2. Add product

        3. Edit product

        4. Delete Product

        5. Search for a Product

        6. Quit

        """)  
        choice3 = int(input("Select Product option:"))  

        # choice 1
        if choice3 == 1:
            print()
            list_products()
        elif choice3 == 2:
            print()
            add_product()
        elif choice3 == 3:
            print()
            edit_product()
        elif choice3 == 4:
            print()
            delete_product()
        elif choice3 == 5:
            print()
            search_product()
        elif choice3 == 6:
            print()
            break
        else:
            print()
            print('Oops! Incorrect choice. Please try again! ')


# required functions
# func to list all products
def list_products():
    pass

# function to add a product
def add_product():
    #open the file in append mode (add to file, we don't wish to overwrite
    with open('product.txt','a',newline="") as fo:
        
        product_id = input("Enter Product id : ")
        product_name = input("Enter Product name:  ")
        amount = input("Enter product amount  :   ")
        product_price = input("Enter the product price:  ")
        fo.write("")
        fo.write(str(product_id)  + ','  +  product_name  +  ', '  +  amount + ', ' + product_price + '\n')
        fo.close()

        if (fo):
            print("Product added succefully!!!")
        print()

# function to edit product with product id
def edit_product():
    pass

# function to delete a product with product id
def delete_product():
    pass

# function to search for product with id and name
def search_product():
    pass