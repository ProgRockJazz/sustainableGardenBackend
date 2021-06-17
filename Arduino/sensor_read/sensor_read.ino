#include <ArduinoJson.h>
#include <DHT.h>

void setup() {
  Serial.begin(115200);
  while (!Serial) continue;

}
void loop() {
  if (Serial.available()) {
    StaticJsonDocument<300> doc;
    DeserializationError err = deserializeJson(doc, Serial);

    if (err == DeserializationError::Ok) {

      
      long pinin = doc["pin"];
      String sensor = doc["sensor"];


      
      if (pinin >= 2 && pinin <= 12 && sensor != "") {
        if (sensor.equals("DHT11")) {
          DHT dht(pinin, DHT11);

          dht.begin();

          delay(2000);

         float h = dht.readHumidity();
        float t = dht.readTemperature();

        if (isnan(h) || isnan(t)) {
          Serial.print("Sensor reading failed!");
          return;
        }

        Serial.print("  Temp: ");
        Serial.println(t);
        Serial.print("  Humidity: ");
        Serial.println(h);
        }
       
      }
      else {
        Serial.println("Invalid input!");
      }
    }
  }
}
