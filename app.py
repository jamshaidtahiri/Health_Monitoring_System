import sqlite3
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

# Define a secret API key for authentication
SECRET_KEY = '123'

# Define a function to check if the API key is valid
def is_valid_api_key(api_key):
    return api_key == SECRET_KEY

@app.route('/')
def index():
    # conn = sqlite3.connect('database.db')
    # c = conn.cursor()
    # c.execute('SELECT * FROM sensor_data')
    # rows = c.fetchall()
    # conn.close()
    #return render_template('index.html', rows=rows)
    return render_template('index.html')

@app.route('/api', methods=['GET'])
def get_sensor_data():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('SELECT temperature, humidity, pulse_rate FROM sensor_data ORDER BY rowid DESC LIMIT 1;')
    result = c.fetchone()
    temperature, humidity, pulse_rate = result
    conn.close()
    data = {
        'temperature': temperature,
        'humidity': humidity,
        'pulse_rate': pulse_rate
    }
    return jsonify(data)

@app.route('/sensor_data', methods=['POST'])
def add_sensor_data():
    # Get the API key from the request headers
    api_key = request.headers.get('X-API-Key')

    # Check if the API key is valid
    if not is_valid_api_key(api_key):
        return jsonify({'error': 'Invalid API key'}), 401
    
    # Get the heart rate data from the request
    data = request.get_json()
    temperature = data['temperature']
    humidity = data['humidity']
    pulse_rate = data['pulse_rate']
    

    # Insert the heart rate into the database
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO sensor_data (temperature,humidity,pulse_rate) VALUES (?,?,?)', (temperature,humidity,pulse_rate))
    conn.commit()
    conn.close()

    return jsonify({'message': 'Heart rate added successfully'}), 201

if __name__ == '__main__':
    #app.run(debug=True)
    app.run(host='192.168.118.186', port=8000, debug=True)