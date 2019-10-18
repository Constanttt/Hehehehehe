import socket
import sys
import time

class IRC:

    irc = socket.socket()
  
    def __init__(self):  
        self.irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def send(self, dst, msg):
        self.irc.send(bytes("PRIVMSG " + dst + " " + msg + "\n", "UTF-8"))

    def connect(self, server, port, botnick):
        print("connecting to:"+server)
        self.irc.connect((server, port))
        self.irc.send(bytes("USER " + botnick + " " + botnick +" " + botnick + " :test\n", "UTF-8"))
        self.irc.send(bytes("NICK " + botnick + "\n", "UTF-8"))               

    def join(self, channel):
        self.irc.send(bytes("JOIN " + channel + "\n", "UTF-8"))

    def get_response(self):
        #time.sleep(1)
        resp = self.irc.recv(2040).decode("UTF-8")
        return resp
