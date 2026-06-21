import socket

def start_server(host='127.0.0.1', port=12350):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.bind((host, port))
        print(f"Zadanie 6: Serwer UDP Hostname->IP działający na {host}:{port}")
        
        while True:
            data, addr = s.recvfrom(1024)
            hostname = data.decode('utf-8').strip()
            print(f"Odebrano hostname: {hostname} od {addr}")
            
            try:
                ip = socket.gethostbyname(hostname)
                result = ip
            except socket.gaierror:
                result = "Blad: Nie mozna znalezc adresu IP dla podanego hostname"
            except Exception as e:
                result = f"Blad: {str(e)}"
                
            s.sendto(result.encode('utf-8'), addr)

if __name__ == "__main__":
    try:
        start_server()
    except KeyboardInterrupt:
        print("\nSerwer zatrzymany.")
