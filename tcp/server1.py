import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("localhost", 9999))
server.listen(1)

client, addr = server.accept()
print(addr)

client.close()
server.close()

print("done")
