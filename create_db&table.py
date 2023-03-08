import sqlite3

conn = sqlite3.connect('database.db')
c = conn.cursor()

c.execute('''
    CREATE TABLE sensor_data (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
             temperature REAL,
             humidity REAL,
             pulse_rate INTEGER);
''')

conn.commit()
conn.close()
