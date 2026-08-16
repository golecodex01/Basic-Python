
Mobileprice =int(input("Enter Mobile Price : "))
Downpayment = int(input("Enter DownPayment : "))
Interestrate = int(input("Enter Interest Rate  : "))
Months = int(input("Enter Months  : "))

RemainingAmount=Mobileprice-Downpayment
interest=RemainingAmount*Interestrate/100
totalwithIntrest=interest+RemainingAmount
monthlyEMI=totalwithIntrest/Months 

print("Remaining Amount: ",RemainingAmount)
print("Total with Interest : ",totalwithIntrest)
print("Monthly EMI : ",monthlyEMI)









