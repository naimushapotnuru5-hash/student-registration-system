#!/usr/bin/env python
# coding: utf-8

# In[1]:


students = []

while True:
    print("\n===== STUDENT REGISTRATION SYSTEM =====")
    print("1. Register Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        roll = input("Enter Roll Number: ")
        name = input("Enter Name: ")
        age = input("Enter Age: ")
        course = input("Enter Course: ")

        student = {
            "Roll": roll,
            "Name": name,
            "Age": age,
            "Course": course
        }

        students.append(student)
        print("Student Registered Successfully!")

    elif choice == "2":
        if len(students) == 0:
            print("No student records found.")
        else:
            print("\nStudent Records")
            print("-" * 50)
            for s in students:
                print("Roll No :", s["Roll"])
                print("Name    :", s["Name"])
                print("Age     :", s["Age"])
                print("Course  :", s["Course"])
                print("-" * 50)

    elif choice == "3":
        roll = input("Enter Roll Number to Search: ")
        found = False

        for s in students:
            if s["Roll"] == roll:
                print("\nStudent Found")
                print("Roll No :", s["Roll"])
                print("Name    :", s["Name"])
                print("Age     :", s["Age"])
                print("Course  :", s["Course"])
                found = True
                break

        if not found:
            print("Student not found.")

    elif choice == "4":
        print("Thank you!")
        break

    else:
        print("Invalid choice. Please try again.")


# In[ ]:




