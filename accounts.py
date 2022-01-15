import random
import datetime

class BasicAccount:
    """A class to represent the basic account of a bank.

    Attributes:
        name (str): name of the account holder
        accNum (int): account number of the account holder
        balance (float): balance on opening an account
        cardNum (str): number of the card issued
        cardExp (tuple(int,int)): expiry date of the card issued (mm,yy)
        accountClose (boolean): checks whether account closure is possible
        overdraft (boolean): checks for overdraft
        overdraftLimit (float): maximum overdraft amount permissible
        
    """
    acNum = 0   # declared globally to increment account number when a new instance is created
    def __init__(self,acName,openingBalance):
        """Constructor to initialize the BasicAccount class.

        Args:
            acName (str): name of the account holder
            openingBalance (float): balance on opening an account
        """
        self.name = acName
        BasicAccount.acNum += 1
        self.accNum = BasicAccount.acNum
        self.balance = openingBalance
        self.cardNum = "Not Present"
        self.cardExp = (0,0)
        self.accountClose = False
        self.overdraft = False  # set to False since basic account does not have overdraft
        self.overdraftLimit = 0
        # to set the balance to zero in case a non number is entered
        if (isinstance(self.balance,float) or isinstance(self.balance,int) == True) and self.balance >= 0:
            self.balance = float(self.balance)
        else:
            print("Opening balance set to zero for %s" %acName)
            self.balance = 0.00
            
    def __str__(self):
        """String representation of the account details of Basic Account.

        Returns:
            str : name, account number, balance, card number and expiry date
        """
        return "Hi {self.name}(account number:{self.accNum}) \n Your balance: £{self.balance} \n Your card number: {self.cardNum} and expiry date: {self.cardExp}".format(self=self)
    
    def deposit(self, amount):
        """Function to deposit money in the bank account.

        Args:
            amount (float): amount of money to be deposited
        """
        if amount < 0:
            print("Negative amount is unacceptable.")
        else:
            self.balance += amount
        if self.overdraft == False: 
            print("Deposited £%.2f. Your total balance is now £%.2f"%(amount,self.balance))
        else:
            print("Deposited £%.2f. Your total avaliable balance is now £%.2f"%(amount,self.balance + self.overdraftLimit))

    def withdraw(self,amount):
        """Function to withdraw money from the bank account.

        Args:
            amount (float): amount of money to be withdrawn
        """
        if self.overdraft == False: # for basic account
            if amount > self.balance:
                print("Can not withdraw £%.2f"%(amount))
            else:
                self.balance -= amount
                print("You have withdrawn £%.2f. New balance is £%.2f"%(amount,self.balance))
        else:   # for premium account
            overdraftAmount = self.overdraftLimit
            moneyAvailable = self.balance + overdraftAmount
            if (amount > moneyAvailable):
                print("Can not withdraw £%.2f"%(amount))
            else:
                self.balance -= amount
                if self.balance < 0:    # overdraft limit is updated if balance is less than zero
                    self.overdraftLimit = overdraftAmount + self.balance
                print("You have withdrawn £%.2f. New balance is £%.2f with an available overdraft of £%.2f"%(amount,self.balance,self.overdraftLimit))
                                              
    def getAvailableBalance(self):
        """Function to get the available balance of the account.

        Returns:
            float : the total balance that is available in the account
        """
        return float(self.balance)

    def getBalance(self):
        """Function to get the balance in the account.

        Returns:
            float : the balance of the account
        """
        return float(self.balance)

    def printBalance(self):
        """Function to print the balance of the account to screen.
        """
        print("Your current balance is:£%.2f. Basic account has no overdraft option"%self.balance)

    def getName(self):
        """Function to get the name of the account holder.

        Returns:
            str : name of the account holder
        """
        return self.name

    def getAcNum(self):
        """Function to get the account number of the account holder.

        Returns:
            str : account number
        """
        return str(self.accNum)

    def issueNewCard(self):
        """Function to issue a new card to the account holder with 16 digit card number and with expiry date three years from now.
        """
        random_numbers = []
        # random 16 digits are added to the list and joined to get the card number as a string
        for i in range(16):
            random_numbers.append(random.randint(0, 9))
        self.cardNum = ''.join(map(str, random_numbers))
        print("Your card number is %s %s %s %s" %(self.cardNum[0:4],self.cardNum[4:8],self.cardNum[8:12],self.cardNum[12:16])) # to display the card number as per convention
        today = datetime.datetime.now()
        expiryMonth = today.month
        expiryYear = str(today.year + 3)
        expiryYear = int(expiryYear[2:])    # to get the last two digits of the year
        self.cardExp = expiryMonth, expiryYear
        print("Card Expiry date is ", self.cardExp)

    def closeAccount(self):
        """Function to close the account if balance is positive.

        Returns:
            bool : account closing possible if True
        """
        if(self.balance < 0):
            print("Can not close account due to customer being overdrawn by £%s" %(self.balance))
            self.accountClose = False
        else:
            self.withdraw(self.balance) # to withdraw all the money from account
            self.accountClose = True
        return self.accountClose
    
class PremiumAccount(BasicAccount):
    """A class to represent the premium account of a bank.

    Attributes:
        name (str): name of the account holder
        overdraftLimit (float): maximum overdraft amount permissible
        balance (float): balance on opening an account
        overdraft (boolean): checks for overdraft
        
    """
    def __init__(self,acName,openingBalance,initialOverdraft):
        """Constructor to initialize the PremiumAccount class.

        Args:
            acName (str): name of the account holder
            openingBalance (float): balance on opening an account
            initialOverdraft (float): overdraft limit while opening an account
        """
        super().__init__(acName,openingBalance)
        self.name = acName
        self.overdraftLimit = initialOverdraft
        self.balance = openingBalance
        self.overdraft = True   # set to True since premium account has overdraft

    def __str__(self):
        """String representation of the account details of Premium Account.

        Returns:
            str : name, account number, balance, overdraft limit, card number and expiry date
        """
        return "Hi,{self.name}(account number:{self.accNum}) \nYour balance: £{self.balance} with an overdraft limit: £{self.overdraftLimit} \nYour card number: {self.cardNum} and expiry date: {self.cardExp}".format(self=self)

    def setOverdraftLimit(self, newLimit):
        """Function to set the overdraft limit of the account.

        Args:
            newLimit (float): new overdraft limit to be set
        """
        self.overdraftLimit = newLimit

    def getAvailableBalance(self):
        """Function to get the available balance of the account including overdraft.

        Returns:
            float : total balance including overdraft
        """
        return float(self.balance + self.overdraftLimit)

    def printBalance(self):
        """Function to print the total balance (including overdraft) of the account to screen.
        """
        print("Current Balance available is:£%.2f.The overdraft remaining is £%.2f" %((self.balance+self.overdraftLimit),self.overdraftLimit))

    def closeAccount(self):
        """Function to close the account if the balance  is positive
        """
        return BasicAccount.closeAccount(self) # calls the closeAccount function from the parent class

def main():
    account1 = BasicAccount("Thankappan", -100)
    account2 = PremiumAccount("Sasi", 1000, 200)
    account3 = BasicAccount("Soman", 350)
    account4 = PremiumAccount("Pushpan", 100, 300)
    # print(account1.getAcNum())
    # print(account3.getAcNum())
    # account1.deposit(-10)
    # account2.issueNewCard()
    # account2.closeAccount()
    # account3.deposit()
    # account3.printBalance()
    # print(account3.withdraw(360))
    # print(account4.getBalance())
    # print(account4.getAvailableBalance())
    # print(account4.closeAccount())

if __name__ == "__main__":
    main()