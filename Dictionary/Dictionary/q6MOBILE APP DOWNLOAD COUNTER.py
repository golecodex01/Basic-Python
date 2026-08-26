'''
6.

=========================================
MOBILE APP DOWNLOAD COUNTER
===========================

Downloads received from different cities:

cities = ["Indore","Bhopal","Indore","Pune","Delhi","Pune","Indore"]

Write a program to:

* Count downloads city-wise.
* Display city with maximum downloads.

Sample Output:
{'Indore':3,'Bhopal':1,'Pune':2,'Delhi':1}
Most Downloads : Indore

---


'''
cities=list(input("Enter Cities : ").split())
d={}
for i in cities:
    if i in d:
        d[i]+=1
    else:
        d[i]=1

maxi=max(d,key=d.get)

print(d)
print("Most Dounloads App : ",maxi)