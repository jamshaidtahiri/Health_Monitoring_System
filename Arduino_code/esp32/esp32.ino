#include <WiFi.h>
#include <HTTPClient.h>
#include <DHT.h>

const char* ssid = "MR MJT";
const char* password = "tahiri123";
const char* serverName = "http://192.168.118.186:8000/sensor_data";
const char* apiKey = "123";

#define DHTPIN 14    // Digital pin connected to the DHT sensor
#define DHTTYPE DHT11 // DHT 11
DHT dht(DHTPIN, DHTTYPE);
//#define SENSORPIN A0  // Analog pin connected to the pulse rate sensor

const int pulseSensor = A7;
int pulseRate;

void setup() {
  Serial.begin(9600);
  pinMode(pulseSensor, INPUT);

  WiFi.begin(ssid, password);
  Serial.print("Connecting to Wi-Fi");
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.print(".");
  }
  Serial.println("connected!");
}

void loop() {
  float temperature = dht.readTemperature();
  float humidity = dht.readHumidity();
  Serial.println(temperature);
  Serial.println(humidity);

  if (isnan(temperature) || isnan(humidity)) {
    Serial.println("Failed to read from DHT sensor!");
    return;
  }

  pulseRate = analogRead(pulseSensor);
  pulseRate = map(pulseRate, 0, 4095, 0, 255);
  Serial.println(pulseRate);

// Create HTTP client object
  HTTPClient http;
  http.begin(serverName);
  http.addHeader("Content-Type", "application/json");
  http.addHeader("X-API-Key", apiKey);

  // Create JSON payload
  String payload = "{\"temperature\": " + String(temperature) +
                   ", \"humidity\": " + String(humidity) +
                   ", \"pulse_rate\": " + String(pulseRate) + "}";
  int httpResponseCode = http.POST(payload);

  if (httpResponseCode > 0) {
    Serial.print("HTTP Response code: ");
    Serial.println(httpResponseCode);
  } else {
    Serial.print("Error code: ");
    Serial.println(httpResponseCode);
  }

  http.end();
  delay(2000);
}
