import socket

def start_server(host='127.0.0.1', port=12349):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.bind((host, port))
        print(f"Zadanie 5: Serwer UDP IP->Hostname działający na {host}:{port}")
        
        while True:
            data, addr = s.recvfrom(1024)
            ip = data.decode('utf-8').strip()
            print(f"Odebrano IP: {ip} od {addr}")
            
            try:
                hostname, alias, addresslist = socket.gethostbyaddr(ip)
                result = hostname
            except socket.herror:
                result = "Blad: Nie mozna znalezc hostname dla podanego IP"
            except Exception as e:
                result = f"Blad: {str(e)}"
                
            s.sendto(result.encode('utf-8'), addr)

if __name__ == "__main__":
    try:
        start_server()
    except KeyboardInterrupt:
        print("\nSerwer zatrzymany.")
