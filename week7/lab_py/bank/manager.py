from config import DTF, NOW

class Manager:
    def __init__(self, bank):
        self.bank = bank
        self.name = "John Smith"

    def read_choice(self):
        print(f"{self.name} admin menu: {NOW.strftime(DTF)}")
        print("Manager menu:")
        print("a = Add customer, r = Remove customer, s = Show customer statement, v = View all customers, x = Exit to bank menu")
        print("Enter choice: ", end="")
        return input().strip().lower()

    def help(self):
        print("Manager menu options:")
        print("a = Add a new customer")
        print("r = Remove a customer")
        print("s = Show a customer's account statement")
        print("v = View all customers")
        print("x = Exit to bank menu")

    def add_customer(self):
        self.bank.add_customer()

    def remove_customer(self):
        name = self.bank.read_name()
        self.bank.remove_customer(name)

    def show_customer(self):
        name = self.bank.read_name()
        self.bank.show_customer(name)

    def view_customers(self):
        self.bank.view()

    def use(self):
        choice = self.read_choice()
        while choice != 'x':
            match choice:
                case 'a':
                    self.add_customer()
                case 'r':
                    self.remove_customer()
                case 's':
                    self.show_customer()
                case 'v':
                    self.view_customers()
                case _:
                    self.help()
            choice = self.read_choice()
        print("Back to Bank menu")
