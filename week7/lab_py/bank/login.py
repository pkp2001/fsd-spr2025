from bank import Bank
from manager import Manager
from config import DTF, NOW

class Login:
    def __init__(self):
        self.bank = Bank()
        self.manager = Manager(self.bank)

    def read_choice(self):
        print(f"Bank menu {NOW.strftime(DTF)}")
        print("Main menu:")
        print("L = Log in as a customer, A = Log in as the manager, X = Exit")
        print("Enter choice: ", end="")
        return input().strip().upper()

    def help(self):
        print("Menu options:")
        print("L = Log in as a customer")
        print("A = Log in as the manager")
        print("X = Exit")

    def main(self):
        choice = self.read_choice()
        while choice != 'X':
            match choice:
                case 'L':
                    name = self.bank.read_name()
                    self.bank.login(name)
                case 'A':
                    self.manager.use()
                case _:
                    self.help()
            choice = self.read_choice()
        print("Done")

if __name__ == "__main__":
    Login().main()
