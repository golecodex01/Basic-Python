p=int(input("Principle ="))
r=int(input("Rate ="))
t=int(input("Time ="))

si=p*r*t/100
amount=p*(1+r/100)**t
print("Amount =",amount)
ci=amount-p
print("Compound Intrest =",ci)
