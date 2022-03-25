import sqlite3
import unittest

class Patients(unittest.TestCase):
    def setUp(self):
        #making connection
        self.connection = sqlite3.connect("Hospital.db")
        self.patientCode ="1"
        self.name = "Utkarsh"
    def tearDown(self):
        self.patientCode = "0"
        self.name =""
        self.connection.close()

    def test_pat1(self):
        result = self.connection.execute("SELECT Name FROM Patient where patientCode ="+self.patientCode)
        for i in result:
            fetchName = i[0]
            self.assertEqual(fetchName,self.name)









if __name__ == "__main__":
        unittest.main()
