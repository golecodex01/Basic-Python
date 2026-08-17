n=int(input("Enter number of products: "))
products=[]

for i in range(n):
    product_id,product_name,price=input().split()
    products.append((product_id,product_name,int(price)))

print("All Products:")
for p in products:
    print(p)

costliest=products[0]
cheapest=products[0]
total=0

for p in products:
    total=total+p[2]

    if p[2]>costliest[2]:
        costliest=p

    if p[2]<cheapest[2]:
        cheapest=p

average=total/n

print("Costliest Product:")
print(costliest)

print("Cheapest Product:")
print(cheapest)

print("Average Price:")
print(average)

print("Products Above ₹50,000:")
for p in products:
    if p[2]>50000:
        print(p)