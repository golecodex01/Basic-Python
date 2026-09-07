patients = {
    101: {
        "name": "Ajay",
        "age": 35,
        "gender": "Male",
        "disease": "Fever",
        "doctor": "Dr. Sharma"
    },
    102: {
        "name": "Ravi",
        "age": 42,
        "gender": "Male",
        "disease": "Diabetes",
        "doctor": "Dr. Gupta"
    }
}

while True:
    print("\n=====================================")
    print("   HOSPITAL PATIENT MANAGEMENT SYSTEM")
    print("=====================================")
    print("1. Add New Patient")
    print("2. Search Patient")
    print("3. Update Patient Disease")
    print("4. Delete Patient Record")
    print("5. Display All Patients")
    print("6. Count Total Patients")
    print("7. Display Patients By Disease")
    print("8. Display Oldest Patient")
    print("9. Display Youngest Patient")
    print("10. Exit")

    choice = int(input("\nEnter your choice: "))

    if choice == 1:
        patient_id = int(input("Enter Patient ID: "))

        if patient_id in patients:
            print("Patient ID already exists.")
        else:
            name = input("Enter Patient Name: ")
            age = int(input("Enter Age: "))
            gender = input("Enter Gender: ")
            disease = input("Enter Disease: ")
            doctor = input("Enter Doctor Name: ")

            patients[patient_id] = {
                "name": name,
                "age": age,
                "gender": gender,
                "disease": disease,
                "doctor": doctor
            }

            print("Patient Added Successfully")

    elif choice == 2:
        patient_id = int(input("Enter Patient ID: "))

        if patient_id in patients:
            print("\nPatient ID :", patient_id)
            print("Name       :", patients[patient_id]["name"])
            print("Age        :", patients[patient_id]["age"])
            print("Gender     :", patients[patient_id]["gender"])
            print("Disease    :", patients[patient_id]["disease"])
            print("Doctor     :", patients[patient_id]["doctor"])
        else:
            print("Patient Record Not Found")

    elif choice == 3:
        patient_id = int(input("Enter Patient ID: "))

        if patient_id in patients:
            new_disease = input("Enter New Disease: ")
            patients[patient_id]["disease"] = new_disease
            print("Disease Updated Successfully")
        else:
            print("Patient Not Found")

    elif choice == 4:
        patient_id = int(input("Enter Patient ID: "))

        if patient_id in patients:
            del patients[patient_id]
            print("Patient Record Deleted Successfully")
        else:
            print("Patient Not Found")

    elif choice == 5:
        if len(patients) == 0:
            print("No Patient Found")
        else:
            for patient_id, data in patients.items():
                print("\n--------------------------------")
                print("Patient ID :", patient_id)
                print("Name       :", data["name"])
                print("Age        :", data["age"])
                print("Gender     :", data["gender"])
                print("Disease    :", data["disease"])
                print("Doctor     :", data["doctor"])
                print("--------------------------------")

    elif choice == 6:
        print("Total Patients :", len(patients))

    elif choice == 7:
        disease = input("Enter Disease : ")
        found = False

        for patient_id, data in patients.items():
            if data["disease"].lower() == disease.lower():
                print(patient_id, data["name"])
                found = True

        if found == False:
            print("No Patient Found")

    elif choice == 8:
        if len(patients) == 0:
            print("No Patient Found")
        else:
            oldest_id = max(patients, key=lambda id: patients[id]["age"])

            print("\nOldest Patient Details")
            print("Patient ID :", oldest_id)
            print("Name       :", patients[oldest_id]["name"])
            print("Age        :", patients[oldest_id]["age"])
            print("Disease    :", patients[oldest_id]["disease"])
            print("Doctor     :", patients[oldest_id]["doctor"])

    elif choice == 9:
        if len(patients) == 0:
            print("No Patient Found")
        else:
            youngest_id = min(patients, key=lambda id: patients[id]["age"])

            print("\nYoungest Patient Details")
            print("Patient ID :", youngest_id)
            print("Name       :", patients[youngest_id]["name"])
            print("Age        :", patients[youngest_id]["age"])
            print("Disease    :", patients[youngest_id]["disease"])
            print("Doctor     :", patients[youngest_id]["doctor"])

    elif choice == 10:
        print("\nThank You For Using Hospital Patient Management System")
        break

    else:
        print("Invalid Choice! Please try again.")
