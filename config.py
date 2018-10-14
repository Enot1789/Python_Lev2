import socket

ADDRESS = "localhost"
#оставил номер порта прежний чтобы ничего не поехало, не стал ставить 7777
PORT = 9292

def get_client_socket():
    s = socket.socket()
    s.connect((ADDRESS, PORT))
    return s

def get_server_socket():
    s = socket.socket()
    s.bind((ADDRESS, PORT))
    s.listen(10)
    return s