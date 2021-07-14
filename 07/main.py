# udp，聊天器plus

import socket
import threading


class chat:
    def __init__(self):
        self.udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.ip = input('您的ip')
        self.api = int(input('您的api'))
        self.opip = input('对方的ip')
        self.opapi = int(input('对方的api'))
        self.tre = threading.Thread(target=self.re)
        self.tse = threading.Thread(target=self.se)
        self.udp.bind((self.ip, self.api))
        self.tre.start()
        self.tse.start()
    def re(self):
        while True:
            data = self.udp.recvfrom(1024)
            print(data[1])
            print(data[0].decode())

    def se(self):
        while True:
            word = input('您想说什么')
            self.udp.sendto(word.encode(), (self.opip, self.opapi))


if __name__ == '__main__':
    me = chat()
