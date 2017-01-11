import socket
import time

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

x = int(input("Введите порт: "))

s.bind(("", x))

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

users_ip = []

sock_con = socket.socket()
sock_con.bind(("", x+1))
sock_con.listen(10)

def some():

	sock_con.setblocking(False)

	try:
		conn, addr = sock_con.accept()
		data = conn.recv(1024).decode("utf-8")
		if data == "!new":
			if addr[0] not in users_ip:
				users_ip.append(addr[0])
				print("new connected")
				conn.send(b"!Ok")
			print(">>>>>>>>>>>>>>>>>")
		else:
			conn.close()
	except:
		print("---------------------")

	s.setblocking(False)

	try:
		#принимаем данные

		data = s.recv(1024).decode("utf-8")
		# if "!new" in data :

		# 	if data[4:] not in users_ip:
		# 		users_ip.append(data[4:])
		# 		print(data[4:], " joined")

		# 	#отправляем ответ
		# 	sock.sendto(b"!Ok", (data[4:], x + 2))

		# else:
		print("have sms: ", data)

		#отправляем их всем юзерам
		for i in users_ip:
			sock.sendto(data.encode("utf-8"), (i, x+2))
			print("to ", i, " send")
	except:
		print("can't open data")

while True:

	some()
	time.sleep(1)