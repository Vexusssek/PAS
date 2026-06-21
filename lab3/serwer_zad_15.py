import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(("127.0.0.1", 2911))
while True:
    data, addr = s.recvfrom(1024)
    msg = data.decode()
    if msg.startswith("zad15odpA"):
        s.sendto(b"TAK", addr)
    elif msg.startswith("zad15odpB"):
        s.sendto(b"TAK", addr)
    else:
        s.sendto(b"BAD SYNTAX", addr)
