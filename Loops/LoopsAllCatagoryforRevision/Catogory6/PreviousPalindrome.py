num1=int(input("Enter 1st Number :"))

prepalin=num1-1

while True:
    temp=prepalin
    rev=0
    while temp>0:
        rev=rev*10+temp%10
        temp=temp//10
    if rev==prepalin:
        print("Previous  Palindrome : ",prepalin)
        break
    prepalin=prepalin+1

