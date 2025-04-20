from studentClass import student

def main():
    student.clean_table(student.csvFilePath)
    student.get_numberOfStudents()
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
            name = input("Please write student first name: ")
            familyName = input("Please write student family name: ")
            personalID = input("Please write student personal Id (10 or 12 digits): ")
            program = input("Please write student program: ")
            grade = input("Please write student grade: ")
            student(name,familyName,personalID,program,grade)
            continue

        elif choice == "view all students" or choice == "2":
            print("Looped current number: " + str(looped))
            student.viewAllStudents(student.csvFilePath)
            continue
        elif choice == "search for a specific student" or choice == "3":
            personalID = input("Please write the personal ID number: ")
            student.searchForStudent(student.csvFilePath, personalID)
        elif choice == "delete a student" or choice == "4":
            studentPID = input("Please write the personal ID of the student you want to delete: ")
            confirm = input("Are you sure you want to delete the student with personal ID: (yes/no) " + studentPID).lower()
            if confirm == "yes":
                student.deleteStudent(student.csvFilePath, studentPID)
            else:
                print("Deletion cancled")
        elif choice == "exit" or choice == "5":
            print("BYE")
            break

        


    """"
    My testing section:
    Zaid = student("zaid", "alrabaia", "20020811-6814", "TCOMK", "A*")
    print(Zaid.get_firstName())
    print(Zaid.get_familyName())
    print(Zaid.get_personalID())
    print(Zaid.get_program())
    print(Zaid.get_grade())
    """
if __name__ == "__main__":
    main()
