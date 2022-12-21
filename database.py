import sqlite3


def create_db():
	try:
		conn = sqlite3.connect('main.db')
	except Exception as e:
		raise 'Failed connection'
	finally:
		cur = conn.cursor()
		cur.execute("CREATE TABLE IF NOT EXISTS to_do(value VARCHAR(20), state INT);")
		conn.commit()
		conn.close()


def add_value(l):
	data = (l[0], l[1])
	try:
		conn = sqlite3.connect('main.db')
	except Exception as e:
		raise 'Failed connection'
	finally:
		cur = conn.cursor()
		cur.execute("INSERT INTO to_do VALUES(?, ?);",data)
		conn.commit()
		conn.close()


def get_all_values():
	try:
		conn = sqlite3.connect('main.db')
	except Exception as e:
		raise 'Failed connection'
	finally:
		cur = conn.cursor()
		cur.execute(f"SELECT * FROM to_do;")
		one_result = cur.fetchall()
		conn.close()
		return one_result


def update_value(l):
	data = (l[1],l[0])
	try:
		conn = sqlite3.connect('main.db')
	except Exception as e:
		raise 'Failed connection'
	finally:
		cur = conn.cursor()
		cur.execute("UPDATE to_do SET state = ? WHERE value = ?;", data)
		conn.commit()
		conn.close()


def delete_value(l):
	data =l[0]
	try:
		conn = sqlite3.connect('main.db')
	except Exception as e:
		raise 'Failed connection'
	finally:
		cur = conn.cursor()
		cur.execute("DELETE FROM to_do WHERE value=?", (data,))
		conn.commit()
		conn.close()





a = get_all_values()
print(a)



