# Python Program to create a Bank Management system in which user can open a main account, savings account and checking account
# Here on this entire code, IBAN is used as unique identifying value
# Date - 18/12/2021
# Presented by - Ayan Abedin and Raghav Bansal

# importing modules
# os module provides functions for ineteracting with the operating system
# here it is used for deleting accounts
import os


# class Bank for creating and managaing the main accout
class Bank:

    # This function would contain ther objects and the opeartions to open an account
    def __init__(self):
        self.client_details_list = []
        self.loggedin = False
        # 100 euros must be deposited to open an account
        self.cash = 100
        self.TranferCash = False

    # function to create registration using name, IBAN, pin and age
    def register(self, name, IBAN, pin, age):
        cash = self.cash
        conditions = True
        # IBAN must be 10 digit characters
        if len(str(IBAN)) > 10 or len(str(IBAN)) < 10:
            print("Invalid IBAN ! please enter 10 digit IBAN number. ")
            conditions = False
        # PIN must be of 4 to 6 digit
        if len(pin) < 4 or len(pin) > 6:
            print("Enter pin greater than 4 and less than 6 character")
            conditions = False

            # age to be verfiy that only 18 yrs older could create account
        # if not donot create account
        if age:
            if age >= 18:
                print("You are valid person")
                conditions = True

            if age < 18:
                print("You must be 18 years or older to create account")
                print("Please try again.")
                conditions = False

        if conditions == True:
            print("Account created successfully")
            self.client_details_list = [name, IBAN, pin, cash]
            with open(f"{name}.txt", "w") as f:
                for details in self.client_details_list:
                    f.write(str(details) + "\n")

    # function to login into the system using name, IBAN and PIN as verfication
    def login(self, name, IBAN, pin):
        with open(f"{name}.txt", "r") as f:
            details = f.read()
            self.client_details_list = details.split("\n")
            if str(IBAN) in str(self.client_details_list):
                if str(pin) in str(self.client_details_list):
                    self.loggedin = True

            if self.loggedin == True:
                print(f"{name} logged in")
                self.cash = int(self.client_details_list[3])
                self.name = name

            else:
                print("Wrong details. Please enter again...!!!");

    # function to add amount to current cash
    def add_cash(self, amount):
        # if amount is >0 then run else not
        if amount > 0:
            self.cash += amount
            with open(f"{name}.txt", "r") as f:
                details = f.read()
                self.client_details_list = details.split("\n")

            with open(f"{name}.txt", "w") as f:
                f.write(details.replace(str(self.client_details_list[3]), str(self.cash)))

            print("Amount added successfully")

        else:
            print("Enter correct value of amount")

    # function to withdraw money from current active account
    def withdraw_money(self, money):
        if money > 0:
            self.cash -= money
            with open(f"{name}.txt", "r") as f:
                details = f.read()
                self.client_details_list = details.split("\n")

            with open(f"{name}.txt", "w") as f:
                f.write(details.replace(str(self.client_details_list[3]), str(self.cash)))

            print("Amount withdrawn successful")
        else:
            print("Enter correct amount to withdraw")

    # function to transfer money to another account using name and IBAN
    def Tranfer_cash(self, amount, name, IBAN, ):
        with open(f"{name}.txt", "r") as f:
            details = f.read()
            self.client_details_list = details.split("\n")
            if str(IBAN) in self.client_details_list:
                self.TranferCash = True

        if self.TranferCash == True:
            total_cash = int(self.client_details_list[3]) + amount
            left_cash = self.cash - amount
            with open(f"{name}.txt", "w") as f:
                f.write(details.replace(str(self.client_details_list[3]), str(total_cash)))

            with open(f"{self.name}.txt", "r") as f:
                details_2 = f.read()
                self.client_details_list = details_2.split("\n")

            with open(f"{self.name}.txt", "w") as f:
                f.write(details_2.replace(str(self.client_details_list[3]), str(left_cash)))

            # then how the left amount
            print("Amount Transfered Successfully to", name, "-", IBAN)
            print("Balance left = €", left_cash)
            self.cash = left_cash

    # adding function to change PIN if they want to
    # new pin must be of 4 digits
    def pin_change(self, pin):
        if len(pin) < 4 or len(pin) > 6:
            print("Enter pin greater than 4 and less than 6 character")
        else:
            with open(f"{self.name}.txt", "r") as f:
                details = f.read()
                self.client_details_list = details.split("\n")

            with open(f"{self.name}.txt", "w") as f:
                f.write(details.replace(str(self.client_details_list[2]), str(pin)))
            print("New pin set up successfully.")

    # deleting current loggedin account
    def delete_account(self, name, IBAN, pin):

        if os.path.exists(name + ".txt"):
            os.remove(name + ".txt")
        else:
            print("The file does not exist.")


