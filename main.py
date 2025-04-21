from studentClass import student

def main():
    student.clean_table(student.csvFilePath)
    print("current number of students is: " + str(student.get_numberOfStudents()))
    repeat = True
    looped = 0

    while repeat:
        if looped == 0:
            print("Welcome to the Student Grade tracker! What would you like to do?\n1. Add a new student\n2. View all students\n3. Search for a specific student\n4. Delete a student\n5. Exit ")
        else:
             print("Welcome Back! What would you like to do?\n1. Add a new student\n2. View all students\n3. Search for a specific student\n4. Delete a student\n5. Exit ")

        looped += 1

        choice = input("Write your answer or write your choice number: ").lower()

        if choice == "add a new student" or choice == "1":
            student.addStudent(student.csvFilePath)
            continue

        elif choice == "view all students" or choice == "2":
            student.viewAllStudents(student.csvFilePath)
            continue
        elif choice == "search for a specific student" or choice == "3":
            student.searchForStudent(student.csvFilePath)
        elif choice == "delete a student" or choice == "4":
            student.deleteStudent(student.csvFilePath)
        elif choice == "exit" or choice == "5":
            print("BYE")
            break

if __name__ == "__main__":
    main()
