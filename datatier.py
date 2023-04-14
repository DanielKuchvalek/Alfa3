import csv

from model import DBConnection
from model import Customer
from model import Order

class Datatier:
    def __init__(self):
        self.db = DBConnection()

    def add_customer(self, customer):
        customer.add_customer()
    def add_order(self, order):
        order.add_order()

    def get_customers(self):
        query = "select name, email, password from Customers"
        customers = self.db.fetch_all(query)
        return [{'name': name, 'email': email, 'password': password} for name, email, password in customers]

    def get_orders(self):
        query = "select Customers.name,order_date,status,total_price from Orders inner join Customers on Orders.customer_id = Customers.customer_id;"
        orders= self.db.fetch_all(query)
        return [{"Customer_name": customer_name, "Order_date": order_date, "Status": status, "Total_price": total_price} for customer_name, order_date, status,total_price  in orders]

    def get_orders_name(self):
        query = "select Customers.name from Orders inner join Customers on Orders.customer_id = Customers.customer_id;"
        orders_name = self.db.fetch_all(query)
        return [{"Customer_name": customer_name} for customer_name in orders_name]

    def delete_order(self, customer_name):
        query = "DELETE from Orders where customer_id=(SELECT customer_id from Customers where Customers.name=%s);"
        params = (customer_name,)
        self.db.execute(query, params)

    def update_order(self, customer_name, new_status, new_total_price):
        query = "UPDATE Orders SET status=%s, total_price=%s WHERE customer_id=(SELECT customer_id FROM Customers WHERE name=%s)"
        params = (new_status, new_total_price, customer_name)
        self.db.execute(query, params)

    def get_order_data(self):
        query = """
        SELECT Orders.order_id AS order_name, Customers.name AS customer_name, 
        Products.name AS product_name, Order_items.quantity AS order_amount
        FROM Orders
        JOIN Customers ON Orders.customer_id = Customers.customer_id
        JOIN Order_items ON Orders.order_id = Order_items.order_id
        JOIN Products ON Order_items.product_id = Products.product_id;
        """
        order_data = self.db.fetch_all(query)
        return [{"order": order, "customer_name": customer_name,
                 "product_name": product_name, "product_amount": product_amount}
                for order, customer_name, product_name, product_amount in order_data]

    def import_customers_from_csv(self, filename):
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            header = next(reader)
            for row in reader:
                print(row)
                customer = Customer(row[0], row[1], row[2])
                print(customer)
                self.add_customer(customer)

    def import_order_from_csv(self, filename):
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            header = next(reader)
            for row in reader:
                print(row)
                order = Order(row[0], row[1], row[2])
                print(order)
                self.add_order(order)