# creating another sub-class for Savings account with requirements
class Savings():
    # _init__ is used as a constructor to initialize object's state.
    # here 'self' is used as a member of the class
    def __init__(self):
        self.client_details_list_1 = []
        self.loggedin_1 = False

        # 100 euros must be deposited to open an account
        self.cash_1 = 100
        self.age_1 = 0
        self.TransferCash_1 = False

    # register_1 to create a register function for Savings account
    def register_1(self, name_1, IBAN_1, pin_1, age_1):
        cash_1 = self.cash_1
        conditions = True

        # IBAN must be of 10 characters
        if len(str(IBAN_1)) > 10 or len(str(IBAN_1)) < 10:
            print("Invalid IBAN ! Please enter 10 digit IBAN characters")
            conditions = False

        # PIN must be of 4 digit
        if len(pin_1) < 4 or len(pin_1) > 6:
            print("Enter pin greater than 4 and less than 6 character")
            conditions = False

            # age must be 14 or older to open a Savings Account
        # if not 14 account creation fails
        if age_1:
            if age_1 >= 14:
                print("Valid member. Please proceed")
                conditions = True

            if age_1 < 14:
                print("You must be 14 years or older to open a Savings Account")
                print("Please try again")
                conditions = False
        # if every variable is successful tehn account created successfully
        if conditions == True:
            print("Account created successfully")
            self.client_details_list_1 = [name_1, IBAN_1, pin_1, cash_1]
            with open(f"{name_1}_savings.txt", "w") as f:
                for details in self.client_details_list_1:
                    f.write(str(details) + "\n")

                    # login_1 to create a login schema for Savings account

    def login_1(self, name_1, IBAN_1, pin_1):
        with open(f"{name_1}_savings.txt", "r") as f:
            details = f.read()
            self.client_details_list_1 = details.split("\n")

            if str(IBAN_1) in str(self.client_details_list_1):
                if str(pin_1) in str(self.client_details_list_1):
                    self.loggedin_1 = True

            if self.loggedin_1 == True:
                print(f"{name_1} logged in")
                self.cash_1 = int(self.client_details_list_1[3])
                self.name_1 = name_1

            else:
                print("Wrong details. Please enter again...!!!");

    # add cash to current Savings account
    def add_cash_1(self, amount_1):
        if amount_1 > 0:
            self.cash_1 += amount_1
            with open(f"{name_1}_savings.txt", "r") as f:
                details = f.read()
                self.client_details_list_1 = details.split("\n")

            with open(f"{name_1}_savings.txt", "w") as f:
                f.write(details.replace(str(self.client_details_list_1[3]), str(self.cash_1)))

            print("Amount added successfully", amount_1)

        else:
            print("Enter correct value of amount")

    # function to withdraw money from Savings account
    def withdraw_money_1(self, money_1):
        # money can go negative when withdrawing
        if money_1 > 0:
            self.cash_1 -= money_1
            with open(f"{name_1}_savings.txt", "r") as f:
                details = f.read()
                self.client_details_list_1 = details.split("\n")

            with open(f"{name_1}_savings.txt", "w") as f:
                f.write(details.replace(str(self.client_details_list_1[3]), str(self.cash_1)))

            print("Amount withdrawn successful")
        else:
            print("Enter correct amount to withdraw")

    # transfer cash from one Savings account to another account
    # only when name and IBAN is verified
    def Transfer_cash_1(self, amount_1, name_1, IBAN_1):
        with open(f"{name_1}_savings.txt", "r") as f:
            details = f.read()
            self.client_details_list_1 = details.split("\n")

            if str(IBAN_1) in self.client_details_list_1:
                self.TransferCash_1 = True

        if self.TransferCash_1 == True:
            total_cash_1 = int(self.client_details_list_1[3]) + amount_1
            left_cash_1 = self.cash_1 - amount_1
            with open(f"{name_1}_savings.txt", "w") as f:
                f.write(details.replace(str(self.client_details_list_1[3]), str(total_cash_1)))

            with open(f"{self.name_1}_savings.txt", "r") as f:
                details_2 = f.read()
                self.client_details_list_1 = details_2.split("\n")

            with open(f"{self.name_1}_savings.txt", "w") as f:
                f.write(details_2.replace(str(self.client_details_list_1[3]), str(left_cash_1)))

            # show how much trabnsferred and what is left
            print("Amount Transferred Successfully to", name_1, "-", IBAN_1)
            print("Balance left = €", left_cash_1)
            self.cash_1 = left_cash_1

    # deleting current loggedin Savings account
    def delete_account(self, name_1, IBAN_1, pin_1):

        if os.path.exists(name_1 + "_savings" + ".txt"):
            os.remove(name_1 + "_savings" + ".txt")
        else:
            print("The file does not exist.")


