# TCP服务器plus

import socket
import multiprocessing


class chat:
    def __init__(self):
        self.tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.tcp.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
        self.ip = input('您的ip')
        self.api = int(input('您的api'))
        self.tcp.bind((self.ip, self.api))
        self.tcp.listen(8)



    def cl(self):
        client, address = self.tcp.accept()
        while True:

            word = client.recv(1024).decode()
            if word:
                print(address)
                print(word)
                print()

                client.send((word + 'back to you\n').encode())
            else:
                client.close()
                break

    def start(self):
        pool = multiprocessing.Pool(32)
        while True:
            pool.apply_async(self.cl)

if __name__ == '__main__':
    a = chat()
    a.start()

