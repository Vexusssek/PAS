import socket, sys
try:
    socket.create_connection((sys.argv[1], int(sys.argv[2])), 2)
    print("Polaczono")
except:
    print("Nie udalo sie polaczyc")
