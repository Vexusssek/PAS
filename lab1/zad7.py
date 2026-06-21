import socket, sys
for p in range(1, 1025):
    s = socket.socket()
    s.settimeout(0.1)
    if not s.connect_ex((sys.argv[1], p)):
        print(f"Port {p} otwarty")
    s.close()
