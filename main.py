import csv
import os
class student:
    numberOfStudents = 0
    def __init__(self, firstName, familyName, personalID, program, grade):
        self.__firstName = firstName
        self.__familyName = familyName
        self.__personalID = personalID
        self.__program = program
        self.__grade = grade
        student.numberOfStudents += 1

        csvFilePath = "studentList.csv"
        found = student.studentFinder(personalID, csvFilePath)

        with open(csvFilePath, "a", newline="") as file:
            writer = csv.writer(file)
            if os.path.getsize(csvFilePath) == 0:
                writer.writerow(["First name","Family Name","Personal ID","Program","Grade"])
            if not found:
                writer.writerow([firstName,familyName,personalID,program,grade])
            else:
                print("The student " + firstName + " " + familyName + " already exists")

    def get_firstName(self):
        return self.__firstName
    def get_familyName(self):
        return self.__familyName
    def get_personalID(self):
        return self.__personalID
    def get_program(self):
        return self.__program
    def get_grade(self):
        return self.__grade
    
    @staticmethod
    def studentFinder(personalID, csvFile):
        if os.path.exists(csvFile):
            with open(csvFile, "r") as file:
                reader = csv.reader(file)
                for row in reader:
                    if row[2] == personalID:
                        return True
        return False
    
Zaid = student("zaid", "alrabaia", "20020811-6814", "TCOMK", "A*")
print(Zaid.get_firstName())
print(Zaid.get_familyName())
print(Zaid.get_personalID())
print(Zaid.get_program())
print(Zaid.get_grade())
