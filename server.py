# encoding: utf-8

from color import colored
import socket
import sys
from src.Server import Server

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


def create_workers():
    """ Create worker threads (will die when main exits) """
    server = MultiServer()
    server.register_signal_handler()
    for _ in range(NUMBER_OF_THREADS):
        t = threading.Thread(target=work, args=(server,))
        t.daemon = True
        t.start()
    return

def main():
    header_program()
    server = Server()
    server.start()

if __name__ == '__main__':
    main()
