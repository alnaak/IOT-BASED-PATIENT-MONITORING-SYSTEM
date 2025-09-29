#include <Wire.h> 
#include <Adafruit_MLX90614.h> 
#include <WiFi.h> 

#define ECG_PIN A0   // Analog pin for ECG sensor 

// WiFi credentials 
const char* ssid = "YourWiFiSSID"; 
const char* password = "YourWiFiPassword"; 

// ECG variables 
unsigned long ecgReading; 
unsigned long lastTime = 0; 
const int ecgInterval = 20; // Interval between ECG readings in milliseconds 

// Initialize the temperature sensor 
Adafruit_MLX90614 mlx = Adafruit_MLX90614(); 

void setup() { 
    Serial.begin(9600); 

    // Connect to WiFi 
    WiFi.begin(ssid, password); 
    while (WiFi.status() != WL_CONNECTED) { 
        delay(1000); 
        Serial.println("Connecting to WiFi..."); 
    } 
    Serial.println("Connected to WiFi"); 

    // Initialize temperature sensor 
    mlx.begin(); 

    // Set ECG pin as input 
    pinMode(ECG_PIN, INPUT); 
} 

void loop() { 
    // Read temperature 
    float objTempC = mlx.readObjectTempC(); 
    Serial.print("Object Temperature: "); 
    Serial.print(objTempC); 
    Serial.println(" °C"); 

    // Read ECG 
    unsigned long currentTime = millis(); 
    if (currentTime - lastTime >= ecgInterval) { 
        ecgReading = analogRead(ECG_PIN); 
        Serial.print("ECG Reading: "); 
        Serial.println(ecgReading); 
        lastTime = currentTime; 
    } 

    // Add your code for sending data to a server or performing any other actions here 
    delay(1000); // Delay between readings 
}
