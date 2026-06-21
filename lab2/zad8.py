import socket
import sys

if len(sys.argv) < 2:
    print("Uzycie: python zad8.py <host>")
    sys.exit(1)

host = sys.argv[1]

for port in range(1, 1025):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(0.05)
        if s.connect_ex((host, port)) == 0:
            try:
                service = socket.getservbyport(port, "tcp")
            except:
                service = "nieznana"
            print(f"Port {port} otwarty. Usluga: {service}")
