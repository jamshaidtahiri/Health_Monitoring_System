$(document).ready(function() {
  // Get references to the gauges
  var tempGauge = new RadialGauge(document.getElementById("temp-gauge"));
  var humidityGauge = new RadialGauge(document.getElementById("humidity-gauge"));
  var pulseRateGauge = new RadialGauge(document.getElementById("pulse-rate-gauge"));

  // Define the URL to fetch the latest data from the backend
  var latestDataURL = "http://192.168.118.186:8000/api";

  // Define a function to update the gauges with the latest data
  function updateGauges() {
      $.getJSON(latestDataURL, function(data) {
          // Get the latest values for temperature, humidity, and pulse rate
          var latestTemp = data.temperature;
          var latestHumidity = data.humidity;
          var latestPulseRate = data.pulse_rate;

          // Update the gauges with the latest values
          tempGauge.value(latestTemp);
          humidityGauge.value(latestHumidity);
          pulseRateGauge.value(latestPulseRate);
      });
  }

  // Call the updateGauges function every 5 seconds
  setInterval(updateGauges, 5000);
});
