'''1.

=========================================
ONLINE SHOPPING CART
====================

A shopping website stores purchased products in a dictionary where:
Key = Product Name
Value = Quantity Purchased

Write a program to:

* Accept a dictionary from the user.
* Calculate and display the total quantity of products purchased.

Sample Input:
{"Laptop":2,"Mouse":3,"Keyboard":1}

Sample Output:
Total Quantity = 6

---
'''
n=int(input("Enter number of Products "))
d={}
for i in range(n):
    key=input("Enter Product Name : ")
    value=int(input("Enter product Quantity : "))
    d[key]=value

s=sum(d.values())
print("Total Quantity ",s)
