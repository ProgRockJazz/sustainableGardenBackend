#include <ArduinoJson.h>
#include <DHT.h>

#define NPINS 12 // pin count

void setup() {
  Serial.begin(115200);
  while (!Serial) continue;
}

// takes sensor type and sensor pin to take appropriate type of reading
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

    serializeJsonPretty(out, Serial);    // pretified shoudn't matter
  }

  else {
    Serial.println("Invalid input!");
  }
}

void openValve(int openTime, int valvePin) {
  pinMode(valvePin, OUTPUT);

  digitalWrite(valvePin, HIGH);
  delay(openTime);
  digitalWrite(valvePin, LOW);

  pinMode(valvePin, INPUT); // set to default
}

void loop() {
  if (Serial.available()) {
    StaticJsonDocument<200> doc;
    DeserializationError err = deserializeJson(doc, Serial);

    if (err == DeserializationError::Ok) {
      // decide whether the input is for a senosr reading or valve opening
      if (doc.containsKey("sensor")) {
        long pinin = doc["pin"];
        String sensor = doc["sensor"];

        readSensor(sensor, pinin);
      }
      else if (doc.containsKey("time")) {
        long openTime = doc["time"];
        long valvePin = doc["pin"];

        openValve(openTime, valvePin);
      }
      else {
        Serial.print("Invalid Input!");
      }
    }
  }
}
