import scpiserver as ss
import unittest

class SomeTests(unittest.TestCase):
    def setUp(self):
        self.server_address = ('localhost', 9876)


    def testPass(self):
        pass

    def testCreate(self):
        c = ss.SCPIServerExample(self.server_address)

    def testC(self):
        c = ss.SCPIServerExample(self.server_address)
