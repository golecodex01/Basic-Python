num=int(input("Enter a Number : "))
nextnum=num+1

while True:
    i=1
    count=0
    while i<=nextnum:
        if nextnum%i==0:
            count=count+1
        i=i+1
    if count==2:
        print("Next Prime , ",nextnum)
        break
    nextnum=nextnum+1

        