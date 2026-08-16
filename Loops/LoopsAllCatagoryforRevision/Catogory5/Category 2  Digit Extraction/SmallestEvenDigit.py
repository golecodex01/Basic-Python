num=int(input("enter a Number : "))
small=10
while num>0:
    digit=num%10
    if digit%2==0:
        if digit<small:
            small=digit
    num=num//10

if small==10:
    print("No even Number is Found in DIgit ")
else:
    print("Smallest Even Number is : ",small)