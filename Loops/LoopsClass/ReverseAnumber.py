num=int(input("ENter A Number :"))
rev=0
while num>0:
    digit=num%10
    rev=digit+rev*10
    num=num//10
print(rev)

print("Way 2 ")


num2=input("ENter A Number :")
rev2=""
for i in num2:
    rev2=i+rev2
print("Reversed NUmber is ",rev2)