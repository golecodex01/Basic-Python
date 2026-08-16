num=int(input("Enter a number "))
count=0
if num<=3:
    print("Not Composite  Number ")
else:
    i=1
    while i<=num//2:
        if num%i==0:
            count=count+1          
        i=i+1
    if count>1:
        print("Composite Number")
    else:
        print("Not Composite Number ")
