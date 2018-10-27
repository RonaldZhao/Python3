import socket
import time

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

while True:
    try:
        sock.connect(("localhost", 9999))
        msg = sock.recv(1024)
        print(msg.decode("utf8"))
        break
    except socket.error:
        print("connection failed, try again after 2 seconds.")
        time.sleep(2)

while True:
    msg = input("Input data to send:\n")
    while not msg:
        print("Data can not be empty!")
        msg = input()
    sock.send(msg.encode("utf8"))
    if msg == "exit":
        break

sock.close()
print("All done.")
