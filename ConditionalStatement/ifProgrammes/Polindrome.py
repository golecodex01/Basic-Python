num=input("Enter a NUmber ")
rev=""
for i in range(len(num)-1,-1,-1):
    rev=rev+num[i]
if num==rev:
    print("Polindrome")
else:
    print("Not Polindrome")