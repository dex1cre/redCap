#-*- coding:utf-8 -*-

from tkinter import *

import socket

class Application(Frame):
	def __init__(self, master):
		super(Application, self).__init__(master)
		self.grid()
		self.create_widgets()

	def create_widgets(self):
		######
		#метки
		######
		#метка для адреса
		self.l1 = Label(self, text = "Введите адрес: ", width = 20)
		self.l1.grid(row = 0, column = 0, sticky = N)

		#метка для порта
		self.l2 = Label(self, text = "Введите порт: ", width = 20)
		self.l2.grid(row = 2, column = 0, sticky = N)

		#метка о сервере
		self.l2 = Label(self, text = "Инфа сервера: ", width = 20)
		self.l2.grid(row = 4, column = 0, sticky = N)

		###############
		#Текстовые поля
		###############

		#текстовое поле для адреса
		self.t1 = Entry(self, width = 19)
		self.t1.grid(row = 1, column = 0, sticky = N)

		#текстовое поле для порта
		self.t2 = Entry(self, width = 19)
		self.t2.grid(row = 3, column = 0, sticky = N)

		#инфа о сервере
		self.text1 = Text(self, width = 19, height = 15, wrap = WORD)
		self.text1.grid(row = 5, column = 0, rowspan = 5)

		self.text2 = Text(self, width = 46, height = 30, wrap = WORD)
		self.text2.grid(row = 0, column = 5, rowspan = 30)

		self.text3 = Text(self, width = 46, height = 2, wrap = WORD)
		self.text3.grid(row = 32, column = 5)

		#######
		#Кнопки
		#######

		#Поключение к серверу
		self.btn1 = Button(self, text = "Подключиться!", width = 15, height = 2)
		self.btn1["command"] = self.conn;
		self.btn1.grid(row = 14, column = 0, sticky = N)


		#Отправка смс
		self.btn2 = Button(self, text = "Отправить!", width = 15, height = 2)
		self.btn2["command"] = self.send_sms;
		self.btn2.grid(row = 20, column = 0, sticky = N)

	def get_sms(self):

		sock = socket.socket()

		sock.connect((self.ip, self.port))
		sock.send(b"!get_m")

		data = sock.recv(1024).decode("utf-8") 

		sock.close()
		if data != "":
			print("get --> ", data)
			
			#отправляем их в ленту
			self.text2.insert(0.0, "--> " + data)
		else:
			print("have not data")

		# try:
		# 	sock.connect((self.ip, self.port))
		# 	sock.send(b"!get_m")

		# 	data = sock.recv(1024).decode("utf-8") 

		# 	sock.close()
		# 	if data != "":
		# 		print("get --> ", data)

		# 		#отправляем их в ленту
		# 		self.text2.insert(0.0, "--> " + data)
		# 	else:
		# 		print("have not data")
			
		# except:
		# 	print("--> can't get sms")
		# 	self.after(200, self.get_sms)
		# 	return

		self.after(200, self.get_sms)
		return


		# self.s.setblocking(False)

		# #################
		# #принимаем данные
		# #################

		# try:

		# 	conn, addr = self.s.accept()

		# 	data = conn.recv(1024).decode("utf-8")

		# 	print("get --> ", data)

		# 	#отправляем их в ленту
		# 	self.text2.insert(0.0, "--> " + data)

		# 	conn.close()
		# except:
		# 	print("--> can't get sms")
		# 	self.after(200, self.get_sms)
		# 	return

		# self.after(200, self.get_sms)
		# return

	def conn(self):

		sock_con = socket.socket()
		sock_con.connect((self.t1.get(), int(self.t2.get())))
		sock_con.send(b"!new")
		data = sock_con.recv(1024).decode("utf-8")

		if data == "!Ok":
			self.ip = self.t1.get()
			self.port = int(self.t2.get())

			self.text1.delete(0.0, END)
			self.text1.insert(0.0, "connected: \n" + self.ip + "\n" + str(self.port))

			sock_con.close()

			print("yes, connected")
		else:
			print("can't connected", data)

		#запускаем фоновую функцию (Да, Да)
		self.after(200, self.get_sms)

		# #создаём сокет для приёма сообщений

		# self.s = socket.socket()
		# self.s.bind(("", int(self.t2.get())+2))
		# self.s.listen(1)


	def send_sms(self):
		sock = socket.socket()
		sock.connect((self.ip, self.port))
		sock.send(("!mes:" + self.text3.get(0.0, END)).encode("utf-8"))

		sock.close()

		print("send --> ", self.text3.get(0.0, END))

		self.text3.delete(0.0, END)



#основная часть
root = Tk()
root.title("redCap")
root.geometry("500x465")

app = Application(root)

root.mainloop()