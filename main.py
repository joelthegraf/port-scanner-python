import sys
import os
import socket
import threading


def scanPorts(fromport, toport, hostaddr, timeout):
    host = socket.gethostbyname(hostaddr)
    try:
        for port in range(int(fromport), int(toport) + 1):
            tcpSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            tcpSocket.settimeout(float(timeout))
            if tcpSocket.connect_ex((host, port)) == 0:
                print("Port {}:\t\t\topen".format(port))
            tcpSocket.close()

    except KeyboardInterrupt:
        print("\nCTRL+C was pressed - Scan stopped")
        sys.exit()

    except socket.gaierror:
        print("\nGiven hostname is invalid - Scan stopped")
        sys.exit()

    except socket.error:
        print("\nAn error occurred - Scan stopped")
        sys.exit()


def scanDefaultPorts(hostaddr, timeout):
    threading.Thread(scanPorts(0, 341, hostaddr, timeout)).start()
    threading.Thread(scanPorts(342, 682, hostaddr, timeout)).start()
    threading.Thread(scanPorts(683, 1023, hostaddr, timeout)).start()


if __name__ == "__main__":
    scanner = """
      _________                                         
     /   _____/ ____ _____    ____   ____   ___________ 
     \_____  \_/ ___\\\\__  \  /    \ /    \_/ __ \_  __ \\
     /        \  \___ / __ \|   |  \   |  \  ___/|  | \/
    /_______  /\___  >____  /___|  /___|  /\___  >__|   
            \/     \/     \/     \/     \/     \/       
    """
    print("-" * 60)
    print(scanner)
    print("-" * 60)
    print("Options:")
    print("1) Scan default port range (0 - 1023) of an host")
    print("2) Scan custom port range (from - to) of an host")
    option = input("Pick an option > ")
    picking = True
    while picking:
        if option == "1":
            picking = False
            os.system("cls")

            print("-" * 60)
            print(scanner)
            print("-" * 60)
            hostaddr = input("Host > ")
            timeout = input("Timeout > ")
            os.system("cls")

            print("-" * 60)
            print(scanner)
            print("-" * 60)
            scanDefaultPorts(hostaddr, timeout)
        elif option == "2":
            picking = False
            os.system("cls")

            print("-" * 60)
            print(scanner)
            print("-" * 60)
            fromport = input("From Port > ")
            toport = input("To Port > ")
            hostaddr = input("Host > ")
            timeout = input("Timeout > ")
            os.system("cls")

            print("-" * 60)
            print(scanner)
            print("Scanning from port {} to port {}. This could take a moment.".format(fromport, toport))
            print("-" * 60)
            scanPorts(fromport, toport, hostaddr, timeout)
        else:
            print("Not an valid option")
            option = input("Pick an option or exit (CTRL+C) > ")