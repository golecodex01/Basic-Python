print("Enter Marks Of your 5 Subjects : ")
m1,m2,m3,m4,m5=map(int,input().split())

totalMarks=m1+m2+m3+m4+m5
avgMarks=totalMarks/5
percent=totalMarks/5

print("Tatal = ",totalMarks)
print("Average = ",avgMarks)
print("Percentage = ",percent)
