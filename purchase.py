
import customer,product

PRODUCTS = []
CUSTOMERS = []
# purchases class
class Purchase:
    pass

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
    customer.load_customers()
    product.load_products()
    # enter customer id 
    customer_exists = False
    product_exists = False
    total_purchase = 0
    cus_id = input("Enter customer id to purchase: ")
    # check if the customer id exists
    for cus in customer.CUSTOMERS:
        if cus_id == cus.id:
            customer_exists = True
            cus_name = cus.name
            print("Customer name is:  " , cus_name)
            # print("Customer exists")

    pro_id = input("Enter product id to purchase: ")
    # check if product exists
    for prod in product.PRODUCTS:
        if pro_id ==prod.id:
            product_exists = True
            # print("Product exists")
      

    if customer_exists and product_exists:
        # make purchase
        purchase_amount = int(input("Enter amount of product to purchase: "))
        # check if amount is available
        for i in range(len(product.PRODUCTS)):
            if pro_id == product.PRODUCTS[i].id:
                name = product.PRODUCTS[i].name
                amount = int(product.PRODUCTS[i].amount)
                if amount >= purchase_amount:
                    # update product amount
                    product.PRODUCTS[i].set_amount(product.PRODUCTS[i].amount - purchase_amount)
                    product.PRODUCTS[i].get_amount()

                    balance = product.PRODUCTS[i].amount - purchase_amount
                    product.PRODUCTS[i].set_amount(balance)
                    product.PRODUCTS[i].get_amount()
                    # print("Product available")
                    price = float(product.PRODUCTS[i].price)
                    price_purchased = price * purchase_amount
                    total_purchase = total_purchase + price_purchased
                    output = {"customer id": cus_id, "product name": name,  "amount purchased": purchase_amount,
                           "total spent": total_purchase}
                    print("Purchase successfull!!!")
                    print()
                    print(output)
                    # write to purchases text file
                    fo = open('purchase.txt','a+',newline='')
                    fo.write(str(output) + "\n")
                    fo.close()

                else:
                    print("Product not available")
  
    else:
        print("Invalid details!!!")
        
            

    # if product_exists and customer_exists:
    #     purchase_amount = input("Enter amount to purchase:  ")


# function to list all purchases
def list_purchases():
    purchases = []
    purchases_list = []
    with open('purchase.txt','r') as reader:
        for line in reader.readlines():
            purchases.append(line)
     # remove \n
    for pur in purchases:
        lists = pur.replace('\n','')
        purchases_list.append(lists)
    print(purchases_list)
    
# function to search for a purchase with customer id or product id
def search_purchase():
    # menu for search options
    while True:
        print("""
        
        Search options:

        1. Search by customer id
        2. Search by product name
        3. Exit

        """)
        choice5 = int(input("Select search option:")) 
        if choice5 ==1:
            fo = open('purchase.txt','r')
            id = input("Please enter customer id to search: ")
            s = ''
            while(s):
                s = fo.readline()
                L = s.split(' ')
                print (L)
                # if len(s)>0:
                #     if int(L[1]) == id:
                        # print(L[1])
    
        elif choice5 ==2:
            pass 
        elif choice5 == 3:
            print()
            break
        else:
            print()
            print('Oops! Incorrect choice. Please try again! ')



