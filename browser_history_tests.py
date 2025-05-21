import unittest

class BrowserCase(unittest.TestCase):
    def testOk(self):
        self.assertEqual(1,1)

if __name__ == "__main__":
    unittest.main()