    count=0
    for i in range(1,num+1):
        if num%i==0:
            count=count+1
    if count==2:
        return "prime number"
    else:
        return "not a prime number"


def reverse(num,sum=0):
    temp=num
    while num>0:
        r=num%10
        sum=sum*10+r
        num=num//10
    return sum



def fact(num):
    fact=1
    for i in range(1,num+1):
        fact=fact*i
    return fact

def factors(num):
    res=[]
    for i in range(1,num+1):
        if num%i==0:
            res.append(i)
    return res

while True:
    print("1. Check Perfect Number")
    print("2. Check Prime Number")
    print("3. Find Reverse of a Number")
    print(" 4. Calculate Factorial")
    print("5. Display Factors of a Number")
    print("6. Exit")
    choice=int(input("enter your your choice"))
    match choice:
        case 1:
            num=int(input("enter a number"))
            if perfect(num):
                print(num,"number is perfect")
            else:
                print(num, "number is not perfect")