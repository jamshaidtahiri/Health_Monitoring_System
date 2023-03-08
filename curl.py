import requests

url = "http://192.168.119.187:8000/sensor_data"
headers = {
    "Content-Type": "application/json",
    "X-API-Key": "123"
}
data = {
    "temperature": 80,
    "humidity": 80,
    "pulse_rate": 80
}

response = requests.post(url, headers=headers, json=data)
print(response.status_code)
print(response.text)
