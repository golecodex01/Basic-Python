
# On day 1, a student gets 1 point, day 2 → 2 points, and so on. This follows a natural number sequence.
#Write a program to calculate the **total points earned after n days** by summing all natural numbers up to n using loops.

#Input: n = 10
#Output: Total Points = 55

n =int (input("ENter Number :"))
points=0
for i in range (1,n+1):
    points=points+i

print("Total Points Earned After ",n,"Days is ",points)

