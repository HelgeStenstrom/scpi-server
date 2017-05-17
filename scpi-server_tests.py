import scpiserver as ss
import unittest
import socket

__author__ = "Helge Stenström"

class SomeTests(unittest.TestCase):
    def setUp(self):
        self.server_address = ('localhost', 9876)
        self.server = ss.SCPIServerExample(self.server_address)

    def tearDown(self):
        self.server.server_close()

    def testPass(self):
        "Pass this test"
        pass

    def testCreate(self):
        "Create a server. Hopefully, it's destroyed by garbage collection."
        theServer = self.server
        self.assertEqual(1,1)

    def testC(self):
        "Start both a server and a client."
        server = self.server

        # todo: gör en klient, som kan prata med servern.
        client = socket.create_connection(self.server_address)

        client.close()
        # print("client closed")
        
        # Enligt dokumentationen måste man ha två trådar. I den ena ska man ha
        # serve_forever(), och i den andra kan man göra shutdown(). 
        # Jag tar bort anrop till shutdown(), tills vidare.
        # Annars får man deadlock.
        # server.shutdown()

        self.assertEqual(1,1)


if __name__ == '__main__':
    unittest.main()
    
