
import os
# customer menu

def display_customer_menu():
    
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
            add_customer()
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
    pass

# function to add a customer
# fields(customer_id(unique),customer_name,addess)
def add_customer():
    fo_p = open('primary.txt','r')
    s= fo_p.read()
    if s == "":
        # if file is empty set the primary key to 1
        customer_id = 1
        fo_p.close()
        # open the file in write mode
        fo_p = open("primary.txt","w")
        fo_p.write(str(customer_id))
        fo_p.close()
    else:
        customer_id = int(s)+1
        # open the file in write mode
        fo_p = open("primary.txt","w")
        fo_p.write(str(customer_id))
        fo_p.close()


    #open the file in append mode (add to file, we don't wish to overwrite
    with open('customer.txt','a',newline="") as fo:
        # customer_id = input("Enter Customer id : ")
        customer_name = input("Enter Customer name:  ")
        address = input("Enter customer address:   ")
        fo.write("")
        fo.write(str(customer_id) +', ' +  customer_name  +  ', '  +  address + "\n")
        fo.close()
      
        if(fo):
            print("Customer added successfully!!!")
        print()
        



# function to edit customer with customer id
def edit_customer():
    fo = open('customer.txt','r')
    # create a temporary file
    temp = open('temp.txt','w')
    # ask user to insert id
    cus_id = int(input("Enter customer id to update:  "))
    # variable for reading the file
    s = ''
    while(s):
        s = fo.readline()
        L = s.split(',')
        if len(s)>0:
            if int(L[0]) == cus_id:
                cus_id = input("Enter customer id:  ")
                name = input("Enter new customer name:  ")
                address = input("Enter new customer address:  ")
                temp.write(str (cus_id)  + ','  +  name  +  ', '  +  address + "\n")
    
            else:
                temp.write(s)

    temp.close()
    fo.close()
    os.remove('customer.txt')
    os.rename('temp.txt','customer.txt')
    


# function to delete a customer with customer id
def delete_customer():
    pass

# function to search for customer with id and name
def search_customer():
    pass



if __name__ == "__main__":
    display_customer_menu()