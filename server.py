import socket
import time

sock = socket.socket()					#сокет для принятия сообщений
x = int(input("Введите порт: "))		#вводим порт
sock.bind(("", x))						#биндим адрес
sock.listen(10)							#включаем прослушку
###########################все по дефолту#############################

users_ip = []
message = ""

def ret(message):

	# sock.setblocking(False)

	conn, addr = sock.accept()

	data = conn.recv(1024).decode("utf-8")
	if data == "!new":
		users_ip.append(addr[0])
		conn.send(b"!Ok")
		print(users_ip[users_ip.index(addr[0])], " --> joined")
	elif "!mes:" in data:
		message = data[5:]
		print(message)
	elif data == "!get_m":
		if message != "":
			conn.send(message.encode("utf-8"))
			print("send --> ", message)
			message = ""
	else:
		conn.close()

	return message

	# try:
	# 	conn, addr = sock.accept()

	# 	data = conn.recv(1024).decode("utf-8")
	# 	if data == "!new":
	# 		users_ip.append(addr[0])
	# 		conn.send(b"!Ok")
	# 		print(users_ip[users_ip.index(addr[0])], " --> joined")
	# 	elif "!mes:" in data:
	# 		message = data[5:]
	# 		print(message)
	# 	elif data == "!get_m":
	# 		if message != "":
	# 			conn.send(message.encode("utf-8"))
	# 			print("send --> ", message)
	# 		# for i in users_ip:

	# 		# 	s = socket.socket()
	# 		# 	s.connect((i, x + 2))
	# 		# 	s.send(data.encode("utf-8"))
	# 		# 	s.close()
	# 		# 	print("sms! --> ", data)

	# 	conn.close()
	# except:
	# 	print("can't connect")

while True:
	message = ret(message)
	time.sleep(0.2)