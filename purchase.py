import os
import customer,product

PRODUCTS = []
CUSTOMERS = []
PURCHASES = []
# purchases class
class Purchase:

    def __init__(self,cus_name,pro_id,purchase_q,price_purchased):
         # Run validations to the received arguments
        assert purchase_q >=0, f"{purchase_q} is not greater or equal to zero!! "

        self.cus_name = cus_name
        self.pro_id = pro_id
        self.purchase_q = purchase_q
        self.price_purchased = price_purchased
    
    # magic method repr for representing objects
    def __repr__(self):
        return f"('{self.cus_name}','{self.pro_id}','{self.purchase_q}','{self.price_purchased}')"
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
    cus_id = input("Enter customer id to purchase: ")
    # check if the customer id exists
    for cus in customer.CUSTOMERS:
        if cus_id == cus.id:
            customer_exists = True
            cus_name = cus.name
            print("Customer name is:  " , cus_name)
            break
            # print("Customer exists")

    
    # check if product exists
    pro_id = input("Enter product id to purchase: ") 
    for prod in product.PRODUCTS:
        if pro_id ==prod.id:
            product_exists = True
    #         # print("Product exists")
      
    if customer_exists and product_exists:
        # make purchase
        purchase_q = int(input("Enter quantity of product to purchase: "))
        # check if amount is available
        for i in range(len(product.PRODUCTS)):
            if pro_id == product.PRODUCTS[i].id:
                name = product.PRODUCTS[i].name
                quantity = int(product.PRODUCTS[i].quantity)
                if quantity >= purchase_q:
                    # update product amount
                    balance = quantity - purchase_q
                    # print("Product available")
                    price = float(product.PRODUCTS[i].price)
                    price_purchased = price * purchase_q
                    output = Purchase(cus_name,pro_id,purchase_q,price_purchased)
                    PURCHASES.append(output)
                    print("Purchase successfull!!!")
                    print()
                    print(PURCHASES)
                    # update_products()
                    while True:
                        print ("""
                        Choose purchase option:

                        1. Make another purchase
                        2. Checkout
                        3.Exit
                        """)
                        choice7 = int(input("Choose a purchase option: "))
                        if choice7 ==1:
                            make_purchase()
                        elif choice7 ==2:
                            checkout()
                            break
                        elif choice7 ==3:
                            print()
                            break
                        else:
                            print("Invalid option!!!")
                        
                else:
                    print("Quantity in stock is below " +str(purchase_q) + ' : ' +"quantity available:"+str(quantity) )
                    make_purchase()
                    break
  
    else:
        print("Invalid details!!!")
        
        

def handle_file():
    with open('purchase.txt','a')as fo:
        for p in PURCHASES:
            print(p.cus_name+','+p.pro_id+','+str(p.purchase_q)+','+str(p.price_purchased),file=fo)
            # break            

def checkout():
    total_purchase = 0
    for p in PURCHASES:
        # pur = p.split(',')
        cost = float(p.price_purchased)
        total_purchase += cost
    print()
    print("Total: "+ str(total_purchase))
    print("purchase complete")
    update_products()
    handle_file()


def update_products():
    for p in PURCHASES:
        # pur = p.split(',')
        product_id = p.pro_id
        p_quantity = int(p.purchase_q)
        # print("quantity: "+ str(quantity))
        # open products file
        file = open('product.txt','r')
        temp = open('temp.txt','w')
        s = ' '
        while(s):
            s = file.readline()
            L = s.split(',')
            if len(s)>0:
                if (L[0]) == product_id:
                    name = L[1]
                    quantity = int(L[2])
                    price = L[3]
                    updated_q = quantity - p_quantity
                    temp.write(str(product_id)+','+name+','+str(updated_q)+','+str(price))
                else:
                    temp.write(s)
        temp.close()
        file.close()
        os.remove('product.txt')
        os.rename('temp.txt','product.txt')
        print("Inventory updated")
        print("Stock remaining for " +name + ':' +str(updated_q))
                    
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
    total = 0
    items_bought = 0
    # menu for search options
    while True:
        print("""
        
        Search options:

        1. Search by customer name
        2. Search by product id
        3. Exit

        """)
        choice5 = int(input("Select search option:")) 
        if choice5 ==1:
            fo = open('purchase.txt','r')
            cus_name = input("Please enter customer name to search: ").lower()
            s = ' '
            while(s):
                s = fo.readline()
                L = s.split(',')
                if len(s)>0:
                    if (L[0]) == cus_name:
                        # print(L)
                        pro_id = L[1]
                        quantity = L[2]
                        price = float(L[3])
                        print( )
                        # Calculate total spend by customer
                        total += price
                        print("customer name: ",cus_name)
                        print("Product id: ",pro_id)
                        print("Quantity purchased: ",quantity)
                        print("Price: ",price)


                        # print(cus_name ,pro_id,quantity,price)
            print('----------------')
            print("Total spent by " +cus_name + ' : ' + str(total))
            break
                
    
        elif choice5 ==2:
            fo = open('purchase.txt','r')
            id = input("Please enter product id to search: ")
            s = ' '
            while(s):
                s = fo.readline()
                L = s.split(',')
                if len(s)>0:
                    if (L[1]) == id:
                        # print(L)
                        cus_name = L[0]
                        quantity = int(L[2])
                        price = float(L[3])
                        print( )
                        # Calculate total spent on the product
                        total += price          
                        # items bought
                        items_bought += quantity
                        print("customer name: ",cus_name)
                        print("product id: ",id)
                        print("Quantity purchased: ",quantity)
                        print("Price: ",price)

                        # print(cus_name ,id,quantity,price)
             
            print('----------------')
            print("Total spent: " + str(total))
            print()
            print("No of products purchased:" + str(items_bought))

            
            
        elif choice5 == 3:
            print()
            break
        else:
            print()
            print('Oops! Incorrect choice. Please try again! ')



