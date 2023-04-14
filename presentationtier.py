from model import Order
from model import Customer

class Presentationtier:
    def show_customers(self, customers):
        cislo = 0
        for customer in customers:
            cislo += 1
            print(str(cislo) +". Name: {}\nEmail: {}\nPassword: {}\n".format(
                customer['name'], customer['email'], customer['password']))
    def show_order_name(self, orders):
        cislo= 0
        for order in orders:
            cislo += 1
            print(str(cislo) +". Customer_name: {}\n".format(
                order['Customer_name']))

    def show_order(self, orders):
        cislo= 0
        for order in orders:
            cislo += 1
            print(str(cislo) +". customer_name: {}\norder_date: {}\nstatus: {}\ntotal_price: {}\n".format(
                order['Customer_name'], order['Order_date'], order['Status'], order['Total_price']))

    def add_order(self, order_controller):

        pokus = True
        while pokus==True:
            customer_id= input("Enter customer id: ")
            status = input("Enter status(Pending,Shipped,Delivered):")
            if status == 'Pending' or status == 'Shipped'or status == 'Delivered':
                total_price= input("Enter total price:")
                order= Order(customer_id,status,total_price)
                order_controller.add_order(order)
                print("Order added successfully.")
                pokus = False
            else:
                print("\nYou have to add Pending, Shipped or Delivered")
                pokus = True

    def add_customer(self, customer_controller):
        name = input("Enter customer name: ")
        email = input("Enter customer email: ")
        password = input("Enter customer password: ")
        if len(name) != 0 and len(email) > 5 and len(password) != 0:
            customer = Customer(name, email, password)
            customer_controller.add_customer(customer)
            print("Customer added successfully.")

    def delete_order(self,order_controller):
        name = input("Enter customer name: ")
        order_controller.delete_order(name)
        print("Order deleted successfully.")

    def update_order(self,order_controller):
        customer_name = input("Enter customer name:")
        if len(customer_name) != 0:
            new_status = input("Enter status(Pending,Shipped,Delivered):")
            if new_status == 'Pending' or new_status == 'Shipped'or new_status == 'Delivered':
                new_total_price =input("Enter total price:")
                order_controller.update_order(customer_name, new_status, new_total_price)
                print("Order has been updated.")

    def show_order_data(self, orders):
        cislo = 0
        for order in orders:
            cislo += 1
            print(str(cislo) + ". Order: {}\nCustomer name: {}\nProduct name: {}\nAmount: {}\n".format(
                order['order'], order['customer_name'], order['product_name'], order['product_amount']))