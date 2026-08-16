n=int(input("Enter a Number :"))
i=1
while i<=n:
    j=n
    while j>=i:
        print(j ,end=" ")
        j=j-1

    print()
    i=i+1