# creating a subclass Checking Account from parent class Bank
class Checking():
    # _init__ is used as a constructor to initialize object's state.
    # here 'self' is used as a member of the class
    def __init__(self):
        self.client_details_list_2 = []
        self.loggedin_2 = False

        # 100 euros must be deposited to open a Checking account
        self.cash_2 = 100
        self.age_2 = 0
        self.TransferCash_2 = False

    # register_2 to create a register function for Checking account
    def register_2(self, name_2, IBAN_2, pin_2, age_2):
        cash_2 = self.cash_2
        conditions = True

        # IBAN must be of 10 characters
        if len(str(IBAN_2)) > 10 or len(str(IBAN_2)) < 10:
            print("Invalid IBAN ! Please enter 10 digit IBAN characters")
            conditions = False

        # PIN must be of 4 digits
        if len(pin_2) < 4 or len(pin_2) > 6:
            print("Enter pin greater than 4 and less than 6 character")
            conditions = False
            # user must be 18 yrs or older to open a Checking account
        if age_2:
            if age_2 >= 18:
                print("Valid member. Please proceed")
                conditions = True

            if age_2 < 18:
                print("You must be 18 years or older to open a Checking Account")
                print("Please try again")
                conditions = False

        # if very variable is successful then account created successfully
        if conditions == True:
            print("Account created successfully")
            self.client_details_list_2 = [name_2, IBAN_2, pin_2, cash_2]
            with open(f"{name_2}_checking.txt", "w") as f:
                for details in self.client_details_list_2:
                    f.write(str(details) + "\n")

                    # login_2 to create a login schema for checking account

    def login_2(self, name_2, IBAN_2, pin_2):
        with open(f"{name_2}_checking.txt", "r") as f:
            details = f.read()
            self.client_details_list_2 = details.split("\n")

            if str(IBAN_2) in str(self.client_details_list_2):
                if str(pin_2) in str(self.client_details_list_2):
                    self.loggedin_2 = True

            if self.loggedin_2 == True:
                print(f"{name_2} logged in")
                self.cash_2 = int(self.client_details_list_2[3])
                self.name_2 = name_2

            else:
                print("Wrong details. Please enter again...!!!");

    # add cash to current Checking account
    def add_cash_2(self, amount_2):
        if amount_2 > 0:
            self.cash_2 += amount_2
            with open(f"{name_2}_checking.txt", "r") as f:
                details = f.read()
                self.client_details_list_2 = details.split("\n")

            with open(f"{name_2}_checking.txt", "w") as f:
                f.write(details.replace(str(self.client_details_list_2[3]), str(self.cash_2)))

            print("Amount added successfully", amount_2)

        else:
            print("Enter correct value of amount")

    # transfer cash from one checking account to another account
    # only when name and IBAN is fully verified
    def Transfer_cash_2(self, amount_2, name_2, IBAN_2):
        with open(f"{name_2}_checking.txt", "r") as f:
            details = f.read()
            self.client_details_list_2 = details.split("\n")

            if str(IBAN_2) in self.client_details_list_2:
                self.TransferCash_2 = True

        if self.TransferCash_2 == True:
            total_cash_2 = int(self.client_details_list_2[3]) + amount_2
            left_cash_2 = self.cash_2 - amount_2
            with open(f"{name_2}_checking.txt", "w") as f:
                f.write(details.replace(str(self.client_details_list_2[3]), str(total_cash_2)))

            with open(f"{self.name_2}_checking.txt", "r") as f:
                details_2 = f.read()
                self.client_details_list_2 = details_2.split("\n")

            with open(f"{self.name_2}_checking.txt", "w") as f:
                f.write(details_2.replace(str(self.client_details_list_2[3]), str(left_cash_2)))

            print("Amount Transferred Successfully to", name_2, "-", IBAN_2)
            print("Balance left = €", left_cash_2)
            self.cash_2 = left_cash_2

    # deleting current loggedin Savings account
    def delete_account(self, name_2, IBAN_2, pin_2):

        if os.path.exists(name_2 + "_checking" + ".txt"):
            os.remove(name_2 + "_checking" + ".txt")
        else:
            print("The file does not exist.")


