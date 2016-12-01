# encoding: utf-8

from color import colored
import socket
import sys

"""
+=================== STEPS ===================+
|                                             |
|   1) Build sock conection                   |
|   2) Receive connections                    |
|   3) Store the connection                   |
|   4) List the connection                    |
|   5) Select a connection                    |
|   6) Create a thread and Stabilizes contact |
|       with this connection                  |
|   7) Send commands to this connection       |
|   8) Close conection                        |
|   9) Kill thread                            |
|                                             |
+---------------------------------------------+
"""


def header_program():
    title = "|\t\t-~=[ BlackSkull ]=~-\t\t|"
    title = title.replace('\t', '        ')
    bar = '+' + (len(title) - 2) * "=" + '+'
    bar_light = '+' + (len(title) - 2) * "-" + '+'
    break_line = '|' + (len(title) - 2) * " " + '|'

    print(bar)
    print(title)
    print(bar)
    print(break_line)
    print("| Developed by: Douglas A. <alves.douglaz@gmail.com> |")
    print("|      Version: 1.0.3                                |")
    print(break_line)
    print(bar_light)
    print(colored("\n\n[] Server initialized...\n\n", 'green', attrs=['bold', 'reverse']))


class Server(object):
    def __init__(self):
        self.host = "0.0.0.0"
        self.port = 443
        self.socket = None

    def build(self):
        self.socket_create()
        self.socket_bind()
        self.new_client()

    def socket_create(self):
        try:
            self.socket = socket.socket()
        except socket.error as e:
            print("erro para criar o socket: %s" % str(e))

    def socket_bind(self):
        try:
            s = self.socket
            s.bind((self.host, self.port))
            s.listen(5)
        except socket.error as e:
            print('Erro para iniciar o servidor: %s' % str(e))
            self.socket_bind()

    def socket_kill(self, conn):
        try:
            conn.close()
            self.socket.close()
        except s.error as e:
            print('Não foi possivel finalizar a conexao com o usuario: %s' % str(e))
            self.socket_bind()

    def listen(self, conn):
        try:
            client_response = str(conn.recv(1024), "utf-8")
            print (client_response)
        except Exception:
            print("Erro para receber responsta do cliente")

    def new_client(self):
        try:
            s = self.socket
            conn, host = s.accept()
            print(colored("[+] Client has been connected: < {host}:{port} >", color='yellow') . format(host=str(host[0]),port=str(host[1])))
            self.send_command(conn)
        except socket.error as e:
            print("Erro ao aceitar conexao: %s" % str(e))
        return

    def send_command(self, conn):
        while True:
            cmd = input()
            print(cmd)
            if cmd == 'quit':
                self.socket_kill(conn)
                sys.exit()
            if len(str.encode(cmd)) > 0:
                conn.send(str.encode(cmd))
                self.listen(conn)

        self.socket_kill(conn)

def main():
    header_program()
    server = Server()
    server.build()

main()
