import socket

hex_data = "ed 74 0b 55 00 24 ef fd 70 72 6f 67 72 61 6d 6d 69 6e 67 20 69 6e 20 70 79 74 68 6f 6e 20 69 73 20 66 75 6e"
data_bytes = bytes.fromhex(hex_data.replace(" ", ""))

src_port = int.from_bytes(data_bytes[0:2], 'big')
dst_port = int.from_bytes(data_bytes[2:4], 'big')
udp_data = data_bytes[8:].decode()

msg = f"zad14odp;src;{src_port};dst;{dst_port};data;{udp_data}"

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.sendto(msg.encode(), ("127.0.0.1", 2910))
res, addr = s.recvfrom(1024)
print(res.decode())
s.close()
