# CUSTOMER PRODUCT SYSTEM
## CLI driven e-commerce system using python
### Introduction

The customer-product system is based on customers, products, and purchases made by customers. The purpose of this project is to implement a Python program that starts with a menu, get customer's choices, and process them. This program will help us to manage customer and product data in the system and enable customers to buy certain products if there are enough items from that product in the system.

Customer and product data will be entered by the user (interactive by using a keyboard). For customers: customer id, name, and address data will be entered.(you might want to use a list of lists). Customer ids will be unique and therefore cannot be
repeated. This will have to be checked when the users enter customer data. Similar operations will be done for the products too. The product name can be repeated but the product id has to be unique as in customers.

After loading customer and product data, a product can be purchased by a customer in the system. For a purchase, customer id, product id, and amount of product will be needed. If the amount is larger than the amount available in the system, the product will not be sold. If the system has enough from the given product, the purchase will be completed by decreasing the amount in the system.

## Language and tools
* Editor (eg Vscode)
* python 

## Clone project
``` git clone https://github.com/Sarah358/cli-ecommerce.git ```

## Run
``` python3 main.py ```

## Concepts
- python fundamentals
- object oriented programming
- code data structures and algorithms
- File handling 
- Git fundamentals

## Project functionalities
The ***main.py*** file consists of the main menu where a user chooses the operations they want to perform within the system. The operations include :
* Customer operations
* Product operations
* Purchases operations

### 1. CUSTOMER OPERATIONS
The ***customer.py*** file describes customer operations which are:
- customer sub-menu which allows users to select an operation to handle
- insert customer which allows users to create new customers and save data in the **customer.txt** file
- update customer which allows users to edit customer details from the text file
- delete customer which allows users to delete customer details from the text file
- search customer which allows users to search for a customer from the text file using customer id 
- list customers which displays all customers from the text file 


### 2. PRODUCT OPERATIONS
The ***product.py*** file handles product operations which are:
- product sub-menu which allows users to select an operation to handle
- insert product which allows users to create new products and save data in the **product.txt** file
- update product which allows users to edit product details from the text file
- delete product which allows users to delete product details from the text file
- search product which allows users to search for a product from the text file using product id 
- list products which displays all products from the text file

### 3. PURCHASES OPERATIONS
The ***purchase.py*** file handles purchases operations which are:
- purchases sub menu which allows users to select an operation to handle
- make purchase operation which prompts the user to enter customer id and product id in order to make a purchase. The purchase details are stored in the **purchase.txt** file.
- Search purchase which allows users to search for purchases made using customer id or product id .
- List purchases which lists all purchases made and total amount spent 

## Project illustration











