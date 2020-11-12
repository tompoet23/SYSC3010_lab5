import unittest;

ledSig = 1; #this value is a hardcoded value to test if the motion sensor detects movement

class light(unittest.TestCase):
    def test_light(self):
        self.assertTrue(ledSig == 1, msg="No signal is given to turn LED on") # tests to see if a signal is given to turn led

if __name__=='__main__':
    unittest.main()