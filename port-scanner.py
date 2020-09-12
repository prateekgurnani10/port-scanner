from socket import *
import sys

def port_scan(host):
    for i in range(1,1025):
        s = socket(AF_INET, SOCK_STREAM) # Setting up TCP protocol
        res = s.connect_ex((str(host),i))
        if res == 0 :
            print("Port {} is open.".format((i)))
        s.close()

if __name__ == '__main__':
    port_scan(sys.argv[1])
