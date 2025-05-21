import unittest
from hospital_1 import *

class hospitalTests(unittest.TestCase):
    def testEnqueue(self):
        before = []

        hospital = queueH()
        hospital.enqueue(patient("Adam","today"))

        self.assertNotEqual(before,hospital.list)

    def testDequeue(self): 
        hospital = queueH()
        patient1 = patient("Adam","today")
        hospital.enqueue(patient1)
        before = [patient1]
        hospital.dequeue()
        self.assertNotEqual(before,hospital.list)

    def testPeek(self):
        hospital = queueH()
        patient1 = patient("Adam","today")
        hospital.enqueue(patient1)
        self.assertNotEqual(hospital.peek(),hospital.dequeue())

if __name__ == "__main__":
    unittest.main()