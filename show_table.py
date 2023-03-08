import sqlite3

conn = sqlite3.connect('heart_rate_data.db')
c = conn.cursor()

c.execute('SELECT * FROM heart_rate')
rows = c.fetchall()

for row in rows:
    print(row)

conn.close()







##



# Create the heart rate table if it does not exist
#conn = sqlite3.connect('database.db')
#c = conn.cursor()
#c.execute('''CREATE TABLE IF NOT EXISTS sensor_data (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             temperature REAL,
#             humidity REAL,
#             pulse_rate INTEGER)''')
#conn.commit()
#conn.close()    