if __name__ == "__main__":
    # initialising classes to a variable
    Bank_object = Bank()
    Bank_object_1 = Savings()
    Bank_object_2 = Checking()

    print("***********BANK MANAGEMENT SYSTEM***********".center(50));
    print("Brought to you by:".center(50));
    print("Ayan|Raghav".center(50));
    print("Welcome to my Bank")
    print("1.Login to main account")
    print("2.Create a new main Account")
    print("3.Login to Savings Account")
    print("4.Create a new Savings Account")
    print("5.Login to Checking Account")
    print("6.Create a new Checking Account")

    # takes user input according to options in integer form
    user = int(input("Please enter your choice: "))

    # If user input is 1 it will log in to the main account by calling the login function
    # logging to main account
    if user == 1:
        print("\nLogging in.......")
        name = input("Enter Name: ")
        IBAN = input("Enter IBAN: ")
        pin = int(input("Enter 4 digit PIN: "))
        Bank_object.login(name, IBAN, pin, )

        # If the user login is true it will log in successfully and perform the following operations
        while True:
            if Bank_object.loggedin:
                print("\n1.Add amount")
                print("2.Check Balance")
                print("3.Withdraw amount")
                print("4.Tranfer Amount")
                print("5.Edit Profile")
                print("6.Close account")
                print("7.Logout")

                # takes user input under logged in account
                login_user = int(input())
                # if user input is 1, it will add cash to current cash by calling the add_cash function
                if login_user == 1:
                    print("Balance = €", Bank_object.cash)
                    amount = int(input("Enter amount: "))
                    Bank_object.add_cash(amount)
                    print("\n1.back menu")
                    print("2.Logout")
                    # then you can go back to menu or just logout
                    choose = int(input())
                    if choose == 1:
                        continue
                    elif choose == 2:
                        break

                # if user input is 2, it will show current amount by using the class Bank_object.cash
                elif login_user == 2:
                    print("Balance = €", Bank_object.cash)
                    print("\n1.back menu")
                    print("2.Logout")
                    choose = int(input())
                    if choose == 1:
                        continue
                    elif choose == 2:
                        break

                # if user input is 3, it will ask ask how much to withdraw then performs the withdraw_money function
                elif login_user == 3:
                    print("Balance = €", Bank_object.cash)
                    money = int(input("Enter amount: "))
                    Bank_object.withdraw_money(money)
                    print("\n1.back menu")
                    print("2.Logout")
                    choose = int(input())
                    if choose == 1:
                        continue
                    elif choose == 2:
                        break

                # if user input is 4, it will ask how much to transfer then ask for the receiver name and IBAN
                elif login_user == 4:
                    print("Balance = €", Bank_object.cash)
                    amount = int(input("Enter amount: "))
                    if amount >= 0 and amount <= Bank_object.cash:
                        name = input("Enter person name: ")
                        IBAN = input("Enter IBAN: ")
                        Bank_object.Tranfer_cash(amount, name, IBAN)
                        print("\n1.back menu")
                        print("2.Logout")
                        choose = int(input())
                        if choose == 1:
                            continue
                        elif choose == 2:
                            break
                    elif amount < 0:
                        print("Enter please correct value of amount")

                    elif amount > Bank_object.cash:
                        print("Not enough balance")

                # if user input is 5, it will allow you to make a new PIN and make it default
                elif login_user == 5:
                    print("1.PIN change")
                    edit_profile = int(input())
                    if edit_profile == 1:
                        new_passwrod = input("Enter new PIN: ")
                        Bank_object.pin_change(new_passwrod)
                        print("\n1.Back to Menu")
                        print("2.Logout")
                        choose = int(input())
                        if choose == 1:
                            continue
                        elif choose == 2:
                            break

                # if user input is 6, then you can delete your account and completely remove the details
                elif login_user == 6:
                    delete_input = input("Are you sure you want to delete you account? (Y/N)")

                    if delete_input == 'Y' or delete_input == 'y':
                        name = input("Enter account name to be deleted: ")
                        Bank_object.delete_account(name, IBAN, pin)
                        print("Account deleted successfully.")

                    if delete_input == 'N' or delete_input == 'n':
                        break
                        # else just logout from the system
                elif login_user == 7:
                    break

    # if user input is 2, it will ask you to create a new account by calling the function login from class Bank
    # signing up to main account
    if user == 2:
        print("Creating a new  Account....")
        name = input("Enter Name: ")
        IBAN = input("Enter IBAN Number: ")
        pin = input("Enter 4 digit PIN: ")
        age = int(input("Enter age: "))
        Bank_object.register(name, IBAN, pin, age)

    # logging to Savings Account
    if user == 3:
        print("\nLogging to Savings Account.....")
        name_1 = input("Enter name: ")
        IBAN_1 = input("Enter IBAN: ")
        pin_1 = int(input("Enter 4 digit PIN: "))
        Bank_object_1.login_1(name_1, IBAN_1, pin_1, )
        # If the user login is true for savings it will log in successfully and perform the following operations
        while True:
            if Bank_object_1.loggedin_1:
                print("\n1.Add amount")
                print("2.Check Balance")
                print("3.Withdraw money")
                print("4.Tranfer Amount")
                print("5.Close account")
                print("6.Logout")
                login_user_1 = int(input())

                # takes user input under logged in status
                if login_user_1 == 1:
                    print("Balance = €", Bank_object_1.cash_1)
                    amount_1 = int(input("Enter amount: "))
                    Bank_object_1.add_cash_1(amount_1)
                    print("\n1.back menu")
                    print("2.Logout")
                    # then you can either go back to menu or log out
                    choose = int(input())
                    if choose == 1:
                        continue
                    elif choose == 2:
                        break

                # if user input is 2, it will show current amount by using the class Bank_object.cash
                elif login_user_1 == 2:
                    print("Balance = €", Bank_object_1.cash_1)
                    print("\n1.back menu")
                    print("2.Logout")
                    choose = int(input())
                    if choose == 1:
                        continue
                    elif choose == 2:
                        break

                # if user input is 3, it will ask ask how much to withdraw then performs the withdraw_money function
                elif login_user_1 == 3:
                    print("Balance = €", Bank_object_1.cash_1)
                    money_1 = int(input("Enter amount: "))
                    Bank_object_1.withdraw_money_1(money_1)
                    print("\n1.back menu")
                    print("2.Logout")
                    choose = int(input())
                    if choose == 1:
                        continue
                    elif choose == 2:
                        break
                # if user input is 4, it will ask how much to transfer then ask for the receiver name and IBAN
                elif login_user_1 == 4:
                    print("Balance = €", Bank_object_1.cash_1)
                    amount_1 = int(input("Enter amount: "))
                    if amount_1 >= 0 and amount_1 <= Bank_object_1.cash_1:
                        name_1 = input("Enter person name: ")
                        IBAN_1 = input("Enter IBAN: ")
                        Bank_object_1.Transfer_cash_1(amount_1, name_1, IBAN_1)
                        print("\n1.back menu")
                        print("2.Logout")
                        choose = int(input())
                        if choose == 1:
                            continue
                        elif choose == 2:
                            break
                    elif amount_1 < 0:
                        print("Enter please correct value of amount")

                    elif amount_1 > Bank_object_1.cash_1:
                        print("Not enough balance")

                # if user input is 5, then you can delete account
                elif login_user_1 == 5:
                    delete_input_1 = input("Are you sure you want to delete you account? (Y/N)")

                    if delete_input_1 == 'Y' or delete_input_1 == 'y':
                        name_1 = input("Enter account name to be deleted: ")
                        Bank_object_1.delete_account(name_1, IBAN_1, pin_1)
                        print("Account deleted successfully.")

                    if delete_input_1 == 'N' or delete_input_1 == 'n':
                        break

                elif login_user_1 == 6:
                    break

    # signing up to Savings Account
    if user == 4:
        print("Creating a new Savings Account....")
        name_1 = input("Enter Name: ")
        IBAN_1 = input("Enter IBAN Number: ")
        pin_1 = input("Enter 4 digit PIN: ")
        age_1 = int(input("Enter age: "))
        Bank_object_1.register_1(name_1, IBAN_1, pin_1, age_1)

        # logging into Checking account
    if user == 5:
        print("\nLogging to new Checking Account.....")
        name_2 = input("Enter name: ")
        IBAN_2 = input("Enter IBAN: ")
        pin_2 = int(input("Enter 4 digit PIN: "))
        Bank_object_2.login_2(name_2, IBAN_2, pin_2, )
        # if details are true then login
        while True:
            if Bank_object_2.loggedin_2:
                print("\n1.Add amount")
                print("2.Check Balance")
                print("3.Tranfer Amount")
                print("4.Close account")
                print("5.Logout")
                login_user_2 = int(input())

                # if input is 1, then add amount
                if login_user_2 == 1:
                    print("Balance = €", Bank_object_2.cash_2)
                    amount_2 = int(input("Enter amount: "))
                    Bank_object_2.add_cash_2(amount_2)
                    print("\n1.back menu")
                    print("2.Logout")
                    choose = int(input())
                    if choose == 1:
                        continue
                    elif choose == 2:
                        break

                # if input is 2, then show current cash
                elif login_user_2 == 2:
                    print("Balance = €", Bank_object_2.cash_2)
                    print("\n1.back menu")
                    print("2.Logout")
                    choose = int(input())
                    if choose == 1:
                        continue
                    elif choose == 2:
                        break

                # if input 3, then transfer amount wi th verifying IBAN and name
                elif login_user_2 == 3:
                    print("Balance = €", Bank_object_2.cash_2)
                    amount_2 = int(input("Enter amount: "))
                    if amount_2 >= 0 and amount_2 <= Bank_object_2.cash_2:
                        name_2 = input("Enter person name: ")
                        IBAN_2 = input("Enter IBAN: ")
                        Bank_object_2.Transfer_cash_2(amount_2, name_2, IBAN_2)
                        print("\n1.back menu")
                        print("2.Logout")
                        choose = int(input())
                        if choose == 1:
                            continue
                        elif choose == 2:
                            break
                    elif amount_2 < 0:
                        print("Enter please correct value of amount")

                    elif amount_2 > Bank_object_2.cash_2:
                        print("Not enough balance")

                # if user input is 4, then delete account
                elif login_user_2 == 4:
                    delete_input_1 = input("Are you sure you want to delete you account? (Y/N)")

                    if delete_input_1 == 'Y' or delete_input_1 == 'y':
                        name_2 = input("Enter account name to be deleted: ")
                        Bank_object_2.delete_account(name_2, IBAN_2, pin_2)
                        print("Account deleted successfully.")

                    if delete_input_1 == 'N' or delete_input_1 == 'n':
                        break
                        # if input is 5, then logout
                elif login_user_2 == 5:
                    break

    # signing up to Checking Account
    if user == 6:
        print("Creating a new Checking Account....")
        name_2 = input("Enter Name: ")
        IBAN_2 = input("Enter IBAN Number: ")
        pin_2 = input("Enter 4 digit PIN: ")
        age_2 = int(input("Enter age: "))
        Bank_object_2.register_2(name_2, IBAN_2, pin_2, age_2)