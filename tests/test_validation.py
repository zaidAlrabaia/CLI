import unittest
import sys
import os
import sys
import csv

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

    









if __name__ == "__main__":
    unittest.main()