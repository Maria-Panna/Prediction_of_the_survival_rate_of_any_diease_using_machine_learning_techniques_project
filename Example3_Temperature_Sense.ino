#include <Wire.h>
#include "MAX30105.h"  // Ensure you are using the correct library

MAX30105 particleSensor;

void setup()
{
  Serial.begin(9600);
  Serial.println("Initializing...");

  // Initialize sensor without arguments
  if (particleSensor.begin() == false) // No arguments needed for this version of the library
  {
    Serial.println("MAX30105 was not found. Please check wiring/power.");
    while (1);
  }

  // Setup other configurations as needed
}

void loop()
{
  float temperatureC = particleSensor.readTemperature(); // Read temperature in Celsius

  // Convert Celsius to Fahrenheit
  float temperatureF = (temperatureC * 9.0 / 5.0) + 32.0;

  Serial.print("Temperature in F: ");
  Serial.println(temperatureF, 2); // Print with 2 decimal places

  delay(1000); // Delay for a second between readings
}
