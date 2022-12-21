from tkinter import *
from app import App
import database


if __name__ == '__main__':
	database.create_db()
	root = Tk()
	my_gui = App(root)
	root.mainloop()