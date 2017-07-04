# -*- coding: utf-8 -*-



def creditCalc(balance, annualInterestRate, monthlyPaymentRate):
    """
    Calculate the credit card balance after one year if a person only pays 
    the minimum monthly payment required by the credit card company each month.
    Args:
        balance - the outstanding balance on the credit card
        annualInterestRate - annual interest rate as a decimal
        monthlyPaymentRate - minimum monthly payment rate as a decimal    
    """
    
    monthlyInterestRate = annualInterestRate / 12.0
    
    for month in range(12):
        minMonthlyPayment = monthlyPaymentRate *  balance
        monthlyUnpaidBalance = balance - minMonthlyPayment
        updatedBalanceEachMonth = monthlyUnpaidBalance + (monthlyInterestRate * monthlyUnpaidBalance)
        balance = round(updatedBalanceEachMonth, 2)        

    return balance

remainBalance = creditCalc(balance, annualInterestRate, monthlyPaymentRate)
print("Remaining balance: " + str(remainBalance))