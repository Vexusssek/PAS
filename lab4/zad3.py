import socket

def start_server(host='127.0.0.1', port=12347):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.bind((host, port))
        print(f"Zadanie 3: Serwer UDP Echo działający na {host}:{port}")
        
        while True:
            data, addr = s.recvfrom(1024)
            print(f"Odebrano od {addr}: {data.decode('utf-8', errors='replace')}")
            s.sendto(data, addr)

if __name__ == "__main__":
    try:
        start_server()
    except KeyboardInterrupt:
        print("\nSerwer zatrzymany.")
