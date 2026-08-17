
# =====================================================================
# QUESTION 3: HOSPITAL PATIENT TRACKER
# ====================================

# A hospital stores patient records for daily monitoring.

# Fields:
# patient_id, patient_name, age, disease

# Requirements:

# 1. Read N patient records from the user and store them in a list of NamedTuples.

# ---

# 2. Display all patient details.

# ---

# 3. Display patients whose age is above 60 years.

# ---

# 4. Search for a patient using Patient ID.

# ---

# 5. Count the number of patients suffering from a particular disease.

# ---

# Test Case:

# Input:
# Enter number of patients: 4

# P101 Rajesh 65 Diabetes
# P102 Suman 45 Fever
# P103 Mohan 70 Diabetes
# P104 Rita 35 Cold

# Enter Patient ID: P103
# Enter Disease: Diabetes

# Expected Output:
# Patient Found:
# P103 Mohan 70 Diabetes

# Patients Above 60:
# P101 Rajesh 65 Diabetes
# P103 Mohan 70 Diabetes

# Patients with Diabetes:
# 2

# =====================================================================
from collections import namedtuple

Patient=namedtuple("Patient",["patient_id","patient_name","age","disease"])

n=int(input("Enter number of patients: "))
patients=[]

for i in range(n):
    patient_id,patient_name,age,disease=input().split()
    patients.append(Patient(patient_id,patient_name,int(age),disease))

print("All Patient Details:")
for p in patients:
    print(p.patient_id,p.patient_name,p.age,p.disease)

patient_id=input("Enter Patient ID: ")

print("Patient Found:")
for p in patients:
    if p.patient_id==patient_id:
        print(p.patient_id,p.patient_name,p.age,p.disease)

print("Patients Above 60:")
for p in patients:
    if p.age>60:
        print(p.patient_id,p.patient_name,p.age,p.disease)

disease=input("Enter Disease: ")

count=0

for p in patients:
    if p.disease==disease:
        count=count+1

print("Patients with",disease+":")
print(count)