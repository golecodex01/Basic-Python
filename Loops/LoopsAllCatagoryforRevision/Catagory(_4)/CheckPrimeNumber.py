num=int(input("Enter a number "))
if num<=1:
    print("Not Prime Number ")
else:
    i=2
    while i<=num//2:
        if num%i==0:
            print("Not Prime Number ")
            break
        i=i+1
    else:
        print("Prime NUmber ")