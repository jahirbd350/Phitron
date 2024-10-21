from abc import ABC,abstractmethod
import datetime

class Person(ABC):
    def __init__(self, name, email, address):
        self.name = name
        self.email = email
        self.address = address

class User(Person):
    def __init__(self, name, email, address, account_type):
        super().__init__(name, email, address)
        x = datetime.datetime.now()
        self.account_number = (str(x.year)+str(x.month)+str(x.day)+str(x.hour)+str(x.minute)+str(x.second))
        self.account_type = account_type
        self.__balance = 0.00
        self.__loan_taken = 0.00
        self.loan_counter = 0
        self.transaction_history = []
    
    @property
    def balance(self):
        return self.__balance
    
    @property
    def loan_taken(self):
        return self.__loan_taken
    
    
    def take_loan(self, amount):
        self.__loan_taken += amount
        self.loan_counter += 1
        user.transaction_history.append(("Loan Taken", amount))
        print(f"Loan Approaved with {amount}")
    
    def deposite(self, amount):
        if amount <=0:
            print("Invalid amount to deposite!!")
        else:
            self.__balance += amount
            self.transaction_history.append(("Deposite", amount))
            print(f"{self.account_number} dipositted {amount} successfully!")

    def withdraw(self, amount):
        if bank.bankrupt:
            print("This bank is Bankrupt!!!")
        else:
            if self.__balance >= amount:
                self.__balance -= amount
                print(f"{self.name} has withdrawn {amount} successfully!!")
                self.transaction_history.append(("withdraw", amount))
            else:
                print("Withdraw amount exceeded!!")

class Admin(Person):
    def __init__(self, name, email, address):
        super().__init__(name, email, address)


class Bank:
    def __init__(self, name):
        self.name = name
        self.users = []
        self.admins = []
        self.__total_balance = 0.00
        self.__loan_given = 0.00
        self.loan_status = True
        self.bankrupt = False

    def add_user(self, user):
        self.users.append(user)

    def add_admin(self, name, email, address):
        admin = Admin(name, email, address)
        self.admins.append(admin)

    def get_total_balance(self):
        for user in self.users:
            self.__total_balance += user.balance
        return self.__total_balance
    
    def get_total_loan(self):
        for user in self.users:
            self.__loan_given += user.loan_taken
        return self.__loan_given
    
    def get_all_users(self):
        print("**All Users**")
        print("Name\tEmail\t\tAddress\tAccount Type\tBalance")
        for user in self.users:
            print(f"{user.name}\t{user.email}\t{user.address}\t{user.account_type}\t\t{user.balance}\n")
    
    def find_user(self, account_no):
        for user in self.users:
            if user.account_number == account_no:
                # print("Login Successfull!")
                return user
        print(f"\nNo user found with Account No: {account_no}")
        
    
    def delete_user(self, account_number):
        for user in self.users:
            if user.account_number == account_number:
                self.users.remove(user)
                print("User Deleted successfully!!")
                return
        print(f"User with account number {account_number} not found!!")
    
    def switch_loan_feature(self):
        if self.loan_status == True:
            self.loan_status = False
        else:
            self.loan_status = True
    
    def transfer(self, sender, receiver, amount):
        user1 = self.find_user(sender)
        user2 = self.find_user(receiver)
        # print(user1)
        # print(user2)
        if user1.balance >= amount:
            user1.withdraw(amount)
            user2.deposite(amount)
            print(f"{amount} transferred successfully!")
            user1.transaction_history.append(("Send Money", {amount}))
            user2.transaction_history.append(("Rcv Money", {amount}))
        else:
            print("Not enough balance to transfer")

bank = Bank("Islami bank")
# bank.add_admin("admin", "admin@email", "dhaka")
# bank.add_user("Jahir", "jahir@email", "dhaka", "savings")
# print(bank.get_total_balance())
# bank.get_all_users()
# print(bank.get_total_loan())
# user = User("Jahir", "jahir@email", "dhaka", "savings")
# user2 = User("Jahir", "jahir@email", "dhaka", "savings")
# bank.add_user(user)

