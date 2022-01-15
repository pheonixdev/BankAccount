# BankAccount
Python program to design and implement two classes in Python: BasicAccount and PremiumAccount.

## Variables:
The variables of the classes are described as follows:

* [name](#name) – the account holder's name.

* [acNum](#acNum) – the number of the account. This should be “serial”, meaning that the first account to be created should have number 1, the second account to be created should have number 2, and so on.

* [balance](#balance) – The balance (in pounds) of the account.

* [cardNum](#cardNum) – The card number, which should be a string containing a 16-digit number (you should import and use the random module for this).

* [cardExp](#cardExp) - a tuple, where the first element is an integer corresponding to the month and the second element is 2-digit year. Eg: 03/23 represents March 2023. (you should import and use the datetime module for this).

* [overdraft](#overdraft) – a Boolean variable, which is True if the account has an overdraft, and False if  does not.

* [overdraftLimit](#overdraftLimit) – The amount that the account can go overdrawn by.

## Methods:
The methods are as follows:

* [__init__](#__init__)(self, str, float) : Initialiser giving the account name and opening balance.

* [__init__](#__init__)(self, str, float, float) : Initialiser giving the account name, opening balance, and overdraft limit (0 or above).

* [deposit](#deposit)(self, float) : Deposits the stated amount into the account, and adjusts the balance appropriately. Deposits must be a positive amount.

* [withdraw](#withdraw)(self, float) : Withdraws the stated amount from the account, prints a message of “<Name> has withdrawn £<amount>. New balance is £<amount>”.
If an invalid amount is requested, then the following message should be printed, and the method should then terminate: “Can not withdraw £<amount>".
An amount is considered to be invalid if it is larger than the balance for (normal) accounts and if it is larger than the balance + overdraft limit for premium accounts.

* [getAvailableBalance](#getAvailableBalance)(self) : Returns the total balance that is available in the account as a float. It should also take into account any overdraft that is available.

* [getBalance](#getBalance)(self) : Returns the balance of the account as a float. If the account is overdrawn, then it should return a negative value.

* [printBalance](#printBalance)(self) : Should print to screen in a sensible way the balance of the account. If an overdraft is available, then this should also be printed and it should show how much overdraft is remaining.
  
* [getName](#getName)(self) : Returns the name of the account holder as a string.

* [getAcNum](#getAcNum)(self) : Returns the account number as a string.

* [issueNewCard](#issueNewCard)(self) : Creates a new card number, with the expiry date being 3 years to the month from now (e.g., if today is 1/12/21, then the expiry date would be (12/24)).

* [closeAccount](#closeAccount)(self) : To be called before deleting of the object instance. Returns any balance to the customer (via the withdraw method) and returns True.
Returns False if the customer is in debt to the bank, and prints message “Can not close account due to customer being overdrawn by £<amount>”.

* [setOverdraftLimit](#setOverdraftLimit)(self, float) : Sets the overdraft limit to the stated amount
