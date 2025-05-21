import unittest
from text_editor_2 import *

class hospitalTests(unittest.TestCase):
    def testPush(self):

        textEdit = stack()
        textEdit.push("Typying")
        self.assertNotEqual([],textEdit.list)

    def testPop(self):

        textEdit = stack()
        textEdit.push("Typying")
        textEdit.push("Delete")
        before = ["Typying","Delete"]
        textEdit.pop()
        self.assertNotEqual(textEdit.list,before)

    def testPeek(self):
        textEdit = stack()
        textEdit.push("Typying")
        textEdit.push("Delete")
        self.assertNotEqual(textEdit.peek(),textEdit.pop())

if __name__ == "__main__":
    unittest.main()