# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
class Account(object):
            
    def __init__(self):
        self.owner = input("What is your name?: ")
        self.balance = float(input("What is the balance of your account?: "))
        #self.accountname = accountname
            
    def print_balance(self):
        #return(self.balance)
        print(f"Your balance is: {self.balance}")
        
    def deposit(self, d_amount):

        if d_amount > 0:
            self.balance += d_amount
            self.print_balance()
         #   recipt_YN = (input("Would you like a recipt? Y/N: ")).upper()

        #    if recipt_YN == 'Y':
        #        print("Your new balance is {0}.".format(self.balance))
        #    elif 'N':
        #        print("Good Bye")
        #    else:
        #        print("Invalid Response") #figure out how to make this re-loop
        #else:                                    #back to ask wether they want a recipt or not
       #     print("Invalid Entry for a deposit.")
    
    def withdrawl(self, w_amount):
        if w_amount > 0 and w_amount <= self.balance:
            self.balance -= w_amount
            #print(f"Your new balance is: {self.balance}") #printing balance works here, but not when I call print balance
            self.print_balance()
            #recipt_yn = (input("Would you like a recipit? Y/N: ")).upper()

            #if recipt_yn == 'Y':
            #    print("Your new balance is {0}.".format(self.balance))
            #elif recipt_yn == 'N':
            #    print("Good Bye")
            #else:
            #    print("Invalid response") #Make a recursion back to the
                                            #reciept question
        else:
            print("Invalid response for a withdrawal")


class Menu(object):


    def __init__(self, accountname):
    #def __init__(self, owner, accountname, balance):
        #self.owner = owner
        #self.balance = balance
        self.accountname = accountname

    def menu_readout(self):
        print("\nWould you like to see your balance, make a deposit or make a withdrawl?")
        choice = (input("Enter your choice: B for balance, D for deposit, or W for withdrawl: ")).upper()
        if choice == 'B':
            print(f"\nyour balance is what it is") #{Account(accountname).pr")int_balance}.")
        elif choice == 'D':
            print("\nyou choose deposit")
            deposit_amount = int(input("Enter how much you would like to deposit: "))
            self.accountname.deposit(deposit_amount)
        elif choice == 'W':
            print("\nYou choose withdrawl")
            withdrawl_amount = int(input("Enter how much you would like to withdrawl: "))
            self.accountname.withdrawl(withdrawl_amount)                         #this function works, is self.accountname just a place holder for a variable?
        else:
            print("\nInvalid response.")
            self.menu_readout()
    
        
    


account1 = Account()
Menu(account1).menu_readout()
#withdrawl_amount = int(input("Enter how much would you like to withdrawl: "))
#account1.withdrawl(withdrawl_amount) #not calling function and I'm not sure why



#w_or_d = (input("Would you like to make a deposit or take a with drawl? W/D: ")).upper()
#if w_or_d == 'W': 
#    withdrawl_amount = float(input("How much would you like to withdrawl?:"))
#    account1.withdrawl(withdrawl_amount)
#elif w_or_d == 'D':
#    deposit_amount = float(input("How much would you like to deposit?: "))
#    account1.deposit(deposit_amount)
#else:
#    print("Invalid Response")
