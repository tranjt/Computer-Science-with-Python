# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.

aString = s[startIndex: curIndex]
"""

def balanceCalc(balance, annualInterestRate):
    """
     Calculates the minimum fixed monthly payment
     needed in order pay off a credit card balance within 12 months. 
     Args:
         balance - the outstanding balance on the credit card
         annualInterestRate - annual interest rate as a decimal
    """
    monthlyInterestRate = annualInterestRate / 12.0
    minFixedMonthlyPayment = 10     
    updatedBalance = balance
    
    
    while True:
        """
        Search for minFixedMonthlyPayment where balance after 12 month is equal or less than 0
        """
    
        for month in range(12):
            monthlyUnpaidBalance = updatedBalance - minFixedMonthlyPayment
            updatedBalance = monthlyUnpaidBalance + monthlyInterestRate *  monthlyUnpaidBalance
        
        if updatedBalance <= 0:
            return minFixedMonthlyPayment
        else:
            updatedBalance = balance
            minFixedMonthlyPayment += 10

        
balance = 3329
annualInterestRate = 0.2
minMonthlyPayment = round(balanceCalc(balance, annualInterestRate))
print("Lowest Payment: " + str(minMonthlyPayment))        

        
        
"""
use brute force
Monthly interest rate= (Annual interest rate) / 12.0
Minimum monthly payment = (Minimum monthly payment rate) x (Previous balance)
Monthly unpaid balance = (Previous balance) - (Minimum monthly payment)
Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance) 

P = (R/(1-(1+R)**-N)) *Loan

"""

"""
p(12) = balance = 0
p(11) = minFixedMonthlyPayment + p(11-1)

Monthly interest rate = (Annual interest rate) / 12.0
Monthly unpaid balance = (Previous balance) - (Minimum fixed monthly payment)
Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance) 

P(12) = monthlyUnpaidBalance + monthlyInterestRate * (P(11) - minFixedMonthlyPayment)
P(11) = monthlyUnpaidBalance + monthlyInterestRate * (P(10) - minFixedMonthlyPayment)
P(10) = monthlyUnpaidBalance + monthlyInterestRate * (P(9) - minFixedMonthlyPayment)
P(9) = monthlyUnpaidBalance + monthlyInterestRate * (P(8) - minFixedMonthlyPayment)
P(8) = monthlyUnpaidBalance + monthlyInterestRate * (P(7) - minFixedMonthlyPayment)
P(7) = monthlyUnpaidBalance + monthlyInterestRate * (P(6) - minFixedMonthlyPayment)
P(6) = monthlyUnpaidBalance + monthlyInterestRate * (P(5) - minFixedMonthlyPayment)
P(5) = monthlyUnpaidBalance + monthlyInterestRate * (P(4) - minFixedMonthlyPayment)
P(4) = monthlyUnpaidBalance + monthlyInterestRate * (P(3) - minFixedMonthlyPayment)
P(3) = monthlyUnpaidBalance + monthlyInterestRate * (P(2) - minFixedMonthlyPayment)
P(2) = monthlyUnpaidBalance + monthlyInterestRate * (P(1) - minFixedMonthlyPayment)
P(1) = monthlyUnpaidBalance + monthlyInterestRate * (P(0) - minFixedMonthlyPayment)


P(12) = P(11) - minFixedMonthlyPayment + monthlyInterestRate * (P(11) - minFixedMonthlyPayment)
P(12) = (P(11) - minFixedMonthlyPayment)(1+monthlyInterestRate)
P(12) = 

P(12) = 0
P(0) = balance

"""
