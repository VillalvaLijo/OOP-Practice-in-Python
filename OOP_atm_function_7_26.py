# -*- coding: utf-8 -*-
"""
ATM OOP Project 
7/26/2019
Samuel Villalva Lijo
"""
class Account(object):
            
    def __init__(self):
        self.owner = input("What is your name?: ")
        self.balance = float(input("What is the balance of your account?: "))
                    
    def print_balance(self):
        
        print(f"You  balance is: {self.balance}")
        
    def deposit(self, d_amount):

        if d_amount > 0:
            self.balance += d_amount
            self.print_balance()
    
    def withdrawl(self, w_amount):
        if w_amount > 0 and w_amount <= self.balance:
            self.balance -= w_amount
            self.print_balance()
        else:
            print("Invalid response for a withdrawal")


class Menu(object):


    def __init__(self, accountname):
        self.accountname = accountname

    def menu_readout(self):
        print("\nWould you like to see your balance, make a deposit or make a withdrawl?")
        choice = (input("Enter your choice: B for balance, D for deposit, or W for withdrawl: ")).upper()
        if choice == 'B':
            print(f"\nyour balance is what it is") 
        elif choice == 'D':
            print("\nyou choose deposit")
            deposit_amount = int(input("Enter how much you would like to deposit: "))
            self.accountname.deposit(deposit_amount)
        elif choice == 'W':
            print("\nYou choose withdrawl")
            withdrawl_amount = int(input("Enter how much you would like to withdrawl: "))
            self.accountname.withdrawl(withdrawl_amount)                         
        else:
            print("\nInvalid response.")
            self.menu_readout()
    
        
    


account1 = Account()
Menu(account1).menu_readout()
