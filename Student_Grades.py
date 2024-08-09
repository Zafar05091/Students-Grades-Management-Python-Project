# First we Initialize a dictionary (Empty Dictionary)
Student_Grades = {}

# Creat  a function to add a new Student

def Add_student(name,grade):
    Student_Grades[name] = grade
    print(f"Added {name} with Grade {grade}")

# Creat a function to Update students name and grade

def Update_student(name,grade):
    if name in Student_Grades:
        Student_Grades[name] = grade
        print(f"{name} with students marks {grade} is updated ")
    else:
        print(f"{name} is not found in Dictionary")

# Creat a function to Delete a Student name and grade

def Del_Student(name):
    if name in Student_Grades:
        del Student_Grades[name]
        print(f"{name} has been Deleted Successfully")
    else:
        print(f"Student with name {name} is not found")

# Creat a function to view all students names and grades

def View_Students():
    if Student_Grades:
        for name, grade in Student_Grades.items():
            print(f"{name} : {grade}")
    else:
        print(f"No student found with name {name}")

def main():
    while True:
        print("\nStudents Grades Managment System")
        print("1. Add Student")
        print("2. Update Student Details")
        print("3. Delete Student Details")
        print("4. Display all Student with Grade")
        print("5. Exit")

        choice = int(input("Enter Your Desired choice: "))

        if choice == 1:
            name = input("Enter the Student name: ")
            grade = int(input("Enter the Grades of Student: "))
            Add_student(name,grade)
        if choice == 2:
            name = input("Enter the Student new name: ")
            grade = int(input("Enter the new Grades of Student: "))
            Update_student(name,grade)
        if choice == 3:
            name = input("Enter the name of Student you want to Delete: ")
            Del_Student(name)
        if choice == 4:
            View_Students()
        if choice == 5:
            print("Closing the program")
            break
        else:
            print("Invalid Choice Please Enter a Valid Choice")

if __name__ == '__main__':
    main()
