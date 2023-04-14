from datatier import Datatier
from presentationtier import Presentationtier


if __name__ == '__main__':
    data_tier = Datatier()
    presentation_tier = Presentationtier()
    while True:
        print("1. Show Customers and Orders\n2. Add Customer\n3. Add Order\n4. Delete Order\n5. Update order\n6. Select Order(Customer name, Product name, Amount)\n7. Import .csv(Customer)\n8. Import .csv(Order)\n9. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            customers = data_tier.get_customers()
            orders = data_tier.get_orders()
            print("\nCustomers------")
            presentation_tier.show_customers(customers)
            print("\nOrders------")
            presentation_tier.show_order(orders)
        elif choice == '2':
            presentation_tier.add_customer(data_tier)
        elif choice == '3':
            orders = data_tier.get_orders_name()
            presentation_tier.show_order_name(orders)
            print("\n---------")
            presentation_tier.add_order(data_tier)
        elif choice == '4':
            orders = data_tier.get_orders()
            presentation_tier.show_order(orders)
            presentation_tier.delete_order(data_tier)
        elif choice == '5':
            orders = data_tier.get_orders()
            presentation_tier.show_order(orders)
            presentation_tier.update_order(data_tier)
        elif choice == '6':
            orders = data_tier.get_order_data()
            presentation_tier.show_order_data(orders)
        elif choice == '7':
            data_tier.import_customers_from_csv('customers.csv')
        elif choice == '8':
            data_tier.import_order_from_csv('orders.csv')
        elif choice == '9':
            break
        else:
            print("Invalid choice. Try again.")