# bank.add_user(user2)
# print((user.account_number))
# print((user2.account_number))
# u2 = bank.find_user(user.account_number)
# print(type(u2.account_number))
    
    
while True:
    print("\nSelect your User Type:")
    print("1. User")
    print("2. Admin") 
    print("3. Exit") 

    op = int(input("\nEnter 1 or 2 as your role: "))
    if op == 1:
        while True:
            print("1. Create an account") 
            print("2. Deposit amount") 
            print("3. Withdraw amount") 
            print("4. Available balance")
            print("5. Transaction history") 
            print("6. Request for LOAN")
            print("7. Transfer amount to others") 
            print("8. Exit")

            userop = int(input("Enter your option: "))
            if userop == 1:
                name = input("Name: ")
                email = input("Email: ")
                address = input("Address: ")
                account_type = input("Enter Account Type: ")
                user = User(name, email, address, account_type)  
                bank.add_user(user)
                print(f"\nWelcome {name}, Your {user.account_type} account number is {user.account_number}")

            elif userop == 2:
                account_no = (input("Enter account number: "))
                deposit_amount = int(input("Enter amount: "))
                u = bank.find_user(account_no)
                if u:
                    u.deposite(deposit_amount)
                
            elif userop == 3:
                account_no = int(input("Enter account number: "))
                withdraw_amount = int(input("Enter amount: ")) 
                u = bank.find_user(account_no)
                if u:
                    u.withdraw(withdraw_amount) 

            elif userop == 4:
                account_no = int(input("Enter account number: "))
                u = bank.find_user(account_no)
                if u:
                    print(f"Present Balance: {u.balance}")

            elif userop == 5:
                for i, transaction in enumerate(user.transaction_history):
                    print(f"\nTransction History of Account no: {user.account_number}")
                    print("Ser\tTransaction Type\tAmount")
                    print(f"{i+1}\t{transaction[0]}\t\t{transaction[1]}\n")  

            elif userop == 6:
                account_no = int(input("Enter account number: "))
                loan_amount = int(input("Enter LOAN Amount: "))
                u = bank.find_user(account_no)
                if u:
                    if loan_amount > bank.get_total_loan():
                        print("Loan amount exceeded bank total balance!!")
                        continue
                    if u.loan_counter >= 2:
                        print("You already taken loan twice!!")
                    else:
                        user.take_loan(loan_amount)
            
            elif userop == 7:
                my_account_no = (input("Enter your account number: "))
                receiver_account_no = (input("Enter receiver account number: "))
                transfer_amount = int(input("Enter transfer amount: "))
                # u1 = bank.find_user(my_account_no)
                # u2 = bank.find_user(receiver_account_no)
                # print(u1, u2)
                bank.transfer(my_account_no, receiver_account_no, transfer_amount)
            
            else:
                break
        
        
    elif op == 2:
        while True:
            print("1. Create an account")
            print("2. Delete any account")
            print("3. All users accounts list")
            print("4. Total available balance")
            print("5. Total LOAN amount")
            print("6. Change LOAN feature / Declare BANKRUPT") 
            print("7. Exit")

            adminop = int(input("Enter your option: "))
            if adminop == 1:
                name = input("Enter Your Name: ")
                email = input("Enter Your Email: ")
                address = input("Enter Your Address: ")
                # admin = Admin(name, email, address)
                bank.add_admin(name, email, address)
                print(f"{name}, Your admin account created successfully!!!")

            elif adminop == 2:
                account_no = (input("User account no to delete: "))
                bank.delete_user(account_no)  
                        
            elif adminop == 3:
                print(f"Name \tAccount No \tAccount Type \tAmount") 
                for u in bank.users:
                    print(f'{u.name}\t{u.account_number}\t{u.account_type}\t{u.balance}')   
                print()
            elif adminop == 4:
                print(f"Available balance of bank: {bank.get_total_balance()}")

            elif adminop == 5:
                print(f"Total LOAN amount: {bank.get_total_loan()}")

            elif adminop == 6: 
                choice = int(input("1 - To declare BANKRUPT or \n0 - To give the loan feature \nType here: "))
                
                if choice == 1: 
                    bank.bankrupt = True
                    print("BANKRUPT mode is ON")            
                elif choice == 0: 
                    Bank.bankrupt = False
                    print("BANKRUPT mode is OFF")  
                else: print("you entered wrong option. type only (1) or (0)")            
            
            else:
                break
    else:
        exit()