
CUSTOMERS = []


class Customer:
    def __init__(self,id,name,address):
        self.id = id
        self.name = name
        self.address = address

    def get_name(self):
        return self.name
          
    
    def set_name(self,name):
        self.name = name

    def get_address(self):
        return self.address
    def set_address(self,address):
        self.address = address

def display_customer_menu():
    # creating options  
    while True:
        print("""

        Customer menu

        1. Show all Customers

        2. Add customer

        3. Edit Customer

        4. Delete Customer

        5. Search for a customer

        6. Quit

        """)  
        choice2 = int(input("Select Customer option:"))  

        # choice 1
        if choice2 == 1:
            print()
            list_customers()
        elif choice2 == 2:
            print()
            add_customer()
            # customer_file()
          
        elif choice2 == 3:
            print()
            update_customer()
            
        elif choice2 == 4:
            print()
            delete_customer()
        elif choice2 == 5:
            print()
            search_customer()
        elif choice2 == 6:
            print()
            break
        else:
            print()
            print('Oops! Incorrect choice. Please try again! ')
# required functions
# func to list all customers
def list_customers():
     
    customer = open("customer.txt", "r")
    for c in customer:
        cust = c.split(" ,")
        print(cust)
    
            
# function to add a customer
# fields(customer_id(unique),customer_name,addess)
def add_customer():
    # handle primary key as id
    fo_p = open('primary.txt','r')
    s= fo_p.read()
    if s == "":
        # if file is empty set the primary key to 1
        id = 1
        fo_p.close()
        # open the file in write mode
        fo_p = open("primary.txt","w")
        fo_p.write(str(id))
        fo_p.close()
    else:
        id = int(s)+1
        # open the file in write mode
        fo_p = open("primary.txt","w")
        fo_p.write(str(id))
        fo_p.close()
    # id = input("Enter Customer id: ")
    name = input("Enter Customer name: ")
    address = input("Enter customer address: ")
    output = Customer(id,name,address)
    # append to list
    CUSTOMERS.append(output)
    print("customer added successfully")
    handle_file()
    
def handle_file():
    for c in CUSTOMERS:
        fo = open('customer.txt','a')
        fo.write(str(c.id)   +','+   c.name+  ','  + c.address + '\n')
        fo.close()
        break

def update_customer():
    get_customer()
    # as for user input
    cus_id = input("Enter customer id to modify:  ")

    


# function to delete a customer with customer id
def delete_customer():
    get_customer()
    cus_id = input("Enter customer id to delete:  ")
    for i in range(len(CUSTOMERS)-1):
        if CUSTOMERS[i].id == cus_id:
            del CUSTOMERS[i]
            print("Customer deleted successfully")
        else:
            print("Invalid ID")
            break
    handle_file()



# function to search for customer with id and name
def search_customer():
    pass

def get_customer():
    customer = open("customer.txt", "r")
    for c in customer:
        cst = c.split(" ")
        print(cst)
        id = cst[0]
        name = cst[1]
        address = cst[2]
        customer = Customer(id, name, address)
        CUSTOMERS.append(customer)


if __name__ == "__main__":
    Customer