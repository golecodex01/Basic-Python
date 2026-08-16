'''1.Vowel Counter in Customer Feedback

 A company wants to analyze customer feedback messages by counting how many vowels are present in the feedback.

Input: Enter feedback message: Hello Customer Service

Output: Total vowels: 8
'''
feedback=input("Enter Your Feedback : ")

count=0
for ch in feedback:
    if ch.lower() in "aeiou":
        count =count+1
    
print("Vowel Count : ",count)