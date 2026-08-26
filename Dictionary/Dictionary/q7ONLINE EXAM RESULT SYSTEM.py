'''
7.
=========================================
ONLINE EXAM RESULT SYSTEM
=========================

Store student marks in a dictionary.

results = {
"Ajay":88,
"Ravi":45,
"Neha":76,
"Aman":39
}

Write a program to:

* Display names of students who passed.
  (Passing Marks = 50)

Sample Output:
Ajay
Neha
Ravi

---

'''
n=int(input("Enter Number of Students "))
d={}
for i in range(n):
    key=input("Enter Student Name : ")
    value=int(input("Enter Student Marks "))
    d[key]=value

for k,v in d.items():
    if v>50:
        print(k)