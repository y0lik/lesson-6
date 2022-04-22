import sqlite3

connection = sqlite3.connect("mydbfile.sl3", 5)
cur = connection.cursor()
def show_with_name():
	cur.execute(f"SELECT rowid, name FROM first_table;")
	connection.commit()
	res = cur.fetchall()
	print("\tID\t\tName")
	for id, name in res:
		print(f"\t{id}\t\t{name}")
# CREATE TABLE first_table (name TEXT); - створити таблицю з колонкою name
# cur.execute("CREATE TABLE first_table (name TEXT);")
# INSERT - вставляє в таблицю данні
# cur.execute("INSERT INTO first_table (name) VALUES ('john'), ('andr');")
# SELECT - вибрати певні данні,
# rowid - унікальний номер рядка в таблиці, генерується автоматично
# cur.execute("SELECT rowid, name FROM  first_table;")
# connection.commit()
# res = cur.fetchall()
# print(res)

# id = int(input("Enter id: "))
#
# cur.execute(f"SELECT rowid, name FROM  first_table WHERE rowid={id};")
# connection.commit()
# res = cur.fetchall()
# print(res)


# UPDATE - оновлення таблиці, SET встановити значення колонці ДЕ(WHERE) ід буде = 2
# cur.execute(f"UPDATE first_table SET name='ron' WHERE rowid=5;")
# delete - видалити , FROM -звідки? WHERE (ДЕ?) -наприклад, де - імя = алекс
# cur.execute("DELETE FROM first_table WHERE name='alex';")
# n = input("Enter name to delete: ")
# cur.execute(f"DELETE FROM first_table WHERE name='{n}';")

# ALTER TABLE table_name ADD column_name datatype;
# ALTER TABLE - змінити таблицу, яку? ADD- що добавити ? column_name - назва колонки, datatype- тип колонки(напр TEXT)

#добавимо нову колонку (як name)
#cur.execute(f"ALTER TABLE first_table ADD age INTEGER; ")

def show_name_and_age():
	cur.execute(f"SELECT rowid, name, age FROM first_table;")
	connection.commit()
	res = cur.fetchall()
	print("\tID\t\tName\t\tAge")
	for id, name, age in res:
		print(f"\t{id}\t\t{name}\t\t{age}")

#cur.execute("INSERT INTO first_table (name, age) VALUES ('john', 21);")
# age - для минулих значень  в нас пустий, тобто є None
#Щоб змінити None на якесь значенни робим перевірку на null,
#cur.execute(f"UPDATE first_table SET age=5 WHERE age IS NULL;")

#show()

#show_name_and_age()

#видалити повністю всю таблицю
cur.execute("DROP TABLE first_table; ")
connection.close()