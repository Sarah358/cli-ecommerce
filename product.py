import os
PRODUCTS = []
# product class
class Product:
    def __init__(self,id,name,amount,price) -> None:
        self.id = id
        self.name = name
        self.amount = amount
        self.price =price


    def set_amount(self,amount):
        self.amount = amount
    
    def get_amount(self):
        return self.amount
        
# product menu

def display_product_menu():

    
    # creating options  
    while True:
        print("""

        Product menu

        1. List all Products

        2. Add Product

        3. Edit Product

        4. Delete Product

        5. Search for a product

        6. Quit

        """)  
        choice2 = int(input("Select Product option:"))  

        # choice 1
        if choice2 == 1:
            print()
            list_products()
        elif choice2 == 2:
            print()
            add_product()

        elif choice2 == 3:
            print()
            edit_product()
            
        elif choice2 == 4:
            print()
            delete_product()
        elif choice2 == 5:
            print()
            search_product()
        elif choice2 == 6:
            print()
            break
        else:
            print()
            print('Oops! Incorrect choice. Please try again! ')



# required functions
# func to list all customers
def list_products():
    products = []
    products_list = []
    with open('product.txt','r') as reader:
        for line in reader.readlines():
            products.append(line)
     # remove \n
    for cust in products:
        lists = cust.replace('\n','')
        products_list.append(lists)
    print(products_list)
    

# function to add a product
# fields(product_id(unique),product_name,amount,price)
def add_product():
    #open the file in append mode (add to file, we don't wish to overwrite
    fo = open('product.txt','a+',newline='')
    product_id = input("Enter Product id : ")
    # check for unique id
    with open("product.txt",'r') as fo_r:
        for line in fo_r.readlines():
            if product_id in line:
                print()
                print("Product id already exists!!Please enter a unique id!!")
                print()
                return add_product()
    product_name = input("Enter Product name:  ")
    amount = int(input("Enter product amount:   "))
    price = float(input("Enter the product price:   "))
    fo.write(product_id + '~ ' +  product_name  +  '~ '  +  str(amount) + '~' +  str(price) + "\n")
    fo.close()
    if(fo):
        print("Product added successfully!!!")
    print()
    output = {"id": product_id, "name": product_name, "amount": amount, "price ": price}
    return output
   

# function to edit customer with customer id
def edit_product():
    file = open('product.txt','r')
    temp = open('temp.txt','w')
    id = int(input("Enter Product id to change: "))
    s = ' '
    while(s):
        s = file.readline()
        L = s.split('~')
        if len(s)>0:
            if int(L[0]) == id:
                name = input("Enter Product name: ")
                amount = input("Enter product amount : ")
                price = input("Enter the product price : ")
                temp.write(str(id) + '~' +  name  +  '~'  +  amount + '~' + price + "\n")
            else:
                temp.write(s)
    temp.close()
    file.close()
    os.remove('product.txt')
    os.rename('temp.txt','product.txt')
    print("Product updated successfuly!!")
    list_products()


# function to delete a customer with customer id
def delete_product():
    product = open("product.txt",'r')
    temp = open("temp.txt",'w')
    id = int(input("Enter product id to delete:  "))
    s = ' '
    while(s):
        s = product.readline()
        L = s.split('~')
        if len(s)>0:
            if int(L[0]) != id:
                temp.write(s)

    product.close()
    temp.close()
    os.remove('product.txt')
    os.rename('temp.txt','product.txt')
    print(" Product deleted successfuly!! ")
    list_products()

# function to search for customer with id and name
def search_product():
    product = open('product.txt','r')
    id = int(input("Enter product id to search:  "))
    print()
    s = ' '
    while(s):
        s = product.readline()
        L = s.split("~")
        if len(s)>0:
            if int(L[0]) == id:
                print("Product details")
                print("------------------------------")
                print("Product id: ",L[0])
                print("Product Name: ",L[1])
                print("Product amount: ",L[2])
                print("Product price: ",L[3])



# load products
def load_products():
    product = open("product.txt","r")
    for p in product:
        prod = p.split('~')
        id = prod[0]
        name = prod[1]
        amount = prod[2]
        price = prod[3]
        output = Product(id,name,amount,price)
        PRODUCTS.append(output)

if __name__ == "__main__":
    display_product_menu()