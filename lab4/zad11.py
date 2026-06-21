import socket

def check_msgA_syntax(txt):
    parts = txt.split(";")
    if len(parts) != 9:
        return "BAD SYNTAX"
    
    if parts[0] == "zad15odpA" and parts[1] == "ver" and parts[3] == "srcip" and parts[5] == "dstip" and parts[7] == "type":
        try:
            ver = int(parts[2])
            srcip = parts[4]
            dstip = parts[6]
            protocol_type = int(parts[8])
            
            if ver == 4 and protocol_type == 6 and srcip == "212.182.24.27" and dstip == "192.168.0.2":
                return "TAK"
            else:
                return "NIE"
        except ValueError:
            return "BAD SYNTAX"
    else:
        return "BAD SYNTAX"

def check_msgB_syntax(txt):
    parts = txt.split(";")
    if len(parts) != 7:
        return "BAD SYNTAX"
    
    if parts[0] == "zad15odpB" and parts[1] == "srcport" and parts[3] == "dstport" and parts[5] == "data":
        try:
            srcport = int(parts[2])
            dstport = int(parts[4])
            data = parts[6]
            
            if srcport == 2900 and dstport == 47526 and data == "network programming is fun":
                return "TAK"
            else:
                return "NIE"
        except ValueError:
            return "BAD SYNTAX"
    else:
        return "BAD SYNTAX"

def start_server(host='127.0.0.1', port=2911):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.bind((host, port))
        print(f"Zadanie 11: Serwer UDP na {host}:{port}")
        while True:
            data, addr = s.recvfrom(1024)
            msg = data.decode('utf-8', errors='replace').strip()
            print(f"Odebrano: {msg} od {addr}")
            
            parts = msg.split(";")
            if not parts:
                answer = "BAD SYNTAX"
            elif parts[0] == "zad15odpA":
                answer = check_msgA_syntax(msg)
            elif parts[0] == "zad15odpB":
                answer = check_msgB_syntax(msg)
            else:
                answer = "BAD SYNTAX"
                
            s.sendto(answer.encode('utf-8'), addr)

if __name__ == "__main__":
    try:
        start_server()
    except KeyboardInterrupt:
        print("\nSerwer zatrzymany.")
