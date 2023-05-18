import socket,os,sys

listening = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listening.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listening.bind(("", 8000))
listening.listen(0)

conn,adress = listening.accept()
com = conn.recv(1024).decode()
print(com)

while True:
    pseudo = sys.argv[1]
    command_input = input(str("\n"+ pseudo +"# "))
    msgsend = pseudo + " : "+ command_input
    conn.send(bytes('\n'+msgsend ,'UTF-8'))
    command = conn.recv(1024).decode()
    print(command)