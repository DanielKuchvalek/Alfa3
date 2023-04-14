import mysql.connector
import configparser

class DBConnection:
    def __init__(self):
        config = configparser.ConfigParser()
        config.read('conf.ini')
        self.cnx = mysql.connector.connect(
            user=config['database']['user'],password =config['database']['password'],
            host=config['database']['host'] ,database=config['database']['database'])
        self.cursor = self.cnx.cursor()
    #Funkce execute vykonává dotaz na databázi a případně s parametry, uloží změny
    def execute(self, query, params=None):
        if params:
            self.cursor.execute(query, params)
        else:
            self.cursor.execute(query)
        self.cnx.commit()
    #fetch_all vrátí výsledky všech řádků z databáze po provedení dotazu
    def fetch_all(self, query, params=None):
        if params:
            self.cursor.execute(query, params)
        else:
            self.cursor.execute(query)
        return self.cursor.fetchall()


    def __del__(self):
        self.cursor.close()
        self.cnx.close()

class Order:
    def __init__(self,customer_id,status,total_price):
        self.customer_id = customer_id
        self.status = status
        self.total_price = total_price
        self.objednavka = None
        self.customer_name = None
        self.db = DBConnection()

    def add_order(self):
        query = "INSERT INTO Orders(customer_id, status, total_price,order_date) VALUES (%s, %s, %s,NOW())"
        params = (self.customer_id, self.status, self.total_price)
        self.db.execute(query, params)

    def to_dict(self):
        return {
            'status': self.status,
            'total_price': self.total_price
        }

class Customer:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password
        self.db = DBConnection()

    def add_customer(self):
        query = "INSERT INTO Customers(name, email, password, registration_date) VALUES (%s, %s, %s, NOW())"
        params = (self.name, self.email, self.password)
        self.db.execute(query, params)

    def to_dict(self):
        return {
            'name': self.name,
            'email': self.email,
            'password': self.password
        }
