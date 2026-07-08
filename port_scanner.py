import sys 
import socket
from datetime import datetime

#define target type
if len(sys.argv) ==2:
    target = socket.gethostbyname(sys.argv[1]) #translate hostname to IPv4
else:
    print("Invalid amount of arguments.")
    print("Syntax: python3 port_scanner.py <ip>")
    sys.exit()

# pretty banner
print("-" * 50)
print("Scanning target: " + target)
print("Scanning started at: " + str(datetime.now()))
print("-" * 50)

try:
    for port in range(1, 65535): #scan ports between 1 and 65535
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #create a socket object
        socket.setdefaulttimeout(1) #set timeout to 1 second
        result = s.connect_ex((target, port)) #returns an error indicator
        if result == 0:
            print("Port {} is open".format(port))
        s.close()
except KeyboardInterrupt:
    print("\nExiting program.")
    sys.exit()
except socket.gaierror:
    print("Hostname could not be resolved.")
    sys.exit()
except socket.error:
    print("Could not connect to server.")
    sys.exit()