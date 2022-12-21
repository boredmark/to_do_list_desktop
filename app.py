from tkinter import *
import database

class App:

	def __init__(self, window):
		self.window = window
		self.window.title("Clicking application")
		self.window.geometry("500x500")
		self.label = Label(window, text = "TO DO").pack()
		self.topFrame = Frame(window)
		self.topFrame.pack()
		self.buttomFrame = Frame(window)
		self.buttomFrame.pack()
		self.l = database.get_all_values()
		for i, j  in zip(self.l, range(len(self.l))):
			self.to_do = Checkbutton(self.topFrame, text = f"{i[0]}", command=lambda s=i[0]:self.switch_checkbox(s))
			if i[1] == 0:
				self.to_do.deselect()
			if i[1] == 1:
				self.to_do.select()
			self.to_do.grid(row = 1 + j, column = 1)
			self.b = Button(self.topFrame, text = 'delete',height=1, width=2, command=lambda x=i[0]:self.delete_item(x))
			self.b.grid(row = 1 + j, column = 3)

		self.entry = Entry(self.buttomFrame)
		self.entry.pack()
		self.button1 = Button(self.buttomFrame, text = "Add",  command = self.add_to_list)
		self.button1.pack()
		self.window.bind('<Return>', self.add_to_list)


	def add_to_list(self, event=None):
		item = self.entry.get()
		if len(item) == 0:
			return None
		for i, j in zip(self.l, range(len(self.l))):
			if i[0] == item:
				return None
		database.add_value([item, 0])
		self.l = database.get_all_values()
		for widget in self.topFrame.winfo_children():
			widget.destroy()
		for i, j in zip(self.l, range(len(self.l))):
			self.to_do = Checkbutton(self.topFrame, text = f"{i[0]}", command=lambda s=i[0]:self.switch_checkbox(s))
			if i[1] == 0:
				self.to_do.deselect()
			if i[1] == 1:
				self.to_do.select()
			self.to_do.grid(row = 1 + j, column = 1)
			self.b = Button(self.topFrame, text = 'delete',height=1, width=2,command=lambda x=i[0]:self.delete_item(x))
			self.b.grid(row = 1 + j, column = 3)
		self.entry.delete(0, END)


	def switch_checkbox(self, sw):
		for i, j in zip(self.l, range(len(self.l))):
			if i[0] == sw:
				if self.l[j][1] == 0:
					database.update_value([sw, 1])
					break
				if self.l[j][1] == 1:
					database.update_value([sw, 0])
		self.l = database.get_all_values()
		for widget in self.topFrame.winfo_children():
			widget.destroy()
		for i, j in zip(self.l, range(len(self.l))):
			self.to_do = Checkbutton(self.topFrame, text = f"{i[0]}", command=lambda s=i[0]:self.switch_checkbox(s))
			if i[1] == 0:
				self.to_do.deselect()
			if i[1] == 1:
				self.to_do.select()
			self.to_do.grid(row = 1 + j, column = 1)
			self.b = Button(self.topFrame, text = 'delete',height=1, width=2, command=lambda x=i[0]:self.delete_item(x))
			self.b.grid(row = 1 + j, column = 3)

	def delete_item(self, item_to_del):
		for i, j in zip(self.l, range(len(self.l))):
			if i[0] == item_to_del:
				database.delete_value([item_to_del, 0])
		self.l = database.get_all_values()
		for widget in self.topFrame.winfo_children():
			widget.destroy()
		for i, j in zip(self.l, range(len(self.l))):
			self.to_do = Checkbutton(self.topFrame, text = f"{i[0]}", command=lambda s=i[0]:self.switch_checkbox(s))
			if i[1] == 0:
				self.to_do.deselect()
			if i[1] == 1:
				self.to_do.select()
			self.to_do.grid(row = 1 + j, column = 1)
			self.b = Button(self.topFrame, text = 'delete',height=1, width=2, command=lambda x=i[0]:self.delete_item(x))
			self.b.grid(row = 1 + j, column = 3)


