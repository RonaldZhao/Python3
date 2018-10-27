import socket
import threading

RECV_BUFFER_SIZE = 1024


def process_connection(sock, addr):
    print("New Connection from {0}:{1}".format(*addr))
    sock.send("<<<< Welcome >>>>".encode("utf8"))
    buffer_list = []
    while True:
        data = sock.recv(RECV_BUFFER_SIZE).decode("utf8")
        # 如果判断本次接收的数据长度小于 RECV_BUFFER_SIZE, 则说明客户端本次发送的数据全部接收完毕了
        if len(data) < RECV_BUFFER_SIZE:
            # 只有在 buffer_list 为空切本次接收的数据为 exit 时才说明客户端本次只发送了 exit
            # 否则可能是发送了一个数据大小为 RECV_BUFFER_SIZE + 4 长度的数据, 最后四个为 exit
            # 这时如果不判断 buffer_list 是否为空就会出现错误, 导致提前跳出循环
            if len(buffer_list) == 0 and data == "exit":
                break
            buffer_list.append(data)
            print("".join(buffer_list))
            buffer_list.clear()
        else:
            # 否则暂存
            buffer_list.append(data)
    sock.close()
    print("Client {0}:{1} closed.".format(*addr))


if __name__ == "__main__":
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("localhost", 9999))
    server.listen(5)
    print("Server listening...\n")

    while True:
        sock, addr = server.accept()
        threading.Thread(target=process_connection, args=(sock, addr)).start()
