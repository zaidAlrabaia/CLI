import unittest
import sys
import os
import sys
import csv
from unittest.mock import patch

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from studentClass import student

class Testing(unittest.TestCase):
    def setUp(self):
        self.test_file = "test_students.csv"
        student.csvFilePath = self.test_file
        with open (self.test_file, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["First name", "Family name", "Personal ID", "Program", "Grade"])
            writer.writerow(["asdasdas", "family", "20020811-6814", "program", "A"])
            writer.writerow(["first", "family", "20020811-2313", "program", "D"])
    
    def tearDown(self):
        os.remove(self.test_file)

    def test_numberOfStudents(self):
        try:
            answer = student.get_numberOfStudents()
            self.assertEqual(answer, 2)
        except Exception as e:
            self.fail("Getting number of students failed with exception: " + str(e))

    def test_student_finder(self):
        try:
            answer = student.studentFinder("20020811-6814", self.test_file)
            self.assertTrue(answer)
        except Exception as e:
            self.fail("Finding student failed with exception: " + str(e))
        try:
            answer = student.studentFinder("20020811-6196", self.test_file)
            self.assertFalse(answer)
        except Exception as e:
            self.fail("Finding student failed with exception: " + str(e))
    
    def test_normalize_personalID(self):
        try:
            answer = student.normalize_personal_ID("0208116814")
            self.assertEqual(answer, "020811-6814")
        except Exception as e:
            self.fail("Error normalizing 0208116814 with exception: " + str(e))
        try:
            answer = student.normalize_personal_ID("200208116814")
            self.assertEqual(answer, "20020811-6814")
        except Exception as e:
            self.fail("Error normalizing 200208116814 with exception: " + str(e))
        
        with self.assertRaises(ValueError) as context:
            student.normalize_personal_ID("02-08116814")
        self.assertIn("Please write 10 or 12 digit Personal ID number", str(context.exception))

        with self.assertRaises(ValueError) as context:
            student.normalize_personal_ID("2002-08116814")
        self.assertIn("Please write 10 or 12 digit Personal ID number", str(context.exception))

        with self.assertRaises(ValueError) as context:
            student.normalize_personal_ID("asjdjklfajsflkjas")
        self.assertIn("Please write 10 or 12 digit Personal ID number", str(context.exception))
        
    def test_personalID_checker(self):
        self.assertTrue(student.personalID_checker("020811-6814"))       
        self.assertTrue(student.personalID_checker("20020811-6814"))     
        self.assertFalse(student.personalID_checker("0208116814"))       
        self.assertFalse(student.personalID_checker("020811--6814"))     
        self.assertFalse(student.personalID_checker("02081a-6814"))      
        self.assertFalse(student.personalID_checker("20020811_6814"))    

    def test_valid_input(self):
        try:
            student.validate_student_input(firstName="Maria",familyName="Barcelona",personalID="20020811-6721",program="tcomk",grade="A")
        except Exception as e:
            self.fail("validate_student_input went wrong with exception: " + str(e))
    
    def test_viewAllStudents(self):
        tempList = student.viewAllStudents(student.csvFilePath, print_mode=False)
        
        columnWidths = []
        myList = []
        with open(student.csvFilePath, "r") as file:
            reader = csv.reader(file)
            headers = next(reader, None)
                
            rows = list(reader)
            columns = list(zip(*([headers]+rows)))

            for col in columns:
                max_len = max(len(cell) for cell in col)
                columnWidths.append(max_len)

            for row in rows:
                padded_row = []
                for i, cell in enumerate(row):
                    padded_row.append(cell.ljust(columnWidths[i]))
                myList.append(" | ".join(padded_row)) 

        self.assertListEqual(myList, tempList)

    def test_addStudent(self):
        inputs = ["Zaid", "Alrabaia", "1234512345", "TCOMK", "A*"]
        with patch("builtins.input", side_effect = inputs):
            myList = student.addStudent(self.test_file)
        with open(self.test_file, "r") as file:
            reader = csv.reader(file)
            rows = list(reader)

        last_row = rows[-1]

        self.assertEqual(last_row[0], "Zaid")           
        self.assertEqual(last_row[1], "Alrabaia")        
        self.assertEqual(last_row[2], "123451-2345")   
        self.assertEqual(last_row[3], "TCOMK")           
        self.assertEqual(last_row[4], "A*")              




if __name__ == "__main__":
    unittest.main()