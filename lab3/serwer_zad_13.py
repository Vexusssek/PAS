import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(("127.0.0.1", 2910))
while True:
    data, addr = s.recvfrom(1024)
    if data.decode().startswith("zad14odp"):
        s.sendto(b"TAK", addr)
    else:
        s.sendto(b"BAD SYNTAX", addr)
