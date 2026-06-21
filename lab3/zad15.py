import socket

hex_data = "45 00 00 4e f7 fa 40 00 38 06 9d 33 d4 b6 18 1b c0 a8 00 02 0b 54 b9 a6 fb f9 3c 57 c1 0a 06 c1 80 18 00 e3 ce 9c 00 00 01 01 08 0a 03 a6 eb 01 00 0b f8 e5 6e 65 74 77 6f 72 6b 20 70 72 6f 67 72 61 6d 6d 69 6e 67 20 69 6e 20 70 79 74 68 6f 6e 20 69 73 20 66 75 6e"
data_bytes = bytes.fromhex(hex_data.replace(" ", ""))

version = data_bytes[0] >> 4
ihl = (data_bytes[0] & 0x0F) * 4
protocol = data_bytes[9]
src_ip = socket.inet_ntoa(data_bytes[12:16])
dst_ip = socket.inet_ntoa(data_bytes[16:20])

msgA = f"zad15odpA;ver;{version};srcip;{src_ip};dstip;{dst_ip};type;{protocol}"

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server = ("127.0.0.1", 2911)
s.sendto(msgA.encode(), server)
resA, addr = s.recvfrom(1024)
print(f"Odp A: {resA.decode()}")

if resA.decode() == "TAK":
    tcp_seg = data_bytes[ihl:]
    src_port = int.from_bytes(tcp_seg[0:2], 'big')
    dst_port = int.from_bytes(tcp_seg[2:4], 'big')
    tcp_offset = (tcp_seg[12] >> 4) * 4
    payload = tcp_seg[tcp_offset:].decode()
    
    msgB = f"zad15odpB;srcport;{src_port};dstport;{dst_port};data;{payload}"
    s.sendto(msgB.encode(), server)
    resB, addr = s.recvfrom(1024)
    print(f"Odp B: {resB.decode()}")

s.close()
