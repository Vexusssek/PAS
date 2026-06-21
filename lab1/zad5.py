import socket, sys
try:
    print(socket.gethostbyname(sys.argv[1]))
except:
    print("Blad")
