price = 30000
downpayment = 5000
interest = 10
months = 10

remaining = price - downpayment
total = remaining + (remaining * interest / 100)
emi = total / months

print("Remaining Amount =", remaining)
print("Total with Interest =", total)
print("Monthly EMI =", emi)