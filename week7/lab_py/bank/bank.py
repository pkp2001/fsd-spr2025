from customer import Customer
from config import DTF,NOW

class Bank:
    def __init__(self):
        self.customers = []
        self.add_customers(3)

    def add_customers(self, n):
        for _ in range(n):
            self.add_customer()

    def add_customer(self):
        name = self.read_name()
        if self.customer(name):
            print("Customer already exists!")
            return
        customer = Customer(name)
        self.customers.append(customer)
        print(f"Customer {name} added.")

    def remove_customer(self, name):
        c = self.customer(name)
        if c:
            self.customers.remove(c)
            print(f"Customer {name} removed.")
        else:
            print("Customer does not exist")

    def show_customer(self, name):
        c = self.customer(name)
        if c:
            c.show()
        else:
            print("Customer does not exist")

    def customer(self, name):
        for c in self.customers:
            if c.match(name):
                return c
        return None

    def read_name(self):
        print("Enter Customer Name: ", end="")
        return input().strip()

    def login(self, name):
        c = self.customer(name)
        if c:
            c.use()
        else:
            print("Customer does not exist")

    def view(self):
        for customer in self.customers:
            print(customer)