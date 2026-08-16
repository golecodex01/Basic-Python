amount=int(input("Amount ="))

hundred=amount//100
remender=amount-hundred*100
fifty=remender//50
remender=remender-fifty*50

ten=remender//10
print("100*",hundred)
print("50*",hundred)
print("10*",hundred)

