import sqlite3

conn = sqlite3.connect('heart_rate_data.db')
c = conn.cursor()

c.execute('DROP TABLE IF EXISTS heart_rate')
conn.commit()

conn.close()
