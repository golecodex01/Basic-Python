n=int(input("Enter N : "))
count=1
for i in range(1,n+1):
    for i in range(1,i+1):
        print(count ,end=" ")
        count=count+1
    print()
