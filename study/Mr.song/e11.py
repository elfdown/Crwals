from socketserver import BaseRequestHandler,UDPServer
import time
class TimeHandler(BaseRequestHandler):
    def handl(self):
        print ("get from ",self.client_address)
        