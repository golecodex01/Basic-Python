'''
11.

=========================================
PRODUCT SALES ANALYSIS
======================

sales = [
"Mobile",
"Laptop",
"Mobile",
"Tablet",
"Laptop",
"Mobile"
]

Write a program to:

* Count sales of each product.
* Display products in sorted order.

Sample Output:
Laptop : 2
Mobile : 3
Tablet : 1

---
'''

product=list(input("Enter Items : ").split())
d={}
for i in product:
    if i in d:
        d[i]+=1
    else:
        d[i]=1

for k,v in sorted(d.items()):
    print(k,":",v)