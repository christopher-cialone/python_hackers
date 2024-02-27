from abc import ABC, abstractmethod
# defne an abstract class called Bank
class Bank(ABC):
    # define a method called basicinfo() inside Bank class
    def basicinfo(self):
        # print a statement 
        print("This is a generic bank")
        # return a string indicating generic bank and balance 0
        return "Generic bank: 0"
    
    # define an abstract method called withdraw() inside Bank class
    @abstractmethod
    def withdraw(self, amount):
        pass # placeholder for abstract method - no implementation

# define a subclass called Swiss inheriting from Bank class
class Swiss(Bank):
    # define constructor method to initialize the Swiss bank object
    def __init__(self):
        # initialize the balance to 1000 when Swiss bank object is created
        self.bal = 1000

# override the basicinfo() method from Bank class
    def basicinfo(self):
        # print a statement
        print("This is a Swiss Bank")
        # return a string indicating Swiss bank and current balance
        return "Swiss Bank: {}".format(self.bal)
    
    # override the withdraw() method from Bank class
    def withdraw(self, amount):
        # check if withdraw amiunt is less than or equal to balance
        if amount <= self.bal:
            # deduct the withdrawl amoiunt from balance
            self.bal -= amount
            # print the withdrawn amount
            print("Withdrawn amount:", amount)
            # print new balance after withdrawl
            print("New balance:", self.bal)
            # return new balance
            return self.bal
        else:
            # if withdrawl amount exceeds balance print message
            print("Insufficient Funds")
            # return current balance without deducting any amount
            return self.bal
# testing the Swiss bank class
# create an instance of the Swiss bank class                
swiss_bank = Swiss()
# print basic info about the Swiss bank
print(swiss_bank.basicinfo())
# withdraw an amount from the Swiss bank and print new balance
print(swiss_bank.withdraw(200))
