num=int(input("Enter a NUmber : "))
i=1
while i<=num:
    if i%3==0 and i%5==0:
        print(i ,end=" ")
    i=i+1