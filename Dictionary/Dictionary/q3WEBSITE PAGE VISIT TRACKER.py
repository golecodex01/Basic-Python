'''
3.

=========================================
WEBSITE PAGE VISIT TRACKER
==========================

A website records page visits.

pages = ["Home","About","Home","Contact","Home","About"]

Write a program to:

* Count visits of each page using a dictionary.
* Display page name and visit count.

Sample Output:
Home visited 3 times
About visited 2 times
Contact visited 1 time

---

'''
l=list(input("Enter your Website pages : ").split())
freq={}
for i in l :
    freq[i]=freq.get(i,0)+1

for k,v in freq.items():
    print(k,"visited ",v,"times ")
