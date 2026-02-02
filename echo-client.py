import socket

HOST = "10.90.14.78"
PORT = 13337

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b"Hello")
    data = s.recv(1024) 

print(f"Received {data!r}")