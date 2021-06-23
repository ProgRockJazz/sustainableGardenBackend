#include <ArduinoJson.h>
#include <DHT.h>

#define NPINS 12 // pin count

void setup() {
  Serial.begin(115200);
  while (!Serial) continue;
}

void readSensor(String sensorName, int sensorPin) {
  if (sensorPin >= 2 && sensorPin <= NPINS && sensorName != "") {
    StaticJsonDocument<200> out;

    if (sensorName.equals("DHT11")) {
      DHT dht(sensorPin, DHT11);

      dht.begin();
      delay(500);

      float h = dht.readHumidity();
      float t = dht.readTemperature();

      if (isnan(h) || isnan(t)) {
        Serial.print("Sensor reading failed!");
        return;
      }

      out["Temperature"] = t;
      out["Humidity"] = h;
    }
    else if (sensorName.equals("Rain")) {
      int reading = digitalRead(sensorPin);
      out["Rain"] = reading;
    }
    
    serializeJsonPretty(out, Serial);
  }

  else {
    Serial.println("Invalid input!");
  }
}

void loop() {
  if (Serial.available()) {
    StaticJsonDocument<200> doc;
    DeserializationError err = deserializeJson(doc, Serial);

    if (err == DeserializationError::Ok) {
      long pinin = doc["pin"];
      String sensor = doc["sensor"];

      readSensor(sensor, pinin);
    }
  }
}
