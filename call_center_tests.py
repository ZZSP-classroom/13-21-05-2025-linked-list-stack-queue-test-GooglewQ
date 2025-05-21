from call_center_4 import *
import unittest

class CallCenterCase(unittest.TestCase):
    def testEnqueue(self):
        q = queueH()
        c1 = call(1, "16:19:25")
        c2 = call(2, "18:19:25")
        q.enqueue(c1)
        q.enqueue(c2)
        self.assertEqual(q.peek(), c1)
    
    def testDequeue(self):
        q = queueH()
        c1 = call(1, "16:19:25")
        c2 = call(2, "18:19:25")
        q.enqueue(c1)
        q.enqueue(c2)
        q.dequeue()
        self.assertEqual(q.peek(), c2)

    def testPush(self):
        s = stack()
        c1 = call(1, "16:19:25")
        c2 = call(2, "18:19:25")
        s.push(c1)
        s.push(c2)
        self.assertEqual(s.peek(), c2)

    def testPop(self):
        s = stack()
        c1 = call(1, "16:19:25")
        c2 = call(2, "18:19:25")
        s.push(c1)
        s.push(c2)
        s.pop()
        self.assertEqual(s.peek(), c1)


if __name__ == "__main__":
    unittest.main()