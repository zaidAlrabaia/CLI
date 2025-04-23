import csv
import os
import logging

logging.basicConfig(level=logging.DEBUG, filename = "log.log",filemode="a", format = "%(asctime)s -- %(levelname)s --  %(message)s")
logger = logging.getLogger(__name__)

class student:
    numberOfStudents = 0
    csvFilePath = "studentList.csv"
    def __init__(self, firstName: str, familyName: str, personalID: str, program: str, grade: str):
        try:
            student.validate_student_input(firstName,familyName,personalID,program,grade)
        except Exception as e:
            logger.warning("There was a validation error: " + str(e))
        self.__firstName = firstName
        self.__familyName = familyName
        self.__personalID = personalID
        self.__program = program
        self.__grade = grade

        found = student.studentFinder(personalID, student.csvFilePath)

        with open(student.csvFilePath, "a", newline="") as file:
            writer = csv.writer(file)
            if os.path.getsize(student.csvFilePath) == 0:
                writer.writerow(["First name","Family Name","Personal ID","Program","Grade"])
            if not found:
                writer.writerow([firstName,familyName,personalID,program,grade])
            else:
                logger.warning("The student " + firstName + " " + familyName + " already exists")
    
    @staticmethod
    def get_numberOfStudents():
        student.numberOfStudents = 0
        if os.path.exists(student.csvFilePath):
            try:
                with open(student.csvFilePath, "r") as file:
                    reader = csv.reader(file)
                    next(reader,None)
                    for row in reader:
                        if not row:
                            continue
                        else:
                            student.numberOfStudents += 1
                print(student.numberOfStudents)
            except Exception as e:
                logger.error("Something went wrong: " + str(e))

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
        if not os.path.exists(csvFile):
            logger.warning("Hello g! File not found do sumn bout it")
            return False
        try:
            with open(csvFile, "r") as file:
                reader = csv.reader(file)
                for row in reader:
                    if not row:
                        continue
                    if row[2] == personalID:
                        return True
        except Exception as e:
            logger.error("Error reading from file: " + str(e))
        return False
    
    @staticmethod
    def validate_student_input(firstName, familyName, personalID, program, grade):
        fields = [firstName,familyName,personalID,program,grade]

        if not (firstName):
            raise ValueError("First name is missing")
        if not (familyName):
            raise ValueError("Family name is missing")
        if not (personalID):
            raise ValueError("Personal ID is missing")
        if not (program):
            raise ValueError("program is missing")
        if not (grade):
            raise ValueError("grade is missing")
        if not all (isinstance(x, str) for x in fields):
            raise ValueError("all inputs must be strings")
        if not firstName.isalpha() or not familyName.isalpha():
            raise ValueError("name must only contain alphabet character")
        if not all (char in "0123456789-" for char in personalID) or len(personalID) not in [11,13]:
            raise ValueError("Personal ID format is wrong")
        if grade not in ["F", "Fx", "E", "D", "C", "B", "A", "A*"]:
            raise ValueError("wrong grade format")
    
    @staticmethod
    def clean_table(file_path):
        if not os.path.exists(file_path):
            logger.warning("File does not exist")
            return
        updated_list = []
        try:
            with open(file_path, "r") as file:
                reader = csv.reader(file)
                for row in reader:
                    if  row and any(cell.strip() for cell in row):
                        updated_list.append(row)
        except Exception as e:
                logger.error("Error reading file: " + str(e))
                return
        try:
            with open(file_path, "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerows(updated_list)
        except Exception as e:
            logger.error("There was an error writing the table: " + str(e))
            return
    
    @staticmethod
    def viewAllStudents(file_path):
        if not os.path.exists(file_path):
            logger.warning("MY BROTHER! FILE NOT FOUND")
            return
        
        columnWidths = []
        try:
            with open(file_path, "r") as file:
                reader = csv.reader(file)
                headers = next(reader, None)

                if not headers:
                    logger.warning("The file is most likely empty and would cause a crash")
                    return
                
                rows = list(reader)
                columns = list(zip(*([headers]+rows)))

                for col in columns:
                    max_len = max(len(cell) for cell in col)
                    columnWidths.append(max_len)

                header_row = []
                for i, cell in enumerate(headers):
                    header_row.append(cell.ljust(columnWidths[i]))
                print(" | ".join(header_row))
                print("-" * sum(columnWidths) + "-"*12)

                for row in rows:
                    padded_row = []
                    for i, cell in enumerate(row):
                        padded_row.append(cell.ljust(columnWidths[i]))
                    print(" | ".join(padded_row))

        except Exception as e:
            logger.error("IDK what happened but sumn went wrong with the view all students method: " + str(e))
    
    @staticmethod
    def addStudent(file_path):
            try:
                name = input("Please write student first name: ").strip()
                if not name.isalpha():
                    raise ValueError("First name must only contain alphabet character")
                familyName = input("Please write student family name: ").strip()
                if not familyName.isalpha():
                    raise ValueError("Family name must only contain alphabet character")
                personalID = input("Please write student personal Id (10 or 12 digits): ").strip()
                if not all (char in "0123456789-" for char in personalID) or len(personalID) not in [11,13]:
                    raise ValueError("Personal ID format is wrong")
                program = input("Please write student program: ").strip()
                grade = input("Please write student grade: ").strip()
                if grade not in ["F", "Fx", "E", "D", "C", "B", "A", "A*"]:
                    raise ValueError("wrong grade format")
                
                if student.studentFinder(personalID, file_path):
                    logger.warning("Student already exists")
                    return
                
                student.validate_student_input(name,familyName,personalID,program,grade)

                student(name,familyName,personalID,program,grade)
                student.numberOfStudents += 1

            except ValueError as ve:
                logger.error("Value Error: " + str(ve))
            except Exception as e:
                logger.error("Something went wrong with the user input: " + str(e))

    @staticmethod
    def searchForStudent(file_path):
        if not os.path.exists(file_path):
            logger.warning("File not found")
            return
        
        if os.path.getsize(file_path) == 0:
            logger.warning("file is empty")
            return
        
        personalID = input("Please write the personal ID number: ").strip()
    
        try:
            with open(file_path, "r") as file:
                reader = csv.reader(file)
                headers = next(reader, None)
                
                if not headers:
                    logger.warning("Header row is missing")
                    return
                
                rows = list(reader)
                columns = list(zip(*[headers] + rows))
                padded_column = []
                for col in columns:
                    max_len = max(len(cell) for cell in col)
                    padded_column.append(max_len)
                padded_header = []
                
                found = False
                for i, cell in enumerate(headers):
                            padded_header.append(cell.ljust(padded_column[i]))
                for row in rows:
                    if row[2].strip() == personalID.strip():
                        found = True
                        padded_row= []
                        print(" | ".join(padded_header))
                        for i, cell in enumerate(row):
                            padded_row.append(cell.ljust(padded_column[i]))
                        print(" | ".join(padded_row))
                        return padded_row
                if not found:
                    logger.info("Student not found")
        except Exception as e:
            logger.error("Sumn went wrong: " + str(e))

    @staticmethod
    def deleteStudent(file_path):
        if not os.path.exists(file_path):
            logger.warning("File not found")
            return
        
        if os.path.getsize(file_path) == 0:
            logger.info("File is empty broski")
            return

        personalID = input("Please write the personal ID of the student you want to delete: ").strip()
        confirm = input("Are you sure you want to delete the student with personal ID: (yes/no) " + personalID).lower()

        if confirm != "yes":
            print("Deletion canceled")
            return

        updated_list = []
        deleted = False

        try:
            with open(file_path, "r") as file:
                reader = csv.reader(file)
                header = next(reader, None)
                for row in reader:
                    if row and row[2].strip() != personalID.strip():
                        updated_list.append(row)
                    elif row and row[2].strip() == personalID.strip():
                        deleted = True

            with open(file_path, "w", newline="") as file:
                writer = csv.writer(file)
                if header:
                    writer.writerow(header)
                writer.writerows(updated_list)

            if deleted:
                print(f" Student with ID {personalID} was deleted.")
            else:
                logger.info(f" Student with ID {personalID} not found.")
        
        except Exception as e:
            logger.error(" Something went wrong during deletion:", str(e))

