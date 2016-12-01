# encoding: utf-8

import socket
import subprocess
import time
import os
from color import colored


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
    print(colored("\n\n[+] Program initialized...\n\n", 'green', attrs=['bold', 'reverse']))


class Client(object):
    def __init__(self):
        # self.serverHost = '192.168.1.9'
        self.serverHost = '127.0.0.7'
        self.serverPort = 443
        self.socket = None

    """ Create a client instance """
    def build(self):
        self.socket_create()
        self.socket_connect()

    """ Create a socket """
    def socket_create(self):
        try:
            self.socket = socket.socket()
        except socket.error as e:
            print(colored("[!] Socket creation error: %s", color='red', attrs=['bold']) % str(e))
            return
        return

    """ Connect to a remote socket server """
    def socket_connect(self):
            try:
                self.socket.connect((self.serverHost, self.serverPort))
            except socket.error as e:
                print(colored("[!] Socket connection error: " + str(e), color='red', attrs=['bold']))
                print(colored("\nTrying to connect again...\n", color='white', attrs=['dark', 'blink']))
                time.sleep(5)
                raise
            try:
                self.socket.send(str.encode(socket.gethostname()))
            except socket.error as e:
                print(colored("[!] Cannot send hostname to server: %s", color='red', attrs=['bold']) % str(e))
                raise
            self.persistent_connect()
            return self.socket #Return socket if connection is success

    """ Persists trying to connect """
    def persistent_connect(self):
        print(colored("[+] Connection stabilized on server: ", color='yellow'))
        while True:
            try:
                self.listen()
            except Exception as e:
                print(colored("[!] Error. Could not keep alive: %s", color='red', attrs=['bold']) % str(e))
                time.sleep(5)
            else:
                break

    """ Keep conection alive """
    def listen(self):
        conn = self.socket
        try:
            data = conn.recv(1024)
            print data
        except socket.error as e:
            print(colored("[!] Listen error: %s", color='red', attrs=['bold']) % str(e))
            self.socket_kill(conn)
            return self.build()

    def socket_kill(self, conn):
        try:
            self.socket.close()
        except s.error as e:
            print('Não foi possivel finalizar a conexao com o usuario: %s' % str(e))


def main():
    header_program()
    client = Client()
    client.build()

main()
#print(colored("Error on socket connections: %s", color='red') % str(e))
