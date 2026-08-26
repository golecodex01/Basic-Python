'''
4.

=========================================
STUDENT GRADE ANALYSIS
======================

Store student marks in a dictionary.

students = {
"Ajay":78,
"Ravi":92,
"Neha":85,
"Aman":65
}

Write a program to:

* Find the student with highest marks.
* Find the student with lowest marks.

Sample Output:
Highest Marks : Ravi 92
Lowest Marks : Aman 65

---

'''

n=int(input("Enter Number of Students : "))

d={}

for i in range(n):
    key=input("Enter Student Name : ")
    value=int(input("Enter Student Marks : "))
    d[key]=value

highestmarks=max(d,key=d.get)
minimum=min(d,key=d.get)

print(highestmarks,"got Highest : ",d[highestmarks])
print(minimum,"got Lowest : ",d[minimum])


    
