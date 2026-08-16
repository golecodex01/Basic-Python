num1=int(input("Enter 1st Number :"))

nextpalin=num1+1

while True:
    temp=nextpalin
    rev=0
    while temp>0:
        rev=rev*10+temp%10
        temp=temp//10
    if rev==nextpalin:
        print("Next Palindrome : ",nextpalin)
        break
    nextpalin=nextpalin+1

