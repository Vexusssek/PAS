import socket

def start_server(host='127.0.0.1', port=12348):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.bind((host, port))
        print(f"Zadanie 4: Serwer UDP Kalkulator działający na {host}:{port}")
        
        while True:
            data, addr = s.recvfrom(1024)
            msg = data.decode('utf-8').strip()
            print(f"Odebrano: {msg} od {addr}")
            
            try:
                parts = msg.split()
                if len(parts) != 3:
                    result = "Blad: Wymagany format 'liczba [spacja] operator [spacja] liczba'"
                else:
                    num1 = float(parts[0])
                    op = parts[1]
                    num2 = float(parts[2])
                    
                    if op == '+': result = str(num1 + num2)
                    elif op == '-': result = str(num1 - num2)
                    elif op == '*': result = str(num1 * num2)
                    elif op == '/': 
                        if num2 == 0: result = "Blad: Dzielenie przez zero"
                        else: result = str(num1 / num2)
                    else:
                        result = f"Blad: Nieznany operator {op}"
            except ValueError:
                result = "Blad: Nieprawidlowe liczby"
            except Exception as e:
                result = f"Blad: {str(e)}"
            
            s.sendto(result.encode('utf-8'), addr)

if __name__ == "__main__":
    try:
        start_server()
    except KeyboardInterrupt:
        print("\nSerwer zatrzymany.")
