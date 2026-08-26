'''
12.

=========================================
ONLINE FOOD DELIVERY ANALYSIS
=============================

orders = [
"Pizza",
"Burger",
"Pizza",
"Pasta",
"Burger",
"Pizza",
"Pasta"
]

Write a program to:

* Count orders of each food item.
* Find the most ordered item.

Sample Output:
Pizza : 3
Burger : 2
Pasta : 2

Most Ordered : Pizza

---
'''

items=list(input("Enter Items : ").split())

d={}

for i in items:
    if i in d:
        d[i]+=1
    else:
        d[i]=1

for k,v in d.items():
    print(k,":",v)




    

