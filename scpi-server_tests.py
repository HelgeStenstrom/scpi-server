import scpiserver as ss
import unittest
import socket


class SomeTests(unittest.TestCase):
    def setUp(self):
        self.server_address = ('localhost', 9876)

    def testPass(self):
        pass

    def testCreate(self):
        theServer = ss.SCPIServerExample(self.server_address)

    def testC(self):
        server = ss.SCPIServerExample(self.server_address)
        print("server created")

        #print("server started")
        # todo: gör en klient, som kan prata med servern.
        client = socket.create_connection(self.server_address)
        print("client created")

        client.close()
        print("client closed")

        # Det här verkar inte hända. Varför? Är inte servern startad?
        server.shutdown()
        print("server shut down")
        server.server_close()
        print("server closed")
        #theServer.
