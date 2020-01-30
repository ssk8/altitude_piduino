#include <Wire.h>
#include <Adafruit_BMP085.h>

Adafruit_BMP085 bmp;
  
void setup() {
  Serial.begin(115200);
  if (!bmp.begin()) {
	Serial.println("Could not find a valid BMP085 sensor, check wiring!");
	while (1) {}
  }
}
  
void loop() {
    Serial.print(bmp.readTemperature());

    Serial.print(' ');
    Serial.print(bmp.readPressure());

    Serial.print(' ');
    Serial.print(bmp.readAltitude());

    Serial.print(' ');
    Serial.print(bmp.readSealevelPressure());

    Serial.print(' ');
    Serial.print(bmp.readAltitude(101500));
    Serial.println();
    delay(500);
}
