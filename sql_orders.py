import sqlite3

conn = sqlite3.connect('orders.db')

cur = conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS Orders(order_id INT, customer_id INT, order_date DATE, amount DECIMAL(10,2))")

cur.close()
conn.close()