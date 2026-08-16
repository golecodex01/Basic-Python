num1=int(input("Enter 1st Number :"))

nextpalin=num1+1

prepalin=num1-1

while True:
    temp=nextpalin
    rev=0
    while temp>0:
        rev=rev*10+temp%10
        temp=temp//10
    if rev==nextpalin:
        nextpalin=rev
        break
    nextpalin=nextpalin+1



while True:
    temp1=prepalin
    rev1=0
    while temp1>0:
        rev1=rev1*10+temp1%10
        temp1=temp1//10
    if rev1==prepalin:
        prepalin=rev1
        break
    prepalin=prepalin-1

print("Previous Palindrome  ",prepalin)
print("Next Palindrome ",nextpalin)
print("Difference ",nextpalin-prepalin)

