bsillAmount=int(input("Enter Total Bill Amount :"))
GST=int(input("Enter GST percent  :"))
ServiceCharge=int(input("Enter Service Charge :"))
freind=int(input("Enter Numbers of Freinds : "))

totalpercent=GST+ServiceCharge
tax=billAmount*totalpercent/100
finalBill=billAmount+tax
each=finalBill/freind

print("Final Bill : ",finalBill)
print("Each to Pay : ",each)

