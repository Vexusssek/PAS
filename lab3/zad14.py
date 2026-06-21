import socket

hex_data = "0b 54 89 8b 1f 9a 18 ec bb b1 64 f2 80 18 00 e3 67 71 00 00 01 01 08 0a 02 c1 a4 ee 00 1a 4c ee 68 65 6c 6c 6f 20 3a 29"
data_bytes = bytes.fromhex(hex_data.replace(" ", ""))

src_port = int.from_bytes(data_bytes[0:2], 'big')
dst_port = int.from_bytes(data_bytes[2:4], 'big')
data_offset = (data_bytes[12] >> 4) * 4
tcp_data = data_bytes[data_offset:].decode()

msg = f"zad13odp;src;{src_port};dst;{dst_port};data;{tcp_data}"

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.sendto(msg.encode(), ("127.0.0.1", 2909))
res, addr = s.recvfrom(1024)
print(res.decode())
s.close()
