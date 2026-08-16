n=int(input("Enter a Number : "))
pro=1
for i in range(1,n+1):
    if i%2!=0:
        pro=pro*i
print("product",pro)