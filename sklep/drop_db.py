import sqlite3


conn = sqlite3.connect('sklep.db')


cursor = conn.cursor()


cursor.execute("DROP TABLE cart")
print("Table dropped... ")


conn.commit()


conn.close()