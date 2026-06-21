import socket

def check_msg_syntax(txt):
    parts = txt.split(";")
    if len(parts) != 7:
        return "BAD SYNTAX"
    
    if parts[0] == "zad14odp" and parts[1] == "src" and parts[3] == "dst" and parts[5] == "data":
        try:
            src_port = int(parts[2])
            dst_port = int(parts[4])
            data = parts[6]

            if src_port == 60788 and dst_port == 2901 and data == "programming in python is fun":
                return "TAK"
            else:
                return "NIE"
        except ValueError:
            return "BAD SYNTAX"
    else:
        return "BAD SYNTAX"

def start_server(host='127.0.0.1', port=2910):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.bind((host, port))
        print(f"Zadanie 9: Serwer UDP na {host}:{port}")
        while True:
            data, addr = s.recvfrom(1024)
            msg = data.decode('utf-8', errors='replace').strip()
            print(f"Odebrano: {msg} od {addr}")
            answer = check_msg_syntax(msg)
            s.sendto(answer.encode('utf-8'), addr)

if __name__ == "__main__":
    try:
        start_server()
    except KeyboardInterrupt:
        print("\nSerwer zatrzymany.")
