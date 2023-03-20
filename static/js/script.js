var xhttp = new XMLHttpRequest();
xhttp.onreadystatechange = function() {
  if (this.readyState == 4 && this.status == 200) {
    // Update the div element with the sensor values
    var data = JSON.parse(this.responseText);

    // Extract the temperature value
    var temperature = data.temperature;

    // Extract the humidity value
    var humidity = data.humidity;

    // Extract the pulse rate value
    var pulseRate = data.pulse_rate;

    // Update the div element with the temperature value
    document.getElementById("temperature").innerHTML = temperature;

    // Update the div element with the humidity value
    document.getElementById("humidity").innerHTML = humidity;

    // Update the div element with the pulse rate value
    document.getElementById("pulse-rate").innerHTML = pulseRate;

    // Update the sensor values with the normal range colors
    updateSensorValues(temperature, humidity, pulseRate);
  }
};
xhttp.open("GET", "http://192.168.118.186:8000/api", true);
xhttp.send();

setInterval(function() {
  xhttp.open("GET", "http://192.168.118.186:8000/api", true);
  xhttp.send();
}, 5000); // Update every 5 seconds

// Get references to the temperature, humidity, and pulse rate elements
const temperatureElement = document.getElementById('temperature');
const humidityElement = document.getElementById('humidity');
const pulseRateElement = document.getElementById('pulse-rate');

// Set the normal range values for temperature, humidity, and pulse rate
const normalRanges = {
  temperature: {
    low: 36.5,
    high: 37.5
  },
  humidity: {
    low: 30,
    high: 60
  },
  pulseRate: {
    low: 60,
    high: 100
  }
};

// Update the temperature, humidity, and pulse rate values
function updateSensorValues(temperature, humidity, pulseRate) {
  // Update the temperature value and color
  if (temperature < normalRanges.temperature.low || temperature > normalRanges.temperature.high) {
    temperatureElement.style.color = 'red';
  } else {
    temperatureElement.style.color = 'green';
  }

  // Update the humidity value and color
  if (humidity < normalRanges.humidity.low || humidity > normalRanges.humidity.high) {
    humidityElement.style.color = 'red';
  } else {
    humidityElement.style.color = 'green';
  }

  // Update the pulse rate value and color
  if (pulseRate < normalRanges.pulseRate.low || pulseRate > normalRanges.pulseRate.high) {
    pulseRateElement.style.color = 'red';
  } else {
    pulseRateElement.style.color = 'green';
  }
}
