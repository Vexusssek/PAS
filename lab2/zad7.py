import socket
import sys

if len(sys.argv) < 3:
    print("aby użyć, trzeba wpisać w konsolii: python zad7.py <host> <port>")
    sys.exit(1)

host = sys.argv[1]
port = int(sys.argv[2])

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.settimeout(2)
    try:
        s.connect((host, port))
        try:
            service = socket.getservbyport(port, "tcp")
        except:
            service = "nieznana"
        print(f"Port {port} jest OTWARTY. Usluga: {service}")
    except socket.error as e:
        print(f"Port {port} jest ZAMKNIETY. Blad: {e}")
