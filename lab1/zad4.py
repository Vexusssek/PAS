import socket, sys
try:
    print(socket.gethostbyaddr(sys.argv[1])[0])
except:
    print("Blad")
