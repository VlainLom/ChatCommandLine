import socket,sys


pseudo = sys.argv[1]
connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connection.connect(('localhost', 8000))
connection.send(bytes("\n[+] "+pseudo+" est connecté", 'UTF-8'))

while True:
	command = connection.recv(1024).decode()
	print(command)
	command_input = input(str("\n"+pseudo+"# "))
	msgsend = pseudo+" : "+ command_input
	connection.send(bytes('\n'+msgsend ,'UTF-8'))