import socket
import time

sock = socket.socket()					#сокет для принятия сообщений
x = int(input("Введите порт: "))		#вводим порт
sock.bind(("", x))						#биндим адрес
sock.listen(10)							#включаем прослушку
###########################все по дефолту#############################

tsock = socket.socket()

users_ip = []

def ret():

	sock.setblocking(False)

	try:
		conn, addr = sock.accept()

		data = conn.recv(1024).decode("utf-8")
		if data == "!new":
			users_ip.append(addr[0])
			conn.send(b"!Ok")
			print(users_ip[users_ip.index(addr[0])], " --> joined")
		else:
			for i in users_ip:
				# tsock.sendto(data.encode("utf-8"), (i, x+2))

				s = socket.socket()
				s.connect((i, x + 2))
				s.send(data.encode("utf-8"))
				s.close()
				print("sms! --> ", data)

		conn.close()
	except:
		print("can't connect")

while True:
	ret()
	time.sleep(0.2)