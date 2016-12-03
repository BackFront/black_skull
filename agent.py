# encoding: utf-8

import socket
import subprocess
import time
import os
from color import colored
from src import Client


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


def main():
    header_program()
    client = Client()
    client.build()

main()
#print(colored("Error on socket connections: %s", color='red') % str(e))
