import socket
import time

sock = socket.socket()					#сокет для принятия сообщений
x = int(input("Введите порт: "))		#вводим порт
sock.bind(("", x))						#биндим адрес
sock.listen(10)							#включаем прослушку
###########################все по дефолту#############################

users_ip = []
message = ""
users_m1 = []
users_m2 = []

def get_sms(conn, addr):
	m = []

	k = 0
	ind = users_ip.index(addr[0])

	for i in users_m2[ind]:
		if i == True:
			m.append(k)
			users_m2[ind][k] = False
		k += 1

	s = ""

	for i in m:
		s = s + "ʥ " + users_m1[i] + "\n"

	conn.send(s.encode("utf-8"))

def ret():

	conn, addr = sock.accept()

	data = conn.recv(1024).decode("utf-8")
	if data == "!new":
		users_ip.append(addr[0])
		users_m2.append([])
		print(users_m2)
		conn.send(b"!Ok")
		print(users_ip[users_ip.index(addr[0])], " --> joined")

	elif "!mes:" in data:

		#добавляем сообщения в массивы сообщений
		users_m1.append(data[5:])
		k = 0

		for i in users_m2:
			users_m2[k].append(True)
			k += 1

		#выводим сообщение
		print(data)

		get_sms(conn, addr)

	elif data == "!get_m":
		get_sms(conn, addr)
	else:
		conn.close()

	return message

while True:
	ret()
	time.sleep(0.2)