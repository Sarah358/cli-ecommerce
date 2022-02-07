import os

CUSTOMERS = []
# customer class
class Customer:
    def __init__(self,id,name,address):
        self.id = id
        self.name = name
        self.address = address

# customer menu

def display_customer_menu():
    customer_list = []
    
    # creating options  
    while True:
        print("""

        Customer menu

        1. List all Customers

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
            customer_list.append(add_customer())
            print (customer_list)
            # add_customer()

        elif choice2 == 3:
            print()
            edit_customer()
            
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
    customers = []
    customers_list = []
    with open('customer.txt','r') as reader:
        for line in reader.readlines():
            customers.append(line)
    # print(customers)
     # remove \n
    for cust in customers:
        lists = cust.replace('\n','')
        customers_list.append(lists)
    print(customers_list)
    
    # customer = open("customer.txt", "r")
    # for c in customer:
    #     cust = c.split(" ,")
    #     print(cust)
    

# function to add a customer
# fields(customer_id(unique),customer_name,addess)
def add_customer():
    #open the file in append mode (add to file, we don't wish to overwrite
    fo = open('customer.txt','a+',newline='')
    customer_id = input("Enter Customer id : ")
    # check for unique id 
    with open("customer.txt",'r') as fo_r:
        for line in fo_r.readlines():
            if customer_id in line:
                print()
                print("Id already exists!!!Please enter a unique id !!!")
                print()
                return add_customer()
    # user inputs
    customer_name = input("Enter Customer name:  ").lower()
    address = input("Enter customer address:   ")
    fo.write(customer_id + ',' +  customer_name  +  ','  +  address + "\n")
    fo.close()
    if(fo):
        print("Customer added successfully!!!")
    print()
    output = {"id": customer_id, "name": customer_name, "address": address}
    return output
        

# function to edit customer with customer id
def edit_customer():
    file = open('customer.txt','r')
    temp = open('temp.txt','w')
    id = int(input("Enter customer id to change: "))
    s = " "
    while(s):
        s = file.readline()
        L = s.split(",")
        if len(s)>0:
            if int(L[0]) == id:
                name = input("Enter customer name: ").lower()
                address = input("Enter the customer address: ")
                temp.write(str(id) + ',' +  name  +  ','  +  address + "\n")
            else:
                temp.write(s)
    temp.close()
    file.close()
    os.remove('customer.txt')
    os.rename('temp.txt','customer.txt')
    print("Customer updated successfuly!!")
    list_customers()


# function to delete a customer with customer id
def delete_customer():
    customer = open("customer.txt",'r')
    temp = open("temp.txt",'w')
    id = int(input("Enter customer id to delete:  "))
    s = ' '
    while(s):
        s = customer.readline()
        L = s.split(',')
        if len(s)>0:
            if int(L[0]) != id:
                temp.write(s)

    customer.close()
    temp.close()
    os.remove('customer.txt')
    os.rename('temp.txt','customer.txt')
    print(" Customer deleted successfuly!! ")
    list_customers()

# function to search for customer with id and name
def search_customer():
    customer = open('customer.txt','r')
    id = int(input("Enter customer id to search:  "))
    print()
    s = ' '
    while(s):
        s = customer.readline()
        L = s.split(",")
        if len(s)>0:
            if int(L[0]) == id:
                print("Customer details")
                print("------------------------------")
                print("Customer id: ",L[0])
                print("Customer Name: ",L[1])
                print("Customer Address: ",L[2])
                # break

            # else:
            #     print("Customer not available!!")
            #     break

# load customers
def load_customers():
    file = open('customer.txt','r')
    for c in file:
        cust = c.split(',')
        id = cust[0]
        name = cust[1]
        address = cust[2]
        customer = Customer(id,name,address)
        CUSTOMERS.append(customer)
        # print(CUSTOMERS)



if __name__ == "__main__":
    display_customer_menu()