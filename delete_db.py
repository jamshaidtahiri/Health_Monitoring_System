import os

if os.path.exists('heart_rate_data.db'):
    os.remove('heart_rate_data.db')
    print("Database file deleted")
else:
    print("The database file does not exist")
