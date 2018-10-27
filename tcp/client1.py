import socket
import time

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print("connecting...")
while True:
    try:
        client.connect(("localhost", 9999))
        break
    except socket.error:
        print("connection failed.retry.")
        time.sleep(2)
print("connected")

print("sending...")
client.send(b"test")
print("sended")

client.close()

print("done")
